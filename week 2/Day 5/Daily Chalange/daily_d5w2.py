import requests
import time

def measure_load_time(url):
    
    start_time = time.time() #start of the request
    response = requests.get(url)# sending an HTTP request to the server at the provided url
    end_time = time.time() #time when the response recieved

   
    load_time = end_time - start_time

    return load_time, response.status_code

# Testing with multiple websites
def test_sites():
    sites = [

        'https://www.codeacademy.com',
        'https://www.sefervesefel.com',
        'https://www.amazon.com/',
        'https://www.bbc.com/',
        'https://www.google.com',
        'https://www.ynet.co.il',
        'https://www.imdb.com',
        
    ]

    for site in sites:
        load_time, status_code = measure_load_time(site)
        print(f"Website: {site}")
        print(f"Load Time: {round(load_time,4)} seconds")
        print(f"Status Code: {status_code}\n")


test_sites()
