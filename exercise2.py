def lucasRow(input):
  firstnumber = 2
  secondnumber = 1
  sum = 1
  while(firstnumber + secondnumber) < input:
    thirtnumber = firstnumber + secondnumber 
    firstnumber = secondnumber
    secondnumber = thirtnumber
    if thirtnumber % 2 != 0:
      sum+= thirtnumber
  return sum

def sumOfEvenLucasNumbers(n):
  current = 1
  sum = 2
  while current < n:
    nextNumber = luc(current)
    if nextNumber % 2 ==0:
      sum += nextNumber
    
    current +=1
  return sum

def luc(n):
  if n == 0:
    return 2
  elif n ==1:
    return 1
  else:
    return luc(n-1) + luc(n-2)

print(lucasRow(4000000))