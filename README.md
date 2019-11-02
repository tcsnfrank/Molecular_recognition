# Molecular_recognition

## Introduction:

This script can be applied to analyze the trajectory files of molecular dynamics simulations by **LAMMPS**. It monitors the identify of the molecules and provide the statistics of individual molecules as the function of the simulation time. More details can be found in Gao et al. “Exploration of the dehydrogenation pathways of ammonia diborane and diammoniate of diborane by molecular dynamics simulations using reactive force fields” to be submitted (2019).


## Requirements:

-	Python 3.6
-	Numpy 
-	Pandas 
-	Matplotlib 
-	Copy 
-	Json 

## Installation
https://github.com/tcsnfrank/Molecular_recognition

## Usage 

- 1). Adapting the elements and cutoff for the bond lengths the **setting** file.

- 2). ``` $ Python3.6 MoleculeClassification.py ```

- 3). Once the program is running, you will be required to type the name of the target trajectory file (one example is provided as *Trajectory_2500K.lammpstrj*), which you want to analyze;

- 3). Then the script will analyze the trajectory file and the outputs are saved in csv files.

- 4). Once the script finishes its analysis, you could use Spyder to visualise the outputs.

- a). Use Spyder to run the file **plot.py**, and you will be asked to input the composition of target molecule: B_X N_Y H_Z, X Y Z means the number of B, N, and H atoms in one molecule, for example, you could input: 0 2 0, then it indicates Hygrogen, and then you can see the plot of generated hydrogen molecules with simulation time, and Spyder is convenient for data saving;

- b). For molecular recognition, in each timestep, the fingerprint data (in the form of vector) will be saved in one csv file, then users could use these data to write the structures of the generated molecules;
