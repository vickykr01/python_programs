# convert all the negetive value to zero in list using list comprehension

nums = [-1 , 3 , -4 , 7 , -8 , 6 , 3 , -11]

ans = [0 if val<0 else val for val in nums]
print(ans)

sq = [i*i for i in range(6)]
print(sq)

odd_sq = [i*i for i in range(6) if i%2 !=0]
print(odd_sq)