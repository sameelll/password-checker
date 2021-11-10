# importing requests HTTP dictionary 
import requests
import hashlib
import sys
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
# How many times the password hacked:
def get_password_leaks_count(hashes, hash_to_check): 
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
        
# Getting sha1 password
def pwned_api_check(password):
    # Converting the password to the sha1 hexadecimal form with upper case
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # Seperation of the hashed form(the first 5 and the tail)
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times. \nYou should probably change your password!')
        else:
            print(f'{password} was NOT found. Carry on!') 
    return 'done!'

main(sys.argv[1:])
