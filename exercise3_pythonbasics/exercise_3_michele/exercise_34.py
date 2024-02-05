######################################
###########  EXERCISE 3.4  ###########
######################################
# this script wants to find the list of prime integer numbers smaller than 100,
# starting by knowing that 2 is a prime number

################################################################################

def prime_factors_finder(limit):

    """function that finds prime integer numbers smaller than a given upper limit
       through the sieve of Eratosthenes procedure

    Parameters
    ----------
    limit : int
            number taken as upper limit

    Returns
    -------
    : list
        a list of prime integer numbers smaller than the upper limit
    """

    if (type(limit) != int) or (limit < 0):
        raise ValueError(f'Positive integer number expected, got "{limit}"') # checking the input

    prime_list = [] # resulting list of prime integer numbers
    bool_list = [True] * (limit + 1) # creating a list of boolean values and setting them all to True
    bool_list[0] = bool_list[1] = False # since the first two elements correspond to 0 and 1, which are not prime
    # the for cycle here below marks multiples of prime numbers efficiently. It stops at int(math.sqrt(limit)
    # instead of going up to limit. This is because, suppose there is still a left non prime number and
    # we have sieved up to math.sqrt(limit), that number can be decomposed in two factors and they are larger than
    # math.sqrt(limit). Thus, their product would be larger than limit itself
    for index_b in range(int(limit**0.5)+1):
        if bool_list[index_b] == True:
            # the nested for loop starts from index_b*index_b since any smaller multiple of index_b
            # would have already been marked as multiple of a smaller prime number
            for index_c in range(index_b*index_b, limit+1, index_b):
                bool_list[index_c] = False

    for index_b in range(limit+1):
        if bool_list[index_b] == True:
            prime_list.append(index_b) # appending prime numbers in the final list

    return prime_list

################################################################################

if __name__ == "__main__":
    print('')
    upper_limit = int(input('You may want to find the list of prime integer numbers smaller than: '))
    pin_list = prime_factors_finder(upper_limit)
    test_pin_list = prime_factors_finder(100) # test list with prime integers up to 100
    check_pin_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]  # check list with prime integers up to 100
    if not (test_pin_list == check_pin_list):
            print('')
            raise Exception('ERROR: the final result is incorrect') # checking the result
    else:
        print('')
        print('The test is ok!')
    print('')
    print(f'The prime integer numbers equal or smaller than {upper_limit} are:')
    if len(pin_list) == 0:
        print('No prime number has been found!')
    else:
        print(*pin_list, sep=', ')
