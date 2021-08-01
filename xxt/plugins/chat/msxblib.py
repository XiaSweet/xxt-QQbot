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