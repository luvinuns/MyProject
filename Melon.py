import requests
import json


def melon_search(q):
    url = "http://www.melon.com/search/keyword/index.json"
    params = {
        'jscallback':'jQuery19103154903463458836_1506147408429',
        'query':q,
    }


    response = requests.get(url, params=params).text

    #print(response)


    json_string = response.replace(params['jscallback'] + '(', '').replace(');', '')
    result_dict = json.loads(json_string)
    #print(result_dict)
    
    if 'SONGCONTENTS' not in result_dict:
        print('not found')
    else:
        for song in result_dict['SONGCONTENTS']:
            print('''{SONGNAME} {ALBUMNAME} {ARTISTNAME} 
            http://www.melon.com/song/detail.htm?songId={SONGID}
            '''.format(**song))
            #print(song['SONGNAME'], song['ALBUMNAME'], song['ARTISTNAME'])
   
if __name__ == '__main__':
#    print('입력해주세요:')
#   line = input()
#   melon_search(line)
    melon_search('아이유')
