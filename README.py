start = input('''
         <><><><><><><><><><> HIT TO PROCEED <><><><><><><><><><>

> Sejá bem vindo ao jogo que irá estimular o seu aprendizado no inglês instrumental!
> Seu objetivo é fazer a maior pontuação traduzindo corretamente as palavras!
> Cada acerto 2 pontos, cada dica -1 ponto, cada erro 0 pontos.

>>>>> Are you ready??? Come on! Let's go!!! 

Pressione enter para continuar
''')

participante = input("Nome do jogador: ")
pontuacao=0

print("")

questao1 = input('Questão {}. Informe a tradução da palavra "demo":'.format(pontuacao + 1))
resposta_correta1 = ['demonstração','demonstracao', 'demonstração']
if resposta_correta1.__contains__(questao1):
     pontuacao = pontuacao+1
     print("Você Acertou!")
else:
    print("Você errou!")

print("=-" * 20)

questao2 = input('Questão {}. Informe a tradução da palavra "disable":'.format(pontuacao + 1))
resposta_correta2 = ['desativar',' desativar','mutilar','incapacitar']
if resposta_correta2.__contains__(questao2):
    pontuacao = pontuacao + 1
    print('Você acertou!')
else:
    print('Você errou!')

print("=-" * 20)

questao3 = input('Questão {}. Informe a tradução da palavra "download":'.format(pontuacao + 1))
resposta_correta3 = ['descarregar','baixar',' descarregar',' baixar']
if resposta_correta3.__contains__(questao3):
    pontuacao = pontuacao + 1
    print('Você acertou!')
else:
    print('Você errou!')

print("=-" * 20)

questao4 = input('Questão {}. Informe a tradução da palavra "data":'.format(pontuacao + 1))
resposta_correta4 = ["dados", "dados","dados "]
if resposta_correta4.__contains__(questao4):
    pontuacao = pontuacao + 1
    print('Você acertou')
else:
    print('Você errou!')

print("=-" * 20)

questao5 = input('Questão {}. Informe a Tradução da palavra "Dual Core ":'.format(pontuacao + 1))
resposta_correta5 = ["dois núcleos","binúcleado"," binucleado","dois nucleos"]
if resposta_correta5.__contains__(questao5):
    pontuacao = pontuacao + 1
    print("Você acertou!")
else:
    print("Você errou!")

print("=-" * 20)

questao6 = input('Questão {}. Informe a tradução da palavra "dial":'.format(pontuacao + 1))
resposta_correta6 = ["discar","ligar"]
if resposta_correta6.__contains__(questao6):
    pontuacao = pontuacao + 1
    print("Você acertou!")
else:
    print("Você errou!")

print("=-" * 20)

questao7 = input('Questão {}. Informe a tradução da palavra "destination":'.format(pontuacao + 1))
resposta_correta7 = ["destino"," destino","destinação"]
if resposta_correta7.__contains__(questao7):
    pontuacao = pontuacao + 1
    print("Você acertou!")
else:
    print("Você errou!")

print("=-" * 20)

questao8 = input('Questão {}. Informe a tradução da palavra "disc":'.format(pontuacao + 1))
resposta_correta8 = ["disco"," disco","disco "]
if resposta_correta8.__contains__(questao8):
    pontuacao = pontuacao + 1
    print("Você acertou!")
else:
    print("Você errou!")

print("=-" * 20)

questao9 = input('Questão {}. Informe a tradução da palavra "drone":'.format(pontuacao + 1))
resposta_correta9 = "zangão"
if questao9 == resposta_correta9:
    pontuacao = pontuacao + 1
    print("Você acertou!")
else:
    print("Você errou!")

print("=-" * 20)

questao10 = input('Questão {}. Informe a tradução da palavra "dash":'.format(pontuacao + 1))
resposta_correta10 = ["travessão"," travessao","travessao"]
if resposta_correta10.__contains__(questao10):
    pontuacao = pontuacao + 1
    print("Você acertou!")
else:
    print("Você errou!")

print("=-" * 20)

questao11 = input('Questão {}. Informe a tradução da palavra "date":'.format(pontuacao + 1))
resposta_correta11 = "data"
if questao11 == resposta_correta11:
    pontuacao = pontuacao + 1
    print("Você acertou!")
else:
    print("Você errou!")

print("=-" * 20)

questao12 = input('Questão {}. Informe a tradução da palavra "developer":'.format(pontuacao + 1))
resposta_correta12 = "desenvolvedor"
if questao12 == resposta_correta12:
    pontuacao = pontuacao + 1
    print("Você acertou!")
else:
    print("Você errou!")

print("=-" * 20)

questao13 = input('Questão {}. Informe a tradução da palavra "dial-up":'.format(pontuacao + 1))
resposta_correta13 = "discado"
if questao13 == resposta_correta13:
    pontuacao = pontuacao + 1
    print("Você acertou!")
else:
    print("Você errou!")

print("=-" * 20)

questao14 = input('Questão {}. Informe a tradução da palavra "dial-up connection":'.format(pontuacao + 1))
resposta_correta14 = "conexão discada"
if questao14 == resposta_correta14:
    pontuacao = pontuacao + 1
    print("Você acertou!")
else:
    print("Você errou!")

print("=-" * 15)

questao15 = input('Questão {}. Informe a tradução da palavra "devlopment":'.format(pontuacao + 1))
resposta_correta15 = "desenvolvimento"
if questao15 == resposta_correta15:
    pontuacao = pontuacao + 1
    print('voCẽ acertou')
else:
    print('Você errou!')

print("=-" * 15)

print("A pontuação do jogador: ",participante, "foi de  ",pontuacao,"pontos!")
