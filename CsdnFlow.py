import re
import requests
from bs4 import BeautifulSoup


def follow(username):
    headers = {
        'Host': 'my.csdn.net',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
        'Accept': '*/*',
        'Referer': 'http://blog.csdn.net/zwj1452267376/article/details/49359983',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'uuid_tt_dd=10_20846746780-1512964358242-799235; UN=qq_27512671; kd_user_id=19f90254-dc59-47ed-9abf-4700f28faec0; bdshare_firstime=1513302064332; _ga=GA1.2.1756792947.1513754991; __utmz=17226283.1514449181.1.1.utmcsr=blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/qq_27512671; __message_sys_msg_id=0; __message_gu_msg_id=0; __message_cnel_msg_id=0; UM_distinctid=160f7e1f8d446e-094b70768297df-454c092b-1fa400-160f7e1f8d5465; CloudGuest=1C7+xHAVnKB27nnIRYV6lEy8RGKD7ABB6jb3KJWrcpZSQvQsyzpxkDdi+1X1gsZDVoofE5CsV4A2Dd5fzqCpA3wNYnEagdqt5eryqAiFQM4gM7iZjG35Cir67e8OizP9YiO09DP73jQ+54fZ/Or3Ok9csyfxXbcSPiOsrLQih44ejysLKaejfK9IQAoz6+dq; __message_in_school=0; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC; __utma=17226283.1756792947.1513754991.1516333419.1517535632.3; UserName=qq_27512671; UserInfo=516ZoXsRpXNZVFVGH2xffpHRh%2BHVBtC9y9CkSaiOwXYgVdsbjpv97NRKhGE7HJCEtH0TI9LzdO03C%2FJzyOV16LR0UDVAs%2FHeTMlAEwClmIcrpxMbSgZ9NVBnd9t8IGUSvp4HEWcT234ZZyeUrLoqdg%3D%3D; UserNick=%E7%97%95%E8%BF%B9%E4%B8%B6; AU=31E; BT=1518055708710; dc_session_id=10_1518078896871.912979; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1518076630,1518077583,1518078153,1518078899; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1518079539; dc_tos=p3tpo3'
    }
    follow = "http://my.csdn.net/index.php/follow/do_follow" \
             "?jsonpcallback=jQuery191086230886103373_1518079539322" \
             "&username={username}" \
             "&_=1518079539325" \
        .format(username=username)
    r = requests.get(follow, headers=headers)
    print(r.status_code)


usernames = []


def getUserId(user):
    # 获取极客头条userid

    # 通过获取到的这一部分,进行迭代粉丝和已关注
    headers = {
        'Host': 'blog.csdn.net',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www.baidu.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
    }
    url = 'http://my.csdn.net/{userid}'.format(userid=user)
    print("开始爬取：")
    r = requests.get(url, headers=headers)
    if r.ok:
        r.raise_for_status()
        r.encoding = 'utf-8'
        data = r.text
        rr = "username='[^<>]*'"
        a = re.findall(rr, r.text, 0)
        for i in a:
            i=i[10:-1]
            if i != '' and i not in usernames:
                usernames.append(i)
                follow(i)
    else:
        print("用户获取失败！", r.status_code)


if __name__ == '__main__':
    getUserId('sinyu890807')
    # 迭代几次  指数增长  慎重!
    for user in usernames:
        getUserId(user)
    for user in usernames:
        getUserId(user)
    for user in usernames:
        getUserId(user)
    for user in usernames:
        getUserId(user)
    for user in usernames:
        getUserId(user)
    print(usernames)