import web
import receive
import reply
import rebot

urls = ('/wx', 'Handle',)


class Handle():
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return 'hello,this is handle view'
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            print(signature, timestamp, nonce, '----')
            token = 'wxpython'
            list_ = [token, timestamp, nonce]
            list_.sort()
            import hashlib
            sha1 = hashlib.sha1()
            sha1.update(''.join(list_).encode('utf8'))
            hashcode = sha1.hexdigest()
            if hashcode == signature:
                return echostr
            else:
                return ''
        except Exception as Argument:
            print(Argument, 'err')
            return Argument

    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)
            # 后台打日志
            recMsg = receive.parse_xml(webData)
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                send = recMsg.Content
                if isinstance(send, bytes):
                    send = send.decode('utf8')

                content = rebot.robot_talk(send)

                print(content, 'content', '----')
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                content = '欢迎来到随身猿，现在就由小猿来陪你'
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
        except Exception as Argument:
            print(Argument, 'err----')
            return Argument


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
