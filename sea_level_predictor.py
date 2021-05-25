import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv')
    # Create scatter plot
    # plt.figure(figsize=(18, 11))
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    # plt.xticks(ticks=[1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0], labels=[1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    plt.xlim(1850, 2075)


    # Create first line of best fit
    res = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], res.intercept + res.slope*df['Year'], color="red")


    # Create second line of best fit
    latest_years = df.loc[df['Year'] >= 2000]

    res_2 = linregress(x=latest_years['Year'], y=latest_years['CSIRO Adjusted Sea Level'])
    plt.plot([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075], res_2.intercept + res_2.slope*[1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075], color="green")

    # Add labels and title
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')
    plt.title('Rise in Sea Level')
    print(len(plt.gca().get_lines()[0].get_ydata().tolist()))
    print(len(df))
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
