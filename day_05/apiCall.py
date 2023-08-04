
import requests

api='https://dummyjson.com/products/1'
def get_data(api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            print(response.json())
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")


get_data(api)