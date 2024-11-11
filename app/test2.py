import requests

# Data to be sent in the POST request
data = {
    'model': 'Qwen/Qwen2-VL-2B-Instruct',
}

data2 = {
    'messages':[
        {
                "role": "user",
                "content": "who are u ?",
        },
    ],
    'seed': '123',
}

# Making a POST request
response = requests.post('https://fzdlfltvyzatf8-8888.proxy.runpod.net//api/v1/load_model', json=data)
# response = requests.post('http://0.0.0.0:8888/api/v1/load_model', json=data)
# response = requests.post('https://fzdlfltvyzatf8-8888.proxy.runpod.net//chat/completions', json=data2)

# Check if the request was successful
if response.status_code == 200:
    print('Success!')
    print('Response:', response.json())
else:
    print('Failed with status code:', response.status_code)
    print('Error:', response.text)