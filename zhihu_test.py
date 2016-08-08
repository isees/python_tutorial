import requests

target = "https://www.zhihu.com/node/ProfileFolloweesListV2"
params = {
    "method": "next",
    "params": '{"offset":40,"order_by":"created","hash_id":"7499178d775dd566fbd1d6fde6a1ff64"}',
    "_xsrf": "ee9056940b15195eece29014cd1d86e8"
}
# cookies = {
#     'q_c1': 'ed311be6f7a346a78556078b42c211b6|1458149807000|1458149807000',
#     'udid': '"AHCAIMEzoAmPTnixU3omYAu-_0f4CpAAFAM=|1458149808"',
#     'cap_id': '"YzM0ZmMyMGU0MGVlNDMyNmI4NzM4ZWJjNWZkOGNmZTM=|1458149807|45e94da3ff48becd930c1c834720596262ad948d"',
#     '_za': '34adb349-e062-46b9-82a5-64fd520ef9c5',
#     'z_c0': '"QUFEQWxBa1pBQUFYQUFBQVlRSlZUYmNtRVZkZ3E1ck4ydzVROWtoeVY4R3IzbVdlNy01REpRPT0=|1458149815|81019dc549068aca2acd2e176470e30bfa6fe3e0"',
#     '_xsrf': '218730119c596a83ce597b8f3d81d131', 'd_c0': '"AFAAEClCoQmPTsKr8UgE_I3xArky-5gOYUk=|1458220693"',
#     '__utmt': '1', '__utma': '51854390.1552009964.1459268660.1459757284.1459757289.8',
#     '__utmb': '51854390.11.9.1459777747630', '__utmc': '51854390',
#     '__utmz': '51854390.1459757284.7.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
#     '__utmv': '51854390.100-2|2=registration_date=20120119=1^3=entry_date=20120119=1'
# }
heads = {
    # "accept": "*/*",
    # "accept-encoding": "gzip, deflate",
    # "accept-language": "en",
    # "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": '_za=34adb349-e062-46b9-82a5-64fd520ef9c5; udid="AHCAIMEzoAmPTnixU3omYAu-_0f4CpAAFAM=|1458149808"; q_c1=ed311be6f7a346a78556078b42c211b6|1460864902000|1458149807000; l_cap_id="Y2I5ZmYzYzFhZTRjNDhkYThjMzNkMzlkNGY3YjIyZWY=|1460881502|0fa71fc7b891599583a904dff0dcf6e480ef3d25"; cap_id="MTVkMmNmNDY1NjVlNDk1YjljZDEyYjIzMTZhNjNmMjU=|1460881502|fee595161b6ce41b29b8da83f60fb0694d09cd72"; d_c0="AFAAEClCoQmPTsKr8UgE_I3xArky-5gOYUk=|1460881506"; _zap=bf766f0b-7c16-4f69-99e7-a8a2d0e8f0c5; login="ODRkNWE5ZGU1ZTQ3NDNhOWJiYjcxNGViYjE3NzNkYTg=|1460881513|6b8cd30a653bc62c06d682efafca6c4e3e0f1789"; z_c0="QUFEQWxBa1pBQUFYQUFBQVlRSlZUV25WT2xlTEVVdk5EZjd1UXdSU2VyakpOd1FEN2Vkdlp3PT0=|1460881513|6aeb5326a984b020a702606e0a2b5aadcb33df9c"; _xsrf=ee9056940b15195eece29014cd1d86e8; gsScrollPos=; s-t=autocomplete; s-q=%E7%BB%9D%E5%BD%B1; s-i=1; sid=f9fmqjro; __utmt=1; __utma=51854390.910875168.1463199081.1463199081.1463199081.1; __utmb=51854390.6.10.1463199081; __utmc=51854390; __utmz=51854390.1463199081.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-2|2=registration_date=20120119=1^3=entry_date=20120119=1',
    # "origin": "https://www.zhihu.com",
    # "referer": "https://www.zhihu.com/people/li-er-ran/followees",
    # "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
    # "x-requested-with": "XMLHttpRequest"
}
# result = requests.post(target, data=params, headers=heads, cookies=cookies)
result = requests.post(target, data=params, headers=heads)
print result.content
