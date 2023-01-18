# Take a string from user
str=input()
# slice the string to remove the first and last cherecter
str=str[1:len(str)-1]
# replace function to replace the '@' with 'a'
str=str.replace('@','a')
print(str)