#! python3
#  Data Processing for Cholesteric 3D
#  Copyright (c) 2025 Justin Swain and Giordano Tierra Chica
#  Licensed under the MIT License (see LICENSE file)
#  
#   This code supports the research in "Directed Self-Assembly of Chiral Liquid Crystals into Biomimetic 
#   Bouligand Structures in Thin Film with Superior Optical-Mechanical Properties" by Tejal Pawale1, Justin Swain, 
#   Mesonma Anwasi1, David A. Czaplewski, Ralu Nana Silvia Divan, Giordano Tierra Chica, and Xiao Li
import os
import glob
import numpy as np

# Prompt user for folder name and change directory
try:
    user = input("Folder name? ")
    os.chdir(user)
    print(f"Changed directory to: {os.getcwd()}")
except FileNotFoundError:
    print(f"Error: Directory '{user}' not found.")
    exit(1)

# Find all q*.gp files and group by timestamp
files = glob.glob('q*.gp')  # Matches q_xx.gp
if not files:
    print(f"Error: No 'q*.gp' files found in {os.getcwd()}")
    exit(1)

# Extract timestamps
timestamps = sorted(set(f.split('_')[-1][:-3] for f in files)) 
print(f"Timestamps found: {timestamps}")

for ts in timestamps:
    print(f"\nProcessing timestamp: {ts}")
    
    # Expected filenames for this timestamp
    expected_files = [f"q{i}_{ts}.gp" for i in range(1, 7)]
    q_files = [f for f in files if f.endswith(f"_{ts}.gp")]
    
    if len(q_files) != 6 or sorted(q_files) != expected_files:
        print(f"Error: Missing or unexpected files for timestamp {ts}. Expected: {expected_files}")
        continue

    # Read data
    data = {}
    mesh_size = None

    for q_file in expected_files:
        with open(q_file, "r") as f:
            lines = f.readlines()
            if not lines:
                print(f"Error: {q_file} is empty")
                break
            
            # Read mesh size from first file encountered
            if mesh_size is None:
                try:
                    mesh_size = int(lines[0].strip())
                except ValueError:
                    print(f"Warning: Invalid mesh size in {q_file}, using default 0")
                    mesh_size = 0
            
            # Read all values from the file 
            raw_values = []
            for line in lines[1:]:
                raw_values.extend([float(val) for val in line.split()])
            data[q_file] = raw_values
            print(f"Loaded {len(data[q_file])} values from {q_file}")

    # Determine the number of nodes 
    num_nodes = min(len(data[f"q1_{ts}.gp"]), len(data[f"q2_{ts}.gp"]), len(data[f"q3_{ts}.gp"]),
                    len(data[f"q4_{ts}.gp"]), len(data[f"q5_{ts}.gp"]), len(data[f"q6_{ts}.gp"]))
    print(f"Processing {num_nodes} nodes for timestamp {ts}")

    # Prepare lists to hold computed quantities
    eigenvalues_max = []
    eigenvectors_max = []
    S_vals = []
    S2_vals = []
    normQ2_vals = []

    # Loop over each node, compute Q matrix and required quantities
    for node in range(num_nodes):
        # Construct Q matrix for this node
        Q = np.array([
            [data[f"q1_{ts}.gp"][node], data[f"q2_{ts}.gp"][node], data[f"q3_{ts}.gp"][node]],
            [data[f"q2_{ts}.gp"][node], data[f"q4_{ts}.gp"][node], data[f"q5_{ts}.gp"][node]],
            [data[f"q3_{ts}.gp"][node], data[f"q5_{ts}.gp"][node], data[f"q6_{ts}.gp"][node]]
        ])
        # Compute normQ2 using the weighted sum
        normQ2 = (data[f"q1_{ts}.gp"][node]**2 +
                  2 * data[f"q2_{ts}.gp"][node]**2 +
                  2 * data[f"q3_{ts}.gp"][node]**2 +
                  data[f"q4_{ts}.gp"][node]**2 +
                  2 * data[f"q5_{ts}.gp"][node]**2 +
                  data[f"q6_{ts}.gp"][node]**2)
        normQ2_vals.append(normQ2)
        
        try:
            # np.linalg.eigh returns eigenvalues in ascending order
            vals, vecs = np.linalg.eigh(Q)
            # Largest eigenvalue is the last element; second largest is the second last.
            eigenvalue1 = vals[-1]
            eigenvalue2 = vals[-2]
            eigenvalues_max.append(eigenvalue1)
            eigenvectors_max.append(vecs[:, -1])
            # S = |eigenvalue1 - eigenvalue2|
            S_vals.append(abs(eigenvalue1 - eigenvalue2))
            # S2 = |third component of the eigenvector corresponding to the largest eigenvalue|
            S2_vals.append(abs(vecs[2, -1]))
        except np.linalg.LinAlgError as e:
            print(f"Error: Eigenvalue computation failed at node {node+1} for timestamp {ts} - {e}")
            break

    # Define output filenames
    output_files = {
        "eigen": f"eigen_{ts}.gp",
        "eigenvector1": f"eigenvector1_{ts}.gp",
        "eigenvector2": f"eigenvector2_{ts}.gp",
        "eigenvector3": f"eigenvector3_{ts}.gp",
        "S": f"S_{ts}.gp",
        "S2": f"S2_{ts}.gp",
        "normQ2": f"normQ2_{ts}.gp"
    }

    try:
        # Write gp file function
        def write_gp_file(filename, values):
            with open(filename, "w") as f:
                f.write(f"{mesh_size}\n")
                for i in range(0, len(values), 5):
                    row = values[i:i+5]
                    f.write("\t".join(f"{val:.16f}" for val in row) + "\n")

        # Write the gp files
        write_gp_file(output_files["eigen"], eigenvalues_max)
        write_gp_file(output_files["eigenvector1"], [vec[0] for vec in eigenvectors_max])
        write_gp_file(output_files["eigenvector2"], [vec[1] for vec in eigenvectors_max])
        write_gp_file(output_files["eigenvector3"], [vec[2] for vec in eigenvectors_max])
        write_gp_file(output_files["S"], S_vals)
        write_gp_file(output_files["S2"], S2_vals)
        write_gp_file(output_files["normQ2"], normQ2_vals)
        
        print(f"Saved results to: {', '.join(output_files.values())}")

    except IOError as e:
        print(f"Error: Failed to write output files for timestamp {ts} - {e}")

print("\nProcessing complete.")
