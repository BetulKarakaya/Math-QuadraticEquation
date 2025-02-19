# Quadratic Equation Solver

This project is a **Quadratic Equation Solver** application built with **PyQt5** and **Matplotlib** for graphical representation of quadratic equations. It calculates the roots of a quadratic equation and displays the graph of the quadratic function.

**Note**: This project is currently under development.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [Error Handling](#error-handling)


## Overview

This Python application calculates the roots of a quadratic equation in the form of: ax² + bx + c = 0


It allows users to input the coefficients `a`, `b`, and `c` and displays:

1. The discriminant (Δ)
2. The roots (if real roots exist)
3. A plot of the quadratic function

The app is built using **PyQt5** for the GUI and **Matplotlib** for plotting the quadratic curve.

## Features

- **Input Form**: Users can enter the coefficients `a`, `b`, and `c` of the quadratic equation.
- **Root Calculation**: Calculates the real roots of the quadratic equation.
- **Graphical Representation**: Plots the quadratic function and marks the roots on the graph.
- **Discriminant Display**: Shows the discriminant value (Δ) and roots if they exist.
- **Error Handling**: Provides user-friendly error messages for invalid inputs.

## Usage

1. **Launch the application**: The application window will appear with input fields for the coefficients of the quadratic equation.
2. **Enter the coefficients**: Fill in the `a`, `b`, and `c` values for the equation.
3. **Click 'Calculate'**: The app will calculate the roots (if real roots exist) and display them along with the discriminant and a plot of the quadratic curve.
4. **Plot Display**: The plot will show the parabola, the x-axis, and y-axis with the roots marked if they exist.

### Example Usage:

For the quadratic equation:
2x² + 3x - 5 = 0


1. Enter `2` for `a`, `3` for `b`, and `-5` for `c`.
2. Click "Calculate."
3. The app will display:
   - The discriminant value.
   - The two real roots.
   - A plot of the equation.

## Error Handling
The application includes custom error handling to manage invalid inputs:

Invalid Input Error: If any of the coefficients are not numeric.
Invalid 'a' Value Error: If the coefficient a is zero (as this would not form a quadratic equation).
These errors are caught and handled, and appropriate error messages are displayed.

