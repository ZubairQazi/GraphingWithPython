import matplotlib as mplb
from matplotlib import pyplot as plt
import csv
from dateutil.parser import parse

# The window sizes can be changed here (width, height)
fig = plt.figure(figsize=(12, 8))
fig2 = plt.figure(figsize=(8, 8.5))
fig3 = plt.figure(figsize=(8, 8.5))
fig4 = plt.figure(figsize=(8, 8.5))

# plt.subplots_adjust(hspace = 0.4)

# Lists for all the data points in each row, relative to the columns
conductivity = []
conductivity_corr = []
dielectric_const_imag = []
dielectric_const_real = []
leaf_id = []
sensor_id = []
seq = []
temp_c = []
temp_f = []
timestamp = []
volwatcont = []

# This correlates to the number of rows in the csv file
row_number = 1
row_numbers = []

filename = input("Enter file name: ")

with open(filename, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots)
    for row in plots:
        row_numbers.append(row_number)
        row_number += 1

    # appending row values to the respective columns (order is important!)
        # conductivity.append(float(row[0]))
        # conductivity_corr.append(float(row[1]))
        # dielectric_const_imag.append(float(row[2]))
        # dielectric_const_real.append(float(row[3]))
        #leaf_id.append(float(row[4]))
        #sensor_id.append(float(row[5]))
        seq.append(float(row[6]))
        # temp_c.append(float(row[7]))
        temp_f.append(float(row[8]))
        timestamp.append(parse(row[9]))
        volwatcont.append(float(row[10]))

    row_numbers.reverse()

    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax3 = fig2.add_subplot()

    ax4 = fig3.add_subplot()

    ax5 = fig4.add_subplot()


    ax1.plot(row_numbers, volwatcont)
    ax1.set_title('Moisture vs. Row Number')
    ax1.set_xlabel('Row Number')
    ax1.set_ylabel('Moisture')

    ax2.plot(row_numbers, seq)
    ax2.set_title('Sequence vs. Row Number')
    ax2.set_xlabel('Row Number')
    ax2.set_ylabel('Sequence')

    ax3.plot_date(timestamp, volwatcont)
    ax3.set_title('Moisture vs. Time Stamp')
    ax3.set_xlabel('Time Stamp')
    ax3.set_ylabel('Moisture')

    ax4.plot_date(timestamp, seq)
    ax4.set_title('Sequence vs. Time Stamp')
    ax4.set_xlabel('Time Stamp')
    ax4.set_ylabel('Sequence')

    ax5.plot_date(timestamp, temp_f)
    ax5.set_title('Temperature(f) vs. Time Stamp')
    ax5.set_xlabel('Time Stamp')
    ax5.set_ylabel('Temperature(f)')

    plt.show()
