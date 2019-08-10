import csv
import pprint


def get_video_data():
    """this function reads from a .csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific videos and their attributes."""


    vid_data = []
    with open('USvideos.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar="")
        for row in spamreader:
            if len(row) == 16:
                vid_dict = {'video_id': row[0],
                            'trending_date': row[1],
                            'title': row[2],
                            'channel_title': row[3],
                            'category_id': row[4],
                            'publish_times': row[5],
                            'tags': row[6],
                            'views': row[7],
                            'likes': row[8],
                            'dislikes': row[9],
                            'comment_count': row[10],
                            'thumbnail_link': row[11],
                            'comments_disabled': row[12],
                            'ratings_disabled': row[13],
                            'video_error': row[14],
                            'description': row[15]
                            }
                vid_data.append(vid_dict)
    return vid_data


def print_data(data):
    for entry in data:
        pprint.pprint(entry)


def my_max_views(dictionary):
    return_dict = {'num_views': 0, 'channel': None}
    for k,v in dictionary.items():
        if int(v) > return_dict['num_views']:
            return_dict['channel'] = k
            return_dict['num_views'] = int(v)
    return return_dict


def my_min_views(dictionary):
    return_dict = {'num_views': float('Inf'), 'channel': None}
    for k,v in dictionary.items():
        if k == 'Unspecified':
            continue
        if int(v) < return_dict['num_views']:
            return_dict['channel'] = k
            return_dict['num_views'] = int(v)
    return return_dict


def my_max_likes(dictionary):
    return_dict = {'numb_likes': 0, 'channel': None}
    for k,v in dictionary.items():
        if int(v) > return_dict['numb_likes']:
            return_dict['channel'] = k
            return_dict['numb_likes'] = int(v)
    return return_dict


def my_max_dislikes(dictionary):
    return_dict = {'numb_likes': 0, 'channel': None}
    for k,v in dictionary.items():
        if int(v) > return_dict['numb_dislikes']:
            return_dict['channel'] = k
            return_dict['numb_dislikes'] = int(v)
    return return_dict


def get_most_popular_and_least_popular_channel(data):
    """ fill in the Nones for the dictionary below using the vid data """
    most_popular_and_least_popular_channel = {'most_popular_channel': None, 'least_popular_channel': None,
                                              'most_pop_num_views': None, 'least_pop_num_views': None}
    aggregate_most_popular_channel = {}
    aggregate_least_popular_channel = {}
    for entry in data[1:]:
        aggregate_most_popular_channel.setdefault(entry['channel_title'], 0)
        aggregate_least_popular_channel.setdefault(entry['channel_title'], 0)
        aggregate_most_popular_channel[entry['channel_title']] += int(entry['views'])
        aggregate_least_popular_channel[entry['channel_title']] += int(entry['views'])

    most_popular_channel_dict = my_max_views(aggregate_most_popular_channel)
    least_popular_channel_dict = my_min_views(aggregate_least_popular_channel)
    most_popular_and_least_popular_channel['channel_title'] = most_popular_channel_dict['channel']
    most_popular_and_least_popular_channel['most_pop_num_views'] = most_popular_channel_dict['num_views']
    most_popular_and_least_popular_channel['channel_title'] = least_popular_channel_dict['channel']
    most_popular_and_least_popular_channel['least_pop_num_views'] = least_popular_channel_dict['num_views']
    return most_popular_and_least_popular_channel


def get_most_liked_and_disliked_channel(data):
    """ fill in the Nones for the dictionary below using the bar party data """

    most_liked_and_disliked_channel = {'most_liked_channel': None, 'num_likes': None, 'most_disliked_channel': None,
                                       'num_dislikes': None}

    aggregate_most_liked_channel = {}
    aggregate_most_disliked_channel = {}
    for entry in data[1:]:
        aggregate_most_liked_channel.setdefault(entry['channel_title'], 0)
        aggregate_most_disliked_channel.setdefault(entry['channel_title'], 0)
        aggregate_most_liked_channel[entry['channel_title']] += int(entry['likes'])
        aggregate_most_disliked_channel[entry['channel_title']] += int(entry['dislikes'])

    most_liked_channel_dict = my_max_likes(aggregate_most_liked_channel)
    most_disliked_channel = my_max_dislikes(aggregate_most_disliked_channel)
    most_liked_and_disliked_channel['most_liked_channel'] = most_liked_channel_dict['channel']
    most_liked_and_disliked_channel['num_likes'] = most_liked_channel_dict['numb_likes']
    most_liked_and_disliked_channel['most_disliked_channel'] = most_disliked_channel['channel']
    most_liked_and_disliked_channel['num_dislikes'] = most_disliked_channel['numb_dislikes']
    return most_liked_and_disliked_channel


if __name__ == '__main__':
    vid_data = get_video_data()

    #uncomment the line below to see what the data looks like
    #print_data(vid_data)

    popularity_metrics = get_most_popular_and_least_popular_channel(vid_data)

    like_dislike_metrics = get_most_liked_and_disliked_channel(vid_data)

    print('Popularity Metrics: {}'.format(popularity_metrics))
    print('Like Dislike Metrics: {}'.format(like_dislike_metrics))
