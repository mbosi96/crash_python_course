######################################
###########  EXERCISE 3.2  ###########
######################################
# this script wants to return the Fibonacci sequence up to the n-th term
# (with n starting from 0)

################################################################################

def calculate_fibonacci_sequence(n):

    """function that calculates the Fibonacci sequence up to the n-th term (with n starting from 0)

    Parameters
    ----------
    n : int
        index of the n-th term of the sequence

    Returns
    -------
    : list
        a list with the Fibonacci sequence
    """

    if (type(n) != int) or (n < 0):
        raise ValueError(f'Positive integer number expected, got "{n}"') # checking the input
    fib_dict = {0: 0, 1: 1} # starting dictionary

    def calculate_fibonacci_number(n):

        """function that calculates the Fibonacci number of n (with n starting from 0)

        Parameters
        ----------
        n : int
            a number

        Returns
        -------
        : int
           the Fibonacci number of n
        """

        if n in fib_dict:
            return fib_dict[n] # returning the base case
        fib_dict[n] = calculate_fibonacci_number(n - 1) + calculate_fibonacci_number(n-2)  # using recursion
        return fib_dict[n]

    calculate_fibonacci_number(n) # calculating the n-th Fibonacci number
    ret_list = list(fib_dict.values()) # list up to the n-th term

    return ret_list # returning the Fibonacci sequence up to the n-th term


def _test1 (input_list):

    """function that creates a new list containing only the elements with even index in the input list

    Parameters
    ----------
    : list
        a list

    Returns
    -------
    : list
        a list
    """

    even_el_list = input_list[::2]

    return even_el_list


def _test2 (input_list):

    """function that creates a new list containing only the elements with odd index in the input list

    Parameters
    ----------
    : list
        a list

    Returns
    -------
    : list
        a list
    """

    odd_el_list = input_list[1::2]

    return odd_el_list

################################################################################

if __name__ == '__main__' :
    print('')
    nth_fib_term = int(input('Enter the n-th term up to which you want to calculate the Fibonacci sequence (with n starting from 0): '))
    test_fib_seq = calculate_fibonacci_sequence(10) # output sequence up to the 10-th nth_fib_term
    check_fib_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55] # check sequence up to the 10-th nth_fib_term
    fib_seq = calculate_fibonacci_sequence(nth_fib_term) # list with the elements of the sequence
    fib_even_seq = _test1(fib_seq) # sublist containing only the elements with even index
    fib_odd_seq = _test2(fib_seq) # sublist containing only the elements with odd index
    if not (test_fib_seq == check_fib_seq):
            print('')
            raise Exception('ERROR: the final result is incorrect') # checking the result
    if not (fib_seq == sorted(fib_even_seq + fib_odd_seq)):
            print('')
            raise Exception('ERROR: the final result is incorrect') # checking the result
    else:
        print('')
        print('All the tests are ok!')
    print('')
    print(f'The Fibonacci sequence up to the {nth_fib_term}-th term is:')
    print(fib_seq)
    print('The sub-sequence containing only the elements with even index is:')
    print(fib_even_seq)
    print('The sub-sequence containing only the elements with odd index is:')
    print(fib_odd_seq)
