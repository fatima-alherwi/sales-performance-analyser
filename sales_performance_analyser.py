# ==========================================
# SALES PERFORMANCE ANALYSER
# ==========================================
# This program collects daily sales figures and calculates:
# - Total and average sales
# - Days above and below the sales target
# - Percentage of days that met the target
# - Highest and lowest sales, including the day they occurred

import math

# --- 1. INITIALISE VARIABLES ---

# Accumulator: adds each day's sales to a running total
total_sales = 0

# Counter: increases by 1 whenever a day exceeds the target
high_sales_days = 0

# Constant-style variable: the sales target used for comparisons
daily_sales_target = 1000

# Counters for days that met or missed the target
days_met_target = 0
below_target_days = 0

# Starting values for tracking the maximum and minimum
# -1 works for the maximum because valid sales cannot be negative
# Positive infinity ensures the first valid sales figure becomes the initial minimum
highest_sales_value = -1
lowest_sales_value = float("inf")

# These variables store the day numbers for the maximum and minimum
highest_sales_days = []
lowest_sales_days = []

# --- 2. VALIDATE THE NUMBER OF DAYS ---

# Outer while loop: repeats until the user enters a valid day count
while True:
    try:
        days = int(input("How many days of sales would you like to analyse?"))
        if days > 0:
            break  # Exit this while loop when the input is valid
        else:
            print("Please enter at least 1 day")
    except ValueError:
        # Handles inputs that cannot be converted to an integer such as "Hello" or "2.5"
        print("Please enter a valid integer.")

# --- 3. COLLECT AND ANALYSE DAILY SALES ---

# for loop: repeats once for each day, from 1 through days.
for day in range(
    1, days + 1
):  # days + 1 is used because range() excludes its ending number
    # Inner while loop: keeps asking for this day's sales until the user enters a valid, non-negative number
    while True:
        try:
            sales = float(input(f"Enter sales for day {day}: "))

            if math.isfinite(sales) and sales >= 0:
                # Accumulator: add this day's sales to the total
                total_sales += sales

                # Counter: count days strictly above the target
                if sales > daily_sales_target:
                    high_sales_days += 1

                # Counter: count days that met or exceeded the target
                if sales >= daily_sales_target:
                    days_met_target += 1

                # Counter: count days that missed the target
                if sales < daily_sales_target:
                    below_target_days += 1

                # Update the maximum and its corresponding day
                if sales > highest_sales_value:
                    highest_sales_value = sales
                    highest_sales_days = [day]
                elif sales == highest_sales_value:
                    highest_sales_days.append(day)

                # Update the minimum and its corresponding day
                if sales < lowest_sales_value:
                    lowest_sales_value = sales
                    lowest_sales_days = [day]
                elif sales == lowest_sales_value:
                    lowest_sales_days.append(day)

                # A valid figure has been processed, exit the inner loop and move to the next day
                break

            else:
                # Negative sales figures are not accepted
                print(
                    "Please enter a finite sales figure greater than or equal to zero."
                )

        except ValueError:
            # Handles text or other inputs that float() cannot convert
            print("Invalid input. Please enter a number.")

# --- 4. CALCULATE SUMMARY METRICS ---

# Calculate the average sales per day
average_daily_sales = total_sales / days

# Calculate the percentage of days that met or exceeded the target
percentage_days_met = (days_met_target / days) * 100

# --- 5. DISPLAY THE RESULTS ---

# Main performance metrics
print(
    f"Total sales: ${total_sales:.2f}\n"
    f"Average daily sales: ${average_daily_sales:.2f}\n"
    f"Number of high-performing days (> ${daily_sales_target:.2f}): {high_sales_days}\n"
    f"Percentage of days that met or exceeded the ${daily_sales_target:.2f} target: {percentage_days_met:.0f}%\n"
    f"Number of days that met the target (sales >= ${daily_sales_target:.2f}): {days_met_target}\n"
    f"Number of days that didn't meet the target (sales < ${daily_sales_target:.2f}): {below_target_days}\n"
    f"Total days accounted for: {days_met_target + below_target_days}"
)

# Highest and lowest sales
if total_sales == 0:
    print("No sales were recorded during this period.")
else:
    print(
        f"Highest daily sales: ${highest_sales_value:.2f} on day(s) {', '.join(map(str, highest_sales_days))}\n"
        f"Lowest daily sales: ${lowest_sales_value:.2f} on day(s) {', '.join(map(str, lowest_sales_days))}"
    )
