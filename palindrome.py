# what is polindrome number
# A Palindrome Number is a number that remains the same when we read it from left to right or right to left.
# In simple words, the reverse of the number is equal to the original number.

    
num = 121
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")
