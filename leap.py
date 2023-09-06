def leapcheck(year):
  if(year%400==0):
    print("The given year",year, "is Leap year")
  elif (year%100==0) :
    print("The given year", year, "is not a leap year ")
  elif(year%4==0):
    print("The given year",year, "is Leap year")
  else:
    print("The given year", year, "is not a leap year ")
year=int(input("Enter the year"))
leapcheck(year)
