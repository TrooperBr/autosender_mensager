#Script feito para gerar Sessoes de divulgaçao no discord, e é gratuito e ninguem tem o direito de vendelo
#Qualquer re-divulgaçao desse Script deve creditalo ao criador OutputPunk
#data de criaçao 14/11/2020
#data de publicação 29/11/2020
#links
#githun.com/Trooperbr
#youtube.com/c/OutputPunk
#https://discord.gg/znnGaZgpZc
#244474477264633857
from div_bot import Divulgation



if __name__ == '__main__':
    token =      str(input('Token :'))
    channel_id = int(input('Digite o id de um channel :'))
    mensage =    str(input('Digite sua mensagem :')) 
    Divulgation(token, 'OutputPunk OWNA', channel_id=channel_id)
