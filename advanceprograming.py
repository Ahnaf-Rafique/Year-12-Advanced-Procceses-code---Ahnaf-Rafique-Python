#string formatting
name = "Thomas"
company = "Microsoft"
profile = "programmer"

a=f"this is {name}"
print(a)
a="this is {}".format(name)
print(a)
a="This is {} and his profile is {}".format(name_profile)

print("This is" , name, "working as" ,profile, "at")


#filter function
def greaterthan5(num):
    if num>5:
        return true
    else:
        return False

    i = 1,2,3,4,5,6,7,98,67,5,432,2
print(list(filter(greaterthan5, [ )))

#list comprehension
a= [3,6,7,8,2,4,23,45,76]
b=[i for i in a if i%2 ==0]
print(b)

#numerate
list1 = [3,53,2, False, 6.2, "Harry"]
for index, item in enumerate(list1):
    print(item, index)

#random password generator

import random
import string
digits = string.digits
letter_digit_list = list(string.digits + string.ascii_letters)
#shuffle random source of letters and digits

random.shuffle(letter_digit_list)

#first generate 4 random digits

sample_str = ''.join((random.choice(digits) for i in range(6)))

#Now create random string of length 6 which is a combination of letters and digits
#Next, concatenate ir with sample_str


sample_str += ''.join((random.choice(letter_digit_list) for i in range(6)))
alist = list(sample_str)
random.shuffle(alist)

final_str = ''.join(alist)
print("random String:", final_str)