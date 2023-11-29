import requests
api = '6b588c217e1446d5e5f3b7589ae47a50'
def get_data(place, focasting_days=None):
    #this api is taken from web called openweathermap.org
    url  = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    no_values = 8*focasting_days
    filtered_data = filtered_data[:no_values]
    return filtered_data

if __name__=="__main__":
    print(get_data(place='Tokyo', focasting_days = 3))