import requests

url = 'http://127.0.0.1:8000/api/answer/'
data = {
    'question': 'What is the next campus event?'
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Text:", response.text)

try:
    print("JSON Response:", response.json())
except Exception as e:
    print("JSON Decode Error:", e)
