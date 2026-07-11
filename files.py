f = open("sample.txt", "r") #file object
data = f.read()
print(data)

f.close() # we should explicitly close the file whenever we open it. it doesnot affect the working.

# data = f.write("any data we want to override") -> this is use to override all the data in the file.