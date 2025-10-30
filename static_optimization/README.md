# Static Optimization Problem

This project solves a simple static optimization problem using `scipy.optimize.minimize`.

## Problem
Maximize:
f(x, y) = 5 \sqrt{x} y^2
subject to:
x + y = c_1, 
0 <= x <= 4;
y >= 0

The code loops over a range of c_1 values (10–20), finds the optimal (x, y), 
and plots the results.

## Requirements
Install dependencies:
```bash
pip install -r requirements.txt