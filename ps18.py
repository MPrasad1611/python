str1="Welcome to python"
res=""

for i in str1:
    if i not in 'aeiou':
        res=i+res
print(res)