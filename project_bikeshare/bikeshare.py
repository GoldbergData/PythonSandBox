import time
import pandas as pd
import calendar
from datetime import date
import math

CITY_DATA = {"chicago": "chicago.csv",
             "new york city": "new_york_city.csv",
             "washington": "washington.csv"}

months = ["january", "february", "march", "april", "may", "june", "all"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday",
        "saturday", "sunday", "all"]
cities = ["Chicago", "New York City", "Washington"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns: (str) city - name of the city to analyze (str) month - name of
    the month to filter by, or "all" to apply no month filter (str) day -
    name of the day of week to filter by, or "all" to apply no day filter
    """
    import os

    while True:
        print("Hello! Let\"s explore U.S. bikeshare data!\n")
        # get user input for city (chicago, new york city, washington). HINT:
        #  Use a while loop to handle invalid inputs
        print("Let's start with the data you're interested in. Enter your city "
              "of choice (Chicago, New York City, Washington): ")
        city = input("City: ").lower()
        i = 0
        while city not in CITY_DATA.keys():
            city = input("Invalid entry. Please Chicago, New York City, "
                         "or Washington: ").lower()
            i += 1
            if i == 2:
                print(os.getcwd())
                print("\nLooks like you're having trouble. Here are the "
                      "available inputs: \n")
                print(cities)
                print()
                city = input("Enter a city: ").lower()
                i += 1
            if i >= 3 and i % 3:
                quitting = input("Do you want to quit (yes/no)? ").lower()
                if quitting == "yes":
                    break
                else:
                    city = input("Enter your city of choice (Chicago, "
                                 "New York City, Washington): ").lower()
        if city not in CITY_DATA.keys():
            quitting = "yes"
            return quitting

        # get user input for month (all, january, february, ... , june)
        month = input(
            "Choose a month (January through June) to filter by, "
            "or all: ").lower()
        i = 0
        while month not in months:
            if month == "all":
                break
            month = input(
                "Invalid entry. Please only filter by January through "
                "June, or all: ").lower()
            i += 1
            if i == 2:
                print("\nLooks like you're having trouble. Here are the "
                      "available inputs: \n")
                print(months)
                print()
                month = input("Choose a month or all: ").lower()
            if i >= 3 and i % 3:
                quitting = input("Do you want to quit (yes/no)? ").lower()
                if quitting == "yes":
                    break
                else:
                    month = input(
                        "Choose a month (January through June) to filter by, "
                        "or all: ").lower()
        if month not in months:
            quitting = "yes"
            return quitting

        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input(
            "Choose a day of the week (Monday through Sunday), or all: "
            "").lower()
        i = 0
        while day not in days:
            if day == "all":
                break
            day = input(
                "Invalid entry. Please enter a valid weekday, or all: ").lower()
            i += 1
            if i == 2:
                print("\nLooks like you're having trouble. Here are the "
                      "available inputs: \n")
                print(days)
                print()
                day = input("Choose a day of the week to filter, "
                            "or all.").lower()
            if i >= 3 and i % 3:
                quitting = input("Do you want to quit (yes/no)? ").lower()
                if quitting == "yes":
                    break
                else:
                    day = input("Choose a day of the week to filter, "
                                "or all: ").lower()
        if day not in days:
            quitting = "yes"
            return quitting

        print("-" * 40)
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

    if city in ["chicago", "new york city"]:

        # imputed age for Chicago and New York City
        df["imputed_age"] = round(date.today().year - df["Birth Year"])
        df["binned_age"] = pd.cut(df["imputed_age"], list(range(1, 100, 15)))

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    if len(df["month"].unique()) != 1:
        # display the most common month
        popular_month = df["month"].mode()[0]
        print("Most popular month: {}\n".format(popular_month))
    else:
        print("Skipped popular month calculation due to filter.\n")

    if len(df["day_of_week"].unique()) != 1:
        # display the most common day of week
        popular_day = df["day_of_week"].mode()[0]
        print("Most popular weekday: {}\n".format(popular_day))
    else:
        print("Skipped popular day of week calculation due to filter.\n")

    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    popular_start_hour = df["hour"].mode()[0]
    print("Most popular start hour: {}\n".format(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    pop_start_station = df["Start Station"].mode()[0]
    print("Most common start station: {}\n".format(pop_start_station))

    # display most commonly used end station
    pop_end_station = df["End Station"].mode()[0]
    print("Most common end station: {}\n".format(pop_end_station))

    # display most frequent combination of start station and end station trip
    pop_start_station, pop_end_station, frequency = df.groupby(["Start "
                                                                "Station",
                                                                "End Station"
                                                                ""]).size().reset_index().max().values
    print("Most frequent combination of start and end station trip: Start "
          "Station: {},\nEnd Station: {}. Frequency: {}\n".format(
        pop_end_station,
        pop_end_station, frequency))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df, city):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration Statistics...\n")
    start_time = time.time()

    # display group travel time
    print("Group Stats:\n")
    df_grouped = df.groupby(["month"])
    df_grouped_dict = dict(df_grouped["Trip Duration"].sum())
    print("Total trip duration by month:\n")
    for k, v in df_grouped_dict.items():
        k = calendar.month_name[k]
        v = "{:,} hours, {:,} minutes, {:,} seconds.".format(
            (v // 60 // 60).__int__(), (v % 60 % 60).__int__(),
            (v % 60).__int__())
        print("{}: {}".format(k, v))
    print()
    print()

    df_grouped_dict = dict(df_grouped["Trip Duration"].mean())
    print("Mean trip duration by month:\n")
    for k, v in df_grouped_dict.items():
        k = calendar.month_name[k]
        v = "{:,} hours, {:,} minutes, {:,} seconds.".format(
            (v // 60 // 60).__int__(), (v % 60 % 60).__int__(),
            (v % 60).__int__())
        print("{}: {}".format(k, v))
    print()
    print()

    df_grouped = df.groupby(["day_of_week"])
    df_grouped_dict = dict(df_grouped["Trip Duration"].sum())
    print("Total trip duration by weekday:\n")
    for k, v in df_grouped_dict.items():
        v = "{:,} hours, {:,} minutes, {:,} seconds.".format(
            (v // 60 // 60).__int__(), (v % 60 % 60).__int__(),
            (v % 60).__int__())
        print("{}: {}".format(k, v))
    print()
    print()

    df_grouped_dict = dict(df_grouped["Trip Duration"].mean())
    print("Mean trip duration by weekday:\n")
    for k, v in df_grouped_dict.items():
        v = "{:,} hours, {:,} minutes, {:,} seconds.".format(
            (v // 60 // 60).__int__(), (v % 60 % 60).__int__(),
            (v % 60).__int__())
        print("{}: {}".format(k, v))
    print()
    print()

    if city in ["chicago", "new york city"]:
        df_grouped = df.groupby(["Gender"])
        df_grouped_dict = dict(df_grouped["Trip Duration"].sum())
        print("Total trip duration by Gender:\n")
        for k, v in df_grouped_dict.items():
            v = "{:,} hours, {:,} minutes, {:,} seconds.".format(
                (v // 60 // 60).__int__(), (v % 60 % 60).__int__(),
                (v % 60).__int__())
            print("{}: {}".format(k, v))
        print()
        print()

        df_grouped_dict = dict(df_grouped["Trip Duration"].mean())
        print("Mean trip duration by Gender:\n")
        for k, v in df_grouped_dict.items():
            v = "{:,} hours, {:,} minutes, {:,} seconds.".format(
                (v // 60 // 60).__int__(), (v % 60 % 60).__int__(),
                (v % 60).__int__())
            print("{}: {}".format(k, v))
        print()
        print()

        df_grouped = df.groupby(["binned_age"])
        df_grouped_dict = dict(df_grouped["Trip Duration"].sum())
        print("Total trip duration by age (inferred from Birth Year):\n")
        for k, v in df_grouped_dict.items():
            v = "{:,} hours, {:,} minutes, {:,} seconds.".format(
                (v // 60 // 60).__int__(), (v % 60 % 60).__int__(),
                (v % 60).__int__())
            print("{}: {}".format(k, v))
        print()
        print()

        df_grouped_dict = dict(df_grouped["Trip Duration"].mean())
        print("Mean trip duration by age:\n")
        for k, v in df_grouped_dict.items():
            if math.isnan(v):
                continue
            v = "{:,} hours, {:,} minutes, {:,} seconds.".format(
                (v // 60 // 60).__int__(), (v % 60 % 60).__int__(),
                (v % 60).__int__())
            print("{}: {}".format(k, v))
        print()
        print()

    df_grouped = df.groupby(["Start Station", "End Station"])
    df_grouped_dict = dict(df_grouped["Trip Duration"].sum().sort_values(
        ascending=False).head(n=5))
    print("Top five (by total trip duration) start/end stations total "
          "trip duration:\n")
    for k, v in df_grouped_dict.items():
        v = "{:,} hours, {:,} minutes, {:,} seconds.".format(
            (v // 60 // 60).__int__(), (v % 60 % 60).__int__(),
            (v % 60).__int__())
        print("{}: {}".format(k, v))
    print()
    print()

    df_grouped_dict = dict(df_grouped["Trip Duration"].mean().sort_values(
        ascending=False).head(n=5))
    print("Top five (by mean trip duration) start/end stations mean trip "
          "duration:\n")
    for k, v in df_grouped_dict.items():
        v = "{:,} hours, {:,} minutes, {:,} seconds.".format(
            (v // 60 // 60).__int__(), (v % 60 % 60).__int__(),
            (v % 60).__int__())
        print("{}: {}".format(k, v))
    print()
    print()

    # display total travel time
    print("Total Stats:\n")
    total_trip_duration_sec = (df["Trip Duration"].sum() % 60).__int__()
    total_trip_duration_min = (df["Trip Duration"].sum() // 60 % 60).__int__()
    total_trip_duration_hr = (df["Trip Duration"].sum() // 60 // 60).__int__()
    print("Total trip duration: {:,} hours, {:,} minutes, {:,} seconds \n".format(
        total_trip_duration_hr, total_trip_duration_min, total_trip_duration_sec))

    # display mean travel time
    mean_travel_time_sec = (df["Trip Duration"].mean() % 60).__int__()
    mean_travel_time_min = (df["Trip Duration"].mean() // 60 % 60).__int__()
    mean_travel_time_hr = (df["Trip Duration"].mean() // 60 // 60).__int__()
    print("Mean duration: {:,} hours, {:,} minutes, {:,} seconds \n".format(
        mean_travel_time_hr, mean_travel_time_min, mean_travel_time_sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types
    user_type_count = df["User Type"].value_counts()
    user_type_count_dict = dict(user_type_count)
    print("Count by user type:\n")
    for k, v in user_type_count_dict.items():
        print("{}: {:,}".format(k, v))
    print()
    print()

    # Display counts of gender
    gender_count = df["Gender"].value_counts()
    gender_count_dict = dict(gender_count)
    print("Count by gender:\n")
    for k, v in gender_count_dict.items():
        print("{}: {:,}".format(k, v))
    print()
    print()

    # Display earliest, most recent, and most common year of birth
    earliest_bd = df["Birth Year"].min().__int__()
    print("Earliest birth year: {}\n".format(earliest_bd))

    recent_bd = df["Birth Year"].max().__int__()
    print("Most recent birth year: {}\n".format(recent_bd))

    common_bd = df["Birth Year"].mode().__int__()
    print("Most common birth year: {}\n".format(common_bd))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def main():
    while True:
        city, month, day = get_filters()
        if (city not in CITY_DATA.keys() or month not in months or day not in
                days):
            break
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df, city)
        if city in ["chicago", "new york city"]:
            user_stats(df)
        restart = input("\nWould you like to restart? Enter yes or "
                        "no.\n").lower()
        if restart != "yes":
            break


if __name__ == "__main__":
    main()
