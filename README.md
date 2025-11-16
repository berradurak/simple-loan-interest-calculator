# Simple Loan / Interest Calculator

A small Python command-line tool that:

- Reads a loan amount (principal), annual interest rate and term in years
- Calculates **simple interest** and the **total amount to repay**
- Calculates an **estimated monthly payment** using a standard annuity formula (with monthly compounding)

> ⚠️ This project is for learning/demo purposes only and is **not** financial advice.

---

## Features

- Input validation for numeric values
- Simple interest calculation
- Annuity-based monthly payment estimate
- No external dependencies (only Python standard library)

---

## How it works

1. The script asks for:
   - `Loan amount (principal)`
   - `Annual interest rate (% per year)`
   - `Loan term (years)`

2. It prints:
   - Principal
   - Annual interest rate
   - Term in years
   - Simple interest
   - Total amount to repay (principal + interest)
   - Estimated monthly payment (annuity formula, monthly compounding)

---

## Requirements

- Python 3.x

You can check your Python version with:

```bash
python3 --version