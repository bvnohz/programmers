str = input()
li = ''
# str = aBcDeFg
# print(ord('A'), ord('a'))
# print(chr(65), chr(95))
for i in str:
    if ord(i) < ord('a') : 
        li += i.lower() # li = li + i.lower()
        # print(li)
    else:
        li += i.upper()
        # print(li)

print(li)       
# print(str.swapcase())    