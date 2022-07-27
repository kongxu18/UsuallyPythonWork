import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models


def robot_talk(query):
    try:
        cred = credential.Credential("AKIDnOjnb7ML3TdXAWbQxDCtKUNyIL7bpmRt", "GLCn7AwRfdKktkKdfPt62h5C2btue7KH")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

        req = models.ChatBotRequest()
        params = {
            "Query": str(query)
        }
        req.from_json_string(json.dumps(params))

        resp = client.ChatBot(req)
        res = resp.to_json_string()

        res_dict = eval(res)

        return res_dict.get('Reply')

    except TencentCloudSDKException as err:
        print(err)
        return '我脑子出问题了,回答不了你'


