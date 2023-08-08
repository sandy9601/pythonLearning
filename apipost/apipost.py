import requests

url = 'http://localhost:8087/connector/database'

custom_headers = {"x-org-id": "620cf19e797a124eb05f02a6",   # adding headers
                  "x-project-id": "620d399fb55de9389175f298"}


query_params = {"name": "sandeep"}
token = "qOSI43IKgQDBAGLOslXih8VrTPePP2O1nqQpYP9hsVqp4bD2ppZYzKhepO/NDPzRskM79JRnmxGk5UJK4oIVPCmQBL6l1WuXqbnJfpDSAHWeveeRrFcMOhj5Fdamc9qDyA5j9S/FKhHmcicnU5CfD2AthvhHkTUnS0Ppv1OLsAw2wA5hLINKeUqzR/+UnIxH7lbqPJPEKAGKgWjSBTjjIzsVpvj69Kps0+npzUDoiW5n4IhbJXyGzDxWEc4r/hRpU7fbEFezF3pj2bf1AuN4VIe0C+8QxY+4m4/psJjt//8a77x8UUl/OJIsCLuuTo1+eCYfsF/S1V7jcxs/VSmYxJRqsXulrWQlmBlm1gtJvu3hs0QhEfuUpOwyOIU5Q1q7twCFCg5oT8ttZ0vbPH+wIJaZbNYURBk9XfLK3Yy/M1KZ9F5O3CyUMUYLlQEMGoVO9T+Tr2ooqFZQtlg3N4z8s3MRrusm46nzH4ArQWCNtniqmrtCqUlR41riMVJ5eu2BKlGrJCOWjlNWd7FHP1qLYoorRAneYwllSPIBqyMdSiMgtN2jTgF3Bw=="

payload = {
    "dbType": "mongo",
    "username": "sandysana",
    "password": "9866203258Aa@1",
    "title": "sample",
    "host": "test",
    "port": 2089,
    "authDb": "test"
}


x = requests.post(url, json=payload,  headers={
                  'Authorization': f'Bearer {token}', **custom_headers}, params=query_params)

# print the response text (the content of the requested file):

print(f"{x.text}")
