############################################
###########  EXERCISE 3.5 - 3.6  ###########
############################################
# this script wants to find the prime factorization of a given integer number (3.5)
# and to provide a module with also the necessary functions of the previous exercises (3.6)

################################################################################

def divisbility_check(first_integer, second_integer):

    """function which determines whether the first input number is divisible by the second

    Parameters
    ----------
    first_integer : integer
                    a number
    second_integer : integer
                     a number

    Returns
    -------
    : boolean
      boolean value attesting the divisibiliy result
    """

    try:
        num = int(first_integer)
        den = int(second_integer)
        rest = num%den
    except ValueError:
        print('')
        print('Error: the input must be integer') # error in the case the input number is not an integer
        print('')
    except ZeroDivisionError:
        print('')
        print('Error: it is not possibile to devide by zero') # error in the case one of the input number is zero
        print('')
    else:
        if rest == 0:
            return True
        else:
            return False


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


def prime_decomposition_of(input_number):

    """function that calculates the prime decomposition of the input integer number

    Parameters
    ----------
    input_number : int
                   number to be decomposed in prime factors

    Returns
    -------
    : list
      a list of prime factors used for the decomposition
    """

    if (type(input_number) != int) or (input_number < 0):
        raise ValueError(f'Positive integer number expected, got "{input_number}"') # checking the input

    prime_decomposition_list = [] # resulting list
    prime_factors_list = prime_factors_finder(input_number) # list of prime numbers up to input_number
    for index_p in range(len(prime_factors_list)): # building the prime decomposition starting from the smaller prime numbers
        # the while loop here below divides the input number for the given prime
        # factor as many times the divisibility condition is satisfied
        # and appends that prime factor to the final list
        while divisbility_check(input_number, prime_factors_list[index_p]):
            prime_decomposition_list.append(prime_factors_list[index_p])
            input_number //= prime_factors_list[index_p]
        if input_number == 1: # the main loop ends when the input_number as been divided up to 1
            break

    return prime_decomposition_list


def _test_prime_decomposition_1():

    """function which verifies if the prime decomposition works correctly

    Returns
    -------
    : boolean
      boolean value attesting the test result
    """

    flag = False # flag monitoring the test process
    for num in range(1,101): # checking the correctness of the procedure for all numbers from 1 to 100
        total_prime_list = prime_factors_finder(num) # list of all the prime numbers up to num
        expected_prime_dec_list = prime_decomposition_of(num) # list of the expected prime factors of num
        if (num == 1) and (expected_prime_dec_list != []): # first error case
            print('Error: the first test failed')
            print(f'{num} is not expected to have a prime decomposition')
            flag = True
            break
        if set(expected_prime_dec_list) > set(total_prime_list): # second error case
            print(f'Error: the second test for {num} failed')
            print(f'The prime numbers obtained from the decomposition are not contained in the list with all the prime factors up to {num}')
            flag = True
            break
        expected_product = 1.0
        for index_p in range(len(expected_prime_dec_list)):
            expected_product *= expected_prime_dec_list[index_p] # product of the expected prime factors of num decomposition
        if num != int(expected_product): # third error case
            print(f'Error: the third test for {num} failed')
            print(f'The product of the expected prime factors of {num} is not equal to {num}')
            flag = True
            break

    return flag


def _test_prime_decomposition_2():

    """function which verifies if the prime decomposition works correctly through
       a comparison with the last script reported on
       https://www.geeksforgeeks.org/python-program-for-efficient-program-to-print-all-prime-factors-of-a-given-number/
       embedded in tha function primeFactors

    Returns
    -------
    : boolean
      boolean value attesting the test result
    """

    def primeFactors(n):

        """function that calculates the prime decomposition of the input integer n
           derived from the last script reported on
           https://www.geeksforgeeks.org/python-program-for-efficient-program-to-print-all-prime-factors-of-a-given-number/

        Parameters
        ----------
        n : int
            an integer

        Returns
        -------
        : list
          a list of prime factors used for the decomposition
        """

        # Using anonymous function
        prime_factors = lambda n: [i for i in range(2, n+1) if n%i == 0 and all(i % j != 0 for j in range(2, int(i**0.5)+1))]
        factors = []
        while n > 1:
            for factor in prime_factors(n):
                factors.append(factor)
                n //= factor

        return factors

    flag = False # flag monitoring the test process
    for num in range(1,101): # checking the correctness of the procedure for all numbers from 1 to 100
        expected_prime_dec_list = sorted(prime_decomposition_of(num)) # sorting the resulting lists because they
        ref_prime_dec_list = sorted(primeFactors(num))                # can have different orders cominf from different procedures
        if (num == 1) and (expected_prime_dec_list != []): # first error case
            print('Error: the first test failed')
            print(f'{num} is not expected to have a prime decomposition')
            flag = True
            break
        if ref_prime_dec_list != expected_prime_dec_list: # second error case
            print(f'Error: the second test for {num} failed')
            print(f'The product of the expected prime factors of {num} does not give the correct result')
            flag = True

    return flag


################################################################################

if __name__ == "__main__":
    print('')
    number_to_dec = int(input('You may want to find the decomposition in prime factors of: '))
    dec_list = prime_decomposition_of(number_to_dec)
    print('')
    print('The factorization in prime integer numbers is:')
    if len(dec_list) == 0:
        print(f'{number_to_dec} is not expected to have a prime decomposition!')
        print('')
    print(*dec_list, sep='*')
    print('')

    test_1_result = _test_prime_decomposition_1() # test with the first test function
    if test_1_result == False: # all the tests are passed
        print('All test cases have been passed with the first test function, the decomposition precedure worked correctly!')
    else:
        print('Something in the decomposition procedure has to be fixed! Please, read the lines above for further details')
    test_2_result = _test_prime_decomposition_2() # test with the second test function
    if test_2_result == False: # all the tests are passed
        print('All test cases have been passed with the second test function, the decomposition precedure worked correctly!')
    else:
        print('Something in the decomposition procedure has to be fixed! Please, read the lines above for further details')
