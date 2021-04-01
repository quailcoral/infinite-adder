# Infinite Adder
Python script for calculating infinite series

## Requirements
* Python 3
* `fractions` and `argparse` (both in standard library)

## Usage
Download or clone repository:
```bash
git clone https://github.com/quailcoral/infinite-adder.git
cd infinite-adding
```
Run script. This defaults to 10 iterations of the 1/2 series with coefficient 1
```bash
python3 infinite-adder.py
```
Customize input. This will give 20 iterations of the 1/3 series all multiplied by 1/2
```bash
python3 infinite-adder.py 1/3 1/2 -i 20
```
Help screen for the inputs
```bash
python3 infinite-adder.py --help
```
