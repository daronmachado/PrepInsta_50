def palindrome(str1):
    n = len(str1)
    flag = -1
    for i in range(0,n//2):
        if str1[i] == str1[n-1-i]:
            flag = flag + 1
    if flag==i:
        print("Palindrome")
palindrome("malayalam")