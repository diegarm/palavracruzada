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

def horizontal(matriz, palavra):

    tamanhoPalavra = len(palavra)
    match = 0
    posicaoPalavra = 0
    global ocorrencias

    for m in range(len(matriz)):       
        linha = list(matriz[m])
        match = 0
        linhaNew =[]
        
        for l in range(len(linha)):
  
            if linha[l].lower() == caracterCoringa or linha[l].lower() == palavra[match].lower():
                linhaNew.append(linha[l].upper())
                match=match+1
            else:
                linhaNew.append(linha[l].lower())


            if match == tamanhoPalavra:
                match = 0
                ocorrencias = ocorrencias + 1
                matriz[m] = linhaNew



def vertical(matriz, palavra):
    
    tamanhoPalavra = len(palavra)
    tamanhoMatriz = len(matriz[0])
    posAtualizar = []
    posAtualizarInv = []
    match = 0
    matchinv = 0
    global ocorrencias

    for col in range(tamanhoMatriz):       
        match = 0
        
        for lin in range(len(matriz)):
         
            if matriz[lin][col].lower() == caracterCoringa: 
                match=match+1
                matchinv = matchinv+1
            else:
                if matriz[lin][col].lower() == palavra[match].lower():
                    posAtualizar.append([lin,col])
                    match=match+1
                else:
                    posAtualizar.clear()
                    match = 0
                
                if matriz[lin][col].lower() == palavra[tamanhoPalavra-matchinv-1].lower():
                    posAtualizarInv.append([lin,col])
                    matchinv = matchinv+1
                else:
                    posAtualizarInv.clear()
                    matchinv = 0

            if match == tamanhoPalavra:
                match = 0
                ocorrencias = ocorrencias+1
                upperMatriz(posAtualizar)
                return True

            if matchinv == tamanhoPalavra:
                matchinv = 0
                ocorrencias = ocorrencias+1
                upperMatriz(posAtualizarInv)
                return True


def diagonal1(matriz, palavra):
    
    tamanhoPalavra = len(palavra)
    tamColunas = len(matriz[0])
    tamLinhas = len(matriz)
    posAtualizar = []
    posAtualizarInv = []
    match = 0
    matchinv = 0
    global ocorrencias

    for linha in range(tamLinhas,-1,-1):
        linhaTemp=linha
        matchinv = 0
        match = 0

        for coluna in range((tamLinhas-linha)*2):
            
            if matriz[linhaTemp][coluna].lower() == ' ':
                continue

            if matriz[linhaTemp][coluna].lower() == caracterCoringa: 
                match=match+1
                matchinv = matchinv+1
            else:
                if matriz[linhaTemp][coluna].lower() == palavra[match].lower():
                    posAtualizar.append([linhaTemp,coluna])
                    match=match+1
                else:
                    posAtualizar.clear()
                    match = 0
                
                if matriz[linhaTemp][coluna].lower() == palavra[tamanhoPalavra-matchinv-1].lower():
                    posAtualizarInv.append([linhaTemp,coluna])
                    matchinv = matchinv+1
                else:
                    posAtualizarInv.clear()
                    matchinv = 0

            if match == tamanhoPalavra:
                match = 0
                matchinv = 0
                ocorrencias = ocorrencias+1
                upperMatriz(posAtualizar)

            if matchinv == tamanhoPalavra:
                matchinv = 0
                match = 0
                ocorrencias = ocorrencias+1
                upperMatriz(posAtualizarInv)


            if matriz[linhaTemp][coluna] != ' ' and linhaTemp+1 < tamLinhas :
                linhaTemp = linhaTemp+1
            

    
    #######


    for coluna in range(2,tamColunas,2):
        
        colunaTemp = coluna
        matchinv = 0
        match = 0

        for linha in range(tamLinhas):
            
            if(tamColunas > colunaTemp):
                if matriz[linha][colunaTemp] == ' ':
                    colunaTemp = colunaTemp+1

                if matriz[linha][colunaTemp].lower() == caracterCoringa: 
                    match=match+1
                    matchinv = matchinv+1
                else:
                    if matriz[linha][colunaTemp].lower() == palavra[match].lower():
                        posAtualizar.append([linha,colunaTemp])
                        match=match+1
                    else:
                        posAtualizar.clear()
                        match = 0
                    
                    if matriz[linha][colunaTemp].lower() == palavra[tamanhoPalavra-matchinv-1].lower():
                        posAtualizarInv.append([linha,colunaTemp])
                        matchinv = matchinv+1
                    else:
                        posAtualizarInv.clear()
                        matchinv = 0

                if match == tamanhoPalavra:
                    match = 0
                    matchinv = 0
                    ocorrencias = ocorrencias+1
                    upperMatriz(posAtualizar)

                if matchinv == tamanhoPalavra:
                    matchinv = 0
                    match = 0
                    ocorrencias = ocorrencias+1
                    upperMatriz(posAtualizarInv)
                
                colunaTemp = colunaTemp+1
                        
                    

                 

def diagonal2(matriz, palavra):
    
    tamanhoPalavra = len(palavra)
    tamColunas = len(matriz[0])
    tamLinhas = len(matriz)
    posAtualizar = []
    posAtualizarInv = []
    match = 0
    matchinv = 0
    global ocorrencias    

    for colunaPivo in range(tamColunas,-1,-2):       
        matchinv = 0
        match = 0
        lin = 0
        for col in range(tamColunas):

            
            colTemp = (colunaPivo - col)-1

            if lin < tamLinhas and colTemp > 0:
                if(matriz[lin][colTemp].lower() == ' '):
                    col=col-1
                    continue
        
                if matriz[lin][colTemp].lower() == caracterCoringa: 
                    match=match+1
                    matchinv = matchinv+1
                else:
                    if matriz[lin][colTemp].lower() == palavra[match].lower():
                        posAtualizar.append([lin,colTemp])
                        match=match+1
                    else:
                        posAtualizar.clear()
                        match = 0
                    
                    if matriz[lin][colTemp].lower() == palavra[tamanhoPalavra-matchinv-1].lower():
                        posAtualizarInv.append([lin,colTemp])
                        matchinv = matchinv+1
                    else:
                        posAtualizarInv.clear()
                        matchinv = 0

                if match == tamanhoPalavra:
                    match = 0
                    matchinv = 0
                    ocorrencias = ocorrencias+1
                    upperMatriz(posAtualizar)

                if matchinv == tamanhoPalavra:
                    match = 0
                    matchinv = 0
                    ocorrencias = ocorrencias+1
                    upperMatriz(posAtualizarInv)
            
                lin = lin+1


    #######


    for coluna in range(2,tamColunas,2):
        
        colunaTemp = coluna
        matchinv = 0
        match = 0

        for linha in range(tamLinhas-1,0,-1):
            
            if(tamColunas > colunaTemp):
                if matriz[linha][colunaTemp] == ' ':
                    colunaTemp = colunaTemp+1

                if matriz[linha][colunaTemp].lower() == caracterCoringa: 
                    match=match+1
                    matchinv = matchinv+1
                else:
                    if matriz[linha][colunaTemp].lower() == palavra[match].lower():
                        posAtualizar.append([linha,colunaTemp])
                        match=match+1
                    else:
                        posAtualizar.clear()
                        match = 0
                    
                    if matriz[linha][colunaTemp].lower() == palavra[tamanhoPalavra-matchinv-1].lower():
                        posAtualizarInv.append([linha,colunaTemp])
                        matchinv = matchinv+1
                    else:
                        posAtualizarInv.clear()
                        matchinv = 0

                if match == tamanhoPalavra:
                    match = 0
                    matchinv = 0
                    ocorrencias = ocorrencias+1
                    upperMatriz(posAtualizar)

                if matchinv == tamanhoPalavra:
                    matchinv = 0
                    match = 0
                    ocorrencias = ocorrencias+1
                    upperMatriz(posAtualizarInv)
                
                colunaTemp = colunaTemp+1


def upperMatriz(posAtualizar):
    for p in posAtualizar:
        matriz_minha[p[0]][p[1]] = matriz_minha[p[0]][p[1]].upper()

def findPalavras(palavras):
    for iPalavra in range(len(palavras)):
        global ocorrencias
        ocorrencias = 0
        palavra = palavras[iPalavra]
        horizontal(matriz_minha, palavra)
        diagonal1(matriz_minha,palavra) 
        diagonal2(matriz_minha, palavra) 
        vertical(matriz_minha, palavra)
        print("Palavra:", "".join(palavra))
        print("Ocorrencias:", ocorrencias)
        print("-" * 40)
        

print("-" * 40)
print("Lista de Palavras")
print("-" * 40)
findPalavras(palavra_letras)
for linha in matriz_minha:
        print(" ".join(linha)) 



#for linha in matriz_minha:
        #print(" ".join(linha)) 