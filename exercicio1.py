#1. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;- A mensagem "Reprovado", se a média for menor do que sete;- A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = int(input("digite a primeira nota"))
n2 = int(input("digite a segunda nota"))
r = (n1 + n2)/2

if r == 10:
  print("aprovado com distincao: ",r)
elif r >= 7:
  print("alundo aprovado: ",r)
else: 
  print("aluno reprovado:", r)
