matriz_minha = []
verificador = True
caracterCoringa = '*'
ocorrencias = 0

N = 0
maiusculas = []
while verificador:
     linha = str(input()) 

     if linha.isdigit():
        N = int(linha)
        verificador = False
     else:
        matriz_minha.append(list(linha))
for linha in matriz_minha:
    for coluna in linha:
         matriz_minha

matriz_lista = []
lista_up = []
matriz_grande = []
palavra_letras = []
n = 0

for n in range(N):
    n = 1 #N é número de palavras a buscar
    palavra_busca = str(input())
    palavra_letras.append(list(palavra_busca))

lista_coluna = []
grande = []

def horizontal(matriz, linha, coluna, palavra):

    tamanhoPalavra = len(palavra)
    match = 0
    posicaoPalavra = 0
    global ocorrencias

    for m in range(len(matriz)):       
        linha = list(matriz[m])
        match = 0
        
        for l in range(len(linha)):
  
            if linha[l].lower() == caracterCoringa or linha[l].lower() == palavra[match].lower():
                match=match+1

            if match == tamanhoPalavra:
                match = 0
                ocorrencias = ocorrencias + 1
                return True

    return False 


def vertical(matriz, linha, coluna, palavra):
    
    tamanhoPalavra = len(palavra)
    tamanhoMatriz = len(matriz[0])
    match = 0
    posicaoPalavra =0
    global ocorrencias

    for col in range(tamanhoMatriz):       
        match = 0
        
        for lin in range(len(matriz)):
         
            if matriz[lin][col].lower() == caracterCoringa or matriz[lin][col].lower() == palavra[match].lower():
                match=match+1

            if match == tamanhoPalavra:
                match = 0
                ocorrencias = ocorrencias+1
                return True

    return False 


def diagonal1(matriz, linha, coluna, palavra):
    
    tamanhoPalavra = len(palavra)
    tamColunas = len(matriz[0])
    tamLinhas = len(matriz)
    match = 0
    global ocorrencias

    for colunaPivo in range(tamColunas):       
        match = 0
        lin = 0
        for col in range(tamColunas):

            colTemp = col + colunaPivo

            if lin < tamLinhas and colTemp < tamColunas:
                if(matriz[lin][colTemp].lower() == ' '):
                    col=col+1
                    continue
        
                if matriz[lin][colTemp].lower() == caracterCoringa or matriz[lin][colTemp].lower() == palavra[match].lower():
                    match=match+1

                if match == tamanhoPalavra:
                    match = 0
                    ocorrencias = ocorrencias+1
                    return True

                lin = lin+1

    return False 

def diagonal2(matriz, linha, coluna, palavra):
    
    tamanhoPalavra = len(palavra)
    tamColunas = len(matriz[0])
    tamLinhas = len(matriz)
    match = 0
    global ocorrencias    

    for colunaPivo in range(tamColunas,-1,-1):       
        match = 0
        lin = 0
        for col in range(tamColunas):

            colTemp = (colunaPivo - col)-1

            if lin < tamLinhas and colTemp > 0:
                if(matriz[lin][colTemp].lower() == ' '):
                    col=col-1
                    continue
        
                if matriz[lin][colTemp].lower() == caracterCoringa or matriz[lin][colTemp].lower() == palavra[match].lower():
                    match=match+1

                if match == tamanhoPalavra:
                    match = 0
                    ocorrencias = ocorrencias+1
                    return True

                lin = lin+1

    return False

def findPalavras(matriz, linha, coluna, palavra):

if horizontal(matriz_minha, linha, coluna, palavra_letras) == True: 
   print("horizontal achou")

if diagonal1(matriz_minha, linha, coluna, palavra_letras) == True: 
   print("diagonal1 achou")


if diagonal2(matriz_minha, linha, coluna, palavra_letras) == True: 
   print("diagonal2 achou")

if vertical(matriz_minha, linha, coluna, palavra_letras) == True: 
   print("vertical achou")

print("-" * 40)
print("Lista de Palavras")
print("-" * 40)

print("Palavra:", palavra_busca)
print("Ocorrencias:", ocorrencias)
print("-" * 40)


#for linha in matriz_minha:
        #print(" ".join(linha)) 