import time
import pandas as pd
import numpy as np

'''
 In this project, the student had to make use of Python to explore data related
 to bike share systems for three major cities in the United States — Chicago,
 New York City, and Washington. The student had to write code to (a) import
 the data and answer interesting questions about it by computing descriptive
 statistics,
 and (b) write a script that takes in raw input to create an interactive
 experience in the terminal to present these statistics.

'''

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
        if city in ['chicago','new york city','washington']:
            break
        else:
            print("wrong city!")
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while(True):
        if month in ['all','january','february','march','april','may','june']:
            break
        else:
            print("wrong month!")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):
        if month in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            break
        else:
            print("wrong day!")

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
    


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The Most Common Months : ",most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print("The Most Common Day : ",most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The Most Common Start Hour : ",most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The Most Common Start Station : ",most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_used_end_station = df['End Station'].mode()[0]
    print("The Most Common Used End Station : ",most_common_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end_trip = most_common_start_station+ " " + most_common_used_end_station
    print("The Most Frequent Combination Of Start Station And End Station Trip : ",combination_start_end_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


""" Function to show trip's statistics """
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The Total Travel Time : ",total_travel_time)  

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The Mean Travel Time : ",mean_travel_time) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print("The Counts Of User Types : ",counts_user_types) 
        
    # TO DO: Display counts of gender
    counts_gender = df['Gender'].value_counts()
    print("The Counts Of Genders : ",counts_gender) 

    # TO DO: Display earliest, most recent, and most common year of birth
    
    # Display earliest
    earliest_year_of_birth = df['Birth Year'].min()
    print("The Earliest Year Of Birth : ",earliest_year_of_birth) 
    
    # Display most recent
    most_recent = df['Birth Year'].max()
    print("The Most Recent Year Of Birth : ",most_recent) 
    
    # most common year of birth
    most_common_year_of_birth = df['Birth Year'].value_counts().idxmax()
    print('The Most Common Year Of Birth : ', most_common_year_of_birth)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
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
