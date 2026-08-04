import requests

from requests.auth import HTTPBasicAuth

base = 'https://httpbin.org'

#Exercise1
url1 = '/basic-auth/student/pass123'
basic = HTTPBasicAuth('student', 'pass123')

req1 = requests.get(base + url1, auth=basic)

print(req1, req1.json())

#Exercise 2
url2 = '/bearer'
tokenhold = 'Bearer abc123'
header = {'Authorization': tokenhold}

req2 = requests.get(base + url2, headers=header)

print(req2)

#Exercise 3
url3 = '/get'
head3 = {'X-API-Key': 'demo-key-001'}
param3 = '?api_key=demo-key-001'

req31 = requests.get(base + url3, headers=head3)
req32 = requests.get(base + url3 + param3)
print(req31, req31.json())
print(req32, req32.json())

#Exercise 4
url4 = '/cookies/set/course_token/python-lesson-10'
url4base = '/cookies'
my_cookie = {'hickey1': 'test1',
             'otherparam': 'value1'}

# s= requests.Session()
# s.cookies.set('logged_in', 'true')
# req4 = s.post(base + url4, cookies=my_cookie)
# print(req4.cookies)
# req4base = s.get(base + url4base)

# print(req4base.cookies)

with requests.Session() as session:
    response = session.get(base + url4)
    print(response.text)
    print(response.cookies)
    response = session.get(base + url4base)
    print(response.request.headers)
    print(response.cookies)