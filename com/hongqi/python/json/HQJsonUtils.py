import json

def parjson(jsonString):
    resultJson = ''
    try:
        resultJson = json.loads(jsonString).replace(r"\\","\\")
    except Exception as e:
        return resultJson

# try:
#     s = '["早上好各位美女帅哥","系统早上好早上好亲","早上好上午好","早上好 ！","领导早上好","你好 ，早","丫头早丫头","嗯早上好","早上好早上好","早上好各位","早上好,肚子咕噜咕噜君","傻逼,早上好","汉子,早上好!","早上好~~~我要上学校~~天天不迟到~~~`走了~~白白~~~~","早早早早早上好!","早上好newday","睡觉去了,大家早上好","早上好了。。","早啊！","早上好!我要正能量~","早上好\\"。有一个姑凉","早上好,清晨的阳光","早啊,众卿～","早上好哟咦呀喂咯～","早上好!!!!准备起床了!","大家早上好...","上班咯 ~ ~ 大家早上 好~","大早晨的 , 早上好各位","哦哈呦 , 早上好 !","早"]'
#     json.loads(s)
#     print('##################')
# except Exception as e:
#     print(e)