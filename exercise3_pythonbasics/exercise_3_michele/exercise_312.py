######################################
##########  EXERCISE 3.1.2  ##########
######################################
# this script wants to check, given two numbers as input, if the first is divisible
# by the second and vice-versa

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
        rest = num % den
    except ValueError:
        print('')
        print('Error: the input must be integer') # error in the case the input number is not an integer
        print('')
    except ZeroDivisionError:
        print('')
        print(f'Error: it is not possibile {first_integer} to divide by 0') # error in the case one of the input number is zero
        print('')
    else:
        if rest == 0:
            return True
        else:
            return False

################################################################################

if __name__ == '__main__' :
   print('')
   print('This script wants to check, given two numbers as input, if the first is divisible by the second and vice-versa')
   first_input_integer = input('Enter the first number: ')
   second_input_integer = input('Enter the second number: ')
   bool_1 = divisbility_check(first_input_integer, second_input_integer)
   bool_2 = divisbility_check(second_input_integer, first_input_integer)
   if bool_1 == True:
       print('')
       print(first_input_integer, 'is divisible by', second_input_integer)
       print('')
   if bool_1 == False:
       print('')
       print(first_input_integer, 'is not divisible by', second_input_integer)
       print('')
   if bool_2 == True:
       print(second_input_integer, 'is divisible by', first_input_integer)
       print('')
   if bool_2 == False:
       print(second_input_integer, 'is not divisible by', first_input_integer)
       print('')
