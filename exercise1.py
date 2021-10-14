def sumOfNumbers(start,end):
  sum = 0
  for i in range (start, end+1):
    if i%7 == 0:      
      sum+=i
    elif i % 9 == 0:
      sum+=i
  return sum
print(sumOfNumbers(0,10000))
    