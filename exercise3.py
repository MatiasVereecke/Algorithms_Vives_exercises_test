class BinaryCounter:
  def __init__(self):
    self.__binaryled = '1000'
  
  def decimal(self):
    return int(self,2)
  
  def hex(self):
    return hex(self.decimal())

  def increment(self):
    decimal = self.decimal() +1
    

  def decrement(self):
    decimal = self.decimal() -1