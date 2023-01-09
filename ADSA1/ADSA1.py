import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data into a DataFrame
df = pd.read_csv("CO2 emissions (metric tons per capita).csv")

# Set the index to the "country" column
df.set_index("country", inplace=True)

def line_plot(countries,years):
    # Create the line plot
    # for country in countries:
    #     plt.plot(years, df.loc[country, years], label=country, figsize=(14,8))
    df.loc[countries, years].plot(kind="line", figsize=(14, 8))
    plt.xlabel("Country")
    plt.ylabel("CO2 emissions (metric tons per capita)")
    plt.title("CO2 emissions (line plot)")
    plt.legend()
    # Display the plot
    plt.show()

def bar_plot(countries,years):
    # Create the bar plot
    df.loc[countries, years].plot(kind="bar", figsize=(14, 8))
    plt.xlabel("Country")
    plt.ylabel("CO2 emissions (metric tons per capita)")
    plt.title("CO2 emissions (bar plot)")
    # Display the plot
    plt.show()
    
def pie_plot(countries,years):
    labels = countries
    sizes = df.loc[countries, years]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()


# Define the years and countries to include in the plots
years = ["1990", "1995", "2000", "2005", "2010", "2015"]
countries = ["France", "Portugal", "Japan", "Germany"]

line_plot(countries,years)
bar_plot(countries,years)
pie_plot(countries,"2015")
