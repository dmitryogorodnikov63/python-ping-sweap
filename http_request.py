import requests

def send_request(url, method, headers, body):
    try:
        if method == 'GET':
            response = requests.request(url=url, method=method, headers=headers)
        else:
            response = requests.request(url=url, method=method, headers=headers, data=body)
    except Exception as e:
        print("Ошибка выполнения программы\n", str(e))
    else:
        print("Response status: " + str(response.status_code))
        print("\nResponse body:")
        print(response.content)
        print("\nResponse headers:")
        print(response.headers)
