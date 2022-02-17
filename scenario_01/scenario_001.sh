#!/bin/bash
# Execution of simulation for Barcelona Core
NET_FILE=core_001.net.xml
ROUTES_FILE=RONDES_dua_astar_cut_dua_fix_astar_p10_.trips.rou.xml
ADD_FILES=vehtype.xml
ROUTING_ALG=astar
STATS_OUT_FILE=sim_stats_output_summary.xml
STEP_LENGTH_VALUE=0.25
TIME_TO_TELEPORT_VALUE=150
REROUT_PROB_VALUE=1.0
REROUT_PERIOD_VALUE=300
W_PRIORITY_FACTOR=100

sumo-gui -n $NET_FILE \
-r $ROUTES_FILE -a $ADD_FILES --routing-algorithm $ROUTING_ALG --statistic-output $STATS_OUT_FILE --step-length $STEP_LENGTH_VALUE --ignore-route-errors --time-to-teleport $TIME_TO_TELEPORT_VALUE --device.rerouting.probability $REROUT_PROB_VALUE --device.rerouting.period $REROUT_PERIOD_VALUE --weights.priority-factor $W_PRIORITY_FACTOR
