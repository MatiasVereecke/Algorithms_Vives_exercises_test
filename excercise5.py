#right riemann sum
#function x^3
def riemannSum(a,b,n):
  funct = 0
  deelint = (b-a)/n
  for i in range(1,n):
    funct += ((a+(i*deelint))**3)
    funct += b**3

  return deelint * funct

print(riemannSum(2,3,4))