# CoCi-MooC-SUMO-scenarios
CoCi MooC SUMO scenarios

This repository stores the scenarios covered by the video lectures Do-It-Yourself for the CoCi MooC.

## Scenario_01
Basic scenario for running a simple SUMO simulation.
The simulated area corresponds to the core of the city of Barcelona (Eixample district) with network created based on OSM data.
Routes are estimated from Activitygen based on sociodemographic data of the simulated area.

![net scenario 1](core_001.PNG)

<p align = "center">
Net for Scenario 1. Section of the core of the city of the Barcelona, centered in the Eixample district.
</p>

For execution it is needed only to run the bash file **scenario_001.sh**.

### Description of files

- **RONDES_dua_astar_cut_dua_fix_astar_p10_.trips.rou.xml**: Route files specifying origin, destination and departure time for each vehicle (agent) in the simulation.

- **core_001.net.xml**: Network. Map of roads, intersections and connectivity rules as the simulation environments. Source: Open Street Map

- **scenario_001.sh**: Bash file for execution

- **vehtype.xml**: additional configuration file for specifying the type of vehicle.
