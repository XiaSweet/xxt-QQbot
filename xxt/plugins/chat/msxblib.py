class xiaobinglib:
    async def chat(msg,uid,source,SUB):
        import requests
        import time
        url_send = 'https://api.weibo.com/webim/2/direct_messages/new.json'
        data = {
            'text': msg,
            'uid': uid,
            'source': source
        }
        headers = {
            'cookie': 'SUB='+SUB,
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Referer': 'https://api.weibo.com/chat/'
        }
        response = requests.post(url_send, data=data, headers=headers).json()
        sendMsg = response['text']
        while True:
            url_get = 'https://api.weibo.com/webim/2/direct_messages/conversation.json?uid={}&source={}'.format(uid, source)
            response = requests.get(url_get, headers=headers).json()
            getMsg = response['direct_messages'][0]['text']
            if sendMsg == getMsg:
                time.sleep(0.5)
            else:
                return getMsg