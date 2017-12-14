import requests
import json
import matplotlib.pyplot as plt
import numpy as np


url_start = 'http://api.openweathermap.org/data/2.5/forecast?q='
appid = 'f92297febd109ccf021620f1e63ebc5f'
city = input('Nurodykite miestą: ')


def get_wind_info(city):

    # Joining part of URL and getting data from Openweather
    url = url_start + city + '&APPID=' + appid
    r = requests.get(url)
    json_data = r.json()

    # Creating a json file and storing data into it
    with open('orai.json', 'w') as f:
        f.write(json.dumps(json_data))

    # Getting data from json file and creating a dictionary
    with open('orai.json', 'r') as f:
        data_str = f.read()
    data_dic = json.loads(data_str)

    # Getting list of wind data
    wind_speed = []
    for item in data_dic['list']:
        wind_speed.append(data_dic['list'][data_dic['list'].index(item)]['wind']['speed'])

    # Getting list of corresponding dates and times
    times = []
    for item in data_dic['list']:
        times.append(data_dic['list'][data_dic['list'].index(item)]['dt_txt'])

    # Crrecting the format of dates and times to have it smaller in the plot
    times_cor = []
    for item in times:
        times_cor.append(item[5:-6] + 'h')

    # Getting average wind speed
    av_wind_speed = sum(wind_speed) / len(wind_speed)

    # Preparing a plot and showing it
    x = np.array(times_cor)
    y = np.array(wind_speed)
    z = np.array([av_wind_speed] * len(wind_speed))
    plt.plot(x, y)
    plt.plot(x, z)
    plt.xticks(rotation=90)
    plt.title('Vėjo poprognozė, miestas: {}, šalis: {}'.format(data_dic['city']['name'], data_dic['city']['country']))
    plt.ylabel('Vėjo greitis (m/s)')
    plt.xlabel('Laikas')
    # Add annotations to each data point in the plot
    for i, j in zip(x, y):
        plt.annotate('{}'.format(j), xy=(i, j), rotation=25)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    get_wind_info(city)
