import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

 
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10)

 
    reg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series([i for i in range(1880, 2051)])
    plt.plot(years_extended, reg.intercept + reg.slope * years_extended, 'r', label='Best Fit Line 1')


    df_recent = df[df['Year'] >= 2000]
    reg_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series([i for i in range(2000, 2051)])
    plt.plot(years_recent, reg_recent.intercept + reg_recent.slope * years_recent, 'green', label='Best Fit Line 2')


    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    

    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()
plt.show()
