# IntegersPython

**IntegersPython** is a simple Python program that calculates the sum of the first `n` positive integers using recursion. It asks the user to enter a number, calculates the sum, and displays the result in the console.

This project demonstrates basic Python programming concepts, including functions, recursion, user input, integer conversion, and output formatting.

## Features

- Accepts a number from the user.
- Uses a recursive function to calculate the sum of integers.
- Displays the calculated result in the console.
- Demonstrates the use of Python functions and conditional statements.

## Requirements

- Python 3
- A Python-compatible IDE or code editor, or a terminal with Python installed

## Installation

1. Clone or download this repository.
2. Open the project folder.
3. Make sure Python 3 is installed.

## How to Run

Open a terminal in the project directory and execute:

```bash
python Integers.py
```

Depending on your system, you may need to use `python3` instead:

```bash
python3 Integers.py
```

Enter a number when prompted.

## Example

```text
Enter a number: 5
The sum of the first 5 integers is 15.
```

The program calculates:

`1 + 2 + 3 + 4 + 5 = 15`

## How It Works

The program defines a recursive function called `find_sum(n)`.

- **Base case:** If `n` is `0`, the function returns `0`.
- **Recursive case:** Otherwise, it adds `n` to the result of `find_sum(n - 1)`.

The recursion continues until the base case is reached, then returns the total.

## Limitations

- The program is designed for non-negative integer inputs.
- Negative inputs are not validated and will not produce the intended result.
- Very large inputs may exceed Python's recursion limit.

## Author

**Ichiro Yamazaki**

## License

No license is currently specified. Please check the repository for licensing information before redistributing or modifying the project.
