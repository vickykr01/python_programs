# we have to find word and its line number.

data = True
line = 1
word = "python"

with open("sample.txt" , "r") as f:
    while data:
        data = f.readline()
        if(word in data):
            print(f"{word} is found at line {line}")
            break
        line += 1
     