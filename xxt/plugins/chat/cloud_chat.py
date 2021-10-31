class txNLP:
    async def chat(query:str,tid,tkey): #TX云语言交流
        #TX云SDK组件与依赖
        import json
        from tencentcloud.common import credential
        from tencentcloud.common.profile.client_profile import ClientProfile
        from tencentcloud.common.profile.http_profile import HttpProfile
        from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
        from tencentcloud.nlp.v20190408 import nlp_client, models
        try:
            cred = credential.Credential(tid, tkey)
            httpProfile = HttpProfile()
            httpProfile.endpoint = "nlp.tencentcloudapi.com"

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

            req = models.ChatBotRequest()
            params = {
                "Query": query
            }
            req.from_json_string(json.dumps(params))
            resp = client.ChatBot(req)
            resp=json.loads(resp.to_json_string())
            resp={"stat":True,
                  "reply":resp["Reply"],
                  "Confidence":resp["Confidence"]}
            return(resp)
        #云交流Debug
        except TencentCloudSDKException as err:
            if err.code=='AuthFailure.SecretIdNotFound':
                err={"stat":False,
                "code":err.code,
                "msg":err.message}
                return(err)
            elif err.code=='AuthFailure.SignatureFailure':
                err={"stat":False,
                "code":err.code,
                "msg":err.message}
                return(err)
            elif err.code=='InvalidParameterValue.TextTooLong':
                err={"stat":False,
                "code":err.code,
                "msg":err.message}
                return(err)
            elif err.code=='ClientNetworkError':
                err={"stat":False,
                "code":err.code,
                "msg":err.message}
                return(err)
            else:
                err={"stat":False,
                "code":err.code,
                "msg":err.message}
                return(err)
