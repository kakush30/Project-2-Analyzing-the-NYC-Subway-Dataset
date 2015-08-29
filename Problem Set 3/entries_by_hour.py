import matplotlib.pyplot as plt
import numpy as np
import pandas

def entries_by_hour(turnstile_weather):
     df = pandas.read_csv(turnstile_weather)
     
     xmin = ymin = 0
     xmax = 23
     ymax = 3000

        
     
     pivot = pandas.tools.pivot.pivot_table(df, values='ENTRIESn_hourly', columns=['Hour'], aggfunc=np.mean)
     print pivot
     entries = pivot.values
     hours = pivot.index
     
    
     
     plt.plot(hours, entries, '-o')

     plt.axis([xmin, xmax, ymin, ymax])
     plt.suptitle('Average subway entries by time of day')
     plt.xlabel('Time of day (24-hr)')
     plt.ylabel('Entries')

     return plt
    


if __name__ == '__main__':
    filename = 'turnstile_data_master_with_weather.csv'
    print entries_by_hour(filename)