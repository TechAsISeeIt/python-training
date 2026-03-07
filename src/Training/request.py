import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)  # Make a GET request to the training endpoint
    response.raise_for_status()
    data = response.json()  # Parse the JSON response
    # print("Training response:", data)

    # You can also make a POST request to send data to the training endpoint
    post_url = "https://jsonplaceholder.typicode.com/posts"
    payload: dict[str, str | int] = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(
        post_url, json=payload
    )  # Make a POST request with JSON payload. you can either use json=payload or data=payload, but json=payload will automatically set the Content-Type header to application/json
    print(response.status_code)
    print("POST response:", response.json())
    result = response.json()

    # url = f"https://jsonplaceholder.typicode.com/posts/100"
    # response = requests.get(url)  # Make a GET request to the training endpoint
    # print("Training response:", response.json())
