
import requests

import time
def main():
    # OpenWeatherMap APIキー
    API_KEY = "d2be2cdb4e4d8b9d4c8fe97d3dce1abe"
    
    # 東京の緯度経度
    TOKYO_LAT = 35.6895
    TOKYO_LON = 139.6917
    
    # APIエンドポイント
    API_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"
    
    # OpenWeatherMap APIから東京の気象データを取得
    params = {
        "lat": TOKYO_LAT,
        "lon": TOKYO_LON,
        "appid": API_KEY,
        "units": "metric"
    }
    
    response = requests.get(API_ENDPOINT, params=params)
    data = response.json()
    
    # 降水確率を抽出
    rain_chance = data["clouds"]["all"]
    
    # 降水確率が50%以上かどうかを判定
    if rain_chance >= 50:
        # LINE Notifyに通知を送信
        access_token = "5NaFyRtQ2Vy5WKlfExfhyKJgArlqScYKsCdC21qoCdS"   
        message = f"東京の降水確率が{rain_chance}%です。"
    
        line_notify_api = "https://notify-api.line.me/api/notify"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        data = {
            "message": message
        }
    
        response = requests.post(line_notify_api, headers=headers, data=data)
    
        if response.status_code == 200:
            print("LINE通知を送信しました。")
        else:
            print("LINE通知の送信に失敗しました。")
    else:
        print("降水確率が50%未満です。")

if __name__ == "__main__":
    while True:
        main() 
