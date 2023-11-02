import requests
# pandas Powerful data science program (possible overkill for this small project but it works really well)
import pandas as pd

baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

# requests the base url plus the endpoint eg 'character' plus the page number to work with and returns in json format
def main_request(baseurl, endpoint, x):
    r = requests.get(baseurl + endpoint + f'?page={x}')
    return r.json()


# returns the number of pages we need to loop through 
def get_pages(response):
    return response['info']['pages']

# loops through the character info on each request we give
def parse_json(response):
    charlist = []
    for item in response['results']:
        char = {
            'id': item['id'],
            'name': item['name'],
            'no_ep': len(item['episode']),
        }

        charlist.append(char)
    return charlist


mainlist = []
data = main_request(baseurl, endpoint, 1)
for x in range(1, get_pages(data)+1):
    print(x)
    mainlist.extend(parse_json(main_request(baseurl, endpoint, x)))

# pandas dataframe and exports to csv file to stop you having to request the server anymore
dataframe = pd.DataFrame(mainlist)

# index false so you remove pandas index which is 0 down the side
dataframe.to_csv('charlist.csv', index=False)




