#TempConvert.py
#Name: Aurora Gunubu  
#Date: 2/9/25
#Assignment: Lab 3 - Temperature Conversion 


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = int(input ("Type in a temperature (in Fahrenheit):\n"))
  tempC = (tempF-32)/(9/5)
  round(tempC, 2)
  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
