import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please enter city name: ').lower()
        if city not in CITY_DATA.keys():
            print('Please choose one of the three cities')
            continue
        else:
            break


    # This code will ask the user for a specific month
    while True:
        month = input('Please enter a specific month or choose all: ').lower()
        if month not in ("january", "fabruary", "march", "april", "may", "june", "all"):
            print("Please choose all or the correct month from January to June")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter a specific day or choose all: ').lower()
        if day not in ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"):
            print("Please choose all or the correct day name")
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != "all":
        months = ["january", "fabruary", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df['month'] = df[df['month'] == month]

    if day != "all":
        df['day_of_week'] = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # Shows the most common month

    datetime = pd.to_datetime(df['Start Time'])
    print(f"Most common month is {df['month'].mode()[0]}")

    # Shows the most common day

    print(f"Most common day of week is {df['day_of_week'].mode()[0]}")

    # TO DO: display the most common start hour
    hour = datetime.dt.hour
    print(f"Most common start hour is {hour.mode()[0]}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print(f"Most common start station is {common_start}")

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(f"Most common end station is {common_end}")

    # TO DO: display most frequent combination of start station and end station trip
    df['comb'] = df['Start Station'] + " to " + df['End Station']
    print(f"Most common route is {df['comb'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(f"Total travel time is {df['Trip Duration'].sum()} seconds")

    # TO DO: display mean travel time
    print(f"Mean travel time is {df['Trip Duration'].mean()} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(f"Number of user types {df['User Type'].value_counts()}")

    # TO DO: Display counts of gender
    if 'Gender' in df and 'Birth Year' in df:
        print(f"Number of user types {df['Gender'].value_counts()}")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Gender' not in df and 'Birth Year' not in df:
        print("This city doesn't have Gender or Birth Year")
    else:
        print(f"Earliest birthdates is {df['Birth Year'].min()}")
        print(f"Most recent birthdates is {df['Birth Year'].max()}")
        print(f"Most common birthdates is {df['Birth Year'].mode()[0]}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_row(df):
    view_data = input("\nWould you like to view five rows of individual trip data? Enter yes or no\n").lower()
    start_loc = 0
    view_display = False
    if view_data == 'yes':
        view_display = True

    while (view_display):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        if view_data == 'yes':
            view_display = True
        else:
            view_display = False


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_row(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
