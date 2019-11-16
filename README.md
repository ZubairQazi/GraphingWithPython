# Irrigation-Data-Visualizer
Python script designed to parse and graph multiple data fields taken from irrigation tools from csv files, using the python libraries matplotlib and dateutil.

### graphing.py
The main script for the project, which uses matplotlib in order to visualize very large data sets from irrigation tools. Each 
column in the data set is parsed by name and graphed separately with their corresponding labels.
The script also uses to dateutil library to be able to parse and graph the data based on their corresponding times and dates.

### input1.csv
This csv is an example of the data which can be parsed and visualized by the python script. 
The data can also be easily visualized using pandas, but per requirements for the project matplotlib was used. 
