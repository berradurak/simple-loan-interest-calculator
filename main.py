def read_float(prompt: str) -> float:
    """Read a float from user input."""
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number (e.g. 1000 or 1000.50).")


def calculate_simple_interest(principal: float, annual_rate: float, years: float) -> tuple[float, float]:
    """Return (interest, total) using simple interest."""
    r = annual_rate / 100.0
    interest = principal * r * years
    total = principal + interest
    return interest, total


def calculate_annuity_monthly_payment(principal: float, annual_rate: float, years: float) -> float:
    """Return monthly payment using a standard annuity formula (with monthly compounding)."""
    months = int(years * 12)
    if months <= 0:
        return principal

    r_monthly = (annual_rate / 100.0) / 12.0

    # If rate is zero, avoid division by zero
    if r_monthly == 0:
        return principal / months

    factor = (1 + r_monthly) ** months
    payment = principal * r_monthly * factor / (factor - 1)
    return payment


def main():
    print("=== Simple Loan / Interest Calculator ===\n")

    principal = read_float("Loan amount (principal): ")
    annual_rate = read_float("Annual interest rate (% per year): ")
    years = read_float("Loan term (years): ")

    simple_interest, simple_total = calculate_simple_interest(principal, annual_rate, years)
    monthly_payment = calculate_annuity_monthly_payment(principal, annual_rate, years)

    print("\n--- Result (Simple Interest) ---")
    print(f"Principal        : {principal:,.2f}")
    print(f"Annual rate      : {annual_rate:.2f}%")
    print(f"Term             : {years:.2f} years")
    print(f"Simple interest  : {simple_interest:,.2f}")
    print(f"Total to repay   : {simple_total:,.2f}")

    print("\n--- Monthly Payment Estimate (Annuity) ---")
    print(f"Estimated monthly payment: {monthly_payment:,.2f}")
    print("\nNote: Monthly payment uses a standard annuity formula with monthly compounding.\n")


if __name__ == "__main__":
    main()