import urllib.request
import urllib.error
import urllib.parse
import json


# 抓取网易云音乐指定url的热评
def get_hotComments(id):
    url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_'+id+'?csrf_token='   # 歌评url
    header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

    # post请求表单数据
    data = {'params':'LPkOcWb/uz2Nj6xw+RFhGJ1PkFi4+lh4agK+1jRGmjMAiOcJ5RHxQBbZa+aME54AUdi21JkqLu/yeHjjIaLQJ4wzqiuzrzYUKciRCqmCDX9ziKoktv5mgvvlA5+A9a7kUF5pabudBaWjsut+9T5kfHQBv75fIcDRt/Anyb8FnG/Ro6R8IStD0/JknFvH5+3S',
            'encSecKey':'5627cc7941cf4cbd59b13668efe38a622ed0889d33cdcf603d18b025eb34ac434c882ed5ad16ca06e88e40a8b91de455483d0b88b6b460ca146b163e67ebab688b2feb4f22369db85a926744bad9114d3cddd00ca6255d7cdcad6cf7b9300a6fdf49adf983087cd830131fabbac39ec4a526432958309cf92c0b5a6bc177078b'}
    postdata = urllib.parse.urlencode(data).encode('utf8')  # 进行编码
    request = urllib.request.Request(url, headers=header, data=postdata)
    response = urllib.request.urlopen(request).read().decode('utf8')
    json_dict = json.loads(response)   # 获取json
    hot_comment = json_dict['hotComments']  # 获取json中的热门评论
    print(id)
    num = 1
    for item in hot_comment:
        printer1=item['content']
        with open("comments.txt","a",encoding='utf-8') as f:
            f.write('id : '+id+' : '+printer1)
            f.write("\n")
            f.close()
        print('id : '+id+' '+'第%d条评论：' % num+printer1)
        num += 1

if __name__ == '__main__':
    id=input()
    get_hotComments(id)