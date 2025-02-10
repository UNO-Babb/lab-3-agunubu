#ApproxPi.py
#Name: Aurora Gunubu
#Date: 2/9/25
#Assignment: Lab C - ApproxPI
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  n = int(input ("Choose a number 1-10:\n"))
  #OMG DO NOT PICK 10... WHY IS IT STILL GOING?!? (TIL: Never print approxPi...)
  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
  approxPi = 4/1
  sign = -1
  denom = 3
  
  while round(approxPi, n) != round(realPi, n):
    approxPi = approxPi + (sign * 4 / denom)
    #print(approxPi)
    sign = sign * -1
    denom = denom + 2
  
  end = time.time()

  elapsedTime = end - start
  print(elapsedTime)

if __name__ == '__main__':
  main()
