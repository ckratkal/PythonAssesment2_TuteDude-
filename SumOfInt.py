#Sum of Integers from 1 to 50 Using a for loop

#Take input from user
start = int(input('Enter the first number for list: '))
end = int(input('Enter the last number for the list: '))
#check if end number is greater that start number
if (end > start):
    total = 0 
    #loop through numbers from start to end
    for num in range(start, end):
        total += num
    print(f'The sum of number from {start} to {end} is {total}')
else:
    #error if input is invalid
    print(f'You entered {end} as the last number, which is smaller than {start}. This is not valid! Please choose a higher number.')