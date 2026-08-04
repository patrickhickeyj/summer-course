import requests

# address = 'http://httpforever.com'
# response = requests.get(address)
# print(response)
# print(response.headers)

#Hands on 1
# exercise 1

address = 'https://jsonplaceholder.typicode.com'
response = requests.get(address)
print(response, response.status_code, response.reason)

# exercise 2
extra2 = '/posts/1'
res2 = requests.get(address + extra2)
print(res2.headers['Content-Type'], res2.elapsed)

# exercise 3
dict2 = res2.json()

try:
    usid = dict2.get('userId')
    id = dict2.get('id')
    title = dict2.get('title')
    other = dict2.get('nothinghere')
except:
    print("Error accessing dictionary")

print(usid)
print(id)
print(title)

# exercise 4
addy4 = '/comments'
res3 = requests.get(address + addy4, params={'postId' : 1})
comment_list = res3.json()
print(f'Number of comments: {len(comment_list)}')
print(comment_list[0]['email'])

#stretch
def fetch(url):
    try:
        timenum = 3
        response = requests.get(url, params={'timeout' : timenum})
        print(response)
        response.raise_for_status()
    except requests.exceptions.Timeout as timeout:
        print(f'Timeout error: {timeout}')
    except requests.exceptions.HTTPError as httperr:
        print(f'HTTP error: {httperr}')
    except requests.exceptions.RequestException as reqexc:
        print(f'Request exception error: {reqexc}')

url1 = address + '/posts/1'
url2 = address + '/not-a-real-route'
fetch(url1)
fetch(url2)