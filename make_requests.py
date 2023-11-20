import requests

# GET

r = requests.get("https://www.python.org")
print(r.status_code)
print(b"Python is a programming language" in r.content)


# POST

payload = dict(key1="value1", key2="value2")
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)
