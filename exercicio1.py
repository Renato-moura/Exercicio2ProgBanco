#1. Fa�a um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a m�dia alcan�ada por aluno e apresentar:- A mensagem "Aprovado", se a m�dia alcan�ada for maior ou igual a sete;- A mensagem "Reprovado", se a m�dia for menor do que sete;- A mensagem "Aprovado com Distin��o", se a m�dia for igual a dez.

n1 = int(input("digite a primeira nota"))
n2 = int(input("digite a segunda nota"))
r = (n1 + n2)/2

if r == 10:
  print("aprovado com distincao: ",r)
elif r >= 7:
  print("alundo aprovado: ",r)
else: 
  print("aluno reprovado:", r)
