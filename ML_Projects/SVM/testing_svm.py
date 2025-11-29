import requests

url = "http://127.0.0.1:8000/predict"

live_data = {
    "features": [14.9, 22.5, 96.9, 657.1, 0.1, 0.15, 0.18, 0.1,
                 0.18, 0.05, 0.4, 1.2, 2.5, 40, 0.01, 0.03, 0.04,
                 0.01, 0.02, 0.003, 16.5, 26.5, 109, 640, 0.13,
                 0.3, 0.38, 0.17, 0.35, 0.08]
}

response = requests.post(url, json=live_data)
print(response.json())
