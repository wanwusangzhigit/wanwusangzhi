import requests
# url = 'https://music.163.com/playlist?id=12311471270&uct2=U2FsdGVkX1/rj6GftP9xp6gJ2ovvUEu/9MCauu4/KhA='
url = input()
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

def get_content(url):
    html=requests.get(url,headers=headers).content.decode('utf-8')
    print("#######")
    print(html)
    print("#######")
    end=0
    while 1:
        start=html.find('<a href="/song?id=',end)
        end=html.find('">',start)
        if start!=-1 and end!=-1:
            s=html[start+18:end]
            print(s)
            with open('id.txt',"a",encoding='utf-8') as f:
                if s.find('x')==-1:
                    f.write(s+'\n')
        else:
            break
        end=start+1
get_content(url)
    
