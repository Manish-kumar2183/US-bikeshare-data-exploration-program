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
    while(True):
        city=input('enter the name of city to analyze')
        city=city.lower()
        if city in('chicago','new york city','washington'):
            break
        else:
            print('invalid input, please try again later')


        # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('if want detail of a particular month from first six months then enter name of month otherwise type "all"    ')
        month=month.lower()
        if month in('january','february','march','april','may','june','all'):
            break
        else:
            print('invalid input, please try again later')

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('want detail of specific day or "all"   ')
        day=day.lower()
        if day in('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
            break
        else:
            print('invalid input, please try again later')

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['weekday']=df['Start Time'].dt.weekday_name
    if month!='all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df[df['month']==month]
    if day!='all':
        df[df['weekday']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("most common month ",df['month'].mode()[0],"\n")

    # TO DO: display the most common day of week
    print("common day of the week ",df['weekday'].mode()[0],"\n")

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print('common start hour ',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("most common used start station:-",df['Start Station'].mode()[0],"\n")

    # TO DO: display most commonly used end station
    print("most common used end station ",df['End Station'].mode()[0],"\n")

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+' '+['End Station']
    print("most frequent combination ",df['combination'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time ",df['Trip Duration'].sum(),"\n")

    # TO DO: display mean travel time
    print("mean travel time ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "\n")
    if city != 'washington':
        # Display counts of gender
        gen = df.groupby(['Gender'])['Gender'].count()
        print(gen)
        # Display earliest, most recent, and most common year of birth
        mryob = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        eyob = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        mcyob = df['Birth Year'].mode()[0]
        print("The earliest year of birth is ", eyob, "\n")
        print("The most recent year of birth is ", mryob, "\n")
        print("The most common year of birth is ", mcyob, "\n")


    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x=1
    while True:
        raw=input('like to see some more raw data? enter y or n')
        if raw.lower()=='y':
            print(df[x:x+5])
            x=x+5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
