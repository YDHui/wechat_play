# _*_ coding:utf-8 _*_
import itchat
import datetime,time
import requests
import sys
reload(sys);
exec("sys.setdefaultencoding('utf-8')");

def post_msg(msg):
    url = "http://www.tuling123.com/openapi/api"
    post_data = {
    "key":"14649a25d50046138b4735a9fc2e049f",
    "userid":"123456",
    "info":msg
    }
    r = requests.post(url,json=post_data).json()
    return r.get('text')

#@itchat.msg_register(itchat.content.TEXT)
# def return_content(msg):
#     return_msg = post_msg(msg['Text'])
#     return return_msg

def get_friend_name():
    f = open("wechat_friends.txt","w+")
    friends = itchat.get_friends()
    #friends_nick = [fri.User["NickName"] for fri in friends]
    friends_nick = [fri.NickName for fri in friends]
    for fri in friends:
        f.write(fri.NickName+",\n")
    f.close()
    return friends_nick

def get_friend_sex():
    friends = itchat.get_friends()
    man = 0
    woman = 0
    all_man = 0
    for fri in friends:
        if fri.Sex == 1:
            man = man + 1
        elif fri.Sex == 2:
            woman = woman + 1
        all_man = all_man + 1
    return man,woman,all_man
def wechat_run():
    itchat.auto_login(hotReload=True)
    man,woman,all_man =  get_friend_sex()
    print "男生数量:%d\n"%man
    print "女生数量:%d\n"%woman
    print "总好友数:%d\n"%all_man
        #itchat.run()

if __name__ == '__main__':
    wechat_run()