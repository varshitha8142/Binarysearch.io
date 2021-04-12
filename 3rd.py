'''s=input("enter:")
a = ""
count = 1
for i, j in enumerate(s):
    if i < len(s) - 1 and j == s[i + 1]:
        count += 1
    else:
        a += str(count) + j
        count = 1
print(a)'''

s=input("Enter a string:")
n = len(s)
count = 0
while count < n- 1:
    count = 1
    while (count < n - 1 and s[count] == s[count + 1]):
        count += 1
        count += 1
    count += 1
print( str(count) + s[count + 1], end = "")
   
