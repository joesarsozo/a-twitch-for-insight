import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
sns.set()


def minutes_to_hours(streamer_data):
    streamer_data['Watch time(Hours)'] = streamer_data['Watch time(Minutes)'] / 60
    streamer_data['Stream time(Hours)'] = streamer_data['Stream time(minutes)'] / 60


def merge_datasets(streamer_data, game_data):
    merged = streamer_data.merge(game_data, left_on='Peak viewers', right_on='Peak_viewers', how='inner')
    merged = merged.loc[:, ['Game', 'Channel', 'Peak viewers']]
    merged = merged.sort_values(by='Peak viewers', ascending=False)
    return merged


def mature_vs_popularity_top_n(streamer_data, n):
    num = int(float(n / 100) * len(streamer_data))
    streamer_data = streamer_data.nlargest(num, 'Average viewers')
    streamer_data = streamer_data[streamer_data['Mature'] == True]
    num_mature = len(streamer_data)
    return (num_mature / 230) * 100


def split_hours(s):
    s_list = s.split()
    return int(s_list[0])


def fix_hours_streamed(game_data):
    game_data['Hours_Streamed(number)'] = game_data['Hours_Streamed'].apply(split_hours)


def plotly_streamer_data(streamer_data):
    streamer_data = streamer_data.nlargest(25, 'Average viewers')
    streamer_data['Watch time(Hours)'] = streamer_data['Watch time(Hours)'] / 10000
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=streamer_data['Channel'],
        y=streamer_data['Stream time(Hours)'],
        name='Stream time (Hours)',
        marker_color='lightslategrey'
    ))
    fig.add_trace(go.Bar(
        x=streamer_data['Channel'],
        y=streamer_data['Watch time(Hours)'],
        name='Watch time (in thousands)',
        marker_color='crimson'
    ))
    fig.update_layout(title='Watch Time vs Stream Time for twitch streamers',
                      barmode='group', xaxis_tickangle=-45)
    fig.update_xaxes(title_text='Twitch Channels')
    fig.show()


def plotly_game_data(game_data):
    game_data = game_data[game_data['Year'] == 2021]
    game_data = game_data.nlargest(100, 'Avg_viewers')
    game_data['Hours_watched'] = game_data['Hours_watched'] / 10
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=game_data['Game'],
        y=game_data['Hours_Streamed(number)'],
        name='Stream time (Hours)',
        marker_color='lightslategrey'
    ))
    fig.add_trace(go.Bar(
        x=game_data['Game'],
        y=game_data['Hours_watched'],
        name='Watch time (Hours) by tens',
        marker_color='rgb(26, 118, 255)'
    ))
    fig.update_layout(title='Watch Time vs Stream Time for games on Twitch',
                      barmode='group', xaxis_tickangle=-45)
    fig.update_xaxes(title_text='Games')
    fig.show()


def main():
    streamer_file_name = "Data\\twitchdata-update.csv"
    streamer_data = pd.read_csv(streamer_file_name)
    game_file_name = "Data\\Twitch_game_data.csv"
    game_data = pd.read_csv(game_file_name, encoding='cp1252')
    minutes_to_hours(streamer_data)
    merged = merge_datasets(streamer_data, game_data)
    fix_hours_streamed(game_data)
    plotly_streamer_data(streamer_data)
    plotly_game_data(game_data)


if __name__ == '__main__':
    main()