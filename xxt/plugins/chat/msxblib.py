class xblib:
    async def chat(msg):
        import requests
        url=f'http://10.14.240.4:6789/chat?text={msg}'
        res=requests.get(url)
        res=res.text
        import json
        res=json.loads(res)
        if res["debug"]=="":
            return res["text"]
        else:
            return False
    def get_image(url):
        import requests
        '''
        图片下载
        @:param url_info ('http://img.xixik.net/custom/section/country-flag/xixik-cdaca66ba3839767.png','北马里亚纳群岛)
        '''
        try:
            response = requests.get(url)
            # 获取的文本实际上是图片的二进制文本
            img = response.content
            # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
            #保存路径
            path='/home/tmp/tmp.jpg'
            with open(path, 'wb') as f:
                f.write(img)
                return True
        except Exception as ex:
            print(ex)
            return(f"DEBUG:{ex}")
    async def imgchat(msg):
        import requests
        url=f'http://10.14.240.4:6789/chat?text={msg}&type=img'
        res=requests.get(url)
        res=res.text
        import json
        res=json.loads(res)
        if res["debug"]=="":
            return res["text"]
        else:
            return False