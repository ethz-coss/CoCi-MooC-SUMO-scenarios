# Run simulation
## A scaling factor is introduced to tests 40 different scenarios with increasing traffic demand.

import os, time

def main():
    #create results folder
    if not os.path.exists('data/results'):
        os.makedirs('data/results')

    total_veh_ref = 315000 # number of vehicles for scale factor 1.0
    scale = 2

    # running a loop from scale factor 2.0 to scale factor 0.05 and writing the results files.
    while scale > 0.0:
        start = time.time()
        print('STARTING sumo simulation with scale {:04.2f}'.format(scale))
        scaled_veh_ref = total_veh_ref * scale
        max_num_teleports = int(scaled_veh_ref * 0.005) #value for stopping the simulation at that iteration
        OUTPUT_PREFIX_ARG = '--output-prefix scale_{:04.2f}_'.format(scale)
        STAT_OUT_ARG = '--statistic-output data/results/overall_stats.xml'.format(scale)
        SUMMARY_ARG = '--summary data/results/summary.xml'.format(scale)
        MAX_TELEP_ARG = '--max-num-teleports {:d}'.format(max_num_teleports)
        SCALE_ARG = '--scale {:f}'.format(scale)
        CONFIG_FILE = r'data/compar_002.sumo.cfg'
        
        # running the simulation
        # ref https://sumo.dlr.de/docs/sumo.html

        os.system(
            "sumo -c {CONFIG_FILE} {OUTPUT_PREFIX_ARG} {STAT_OUT_ARG} {SUMMARY_ARG} {MAX_TELEP_ARG} {SCALE_ARG} --threads 1 -W"
            .format(CONFIG_FILE=CONFIG_FILE, OUTPUT_PREFIX_ARG=OUTPUT_PREFIX_ARG, STAT_OUT_ARG=STAT_OUT_ARG, 
                SUMMARY_ARG=SUMMARY_ARG, MAX_TELEP_ARG=MAX_TELEP_ARG, SCALE_ARG=SCALE_ARG))
        
        # measuring time for performance
        end = time.time()
        elapsed_time = (end-start)/60
        
        print('\nDONE sumo simulation with scale {:04.2f} in {:04.1f} minutes \n'.format(scale, elapsed_time))
        
        scale -= 0.05 #updating scale value

if __name__ == "__main__":
    main()