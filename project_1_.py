import pandas as pd
import matplotlib.pyplot as plt

# addding the csv file path
project1_csv_path= "D:\Python\Project_1/results.csv"

# reading the csv file
project1_file= pd.read_csv(project1_csv_path)
project1_file= project1_file.sort_values('year')

# calculating a moving average of 10 years
project1_file['NYC_moving_average_10']=project1_file['newyork_temp'].rolling(10).mean()
project1_file['global_moving_average_10']=project1_file['global_temp'].rolling(10).mean()

# eliminating the nulls
project1_file.dropna(inplace=True)

# selecting the x and y axis for the plot 
ax = project1_file.plot(x='year', y=['NYC_moving_average_10', 'global_moving_average_10'])

# Adjusting the legend
plt.legend(["New York 10-year moving average temperature", "global 10-year moving average temperature"], loc ="upper left")

# adding xlable, ylabe and title for the plot
ax.set_xlabel('Years')
ax.set_ylabel('Average Temperature in Celcius')
ax.set_title('New York VS Global Weather Trends')

# here I am just displaying the info on the terminal to observe if there is any null values
project1_file.info()

# print the dataframe
print(project1_file)

# show the visualization of the dataframe
plt.show()


