# importing requests HTTP dictionary 
import requests
# SHA1 Hash method with the first 5 digit of a password 
url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
# getting api
res = requests.get(url)
# response check(<Response [200]>)
print(res)