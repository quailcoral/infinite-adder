# Infinite Adder
Python script for calculating infinite series

## Requirements
* Python 3
* `fractions` and `argparse` packages (both in standard Python library)

## Usage
First, download or clone the repository
```bash
git clone https://github.com/quailcoral/infinite-adder.git
cd infinite-adder
```
To use the script, run
```bash
python3 infinite-adder.py
```
This defaults to 10 iterations of the 1/2 series with coefficient 1.

To customize the series, add inputs at the end. This example will run 20 iterations of the 2/3 series multiplied by 1/2, summing `1/2*((2/3)^1+(2/3)^2+(2/3)^3...) = 1`
```bash
python3 infinite-adder.py 2/3 1/2 -i 20
```
To access the help screen, run
```bash
python3 infinite-adder.py --help
```

## Resources
* [Fraction module](https://www.tutorialspoint.com/fraction-module-in-python)
* [Argparse module](https://zetcode.com/python/argparse/)
* [Printing columns](https://scientificallysound.org/2016/10/17/python-print3/)
