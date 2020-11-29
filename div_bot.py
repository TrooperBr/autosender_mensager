import requests
import random
import time
import os
#Script feito para gerar Sessoes de divulgaçao no discord, e é gratuito e ninguem tem o direito de vendelo
#Qualquer re-divulgaçao desse Script deve creditalo ao criador OutputPunk
#data de criaçao 14/11/2020
#data de publicação 29/11/2020
#links
#githun.com/Trooperbr
#youtube.com/c/OutputPunk
#https://discord.gg/znnGaZgpZc
#244474477264633857


class Divulgation:
    token = None #token]
    colors = ['0','8','1','9','2','A','3','B','4','C','5','D','6','E','7','F']
    for_nonce = [782143483430305792, 1606547938.2630892] #379 1963 3408 time.time()-for_nonce[1]
    authority = 'discordapp.com'

    def __init__(self,token, mensage, channel_id):
        self.session = requests.Session()
        self.session.headers['Authorization'] =token
        self.session.headers['authority'] = self.authority
        self.token = token
        self.change_windows_color()
        tr = int(input('numero de tentativas :'))
        for i in range(0,tr):
            self.send_to_room(self.get_payload(), channel_id)
            self.change_windows_color()

    #you can add a name with the mensage add [NAME] on menssage and creating a get_people_name function
    def get_msg(self, name='juau'):
        _str = ''
        c = 1
        l = self.msg.split('[NAME]')
        for i in l:
            _str += str(i)
            if c != len(l):
                _str += name
            c += 1
        return _str


    def change_windows_color(self):
        if os.name == 'nt':
            os.system(f'color 0{random.choice(self.colors)}')


    def get_nonce(self):
        return self.for_nonce[1]+((time.time()-self.for_nonce[1])*1_00_0000_0000)

    #you can make a outher def or adapt this function for channels messagens
    def get_headers_pv(self,token, pv_id):
        return {'Authorization':token,
        'User-Agent':self.random_agent(),
        'Connection':'keep-alive',
        'Content-Type':'application/json',
        'Host':'discord.com',
        'Origin':'https://discord.com',
        'Referer':f'https://discord.com/channels/@me/{pv_id}'}


    def get_payload(self, msg='OutputPunk OWNA'):
        payload = {'content':msg}
        payload['nonce'] = self.get_nonce()
        payload['tts']   = 'false'
        return payload


    def send_to_room(self, payload, room):
        try:
            request = requests.Request('POST',f'https://discord.com/api/v8/channels/{room}/messages', data=payload)
            prepper = self.session.prepare_request(request)
            prepper.headers['content-type'] = 'application/json'
            r = self.session.send(prepper, verify=True) #se bugar troca o veridy=True para False e testa denovo
            if r.status_code == 200:
                print('sended !')
            elif r.status_code == 429:
                data = json.loads(r.text)
                print('Wait')
                time.sleep(data['retry_after'])
            else:
                print(f'erro {r.status_code}')

        except Exception as e:
            print(errorWarn)




    def send_to_people(self, payload, pv_id): #@me/xxxxxxxxxxx ---> pv_id
        headers = self.get_headers_pv(self.token, pv_id)
        r = requests.post(f'https://discord.com/api/v8/channels/{pv_id}/messages', headers=headers, json=payload)
        print(r)

    def random_agent(self):
    	uagent=[]
    	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    	uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0")
    	return random.choice(uagent)



if __name__ == '__main__':
    token = str(input('Token :'))
    channel_id = int(input('Digite o id de um channel :'))
    Divulgation(token, 'OutputPunk OWNA', channel_id=channel_id)
