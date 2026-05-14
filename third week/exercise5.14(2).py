import json

import requests


def get_weather(
    city, key="SGiJMqsJ-UAWcPLcR", url="https://api.seniverse.com/v3/weather/now.json"
):
    return requests.get(
        url,
        params={"key": key, "location": city, "language": "zh-Hans", "unit": "c"},
        timeout=5,
    )


if __name__ == "__main__":
    response = get_weather("南京")
    if response.status_code == 200:
        data = response.json()  # 把返回的 JSON 字符串转换成 Python 字典

        # 提取我们需要的具体信息
        location_name = data["results"][0]["location"]["name"]
        weather_text = data["results"][0]["now"]["text"]
        temperature = data["results"][0]["now"]["temperature"]

        data_json = {"城市": location_name, "天气": weather_text, "气温": temperature}
        print(data_json)
        try:
            with open("weather.json", "r", encoding="utf-8") as f:
                data_lst = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data_lst = []
        flag = True
        for i, item in enumerate(data_lst):
            if data_json["城市"] == item["城市"]:
                data_lst[i] = data_json
                flag = False
                break
        if flag:
            data_lst.append(data_json)
        with open("weather.json", "w", encoding="utf-8") as f:
            json.dump(data_lst, f, ensure_ascii=False, indent=2)
    else:
        print(f"请求失败，状态码：{response.status_code}")
        print(response.text)
