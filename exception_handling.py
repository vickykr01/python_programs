try:
    x = int(input("Enter x: "))
    ans = 10/x

except ZeroDivisionError:
    print("division with 0 is not allowed")
except ValueError:
    print("invalid input")

else:
    print(f"ans = {ans}")