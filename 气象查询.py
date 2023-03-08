import requests
import json

def get_weather_data(city):
    api_key = "2e8574ffeab7a965ba0e9eeed30ed016"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode())
        return data
    else:
        return None

city = input("请输入要查询的城市名：")
weather_data = get_weather_data(city)

if weather_data:
    weather_desc = weather_data["weather"][0]["description"]
    temp = round(weather_data["main"]["temp"] - 273.15, 1) # 转换成摄氏度
    feels_like = round(weather_data["main"]["feels_like"] - 273.15, 1) # 转换成摄氏度
    humidity = weather_data["main"]["humidity"]
    print(f"{city}的天气：{weather_desc}")
    print(f"温度：{temp}℃，体感温度：{feels_like}℃，湿度：{humidity}%")
else:
    print(f"未能找到{city}的天气信息")
# 在这个程序中，我们使用了OpenWeatherMap提供的API来获取天气数据。
# 你需要去OpenWeatherMap官网注册账户，并且获取一个API密钥（免费的API密钥每分钟最多访问次数是60次）。

# 这个程序会先提示你输入要查询的城市名，然后使用API获取该城市的气象数据，并显示温度、体感温度、湿度等信息。
# 你可以根据需要修改代码，以实现更多功能，例如显示预报、获取其他天气信息等等。