import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def minutes_to_hours(streamer_data):
    streamer_data['Watch time(Hours)'] = streamer_data['Watch time(Minutes)'] / 60
    streamer_data['Stream time(Hours)'] = streamer_data['Stream time(minutes)'] / 60


def game_hours_streamed_fix(game_data):
    game_data['Hours_Streamed(number)'] = game_data['Hours_Streamed'].str[:game_data['Hours_Streamed'].index('hours')]
    print(game_data['Hours_Streamed'])


def merge_datasets(streamer_data, game_data):
    merged = streamer_data.merge(game_data, left_on='Peak viewers', right_on='Peak_viewers', how='inner')
    merged = merged.loc[:, ['Game', 'Channel']]
    return merged


def mature_vs_popularity_top_500(streamer_data):
    streamer_data = streamer_data.sort_values(by='Average viewers', ascending=True)
    streamer_data = streamer_data.nlargest(500, 'Average viewers')
    streamer_data = streamer_data[streamer_data['Mature'] == True]
    num_mature = len(streamer_data)
    return (num_mature / 230) * 100


def mature_vs_popularity_top_250(streamer_data):
    streamer_data = streamer_data.sort_values(by='Average viewers', ascending=True)
    streamer_data = streamer_data.nlargest(250, 'Average viewers')
    streamer_data = streamer_data[streamer_data['Mature'] == True]
    num_mature = len(streamer_data)
    return (num_mature / 230) * 100


def mature_vs_popularity_top_50(streamer_data):
    streamer_data = streamer_data.sort_values(by='Average viewers', ascending=True)
    streamer_data = streamer_data.nlargest(50, 'Average viewers')
    streamer_data = streamer_data[streamer_data['Mature'] == True]
    num_mature = len(streamer_data)
    return (num_mature / 230) * 100


def main():
    streamer_file_name = "Data\\twitchdata-update.csv"
    streamer_data = pd.read_csv(streamer_file_name)
    game_file_name = "Data\\Twitch_game_data.csv"
    game_data = pd.read_csv(game_file_name, encoding='cp1252')
    minutes_to_hours(streamer_data)
    merged = merge_datasets(streamer_data, game_data)
    percent_top_500 = mature_vs_popularity_top_500(streamer_data)
    percent_top_250 = mature_vs_popularity_top_250(streamer_data)
    percent_top_50 = mature_vs_popularity_top_250(streamer_data)


if __name__ == '__main__':
    main()