from math import comb

def Fact(n):
  if (n == 0):
    return 1
  else:
    return n * Fact(n - 1)

def my_Bernoulli(n, m, p):
  return (Fact(n) / (Fact(n-m) * Fact(m))) * (p ** m) * ((1-p) ** (n - m))

def Bernoulli(n, m, p):
  result = comb(n,m) * p ** m * (1-p) ** (n-m)
  # print (" - вероятность по формуле Бернулли=", result)
  return result

p_ = 0.95 # p - вероятность что ручка исправная
n = m = 5 # m - требуемое кол-во исправных ручек
Pmax = 0.99 # Pmax - заданная вероятность вытащить m исправных ручек

while True :
  print("Испытание при n =", n)
  Psum = 0.0  # Psum - текушая вероятность вытащить m исправных ручек в n испытаниях
  for i in range(m, n+1):
    Psum += Bernoulli(n, i, p_)
    print(" > суммарная вероятность при m =", i, "равна =", Psum)
  if Psum >= Pmax:
    break
  n += 1

print("Ответ 1: Требуется вытащить n =", n, "ручек с вероятностью", Psum)