'''
Instruções: 
• Leia atentamente cada pergunta. 
• Escreva os scripts em Python para responder a cada questão. 
• Cada questão possui quatro alternativas, sendo apenas uma correta. 
• A cada pergunta, coloque a alternativa correta que corresponde ao resultado do script. 
• Crie um projeto no git (público) 
o O código no git deverá ter o arquivo (main) que será responsável por fazer todas a chamadas das funções 
o Se necessário adicionar pacotes e versões utilizadas no README 

'''

from questions import *

def main():

    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    print("Resposta da questão 1:", question_1(lista))

    lista = ["engenharia", "dados", "python", "engenharia", "dados", "engenharia","produção", "engenharia"]
    palavra = "engenharia"
    print("Resposta da questão 2:", question_2(lista, palavra))

    lista = [4,2,3,5,8,10,15,11,16,20]
    print("Resposta da questão 3:", question_3(lista))

    lista = ["dados", "engenharia", "desenvolvimento", "python", "processos", "data", "pipeline"]
    print("Resposta da questão 4:", question_4(lista))

    n = 5
    print("Resposta da questão 5:", question_5(n))

    data = "2021-09-11"
    print("Resposta da questão 6:", question_6(data))

    palavra = "arara"
    print("Resposta da questão 7:", question_7(palavra))

    nome_arquivo = "arquivo.txt"
    print("Resposta da questão 8:", question_8(nome_arquivo))

if __name__ == "__main__":
    main()