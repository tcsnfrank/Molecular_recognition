# Molecular_recognition
Once you got a LAMMPS Trajectory file, you could apply our script for compositional analysis. 
The main procedure is like this:
1). You have to install Python in your desktop, keep all the files in one folder (you could change the bonding length in the setting file), and then run the main program MoleculeClassification.py;
2). Once the program is running, you need to type the name of the trajectory file;
3). The script will work and analyze the trajectory file;
4). Once the script finishes its analysis, you could use Spyder to see the data and plots;
5). Use Spyder to run the file plot.py, and you will be asked to input the composition of target molecule: B_X N_Y H_Z, X Y Z means the number of B, N, and H atoms in one molecule, for example, you could input: 0 2 0, then it indicates Hygrogen, and then you can see the plot of generated hydrogen molecules with simulation time;
6). For molecular recognition, in each time_step, the fingerprint data (in the form of vector) will be saved in excel format, users could use these data to write the structures of the generated molecules;
This is a basic version for molecular recognition, more functions will be added into it, to make it more convenient for computational chemists.
