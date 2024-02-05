####################################
###########  EXERCISE 4  ###########
####################################
# this script wants to define a class to handle rational numbers

################################################################################

from package_exercise_4 import exercise_35_36 # importing the submodule for the prime decomposition

################################################################################

class rational_handler():

    """class to handle rational numbers

    Attributes
    ----------
    numerator : integer
                numerator of the fraction related to the rational number
    denominator : integer
                  denominator of the fraction related to the rational number
    """

    def __init__ (self, num, precision=1e-5):

        """the constructor for the rational_handler class

        Parameters
        ----------
        num : float
              the number to be converted into a rational number
        precision : float
                    required precision for the conversion (default is 1e-5)
        """

        if not (0.0 <= precision <= 1.0):
            raise ValueError('Precision must be 0 <= precision <= 1')
        numerator, denominator = self.approximate_rational(num)
        self.numerator, self.denominator = self.simplify_fraction(numerator, denominator)

    def __abs__(self):

        """dundler method to get the absolute value of the rational number

        Returns
        -------
        : rational_handler
          the absolute value of the rational number
        """

        return rational_handler(abs(self.numerator)/self.denominator)

    def __str__(self):

        """dundler method to get an user-frienldy (readable) string representation of the rational number

        Returns
        -------
        : string
          user-friendly (readable) string representation of the rational number
        """

        return f'{self.numerator}/{self.denominator}'

    def __repr__(self):

        """dundler method to get a developer-frienldy (unambiguous) string representation of the rational number

        Returns
        -------
        : string
          developer-friendly (unambiguous) string representation of the rational number
        """

        return f'rational({self.numerator/self.denominator}, precision=1e-5)'

    def __add__(self, other):

        """dundler method to sum two rational numbers

        Returns
        -------
        : rational_handler
          the sum of the two rational numbers
        """

        if isinstance(other, rational_handler):
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return rational_handler(new_numerator/new_denominator)
        else:
            raise TypeError('Unsupported operand type. Addition operator only supported between rational_handler instances')

    def __sub__(self, other):

        """dundler method to subtract two rational numbers

        Returns
        -------
        : rational_handler
          the subtraction of the two rational numbers
        """

        if isinstance(other, rational_handler):
            new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return rational_handler(new_numerator/new_denominator)
        else:
            raise TypeError('Unsupported operand type. Subtraction operator only supported between rational_handler instances')

    def __mul__(self, other):

        """dundler method to multiplicate two rational numbers

        Returns
        -------
        : rational_handler
          the multiplication of the two rational numbers
        """

        if isinstance(other, rational_handler):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return rational_handler(new_numerator/new_denominator)
        else:
            raise TypeError('Unsupported operand type. Multiplication operator only supported between rational_handler instances')

    def __truediv__(self, other):

        """dundler method to divide two rational numbers

        Returns
        -------
        : rational_handler
          the division of the two rational numbers
        """

        if isinstance(other, rational_handler):
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return rational_handler(new_numerator/new_denominator)
        else:
            raise TypeError('Unsupported operand type. Division (float) operator only supported between rational_handler instances')

    def __floordiv__(self, other):

        """dundler method to (floor) divide two rational numbers

        Returns
        -------
        : int
          the result of the division is rounded to the nearest integer number (the smaller one)
        """

        if isinstance(other, rational_handler):
            return int(self.__truediv__(other))
        else:
            raise TypeError('Unsupported operand type. Division (floor) operator only supported between rational_handler instances')

    def __pow__(self, exp):

        """dundler method to raise the rational number to a given power

        Parameters
        ----------
        exp : integer
              exponent of the power

        Returns
        -------
        : rational_handler
          rational number raised to the power of exp
        """

        if not isinstance(exp, int):
            raise TypeError('Exponent must be an integer')
        if exp < 0:
            new_numerator = self.denominator ** abs(exp)
            new_denominator = self.numerator ** abs(exp)
        else:
            new_numerator = self.numerator ** exp
            new_denominator = self.denominator ** exp
        return rational_handler(new_numerator/new_denominator)

    def __mod__(self, other):

        """dundler method to calculate the modulus of two rational numbers

        Returns
        -------
        : rational_handler
          the modulus of the two rational numbers
        """

        if isinstance(other, rational_handler):
            new_numerator = (self.numerator * other.denominator) % (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return rational_handler(new_numerator/new_denominator)
        else:
            raise TypeError('Unsupported operand type. Modulus operator only supported between rational_handler instances')

    def __eq__(self, other):

        """dundler method to test if two rational numbers are equal

        Returns
        -------
        : boolean
          True if the two rational numbers are equal
        """

        if isinstance(other, rational_handler):
            return (self.numerator, self.denominator) == (other.numerator, other.denominator)
        else:
            raise TypeError('Unsupported operand type. Equal to operator only supported between rational_handler instances')

    def __ne__(self, other):

        """dundler method to test if two rational numbers are not equal

        Returns
        -------
        : boolean
          True if the two rational numbers are not equal
        """

        if isinstance(other, rational_handler):
            return (self.numerator, self.denominator) != (other.numerator, other.denominator)
        else:
            raise TypeError('Unsupported operand type. Not equal to operator only supported between rational_handler instances')

    def __lt__(self, other):

        """dundler method to test if the left operand is smaller than the right

        Returns
        -------
        : boolean
          True if the left operand is smaller than the right
        """

        if isinstance(other, rational_handler):
            return (self.numerator / self.denominator) < (other.numerator / other.denominator)
        else:
            raise TypeError('Unsupported operand type. Less than operator only supported between rational_handler instances')

    def __gt__(self, other):

        """dundler method to test if the left operand is larger than the right

        Returns
        -------
        : boolean
          True if the left operand is larger than the right
        """

        if isinstance(other, rational_handler):
            return (self.numerator / self.denominator) > (other.numerator / other.denominator)
        else:
            raise TypeError('Unsupported operand type. Greater than operator only supported between rational_handler instances')

    def __le__(self, other):

        """dundler method to test if the left operand is smaller than or equal to the right

        Returns
        -------
        : boolean
          True if the left operand is smaller than or equal to the right
        """

        if isinstance(other, rational_handler):
            return (self.numerator / self.denominator) <= (other.numerator / other.denominator)
        else:
            raise TypeError('Unsupported operand type. Less than or equal to operator only supported between rational_handler instances')

    def __ge__(self, other):

        """dundler method to test if the left operand is larger than or equal to the right

        Returns
        -------
        : boolean
          True if the left operand is larger than or equal to the right
        """

        if isinstance(other, rational_handler):
            return (self.numerator / self.denominator) >= (other.numerator / other.denominator)
        else:
            raise TypeError('Unsupported operand type. Greater than or equal to operator only supported between rational_handler instances')

    def __int__(self):

        """dundler method to convert the rational number to an integer

        Returns
        -------
        : integer
          integer representation of the rational number
        """

        return self.numerator // self.denominator

    def __float__(self):

        """dundler method to convert the rational number to a float

        Returns
        -------
        : float
          float representation of the rational number
        """

        return self.numerator / self.denominator

    def __hash__(self):

        """dundler method to associate an unambiguous numerical value to the rational number
           represented here by the immutable tuple (self.numerator, self.denominator)

        Returns
        -------
        : integer
          integer value representing unambiguous the rational number
        """

        return hash((self.numerator, self.denominator))

    def simplify_fraction(self, numerator, denominator):

        """function to simplify the rational number using the prime decomposition
           function present in exercise_35_36.py

        Attributes
        ----------
        numerator : integer
                    numerator of the fraction related to the rational number
        denominator : integer
                      denominator of the fraction related to the rational number

        Return
        -------
        : integers
          simplified values of the numerator and denominator
        """
        # checks on the value and sign of self.numerator
        if numerator == 0:
            return 0
        if numerator < 0:
            neg = True # flag set to True if the number is negative
            numerator = abs(numerator)
        else:
            neg = False

        numerator_prime_list = exercise_35_36.prime_decomposition_of(numerator) # prime decomposition of the numerator
        denominator_prime_list = exercise_35_36.prime_decomposition_of(denominator) # prime decomposition of the denominator

        # simplification process
        occurrences_num = {}
        occurrences_den = {}
        numerator_simp_list = []
        denominator_simp_list = []
        for value in numerator_prime_list:
            occurrences_num[value] = occurrences_num.get(value, 0) + 1
        for value in denominator_prime_list:
            occurrences_den[value] = occurrences_den.get(value, 0) + 1
        for value in numerator_prime_list:
            if occurrences_den.get(value, 0) > 0:
                occurrences_den[value] -= 1
            else:
                numerator_simp_list.append(value)
        for value in denominator_prime_list:
            if occurrences_num.get(value, 0) > 0:
                occurrences_num[value] -= 1
            else:
                denominator_simp_list.append(value)

        # multiplication of the prime factors (if present) to calculate the simplified numerator and denominator
        simp_numerator = 1
        simp_denominator = 1
        if len(numerator_simp_list) != 0:
            for element in numerator_simp_list:
                simp_numerator *= element
        if len(denominator_simp_list) != 0:
            for element in denominator_simp_list:
                simp_denominator *= element

        if neg == True:
            simp_numerator = -simp_numerator # if self.numerator is initially negative the final self.numerator will be negative

        return simp_numerator, simp_denominator

    def approximate_rational(self, num, precision=1e-5):

        """function to get a rational number representation of the input number
           approximating the fractional part with the continued fractions algorithm

        Parameters
        ----------
        num : float
              the number to be converted into a rational number
        precision : float
                    required precision for the conversion (default is 1e-5)

        Returns
        -------
        : integers
          numerator and denominator of the rational number
        """

        # checks on the value and the sign of the input number
        if num == 0:
            return 0
        if num < 0:
            neg = True # flag set to True if the number is negative
            num = abs(num)
        else:
            neg = False

        # variables initialisation
        a_0 = int(num) # it corresponds to a_0 in the instructions list in the exercise text
        reciprocal_fractional_part = num - a_0 # it corresponds to x_1 in the instructions list in the exercise text
        numerator_list = [1] # list for all the numerators. numerator_list[0] corresponds to n_0 in the instructions list in the exercise text
        denominator_list = [0]  # list for all the denominators. denominator_list[0] corresponds to d_0 in the instructions list in the exercise text
        precision_utd = 1.0
        i = 1

        # continued fractions algorithm follwing the instructions list in the exercise test
        while (precision_utd > precision):
            if i == 1:
                numerator_i = a_0
                denominator_i = 1
            else:
                a_i = int(1 / reciprocal_fractional_part) # it corresponds to a_i in the instructions list in the exercise text
                reciprocal_fractional_part = 1 / reciprocal_fractional_part - a_i # it corresponds to x_{i+1} in the instructions list in the exercise text
                numerator_i = a_i * numerator_list[i-1] + numerator_list[i-2]
                denominator_i = a_i * denominator_list[i-1] + denominator_list[i-2]
            numerator_list.append(numerator_i)
            denominator_list.append(denominator_i)
            precision_utd = abs(numerator_i / denominator_i - num)
            i += 1

        if neg == True:
            return -numerator_list[-1], denominator_list[-1] # if num is negative the numerator will be negative
        else:
            return numerator_list[-1], denominator_list[-1]
