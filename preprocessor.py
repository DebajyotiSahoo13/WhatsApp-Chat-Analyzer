import re
import pandas as pd


def gettimeanddate(string):
    string = string.split(',')
    date, time = string[0], string[1]
    time = time.split('-')
    time = time[0].strip()

    return date+" "+time

def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    # convert message_date type
    # df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ')

    df['message_date'] = df['message_date'].apply(
        lambda text: gettimeanddate(text))
    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)


# pd.to_datetime(df['date']).dt.date

    df['only_date'] = pd.to_datetime(df['date']).dt.date
    df['year'] = pd.to_datetime(df['date']).dt.year
    df['month_num'] = pd.to_datetime(df['date']).dt.month
    df['month'] = pd.to_datetime(df['date']).dt.month_name()
    df['day'] = pd.to_datetime(df['date']).dt.day
    df['day_name'] = pd.to_datetime(df['date']).dt.day_name()
    df['hour'] = pd.to_datetime(df['date']).dt.hour
    df['minute'] = pd.to_datetime(df['date']).dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df