# Infinite Adder
# For calculating infinite series
import argparse
from fractions import Fraction as frac

# Handle command line arguments
parser = argparse.ArgumentParser()

parser.add_argument('fraction', nargs='?', default='1/2', 
        help='Fraction to add powers of. Default is 1/2')
parser.add_argument('coefficient', nargs='?', default='1', 
        help='Coefficient to multiply entire series by. Default is 1')
parser.add_argument('-i', '--iterations', type=int, default=10, 
        help='Set number of iterations. Default is 10')

args = parser.parse_args()

# Convert inputs from string to fraction
fraction = frac(args.fraction)
coefficient = frac(args.coefficient)

# Variables for looping
exponent = fraction
total = coefficient*fraction

for i in range(0, args.iterations):
    print(str(total)+'='+str(float(total)))
    exponent *= fraction
    total += coefficient*exponent
