# Desafio: A Aventura do Explorador

quantidade_passos = int(input())

if quantidade_passos == 0:
  print('Nenhum passo dado na floresta.')
elif quantidade_passos > 0:
  for i in range(1, quantidade_passos + 1):
    print (f'Explorador: {i} {"passos" if i > 1 else "passo"}')