def question_1(lista):
    '''
        Questão 1: Soma de Números Pares 
        Escreva um script em Python que soma todos os números pares de uma lista de inteiros fornecida. 
        lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30] 
        Qual será o valor retornado pelo código? 
        A) 160 
        B) 240 
        C) 200 
        D) 120 
    '''
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    return soma


def question_2(lista, palavra):
    '''
    Escreva um script que conte quantas vezes uma palavra específica aparece em uma lista de strings. 
    lista = ["engenharia", "dados", "python", "engenharia", "dados", "engenharia","produção", "engenharia"] 
    palavra = "engenharia" 
    Quantas vezes a palavra "engenharia" aparece na lista? 
    A) 2 
    B) 3 
    C) 4 
    D) 5 
    '''

    count = 0

    for i in lista:
        if i == palavra:
            count += 1

    return count
    
def question_3(lista):
    '''
        Dada uma lista de números inteiros, escreva um script que retorne apenas os valores maiores que 10. 
        Qual será o valor retornado pelo código? 
        Lista = [4,2,3,5,8,10,15,11,16,20]
        A) [11, 15, 16, 20]
        B) [10, 15, 20, 30] 
        C) [11, 20] 
        D) [15] 
    '''

    lista_new = []
    for i in lista:
        if i > 10:
            lista_new.append(i)
            lista_new.sort()

    return lista_new

def question_4(lista):
    '''
        Escreva um script em Python que agrupa as palavras de uma lista por sua primeira letra. 
        lista = ["dados", "engenharia", "desenvolvimento", "python", "processos", "data", "pipeline"]
        Qual será o dicionário de saída esperado? 
        A) {'d': ['dados', 'desenvolvimento', 'data'], 'e': ['engenharia'], 'p': ['python', 'processos', 'pipeline']} 
        B) {'d': ['dados', 'desenvolvimento'], 'e': ['engenharia'], 'p': ['python', 'processos']} 
        C) {'d': ['dados', 'data'], 'e': ['engenharia'], 'p': ['python', 'pipeline']} 
        D) {'d': ['data'], 'e': ['engenharia'], 'p': ['pipeline']} 
    '''
    dicionario = {}
    for palavra in lista:
        primeira_letra = palavra[0]
        if primeira_letra not in dicionario:
            dicionario[primeira_letra] = []
        dicionario[primeira_letra].append(palavra)
    return dicionario

def question_5(n):
    '''Questão 5: Fatorial Recursivo 
        Escreva um script para calcular o fatorial de um número de forma recursiva. 
        Qual será o resultado de fatorial(5)? 
        A) 120 
        B) 24 
        C) 60 
        D) 5 
    '''
    fatorial = 1

    while n > 0:
        fatorial *= n
        n-=1

    return fatorial

def question_6(data):
    '''
        Escreva um script que converta uma data no formato YYYY-MM-DD para o formato DD/MM/YYYY. 
        Qual será o valor retornado pelo código? 
        Data = 2021-09-11
        A) 11/09/2021 
        B) 09/11/2021 
        C) 2021/11/09 
        D) 09/2021/11 
    '''
    data_split = data.split("-")
    nova_data = f'{data_split[2]}/{data_split[1]}/{data_split[0]}'

    return nova_data

def question_7(palavra):
    '''
        Questão 7: Palíndromo 
        Escreva um script que verifique se uma string é um palíndromo (lê-se da mesma forma de trás para frente). 
        Qual será o resultado para a palavra "arara"? 
        A) Verdadeiro 
        B) Falso 
        C) Nenhum resultado 
        D) Erro no código
    '''

    if palavra == palavra[::-1]:
        palindromo = 'Verdadeiro'
    else:
        palindromo = 'Falso'

    return palindromo

def question_8(nome_arquivo):
    '''
        Questão 8: Leitura de arquivo 
        O código abaixo tenta contar o número de linhas em um arquivo, mas contém um erro. 
        arquivo.txt
        Linha 1
        Linha 2
        Linha 3
        Linha 4
        Linha 5
        Linha 6

        def contar_linhas(nome_arquivo): 
        arquivo = open(nome_arquivo, 'r') 
        contador = 0 
        for linha in arquivo.readlines(): 
            contador = contador + 1 
        return contador 

        Erro: O arquivo não é fechado após a leitura. 
        Como corrigir o código? 
        A) Usar with open(). 
        B) Adicionar arquivo.close() ao final. 
        C) Trocar open() por with(). 
        D) O código está correto.
    '''
    def contar_linhas(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            contador = 0
            for linha in arquivo:
                contador += 1
            return contador
    
    contador = contar_linhas(nome_arquivo)
    return contador