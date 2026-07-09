"""Calculate gross pay for an employee based on hours worked.

Inputs:
- REGULAR_RATE (float): Regular rate of pay ($/hr).
- OT_MULTIPLIER (float): Overtime pay multiplier (1.5x regular rate).
- OT_THRESHOLD (float): Overtime threshold (hrs/wk).
- hours_worked (float): Number of hours entered by the user via input.

Processing:
- Applies regular pay up to 40 hours and overtime pay (1.5 times rate)
  for any additional hours worked.

Outputs:
- gross_pay (float): Total pay displayed to the console as currency.

Typical usage example:
    Enter hours worked: 48
    Gross pay is: $1,040.00
"""

# === Constants ===
# TODO: Initialize constants for regular rate, overtime multiplier, and overtime threshold.


# === Main Function ===
def main() -> None:
    """Run the program."""

    # Get hours worked from user.
    # TODO: Prompt user for hours worked and convert to float.

    # Decide how to calculate regular and overtime hours.
    # TODO: Use conditional logic to determine regular and overtime hours based on OT_THRESHOLD.

    # Calculate regular, overtime, and gross pay.
    # TODO: Calculate regular pay, overtime pay, and gross pay using the constants and hours worked.

    # Display gross pay message
    # TODO: Format gross pay as currency and display to console.


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# TODO: Add references to any resources used to complete this assignment.
