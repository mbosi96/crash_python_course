#  EXERCISE 4  

## Introduction and general comments

This file contains some indications on the solution of the exercise 4 of the Crash Course On Python.
The aim of the exercise is creating a new type for handling rational numbers in the more pythonic way as possible.
In the current directory, besides the file you are reading, the reader can find also a Python package where there are three .py files:
* ``__init__.py`` (necessary to have a working Python package);
* ``exercise_4.py`` reporting the class written to handle rational numbers:
* ``exercise_35.py`` which is the Python module with the functions deriving from the previous exercise. In particular, it contains the ``prime_decomposition_of`` function that is used in one of the class methods to simplify the fractional part of the resulting rational number.
In addition to this package, the reader can find the file ``exercise_4_tests.ipynb``. It is a jupyter notebook with some tests on the ``prime_decomposition_of function`` and on the methods of the above mentioned class.

## Comments on Python package

As stated above, in ``exercise_4.py`` there is the definition of a class to handle rational numbers, named ``rational_handler``.

At first, the function ``prime_decomposition_of`` is imported from the module ``exercise_35.py``, in order to be used later.
Then there is the actual class definition. It presents two attributes ``numerator`` and ``denominator``, which are the numerator and the denominator of the resulting rational number and several methods.

The constructor ``__init__`` takes a positional argument for the number to be converted into rational and a keyword argument to set the required precision of the approximation. The precision must be between 0 and 1 (this is the reason of the check inside the constructor) and its default value is $10^{-5}$. In addition, in the constructor the input number is converted to rational through the ``approximate_rational`` method and the resulting numerator and denominator are simplified through the ``simplify_fraction`` method and get stored internally.

Then many dundler methods are defined. Starting from ``__abs__``, which takes into account the fact that the sign of the rational number is stored in the numerator, ``__str__`` and ``__repr__``, giving the requested string representations, up to all the arithmetic and comparison dundler methods, casted in the rational number case. Finally, there are also the definitions of the dundler functions ``__int__`` and ``__float__``, to cast a rational number into an integer or a float, respectively, and of ``__hash__``, which gives an unambiguous integer number for the immutable tuple constituted by numerator and denominator.

At this point the ``simplify_fraction`` method is defined. Its aim is to simplify the common elements in the prime decomposition of the numerator and denominator, in order to get a simplified fraction.
It first presents a check on the value and sign of the numerator: if it is 0, the function will return 0 and, if it is negative, it is set to positive and a boolean flag is set to ``True``; it will be used at the end of the function to give the correct sign back to the simplified rational number. Then the numerator and denominator go through a prime decomposition thanks to the imported ``prime_decomposition_of`` function. May the reader open the module ``exercise_35.py`` for detailed comments on how this function actually works.
Now one dictionary and one list for the numerator, and the same for the denominator, are initialised. The dictionaries are populated with the keys given by the prime factors and the values given by their occurrences in the prime decomposition. This is done in the same way both for numerator and denominator. For instance, if the numerator is 20, it will have a corresponding dictionary such as ``{2: 2, 5: 1}`` and, if the denominator is 30, its dictionary will be ``{2: 1, 3: 1, 5: 1}``. Once the dictionaries are populated, there are other two for loops on the prime decompositions of the numerator and denominator, respectively. Taking the first one as an example, it runs over the prime factors of the numerator and, if one factor appears in the denominator dictionary with a given occurrence, that factor is skipped and the occurrence gets decreased by -1. If the following factor is not present in the denominator dictionary with a positive occurrence, it is appended in the new initialised list for the numerator. In the end this list will contains all those prime factors that do not appear in the denominator dictionary with an occurrence major than 0 and, thus, it will represent a list with the simplified prime factors for the numerator. The same is done for the denominator in the other for loop.
Finally, if these lists are not empty, their elements are multiplied to get the simplified numerator and denominator, respectively, otherwise they will be put equal to 1.
In the last part the correct sign is given back (or is not) to the new numerator.

The last method to be defined is the ``approximate_rational``. Its aim is to a provide a fractional representation of the rational number with the continued fraction approximation algorithm.
It first presents a check on the value and sign of the number to convert into rational: if it is 0, the function will return 0 and, if it is negative, it is set to positive and a boolean flag is set to ``True``; it will be used at the end of the function to give the correct sign back to the numerator of the obtained fraction.
Regarding the continued fraction approximation algorithm, the prescription suggested in the exercise text is adopted. Therefore, in a first place, variables are initialised: a_0 is set equal to the greatest integer less than or equal to the number to convert, reciprocal_fractional_part corresponds to $x_1$ in the prescription and two lists, for the numerators and denominators, are defined. Their zero-th elements are the $n_0$ and $d_0$ of the prescription.
At this point the while loop starts to run, actually from the iteration number 1, and it will stop when the required precision is achieved. May the reader notice that, in the first iteration, numerator_i is set to a_0 and denominator_i to 1, as in the prescription it suggested to put $n_1 = a_0$ and $d_1 = 1$. In the following iterations the suggested recursive scheme is followed step by step.
The last numerator and denominator appended will be those satisfying the precision requirement and, thus, are the numerator (with the correct sign) and the denominator of the fractional representation of the input number.

## Comments on jupyter notebook

As mentioned before in the jupyter notebook there are some tests on the ``prime_decomposition_of`` function and on the methods of the ``rational_handler`` class.
The notebook has the following structure:
* the Python package and the math Python library (just to use pi and the Euler's number) are imported;
* a quick test on the ``prime_decomposition_of`` function from the ``exercise_35.py`` is performed. More detailed tests are present in the very same module in case the reader may be interested;
* tests on ``__str__``, ``__repr__``, ``__abs__``, ``__int__``, ``__float__`` and  ``__hash__`` dundler methods;
* tests on the arithmetic dundler methods;
* tests on the comparison dundler methods;
* test on the fraction simplification;
* tests on the continued fraction approximation algorithm.
