#Imports das bibliotecas
import json
import random

jogadores = {}


#Variáveis para abri o banco de dados em arquivo json
a = open("perguntas.json",encoding="utf8")
questoes = json.load(a)
questoes = questoes["questoes"]

#Váriavel para pegar uma questão aleatória
numeroaleatorio = random.randint(1,27)


#Várievel para não repetir questões
jatem = False
questoeslidas = []
temporizador = 0


while True:
    #Váriavel nome
    user = ''
    #Variável do temporizador para rodar 5 questões a cada partida
    temporizador = 0  
    #Pontução
    pontuacao = 0
    #Lista das questões já lidas
    questoeslidas = []
    acaboupartida = False
    print('----------------------')
    print('Olá, bem vindo ao quiz')
    print('Tema: Assuntos Gerais')
    print('----------------------\n')
    user = input('Digite seu nome: ')
    #While para verificar se já foram enviadas 5 perguntas.
    while temporizador != 5 and temporizador < 5:   
        for x in questoes:#For para printar as questões
            if acaboupartida == True:
                break    
            elif jatem != False:#estrutura com if para verificar se a pergunta é repetida.
                for idquestao in questoeslidas:
                    if idquestao == numeroaleatorio:
                        jatem = True   
                    elif jatem == True:
                        numeroaleatorio = random.randint(1,27)
                        jatem = False
                        continue        
                jatem = False 

            #If para linkar o numeroaleatorio com o número do id da questao no arquivo json    
            if numeroaleatorio == (x["id"]):
                print(f'Id da questão: {x["id"]}')
                print(f'Dificuldade: {x["dificuldade"]}')
                print(f'Pontuação: {x["pontuacao"]}')
                print(f'Pergunta: {x["pergunta"]}')
                print(f'Alt1: {x["alt1"]}')
                print(f'Alt2: {x["alt2"]}')
                print(f'Alt3: {x["alt3"]}')
                print(f'Alt4: {x["alt4"]}')
                print(f'Alt5: {x["alt5"]}')
                resposta = input('Digite sua resposta: ')
                if resposta == x["altcert"]:    #verificações se a resposta está correta
                    soma = eval(x["pontuacao"])
                    pontuacao += soma
                    print('----------------------')
                    print('Parabéns você acertou!')
                    print('-----------------------')
                    questoeslidas += [numeroaleatorio]#Adicionar as questões já enviadas, roletar um novo número e atualizar o temporizador de questões
                    numeroaleatorio = random.randint(1,27)
                    temporizador += 1
                    jatem = None#játem zerado para conferir se a questão vai ser repetida
                    if temporizador == 5:#If para verificar o fim da partida.
                        acaboupartida = True
                        print(f'Sua pontuação foi :{pontuacao}\nObrigado por jogar,{user}.\n-----------------------')
                        jogadores["pontuacao"] = pontuacao#variavel jogador enviada para o arquivo json jogadores para salvar os players
                        jogadores["nome"] = user
                        with open("player.json", 'a') as player:#parte na qual envia os nomes e as respectivas pontuações para o json
                            json.dump(jogadores, player, indent=4)           
                else:
                    print('-----------------------')
                    print('Você errou.')
                    print('-----------------------')
                    questoeslidas += [numeroaleatorio]
                    numeroaleatorio = random.randint(1,27)
                    temporizador += 1
                    jatem = None
                    if temporizador == 5:#If para verificar o fim da partida.
                        acaboupartida = True
                        print(f'Sua pontuação foi :{pontuacao}\nObrigado por jogar, {user}.\n-----------------------')
                        jogadores["pontuacao"] = pontuacao
                        jogadores["nome"] = user
                        with open("player.json", 'a') as player:
                            json.dump(jogadores, player, indent=4)
                            
                      