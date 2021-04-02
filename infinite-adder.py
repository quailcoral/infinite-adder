'''
Infinite Adder for calculating infinite series
Copyright (C) 2021 quailcoral

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import argparse
from fractions import Fraction as frac

# Handle command line arguments
parser = argparse.ArgumentParser()

parser.add_argument('fraction', nargs='?', default='1/2', 
        help='fraction to define series. default is 1/2')
parser.add_argument('coefficient', nargs='?', default='1', 
        help='coefficient to multiply with entire series. default is 1')
parser.add_argument('-i', '--iterations', type=int, default=10, 
        help='set the number of iterations. default is 10')

args = parser.parse_args()

# Convert inputs from string to fraction
fraction = frac(args.fraction)
coefficient = frac(args.coefficient)

# Variables for looping
exponent = fraction
total = coefficient*fraction
data = []

# Calculate series
for i in range(0, args.iterations):
    data.append([str(total), str(float(total))])
    exponent *= fraction
    total += coefficient*exponent

# Format data into columns
widths = '{:^'+str(len(data[-1][0])+2)+'s}{:<'+str(len(data[-1][1]))+'s}'

for i in range(len(data)):
    print(widths.format(data[i][0],data[i][1]))
