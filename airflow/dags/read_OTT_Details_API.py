import requests as rq
import keyring as kring
import json


# api_url = 'https://ott-details.p.rapidapi.com/advancedsearch'
# header = {
#     'X-RapidAPI-Key': kring.get_password('OTT_Details_API','api_key') ,
#     'X-RapidAPI-Host': kring.get_password('OTT_Details_API','host_name')
#   }
# params= {   'start_year': '2020',
#     'end_year': '2020',
#     'genre': 'action',
#     'language': 'hindi',
#     'type': 'movie',
#     'sort': 'latest',
#     'page': '1'
#   }
# data  = rq.get(url=api_url , headers= header,params = params).json()
# print(data)
# with open('ott_advance_search.json','w') as f:
#     f.writelines(json.dumps(data,indent=4))



api_url = 'http://moviesminidatabase.p.rapidapi.com/series/byYear/2021/'
header = {
    'X-RapidAPI-Key': kring.get_password('OTT_Details_API','api_key') ,
    'X-RapidAPI-Host': kring.get_password('OTT_Details_API','host_name')
  }
params = {'region':'US', 'page' : '1'}
data  = rq.get(url=api_url , headers= header).json()
print(data)
with open('ott_params.json','w') as f:
    f.writelines(json.dumps(data,indent=4))