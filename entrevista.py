import json

#QUESTÃO 1


#vars
INDICE = 13
SOMA = 0
K = 0
while K<INDICE:
    K= K+1
    SOMA = SOMA + K
    print(SOMA)
#ao final do processo o valor será 91    


#QUESTÃO 2 


#vars
num = int(input('Digite um número ->'))

#functions
def fibonacci(numero):
    a, b = 0, 1 #primeiros numeros da sequencia
    while a <= numero: #se a for igual ao numero digitado ele é fibonacci
        if a == numero: 
            return True
        a,b = b, a + b #se n for igual aumenta a sequencia de fibonacci e testa novamente
    return False

if fibonacci(num):
    print(f'O número {num} pertence a sequencia de Fibonacci')
else:
    print(f'O número {num} não pertence a sequencia de Fibonacci')
    
    
    
#QUESTÃO 3 
# não encontrei a fonte de dados json para usar na questão portanto criei essa por conta propria
import json

faturamentoMensal = {
    "faturamento_diario": [
        {"dia": 1, "valor": 22174.1664},
        {"dia": 2, "valor": 24537.6698},
        {"dia": 3, "valor": 26139.6134},
        {"dia": 4, "valor": 0.0},
        {"dia": 5, "valor": 0.0},
        {"dia": 6, "valor": 26742.6612},
        {"dia": 7, "valor": 0.0},
        {"dia": 8, "valor": 42889.2258},
        {"dia": 9, "valor": 46251.174},
        {"dia": 10, "valor": 11191.4722},
        {"dia": 11, "valor": 0.0},
        {"dia": 12, "valor": 0.0},
        {"dia": 13, "valor": 3847.4823},
        {"dia": 14, "valor": 373.7838},
        {"dia": 15, "valor": 2659.7563},
        {"dia": 16, "valor": 48924.2448},
        {"dia": 17, "valor": 18419.2614},
        {"dia": 18, "valor": 0.0},
        {"dia": 19, "valor": 0.0},
        {"dia": 20, "valor": 35240.1826},
        {"dia": 21, "valor": 43829.1667},
        {"dia": 22, "valor": 18235.6852},
        {"dia": 23, "valor": 4355.0662},
        {"dia": 24, "valor": 13327.1025},
        {"dia": 25, "valor": 0.0},
        {"dia": 26, "valor": 0.0},
        {"dia": 27, "valor": 25681.8318},
        {"dia": 28, "valor": 1718.1221},
        {"dia": 29, "valor": 0.0},
        {"dia": 30, "valor": 0.0}
    ]
}

def calcularEstaticas(faturamento):
    faturamento = [dia['valor'] for dia in faturamento if dia['valor'] > 0] 
    # Não contabiliza dias com faturamento 0
    
    menorFaturamento = min(faturamento)
    maiorFaturamento = max(faturamento) 
    mediaMensal = sum(faturamento) / len(faturamento)
    
    acimaMedia = sum(1 for valor in faturamento if valor > mediaMensal)
    return menorFaturamento, maiorFaturamento, acimaMedia

menorFaturamento, maiorFaturamento, acimaMedia = calcularEstaticas(faturamentoMensal['faturamento_diario'])

# Resultados
print(f"Menor valor de faturamento em um dia foi de R$ {menorFaturamento:.2f}")
print(f"Maior valor de faturamento em um dia foi de R$ {maiorFaturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {acimaMedia}")


#QUESTÃO 4
SP = 67836.43 
RJ = 36678.66 
MG = 29229.88 
ES = 27165.48 
OUTROS = 19849.53 
total = SP+RJ+MG+ES+OUTROS
#formula abstraida da regra de 3
def porcentagemFaturamento(cidade):
    porcento = (cidade*100)//total
    return porcento
faturamentoSP = porcentagemFaturamento(SP)
faturamentoRJ = porcentagemFaturamento(RJ)
faturamentoMG = porcentagemFaturamento(MG)
faturamentoES = porcentagemFaturamento(ES)
faturamentoOutros = porcentagemFaturamento(OUTROS)
#divisão assim para reduzir as casas decimais
print(f'Sp teve {faturamentoSP}%,MG teve {faturamentoMG}%,RJ teve {faturamentoRJ}%,ES teve {faturamentoES}%,OUTROS teve {faturamentoOutros}%')


#QUESTÃO 5
palavra = str(input('digite uma palavra: '))

def inverterString(palavra):
    StringInvertida = ""
    for i in range(len(palavra)- 1,-1,-1):
    #cria uma sequência de índices que começa do último caractere, vai até o primeiro caractere, e decrementa de um em um, permitindo que o loop percorra a string de trás para frente.
        StringInvertida += palavra[i]
    return StringInvertida     

print(inverterString(palavra))   
