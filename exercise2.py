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
print(lucasRow(4000000))