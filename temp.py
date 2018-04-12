# Time Series analysis of mean global land temperature (from Berkeley Earth) - April 2018
import numpy as np
import matplotlib.pyplot as plt


# Loads data

temp_file = open('data.txt','r')

# Array containing all the monthly temperatures
monthly_temp = np.zeros(3211)
# Array containing the uncertainty with which each measurement is made
uncertainties = np.zeros(3211)

# Ignores the lines that are commented
counter = -35

# Each stripped line has length 95
for line in temp_file:

    if counter >= 0:
        line = line.strip()
        # NaN are counted as zero
        if line[17] != 'N':
            monthly_temp[counter] = float(line[14:20])
        # Nan are counted as 7
        if line[24] != 'N':
            uncertainties[counter] = float(line[22:27])
        else:
            uncertainties[counter] = 7

    # Keeps track of which line is being studied
    counter += 1

temp_file.close()


# Plots TS

time = np.linspace(1750,2017,3211)

plt.plot(time,monthly_temp)
plt.title('Evolution of the global monthly average land temperature over time')
plt.xlabel('Year')
plt.ylabel('Average temperature difference')
plt.show()

plt.plot(time,uncertainties)
plt.title('Evolution of the uncertainty of measurements over time')
plt.xlabel('Year')
plt.ylabel('Uncertainty (degree Celsius)')
plt.show()
