'''print("------------program1--------------")
def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
        return True
str="kanak"
print(isPalindrome(str))
1.First we have created a function isPalindrome() using def keyword
2.we r passing a str parameter in th isPalindrome(str)
3."kanak" is given string, it will give the true condition
4.If i give "manasa" it give false condition.
'''


'''print("-----------------------program2---------------------")
def sum_of_digit(num1, num2):
    return int(num1) + int(num2)
num1 = list(str(int(input("Enter first number : "))))
num2 = list(str(int(input("Enter second number : "))))
res = list(map(sum_of_digit, num1, num2))
temp = 0
for i in res:
    temp = temp + i
print("Final output : ", temp)
1.I have created function using keyword of def,the function name is sum_of_digit,and passed two parameters num1,num2.
2.returning a value int(num1)+int(num2)
3.temp=0
4.result should be increased by 1.


'''


'''print("-------------------program4--------------")
from collections import Counter
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
counts = dict(Counter(some_list))
duplicates = {key:value for key, value in counts.items() if value > 1}
print(duplicates)

1.some list has given already,in dat we to remove duplicates using dictionary.
2. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
3.{'a': 2, 'b': 2, 'n': 2, 'm': 2} output.
'''

'''print("-------------program5---------------")
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
lis1 = []
lis2 = []
for t in t1:
    if isinstance(t, int):
        for i in t2:
            if i not in lis2 and isinstance(i, int):
                lis2.append(i)
                lis1.append((t + i))
                break
    else:
        for i in t2:
            if i not in lis2 and isinstance(i, str):
                lis2.append(i)
                lis1.append((t + i))
                break
print(lis1)
'''
'''
1.Here we have to take a given two lists 
   t1 = (1, 2, 3, "a", "c") 
   t2 = ("b", "d", 9, 8, 7)
2.And taken two empty lists for appending
3.lis2.append(i) it uppend the values 
4.lis1.append((t+i)) here it list1 and list 2 values
5. for characters also same
6.break is using for break the loop
7.Finally Output is : (10,10,10,"ab","cd")'''





'''print("------------program6----------------------")
def remove_zero_from_ip(ip_add):
    new_ip_add=".".join([str(int(i))for i in ip_add.split(".")])
    return new_ip_add;
print(remove_zero_from_ip("216.08.094.196"))
'''


'''1. given inp = "216.08.094.196" 
2.here we have to remove the 0's usin remove_zero_from_ip function
3.print(remove_zero_from_ip("216.08.094.196"))
4.final output is 216.8.94.196
'''


'''print("--------------program3------------------")
st =  "ab@#cd!ef"
st1 = st[::-1]
st1 = list(st1)
rev = ''
lis = []
for idx, val in enumerate(st1):
    if val.isalpha():
        lis.append(val)
    else:
        lis.insert(idx, st[idx])
rev_str = rev.join(lis)
print(rev_str)
'''
'''
1.our input is  "ab@#cd!ef"
2.I have taken two lists st1 and st2.
3 using for loop enumerate st1
4.using if condition appending and inserting the elements
5.rev_str is reversing only the alphabets not disurbing the special characters
'''

'''print("--------------Program 7-------------------")
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
print(list(map(lambda  x:int(x),str(l).replace("[",'').replace("]","").split(","))))
'''
'''
1.input list is  l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
2.firs here mapping the indexes using lamda function with the help of replace and split methods
3.out is output= [1,2,3,4,5,6,7,8,9,10]
'''







