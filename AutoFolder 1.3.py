import os
import shutil

#aqui é um trecho de código para quando se cria uma pasta nova, e ai nao terá a detecção do número do sequencial automaticamente
seq = 0
#percorre o diretório atual
for name in os.listdir("."):
    #checa se o "name" é uma pasta
    if os.path.isdir(name):
        #se for uma pasta separa o nome da pasta em uma lista
        num = name.split()
        #se o nome da pasta estiver no padrão de proposta (QTSL XXXX CLIENTE) o len será >1
        if len(num)>1:
            #compara o sequencial da pasta encontrada com a variável seq = 0
            if int(num[1]) > seq:
                #se o sequencial da pasta existir, iguala o sequencial
                seq = int(num[1])
#adiciona 1 unidade ao sequencial para gerar a pasta da próxima proposta posteriormente
seq +=1


#Aqui entra na parte principal do programa
if seq > 2:
    #detecta o sequencial da pasta da proposta anterior e pergunta ao usuário se deseja usar o sequencial anterior +1
    print ("Deseja usar o número sequencial detectado para esta proposta "+ str(seq) +"? (s/n)")
    s_n = input()
    if s_n == "s":
      sequencial = str(seq)
    #caso o usuário nao queira usar o sequencial detectado deverá inserir a numeraçao manualmente
    elif s_n == "n":
        print("Insira o número da proposta: ")
        sequencial = input()
    #se o usuário inserir uma resposta inválida acima deverá inserir o sequencial manualmente
    else:
        print("Resposta inválida. Insira o número do sequencial manualmente:")
        sequencial = input()

#captura o nome do cliente para inserir no endereço da pasta posteriormente        
print("Insira o nome do cliente: ")
nome_cliente = input()

#Endereço da pasta a ser copiada
fonte = r"000_modelo_pasta_proposta"

#destino1 cria o endereço da pasta a ser criada com base no input do usuário
destino1 = r"QTSL " + sequencial + " - " + nome_cliente
#aqui é definido as subpastas que conterão arquivos
#as demais pastas que nao terão arquivos renomeados dentro nao precisam ser referenciadas pois a função copytree copia as subpastas como padrão
destino2 = destino1+r"\06. Dimensionamento"
destino3 = destino1+r"\07. Proposta"
destino4 = destino1+r"\05. Registros Fotográficos"

#cria os parâmetros para renomear o arquivo de dimensionamento para adicionar o sequencial da proposta
old_name2 = destino2+r"\QTSL XXXX Dimensionamento Rev00.xvsp"
new_name2 = destino2+r"\QTSL "+ sequencial +" Dimensionamento Rev00.xvsp"
#cria os parâmetros para renomear o arquivo de proposta comercial para adicionar o sequencial da proposta
old_name3 = destino3+r"\QTSL XXXX - Proposta Comercial de Serviço Rev00 V1.2.xlsx"
new_name3 = destino3+r"\QTSL "+ sequencial +" - Proposta Comercial de Serviço Rev00.xlsx"
#cria os parâmetros para renomear o arquivo de proposta formato .doc para adicionar o sequencial da proposta
old_name4 = destino3+r"\QTSL XXXX - Proposta Comercial de Serviço Rev00.doc"
new_name4 = destino3+r"\QTSL "+ sequencial +" - Proposta Comercial de Serviço Rev00.doc"
#cria os parâmetros para renomear o arquivo de registro fotográfico para adicionar o sequencial da proposta
old_name5 = destino4+r"\QTSL XXXX - Registro Fotográfico.docx"
new_name5 = destino4+r"\QTSL "+ sequencial +" - Registro Fotográfico.docx"

#cria a pasta raiz da nova proposta
shutil.copytree(fonte, destino1)

#renomeia os arquivos
os.rename(old_name2, new_name2)
os.rename(old_name3, new_name3)
os.rename(old_name4, new_name4)
os.rename(old_name5, new_name5)

print('\n')
print('Pasta criada com sucesso!!!')

print('\n\n')
print('Pressiona qualquer tecla para fechar esta janela...')
#o parâmetro >nul faz com que não exiba a mensagem padrão do comando "pause"
os.system("pause >nul")

exit()
