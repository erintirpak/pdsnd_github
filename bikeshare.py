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
    city = 'city'
    cities = ['chicago', 'new york city', 'washington']
    while city not in cities:
        city = input("Please enter the city you'd like to analyze (must be chicago, new york city, or washington)").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = 'month'
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in months:
              month = input("Please enter the name of the month you'd like to analyze (from January through June, or 'all' to apply no month filter)").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = 'day'
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days:
              day = input("Please enter the name of the day you'd like to analyze (or 'all' to apply no day filter)").lower()

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
   # copied from practice problem 3
   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    commonth = df['month'].mode()[0]
    print('most common month: {}'.format(commonth))

    # TO DO: display the most common day of week
    comweek = df['day_of_week'].mode()[0]
    print('most common day of the week: {}'.format(comweek))

    # TO DO: display the most common start hour
    #df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    comhour = df['hour'].mode()[0]
    print('most common start hour: {}'.format(comhour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    comstart = df['Start Station'].mode()[0]
    print('Most commonly used start station: {}'.format(comstart))

    # TO DO: display most commonly used end station
    comend = df['End Station'].mode()[0]
    print('Most commonly used end station: {}'.format(comend))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combo'] = df['Start Station'] + ' to ' + df['End Station']
    comcombo = df['Combo'].mode()[0]
    print('The most frequent combination of start station and end station: from {}'.format(comcombo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print('The total travel time is {} seconds'.format(total))

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print('The mean travel time is {} seconds'.format(mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # from Practice Problem 2
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if city == 'washington':
        print('There is not gender data for Washington')
    else:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('There is not birth year data for Washington')
    else:
        early = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
        print('The earliest year of birth is ', early)
        print('The most recent year of birth is ', recent)
        print('The most common year of birth is ', common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        lines = 'start'
        i = 0
        while lines != 'no':
            lines = input('Would you like to see 5 (more) lines of raw data? Enter yes or no.\n').lower()
            if lines == 'yes':
                j = i + 5
                print(df[i:j])
                i += 5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
