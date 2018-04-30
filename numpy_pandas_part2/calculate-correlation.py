import pandas as pd
import os

cwd = os.getcwd()
filename = "nyc_subway_weather.csv"
subway_df = pd.read_csv("{}/{}".format(cwd, filename))


def correlation(x, y):
    """
    Fill in this function to compute the correlation between the two
    input variables. Each input is either a NumPy array or a Pandas
    Series.

    correlation = average of (x in standard units) times (y in standard units)

    Remember to pass the argument "ddof=0" to the Pandas std() function!
    """
    z_score_x = (x - x.mean()) / x.std(ddof=0)
    z_score_y = (y - y.mean()) / y.std(ddof=0)
    cor = (z_score_x * z_score_y).mean()
    return cor

entries = subway_df['ENTRIESn_hourly']
cum_entries = subway_df['ENTRIESn']
rain = subway_df['meanprecipi']
temp = subway_df['meantempi']

print(correlation(entries, rain))
print(correlation(entries, temp))
print(correlation(rain, temp))

print(correlation(entries, cum_entries))