#Check if a Number is Even or Odd

#integer input from user
num = int(input('Enter the number: '))

#if-else to check even/odd and print result
if (num % 2 == 0):
    print(f'{num} is an even number')
else:
    print(f'{num} is an odd number')
print('Thank you')