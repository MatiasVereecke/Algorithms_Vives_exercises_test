class LineSegment:
  def calculateDistance(x1,y1,x2,y2):
    distance = ((((x2-x1)**2)+((y2-y1)**2))**0.5)
    return distance

line1 = LineSegment.calculateDistance(1,1,4,4)
print(line1)
