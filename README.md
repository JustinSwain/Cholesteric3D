<h1>Cholesteric 3D</h1>

<p>
  This software is used to simulate choelsteric liquid crystals in three dimensions using a Q-tensor model by way of a Finite Element method. The Finite Element problem is solved using FreeFEM++. Data is processed using MATLAB and Python. Data is visualized using ParaView.
</p>
<p>
  This code accompanies the paper "Directed Self-Assembly of Chiral Liquid Crystals into Biomimetic Bouligand Structures in Thin Film with Superior Optical-Mechanical Properties" by Tejal Pawale1, Justin Swain, Mesonma Anwasi1, David A. Czaplewski, Ralu Nana Silvia Divan, Giordano Tierra Chica, and Xiao Li. This software was developed by Justin Swain and Giordano Tierra Chica and released as open source under the MIT license.
</p>

<h2>Repository Contents</h2>
<ul>
<li> Cholesteric3D.edp</li>
<li> processData.py</li>
<li> loaddata.edp</li>
</ul>
<p>Optional</p>
<ul>
  <li>data - a few sample data files</li>
  <li>energyData.m - sample energy data</li>
</ul>

<h2>Hardware Requirements:</h2>
<p>
  A standard desktop computer with moderate memory (RAM) requirements. For example, we used a computer with 64gb of RAM. 
</p>
<p>
  The codes were tested on the following operating systems:
</p>
<ul>
  <li>Windows 10, 11</li>
  <li>macOS 13, 14, 15</li>
</ul>

<h2>Software Requirements:</h2>
<p>
  The following software is required, but none are complicated to install. A typical install time should be less than 30 minutes. Most versions of each software should be sufficient.
</p>
<ul>
<li>
  FreeFEM++: <br>
  https://freefem.org/ <br> 
  (Free and open-source) <br>
  Tested on version 4.9
</li>

<li>
Python: <br>
https://www.python.org/<br>
(free and open-source)<br>
Tested on version 3.13.2
</li>

<li>
MATLAB:<br>
https://www.mathworks.com/<br>
(proprietary)<br>
Tested on version 2024a
</li>

<li>
Paraview:<br>
https://www.paraview.org/<br>
(free and open-source)<br>
Tested on version 5.9.1
</li>
</ul>

<h1>Instructions</h1>
<p>
  The following instructions will allow the user to reproduce a result from the research article that this code supports.
</p>
<ol>
<li>
  Follow the installation steps for each of the software requirements according to the developer's instructions. 
</li>

<li>
  Clone this repository or extract the contents to your working directory.
</li>

<li>
  Run Cholesteric3D.edp and wait until it finishes (about 26 hours for this simulation on our computer with and Intel Xeon 10-core cpu). The simulation data is saved in the data directory and the energy data is saved as a MATLAB script file in energyData.m.
</li>

<li>
  Run processData.py, type 'data', and hit enter to process the data.
</li>

<li>
  Run loaddata.edp to convert the data to .vtu files which can be read by Paraview. The program will run until it has processed all of the available data files inside of the data folder.
</li>

<li>
  Open the .vtu files in ParaView to view the simulation data. Run the energyData.m script in MATLAB to view the energy data.
</li>
</ol>

