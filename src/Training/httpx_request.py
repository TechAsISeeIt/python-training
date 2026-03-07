import httpx

with httpx.AsyncClient() as client:
    response = client.get("https://jsonplaceholder.typicode.com/users")
    print(response.json())
