# FDS_String_operations

'''Write a Python program to compute following operations on String: 
  a) To display word with the longest length 
  b) To determines the frequency of occurrence of particular character in the string 
  c) To check whether given string is palindrome or not 
  d) To display index of first appearance of the substring 
  e) To count the occurrences of each word in a given string'''


# Length of string

str1 = input("Enter the string 1: ")
n =0
for i in str1:
    n=n+1
print("Length of the input string 1: ",n) 

# Frequency of occurrence of char in string

str2= input("Enter the string 2: ")
ch=input("Enter the chracter: ")
count=0
for i in range(len(str2)):
    if ch==str2[i]:
        count+=1
print("The above Character repeats",count,"Time")

# Determine the frequency of occurrence of particular character in the string 

str3= input("Enter the string 3: ")
list=str3.split()
l=0
for i in range(len(list)):
    if l<len(list[i]):
        l= len(list[i])
print(l) 

# To check whether given string is palindrome or not

str4=input("Enter the string 4: ")
n =""
for i in str4:
    n=i+n
if(str4==n):
    print("The string is Palindrome: ")
else:
    print("The string is not Palindrome")
    
 #  To display index of first appearance of the substring 
 
 str5= input("Enter the string 5: ")
char=input("Enter the character: ")
flag=0
for i in range(len(str5)):
    if(str5[i]==char):
        flag=1
        break
if(flag==0):
    print("Invalid entered Character")
else:
    print("The first Occurence of",char,"is found at position: ",i+1)    
