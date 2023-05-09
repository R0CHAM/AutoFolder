import os
import shutil
import time

seq = 0
for name in os.listdir("."):
    if os.path.isdir(name):
        num = name.split()
        if len(num)>1:
            if int(num[1]) > seq:
                seq = int(num[1])
seq +=1

if seq > 2:
    print ("Deseja usar o número sequencial detectado para esta proposta "+ str(seq) +"? (s/n)")
    s_n = input()
    if s_n == "s":
      sequencial = str(seq)
    elif s_n == "n":
        print("Insira o número da proposta: ")
        sequencial = input()
    else:
        print("Resposta inválida. Insira o número do sequencial manualmente. \n")
        
else:
    print("Insira o número da proposta: ")
    sequencial = input()
        
print("Insira o nome do cliente: ")
nome_cliente = input()

fonte = r"000_modelo_pasta_proposta"

destino1 = r"QTSL " + sequencial + " - " + nome_cliente
destino2 = destino1+r"\06. Dimensionamento"
destino3 = destino1+r"\07. Proposta"
destino4 = destino1+r"\05. Registros Fotográficos"

old_name2 = destino2+r"\QTSL XXXX Dimensionamento Rev00.xvsp"
new_name2 = destino2+r"\QTSL "+ sequencial +" Dimensionamento Rev00.xvsp"

old_name3 = destino3+r"\QTSL XXXX - Proposta Comercial de Serviço Rev00 V1.11.xlsx"
new_name3 = destino3+r"\QTSL "+ sequencial +" - Proposta Comercial de Serviço Rev00.xlsx"

old_name4 = destino3+r"\QTSL XXXX - Proposta Comercial de Serviço Rev00.doc"
new_name4 = destino3+r"\QTSL "+ sequencial +" - Proposta Comercial de Serviço Rev00.doc"

old_name5 = destino4+r"\QTSL XXXX - Registro Fotográfico.docx"
new_name5 = destino4+r"\QTSL "+ sequencial +" - Registro Fotográfico.docx"

shutil.copytree(fonte, destino1)

os.rename(old_name2, new_name2)
os.rename(old_name3, new_name3)
os.rename(old_name4, new_name4)
os.rename(old_name5, new_name5)


print('Pasta criada com sucesso!!!')


print('\n\nEsta janela fechará em 3 segundos...')
time.sleep(3)


exit()
