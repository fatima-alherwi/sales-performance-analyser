# sales-performance-analyser
A beginner Python program that analyses daily sales performance against a target.

**Features**
- Collects daily sales figures from the user
- Validates user input and handles invalid entries
- Calculates total and average daily sales
- Counts days that exceeded, met, or missed the sales target
- Calculates the percentage of days that met or exceeded the target
- Identifies the highest and lowest sales figures, including all days tied for each
- Handles zero-sales periods and rejects negative or non-finite sales values
  
**Python Concepts Practised**
- Variables, data types, and arithmetic
- while and for loops
- Conditional statements
- Lists and counters
- Input validation and exception handling
- Functions from Python's math module
- Formatted strings and numerical formatting
  
**How to Run**
- Ensure Python 3 is installed
- Download or clone this repository
- Open a terminal in the project folder
- **Run**:

```bash
python sales_performance_analyser.py
```

**Configuration**

The daily sales target is currently set to $1,000 and can be changed in the source code

**Learning Goals**

This project was created to practise Python fundamentals through a practical business-analysis scenario

**Sample Output**

For example, with daily sales of $500, $1,200, and $500:

```Total sales: $2200.00
Average daily sales: $733.33
Number of high-performing days (> $1000.00): 1
Percentage of days that met or exceeded the $1000.00 target: 33%
Number of days that met the target (sales >= $1000.00): 1
Number of days that didn't meet the target (sales < $1000.00): 2
Total days accounted for: 3
Highest daily sales: $1200.00 on day(s) 2
Lowest daily sales: $500.00 on day(s) 1, 3

