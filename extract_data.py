import requests

def extract_data():
    
    # Define the API endpoint URL
    url = "https://jsonplaceholder.typicode.com/users"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Parse the JSON data from the response
    data = response.json()
    
    return data