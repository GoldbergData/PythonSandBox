import time
import pandas as pd
import numpy as np
import os

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    months = ["january", "february", "march", "april", "may", "june"]
    days = ["monday", "tuesday", "wednesday", "thursday", "friday",
            "saturday", "sunday"]

    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use
    #  a while loop to handle invalid inputs
    print("Let's start with the data you're interested in. Enter your city "
          "of choice (Chicago, New York City, Washington)?")
    city = input("City: ").lower()

    while city not in CITY_DATA.keys():
        city = input("Invalid entry. Please Chicago, New York City, "
                     "or Washington: ").lower()

    # get user input for month (all, january, february, ... , june)
    month = input("Choose a month (January through June) to filter by, or all "
                  "for no "
                  "filter.").lower()

    while month not in months:
        if month == "all":
            break
        city = input("Invalid entry. Please only filter by January through "
                     "June, or all for no filter: ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Choose a day of the week (Monday through Sunday), or all for "
                "no filter.").lower()

    while day not in days:
        if day == "all":
            break
        day = input("Invalid entry. Please enter a valid weekday, or all for "
                    "no filter:").lower()

    print('-'*40)
    return city, month, day




def load_data(city, month="all", day="all"):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    # filter by month if applicable
    if month != "all":
        # use the index of the months list to get the corresponding int
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df["month"] == month]

        # filter by day of week if applicable
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df["month"].mode()[0]
    print("Most popular month: {}\n".format(popular_month))

    # display the most common day of week
    popular_day = df["day_of_week"].mode()[0]
    print("Most popular weekday: {}\n".format(popular_day))

    # display the most common start hour
    popular_start_hour = df["hour"].mode()[0]
    print("Most popular start hour: {}\n".format(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]
    print("Most common start station: {}\n".format(pop_start_station))

    # display most commonly used end station
    popular_end_station = df["End Station"].mode()[0]
    print("Most common end station: {}\n".format(pop_end_station))


    # display most frequent combination of start station and end station trip
    pop_start_station, pop_end_station, frequency = df.groupby(['Start Station',
                                                                'End Station']).size().reset_index().max(

    ).values
    print("Most frequent combination of start and end station trip: Start "
          "Station: {}, End Station: {}, Frequency: {}\n".format(pop_end_station,
                                               pop_end_station, frequency))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip_duration_sec = df["Trip Duration"].sum()
    print("Total trip duration (seconds): {}\n".format(total_trip_duration_sec))

    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean trip duration (seconds): {}\n".format(total_trip_duration_sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df["User Type"].value_counts()
    print("Count by user type: {}\n".format(user_type_count))


    # Display counts of gender
    gender_count = df["Gender"].value_counts()
    print("Count by gender: {}\n".format(gender_count))

    # Display earliest, most recent, and most common year of birth
    earliest_bd = df["Birth Year"].min()
    print("Earliest birthday: {}\n".format(earliest_bd))

    recent_bd = df["Birth Year"].max()
    print("Recent birthday: {}\n".format(recent_bd))

    common_bd = df["Birth Year"].mode()
    print("Most common birthday: {}\n".format(common_bd))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    import time
    import pandas as pd
    import numpy as np
    import os
    while True:
        city, month, day = get_filters()
        if os.getcwd() == os.getcwd() + "/project_divy_bike_share":
            continue
        else:
            os.chdir(os.getcwd() + "/project_divy_bike_share")
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
