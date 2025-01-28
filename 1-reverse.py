# Write a code to reverse a number
def reverse_number(n):
    result = 0 
    rev = 0
    orignal = n
    while n>0:
        remainder = n%10
        result = result*10 + remainder
        n = n//10
    return result

reverse_number(89)