import pandas as pd


def minutes_to_hours(streamer_data):
    streamer_data['Watch time(Hours)'] = streamer_data['Watch time(Minutes)'] / 60
    streamer_data['Stream time(Hours)'] = streamer_data['Stream time(minutes)'] / 60


def merge_datasets(streamer_data, game_data):
    merged = streamer_data.merge(game_data, left_on='Peak viewers', right_on='Peak_viewers', how='inner')
    return merged


def mature_vs_popularity(streamer_data):
    streamer_data = streamer_data.sort_values(by='Average viewers', ascending=True)
    streamer_data = streamer_data.nlargest(500, 'Average viewers')
    streamer_data = streamer_data[streamer_data['Mature'] == True]
    num_mature = len(streamer_data)
    percent = (num_mature / 230) * 100


def main():
    streamer_file_name = "C:\\Users\\jiann\\CS163Final\\a-twitch-for-insight\\Data\\twitchdata-update.csv"
    streamer_data = pd.read_csv(streamer_file_name)
    game_file_name = "C:\\Users\\jiann\\CS163Final\\a-twitch-for-insight\\Data\\Twitch_game_data.csv"
    game_data = pd.read_csv(game_file_name, encoding='cp1252')
    minutes_to_hours(streamer_data)
    merged = merge_datasets(streamer_data, game_data)
    mature_vs_popularity(streamer_data)


if __name__ == '__main__':
    main()