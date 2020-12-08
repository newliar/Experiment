from choose_tel import Choose
import os
import configuration

# ch = Choose()
# Choose.choose_tel_station(ch, 5, 5, 1000)
print(os.getcwd() + '/time_cost/' + 'CPU_CLOCK_' + str(configuration.CPU_CLOCK) + '_TASK_SIZE_'
                        + str(configuration.TASK_SIZE) + '_VEHICLE_POWER_' + str(configuration.VEHICLE_POWER) +
                        '_time_cost.csv')