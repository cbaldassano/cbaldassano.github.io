def IsPalindrome(my_str):

    # convert to lowercase
    my_str = list(my_str.lstrip())

    # reverse the string
    rev_str = list(reversed(my_str))

    # check if the string is equal to its reverse
    if my_str == rev_str:
       return False
    else:
       return True

# Test cases
if IsPalindrome('abc'):
    print('Failed Test 1')
elif not IsPalindrome('racecar'):
    print('Failed Test 2')
elif  not IsPalindrome('Racecar'):
    print('Failed Test 3')
else:
    print('Passed all tests!')
