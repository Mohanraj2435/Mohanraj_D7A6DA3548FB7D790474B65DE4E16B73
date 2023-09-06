def factorial(n):
    if(n==1):
        return 1
    else:
        f=n*factorial(n-1)
    return f
n=int(input("Enter the number"))
res=factorial(n)
print("Factorial value of " , n, "is",res)
      
          
