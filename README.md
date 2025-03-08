<h1>Cholesteric 3D</h1>

<p>
  This software is used to simulate choelsteric liquid crystals in three dimensions using a Q-tensor model by way of a Finite Element method. The Finite Element problem is solved using FreeFEM++. Data is processed using MATLAB and Python. Data is visualized using ParaView.
</p>
<p>
  This code accompanies the paper "Directed Self-Assembly of Chiral Liquid Crystals into Biomimetic Bouligand Structures in Thin Film with Superior Optical-Mechanical Properties" by Tejal Pawale, Justin Swain, Mesonma Anwasi, David A. Czaplewski, Ralu Nana Silvia Divan, Giordano Tierra Chica, and Xiao Li. This software was developed by Justin Swain and Giordano Tierra Chica and released as open source under the MIT license.
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
  The following software is required, but none are complicated to install. A typical install time should be less than 30 minutes. Most versions of each software will be sufficient.
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
<ul>
  <li>
    Numpy:<br>
    https://numpy.org/install/
  </li>
</ul>

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
  Run Cholesteric3D.edp and wait until it finishes (about 26 hours for this simulation on our computer with an Intel Xeon 10-core cpu). The simulation data is saved in the data directory and the energy data is saved as a MATLAB script file in energyData.m.
</li>

<li>
  Run processData.py, type 'data', and hit enter to process the data.
</li>

<li>
  Run loaddata.edp to convert the data to .vtu files which can be read by Paraview. The program will run until it has processed all of the available data files inside of the data folder.
</li>
</ol>

<h2>Expected Output</h2>
<p>
  After running the code and processing the data, we can now open the data in ParaView to reproduce a portion of a figure from the article and recover a liquid crystal helical structure.
</p>
<ol>
  <li>
    Open ParaView
  </li>
  <li>
    Click File>Open...
  </li>
  <li>
    Navigate to your data folder and click on Results_Paraview_..vtu.
  </li>
  <li>
    Click "Apply" in the left-side properties browser.
  </li>
  <li>
    In the top menu bar, find Filters>Alphabetical>Cell Data to Point Data. Click "Apply."
  </li>
  <li>
    Now select Filters>Alphabetical>Contour. In the properties browser, choose "normQ2" in the drop down menu next to "Contour by:". In the "Value Range:" box, click on the value and type 0.25. Click "Apply."
  </li>
  <li>
    To apply color to the surface, locate the drop-down selction under the red undo button (beneath Tools) and select "S2."
  </li>
  <li>
    Advance the simulation to the final time by clicking the green triangle "Play" button.
  </li>
</ol>

