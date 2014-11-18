__author__ = 'matt'
from urllib2 import Request, urlopen
import json


api_key = '?apikey=[38bcb60077966674b2985d33ad35abbd]'
endpoint = 'http://private-770c9-themoviedb.apiary-mock.com/3/movie/26/images'


headers = {
    'Accept': 'application/json'
}

request = Request(endpoint + api_key, headers=headers)

response_body = urlopen(request).read()

print response_body