#Script feito para gerar Sessoes de divulgaçao no discord, e é gratuito e ninguem tem o direito de vendelo
#Qualquer re-divulgaçao desse Script deve creditalo ao criador OutputPunk
#data de criaçao 14/11/2020
#data de publicação 29/11/2020
#this script is a public and free, dond re-selling plz
#
#links
#githun.com/Trooperbr
#youtube.com/c/OutputPunk
#https://discord.gg/znnGaZgpZc
#244474477264633857
#https://github.com/TrooperBr/autosender_mensager.git

from div_bot import Divulgation


print('[x] Hellow Web User, shall we be humble ?')
print('[x] dont use to free offend')
print('[x] good look')

if __name__ == '__main__':
    token =      str(input('[x]Token :'))
    channel_id = int(input('[x]Digite o id de um channel :'))
    mensage =    str(input('[x]Digite sua mensagem :'))
    if mensage == '':
        Divulgation(token, 'OutputPunk OWNA', channel_id=channel_id)
    else:
        Divulgation(token, mensage, channel_id = channel_id)
