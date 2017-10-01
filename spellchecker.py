import requests
import re
import json

def spellchecker(q):
    #url 이 모바일로 바뀌어서 headers 를 추가해줘야 동작했다.
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ko; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 IPMS/A640400A-14D460801A1-000000426571',   # firefox UserAgent
    }

    url = "https://m.search.naver.com/p/csearch/dcontent/spellchecker.nhn"

    params = {
        '_callback' : 'window.__jindo2_callback._spellingCheck_0',
        'q' : q,
    }

    response = requests.get(url, params=params, headers=headers).text
    #response = response.replace('window.__jindo2_callback._spellingCheck_0(', '').replace(');', '')
    response = response.replace(params['_callback'] + '(', '')
    response = response.replace(');', '')

    #print(response)

    response_dic = json.loads(response)

    #print(result.__class__)
    #print(result)

    result_text = response_dic['message']['result']['html']
    #print(result_text)
    result_text = re.sub(r'<\/?.*?>', '', result_text)
    #print(result_text)
    return result_text



if __name__ == '__main__':
    #print('입력해주세요:')
    #line = input()    
    #print(spellchecker(line))
    print(spellchecker('아버지가방에들어가신다'))
    #20171001 Test comment
    #20171001-2 커밋 푸쉬 테스트중
