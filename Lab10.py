matriz_minha = []
verificador = True
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
n = 0

for n in range(N):
    n = 1 #N é número de palavras a buscar
    palavra_busca = str(input())
    palavra_letras = list(palavra_busca)

lista_coluna = []
grande = []
#print(matriz_minha)
#print(palavra_letras)
#função que busca a palavra na horizontal

def horizontal(matriz, linha, coluna, palavra):
      for i in range(len(matriz)):       
          linha = list(matriz[i])
          print(linha) 
          posição = i
          print(posição)
          for j in range(len(linha)):
               coluna = linha[j]
               print(coluna)
               posição_2 = j
               print(posição_2)
               #continue
               for x in range(len(palavra)):
                   #print((max(range(len(linha)))))
       #x é a posição que a letra ocupa na lista
                   i1 = posição
                   j1 = posição_2 + x
                   print(i)
                   print(j)
                   print(x)
                   if j1 < max(range(len(linha))) or j1 == max(range(len(linha))):
                       if matriz[i1][j1] == palavra[x] or matriz[i1][j1] == "*":
                           matriz[i1][j1] = matriz[i1][j1].upper()
                           grande.append(matriz[i1][j1])
                           continue
                           #if len(grande) == len(palavra_letras):
                                 #continue
                                       
          #continue
      return True 

print("-" * 40)
print("Lista de Palavras")
print("-" * 40)

print("Palavra:", palavra_busca)
#print("Ocorrencias:", ocorrencias)
print("-" * 40)

if horizontal(matriz_minha, linha, coluna, palavra_letras) == True: 
   for linha in matriz_minha:
        print(" ".join(linha))

#for linha in matriz_minha:
        #print(" ".join(linha)) 