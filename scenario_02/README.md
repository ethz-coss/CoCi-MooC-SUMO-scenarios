# CoCi-MooC-SUMO-scenarios
CoCi MooC SUMO scenarios

This repository stores the scenarios covered by the video lectures Do-It-Yourself for the CoCi MooC.

## Scenario_02
Set of 4 different networks for comparing alternative scenarios as an extended A/B testing.
These 4 networks are abstractions and simplifications of an area of 9x9 blocks of the Eixample district of Barcelona, which is equivalent roughly to 1.44km<sup>2</sup>. outes are estimated from Activitygen based on sociodemographic data of the simulated area.
Each alternative needs to be run separately for obtaining the results. A script is provided for visualization and comparison of results.

### Description of files

For each of the four alternatives (*net01*, *net02*, *net03*, and *net04*) the files structure is the same :

- **run_simu_net0x.sh**: Bash file for executing Python script

- **simu_net0x.py**: Python script for simulation.

- **data/activitygen-bcn_xx.rou.xml**: Routes file specifying origin, destination and departure time for each vehicle (agent) in the simulation from activitygen script based on sociodemographic data.

- **data/grid01-bcn_xx.net.xml**: Network. Map of roads, intersections, and connectivity rules as the simulation environments.

- **data/compar_xxx.sumo.cfg**: SUMO configuration file for specifying files (input and output) and parameters involved in the simulation.

- **data/init_edgedata_additional_file.xml**: configuration file for specifying the output files to save the results of the simulations.

- **data/random/random_ALL.rou.xml**: Routes file specifying origin, destination and departure time for each vehicle (agent) in the simulation from random generator to add diversity and noise to the traffic demand.

For obtaining the results, the Bash files (**run_simu_net0x.sh**) in each alternatives folders (*net01*, *net02*, *net03*, and *net04*) need to be run separately.

Once the results are obtained, they are saved in a **data/results** folder. These files can be read for visualization using the Jupyter Notebook  **results_processing_micro.ipynb**.