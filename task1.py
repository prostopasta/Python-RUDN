from math import comb

def Fact(n):
  if (n == 0):
    return 1
  else:
    return n * Fact(n - 1)

def Bernoulli(n, m, p):
  return comb(n,m) * p ** n * (1-p) ** (n-m)

p_ = 0.95 # p - вероятность что ручка исправная
n = m = 5 # m - требуемое кол-во исправных ручек
Pmax = 0.99 # Pmax - заданная вероятность вытащить m исправных ручек

Psum = 0  # Psum - текушая вероятность вытащить m исправных ручек в n испытаниях
while Psum < Pmax:
  for i in range(m, n+1):
    Psum += Bernoulli(i, m, p_)
  n += 1

print("Ответ 1: Требуется вытащить n =", n, "ручек." )