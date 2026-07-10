# takes a salary as input and use conditional statements to calculate and display the applicable tax rate.

salary = float(input("Enter your salary: "))
if (salary<30_000):
    new_salary = salary - salary*(5/100)
elif(salary<=70_000):
      new_salary = salary - salary*(15/100)
elif(salary>70_000):
       new_salary = salary - salary*(25/100)      
print(f"your salary after taxex is {new_salary}")

# write a function that takes two integers a and b and print all the even numbers between them.

def get_even_number():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    print(f"even numbers between {num1} and {num2} are :")    
    for i in range(num1 , num2):
        if(i % 2 == 0):
            print(i)
        
get_even_number()