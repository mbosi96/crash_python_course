######################################
##########  EXERCISE 3.1.1  ##########
######################################
# this script wants to check if the integer given as input is divisible by 2, 3, 5, or 7

################################################################################

print('')
integer_to_be_checked = input('Enter a number to determine whether it is divisible by 2, 3, 5, or 7: ') # to give the input number
denominators_list = [2,3,5,7] # list of divisors to be checked
divisor_list_output = [] # list of the actual divisors of the input integer

################################################################################

try:
    val = int(integer_to_be_checked)

except ValueError:
    print('')
    print('Error: the input must be an integer') # error in the case the input number is not an integer
    print('')

else:
    for index_div in range(len(denominators_list)): # checking the divisibility of the input integer number
        rest = val%denominators_list[index_div]
        if rest == 0:
            divisor_list_output.append(denominators_list[index_div]) # inserting the divisor in the list of divisors of the input integer
        else:
            continue
    if divisor_list_output != []: # printing the result of the check
        print('')
        print (val, 'is divisible by:')
        print(*divisor_list_output, sep = ', ')
        print('')
    else:
        print('')
        print(val, 'is not divisible by 2, 3, 5, or 7')
        print('')
