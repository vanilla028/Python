s = input()
s_list = [i for i in s]
result= ""
for i in s_list:
    if i.islower():
        result += i.upper()
    else:
        result += i.lower()

print(result)
