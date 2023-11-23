import random
ponto_meu = 0
ponto_pc = 0

opcoes = ["pedra", "papel", "tesoura"]
while(True):
  jogada_usuario = input("Escolha uma opção: pedra, papel ou tesoura? ").lower()
  jogada_computador = random.choice(opcoes)
  print(f'O computador escolheu {jogada_computador}')
  if jogada_usuario == jogada_computador:
      print('Empatei')
  elif jogada_usuario == 'pedra' and jogada_computador == 'tesoura':
    print('Você ganhou')
    ponto_meu = ponto_meu + 1
  elif jogada_usuario == 'papel' and jogada_computador == 'pedra':
    print('Você ganhou')
    ponto_meu = ponto_meu + 1
  elif jogada_usuario == 'tesoura' and jogada_computador == 'papel':
    print('Você ganhou')
    ponto_meu = ponto_meu + 1
  else:
    print('Você perdeu')
    ponto_pc = ponto_pc + 1
  print(f'Pontos: Você, {ponto_meu}, X {ponto_pc}') 
  if ponto_meu == 5:
    print('VOCÊ GANHOUUU!!!')
    break
  elif ponto_pc == 5:
    print('Você perdeu')
    break