# importing requests HTTP dictionary 
import requests
import hashlib
# API request
def request_api_data(query_char):
    # SHA1 Hash method with the first 5 digit of a password 
    url = 'https://api.pwnedpasswords.com/range/' + query_char    
    # getting api
    res = requests.get(url)
    # response check(<Response [200]>)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res 
    pass
# Getting sha1 password
def pwned_api_check(password):
    # Converting the password to the sha1 hexadecimal form with upper case
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password

