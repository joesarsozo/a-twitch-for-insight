"""
Jianna Braza and Joseph Sarsozo
CSE 163 AH
This files contains all the necessary tests for the functions
that were implemented in the analysis.py file
"""
import analysis
import pandas as pd


def main():
    """
    initializes the streamer and game datasets
    and runs all of the functions in analysis.py
    adjusts the dataset to be easier to use
    merge them together to answer research question 2
    calculates the percent of mature streamers found
    in the top n% of streamers
    and plots the watch time vs stream time
    of both games and streamers.
    """
    streamer_file_name = "Data\\twitchdata-update.csv"
    streamer_data = pd.read_csv(streamer_file_name)
    game_file_name = "Data\\Twitch_game_data.csv"
    game_data = pd.read_csv(game_file_name, encoding='cp1252')
    print('stream time and watch time before in minutes:')
    print('for the streamer dataset')
    print(streamer_data['Watch time(Minutes)'])
    print(streamer_data['Stream time(minutes)'])
    streamer_data = analysis.minutes_to_hours(streamer_data)
    print('stream time and watch time afterwards in hours:')
    print(streamer_data['Watch time(Hours)'])
    print(streamer_data['Stream time(Hours)'])
    print()
    print('game dataset hours streamed before:')
    print(game_data['Hours_Streamed'])
    game_data = analysis.fix_hours_streamed(game_data)
    print('game dataset hours streamed without the word "hours" in it')
    print('and changed into an int:')
    print(game_data['Hours_Streamed(number)'])
    merged = analysis.merge_datasets(streamer_data, game_data)
    print('Datasets merged together using peak viewers')
    print(merged)
    print('upon further research, most game and streamer pairs are not accurate')
    print()
    print('testing maturity vs popularity method:')
    print('percent mature in top 50 percent streamers:')
    print(analysis.mature_vs_popularity_top_n(streamer_data, 50))
    print('percent mature in top 25 percent streamers:')
    print(analysis.mature_vs_popularity_top_n(streamer_data, 25))
    print('percent mature in top 10 percent streamers:')
    print(analysis.mature_vs_popularity_top_n(streamer_data, 10))
    print('percent mature in top 5 percent streamers:')
    print(analysis.mature_vs_popularity_top_n(streamer_data, 5))
    print()
    print('plots:')
    analysis.plotly_streamer_data(streamer_data)
    analysis.plotly_game_data(game_data)


if __name__ == '__main__':
    main()
