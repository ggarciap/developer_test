import requests
import pandas as pd

base_url = 'https://api.github.com/'
user = 'geohot'
query_parameters = '?per_page=50'

def main_request_user_repo(baseurl, user, query_param):
    endpoint = f'users/{user}/repos'
    r = requests.get(baseurl + endpoint + query_param)
    return r.json()

def parse_json(response):
    charlist = []
    
    for item in response:
        char = {
            'id':item['id'], 
            'name':item['name'], 
            'description':item['description'], 
            'html_url':item['html_url'],
            'url':item['url'], 
        }
        charlist.append(char)
    return charlist

data = main_request_user_repo(base_url, user, query_parameters)
df_test = pd.DataFrame(parse_json(data))
# print(df_test.head(5))

# From pandas dataframe to CSV
df_test.to_csv('./Q14-output.csv',index=False)
