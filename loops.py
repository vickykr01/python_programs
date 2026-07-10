# loops - while loop and for loop


# while loop example

'''
i = 1  #iterator
while(i<=5):  #condition
    print(i)  #satetment
    i+=1      #updater
print("value of i after loop ends =" , i)  '''

# table of any number entered by user
'''
num = int(input("please enter a number you want table of: "))

i = 1
while(i <= 10):
    print(num * i)
    i += 1    '''

# break and continue - break is use to escape the loop and continue is use for skip the iteration.
''' 
i = 0
while(i < 10):
    i += 1
    if(i % 7 == 0):
        break  # when the value becomes multiple of 7 we will be outside of loop
    print(i)
print("outside of loop...")  '''

''''
i = 0
while( i < 10):
    i += 1
    if( i % 2 == 0):
        continue # we will skip all the iteration of multiple of 2
    print(i)
print("outside of loop...")  '''


# for loop are used for sequential traverse like string , tupples , lists and dictionaries..
# syntax = ( for var in sequance_name ) => here ' var ' is variable and ' in ' is membership operator which is use to check the presence.

# for loop examples -
'''
name = "vicky"
for var in name :
    print(var)  ''' 

# To count numbers o i's occur in " artificial intelligence" => 5

word = "artificial intelligence"
count = 0
for ch in word:
    if(ch == "i"):
        count += 1
print("count of i in given word =" , count)