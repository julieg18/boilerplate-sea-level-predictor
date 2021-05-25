import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("./epa-sea-level.csv")
    plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    plt.xlim(1850, 2075)

    # Create first line of best fit
    res = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    years_arr = pd.Series(range(1880, 2051))
    plt.plot(years_arr, res.intercept + res.slope * years_arr, color="red")

    # Create second line of best fit
    latest_years = df.loc[df["Year"] >= 2000]
    res_2 = linregress(
        x=latest_years["Year"], y=latest_years["CSIRO Adjusted Sea Level"]
    )
    recent_years_arr = pd.Series(range(2000, 2051))
    plt.plot(
        recent_years_arr,
        res_2.intercept + res_2.slope * recent_years_arr,
        color="green",
    )

    # Add labels and title
    plt.ylabel("Sea Level (inches)")
    plt.xlabel("Year")
    plt.title("Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
