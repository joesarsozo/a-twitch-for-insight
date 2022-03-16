"""
Jianna Braza and Joseph Sarsozo
CSE 163 AH
This files contains several functions that utilize
two data sets pertaining to The Top Twitch Streamers and the Top
Games streamed on Twitch. Some functions altered the datasets
to be easier to work with as well as create several data
visualizations that help us analyze and answer our intended
research questions related to the data
"""
import plotly.graph_objects as go


def minutes_to_hours(streamer_data):
    """
    This function takes the streamer data set
    and converts the watch time and stream
    time data values from minutes to hours
    so both datasets use the same unit of time
    """
    streamer_data['Watch time(Hours)'] = streamer_data['Watch time(Minutes)'] / 60
    streamer_data['Stream time(Hours)'] = streamer_data['Stream time(minutes)'] / 60
    return streamer_data


def merge_datasets(streamer_data, game_data):
    """
    This function takes the two datasets and merges them together
    to create a new dataset aligning the peak viewers for games and streamers
    sorted from largest to smallest
    upon further research, data point do not actually align
    will be explained in report
    """
    merged = streamer_data.merge(game_data, left_on='Peak viewers', right_on='Peak_viewers', how='inner')
    merged = merged.loc[:, ['Game', 'Channel', 'Peak viewers']]
    merged = merged.sort_values(by='Peak viewers', ascending=False)
    return merged


def mature_vs_popularity_top_n(streamer_data, n):
    """
    This function takes the streamer dataset and an integer n
    representing the percentage of the total streamer dataset
    ex. n = 50 means top 50% of the streamer dataset
    and returns the percentage of mature streamers found within
    the top n% of streamers.
    ex. n = 50 returns about 43% meaning 43% of the mature streamers
    in this dataset are in the top 50% of the entire streamer dataset
    """
    num = int(float(n / 100) * len(streamer_data))
    streamer_data = streamer_data.nlargest(num, 'Average viewers')
    streamer_data = streamer_data[streamer_data['Mature'] == True]
    num_mature = len(streamer_data)
    return (num_mature / 230) * 100


def split_hours(s):
    """
    This is a helper function that splits
    the string in the Hours Streamed column of the game dateset
    by the space. It then returns the first index as an integer.
    """
    s_list = s.split()
    return int(s_list[0])


def fix_hours_streamed(game_data):
    """
    This function applies the split hours function on
    the hours streamed column of the game dataset
    It then returns the game data set with the
    word 'hours' removed from the aforementioned column
    """
    game_data['Hours_Streamed(number)'] = game_data['Hours_Streamed'].apply(split_hours)
    return game_data


def plotly_streamer_data(streamer_data):
    """
    This function takes the streamer dataset and makes a bar chart
    that compares the stream time and watch time of the top 25
    streamers on Twitch.
    uses plotly which opens browser
    """
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
    """
    This function takes the game data set and makes a bar chart
    that compares the stream time and watch time of the top 100
    games streamed on Twitch
    uses plotly which opens browser
    """
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
