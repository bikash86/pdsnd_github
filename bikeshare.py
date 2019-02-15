import time
import calendar as cal
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['all', 'jan', 'feb', 'mar', 'apr', 'may', 'jun']

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
    city = input("Which city would you like to explore: Chicago, New York City or Washington?\n").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Please choose one of these: Chicago, New York City or Washington\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month? Jan, Feb, Mar, Apr, May, Jun or all?\n").lower()
    while month not in MONTHS:
        month = input("Please choose one of these: Jan, Feb, Mar, Apr, May, Jun or all\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    try:
        day = int(input("Which day? Please input 1-7 for Mon-Sun or 0 for all.\n"))
    except:
        day = 8
    while (day < 0 or day > 7):
        try:
            day = int(input("Please input a number between 1-7 for Mon-Sun or 0 for all.\n"))
        except:
            day = 8


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday + 1
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month)

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 0:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        popular_month = cal.month_name[df['month'].value_counts().idxmax()]
        print('Most popular month is: ', popular_month)

    # TO DO: display the most common day of week
    if day == 0:
        popular_day = cal.day_name[df['day_of_week'].value_counts().idxmax()]
        print('Most popular day of week is: ', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('Most popular hour of day is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station is: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station is: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['trip'].value_counts().idxmax()
    print('Most commonly used trip: ', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is {} seconds'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Average travel time is', df['Trip Duration'].mean(), 'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of different user types:')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('\nCounts of gender:')
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nEarliest year of birth is ', int(df['Birth Year'].min()))
        print('Most recent year of birth is ', int(df['Birth Year'].max()))
        print('Most common year of birth is ', int(df['Birth Year'].value_counts().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def sample_data(df):
    # Display sample data from DataFrame
    index = 0
    while True:
        sample_data = input('\nWould you like to see some sample data? Enter yes or no.\n')
        if sample_data.lower() != 'yes':
            break
        else:
            print(df[index:index + 5])
            index += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        sample_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
