# Lógicas programaticas de circuito

from doors import _and, _nand, _or, _nor, _xor
from neural_lib import Perceptron


# meia soma de bits 
def simple_sum_bits(a,b):
   s1= _nand([a,b])
   carry_bite= _and([a,b])

   return (s1,carry_bite)

