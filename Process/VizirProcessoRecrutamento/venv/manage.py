import Sem_FaleMais as sfm
import Com_FaleMais as cfm
import validacao as val


#           Dicionário
#     eo = escolha origem
#     ed = escolha destino
#     min = minutos escolhidos pelo usuário
#     total = total do valor
#     sfm = sem fale mais
#     val = validação
#     vl = validação range 1:5
#     ofm = opção fale mais
#     cfm = com fale mais
#     fmt = falemais total
#     dm = difereça do minuto
#     vm = valor do minuto
#     tsfm = total sem fale mais


print('Escolha dentre as opções o dd origem e logo o dd destino'
      ' \n[1] 011\n[2] 016\n[3] 017\n[4] 018')
eo = int(input("coloque a opção do dd origem: "))
val.vl(eo)
ed = int(input("coloque a opção do dd destino: "))
val.vl(ed)
min = int(input("número de minutos: "))
print('Escolha dentre as opções o plano que deseja:'
      '\n[1] FaleMais 30\n[2] FaleMais 60\n[3] FaleMais 120\n[4] Sem FaleMais')
ofm = int(input("Qual opção deseja escolher: "))
val.vl(ofm)
vm = 0
total = sfm.Sem_Fale(eo, ed, min.__abs__())
vm = total[1]
fmt = cfm.Com_FaleMais(ofm, min, vm, total[0])
print(f'O preço da ligação será de R${fmt:.2f} com o plano e R${total[0]} sem o plano')



