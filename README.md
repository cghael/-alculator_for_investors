# Calculator for Investors
Simple CRUD python application with SQLAlchemy

A small program that helps investors make a fundamental analysis based on the company's reports and estimate the company's performance. With this calculator, you can choose the best company in the industry and decide whether to buy its shares or not.

## Examples
```
MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> 1

CRUD MENU
0 Back
1 Create a company
2 Read a company
3 Update a company
4 Delete a company
5 List all companies

Enter an option:
> 2
Enter company name:
> notacompany
Company not found!

MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> 1

CRUD MENU
0 Back
1 Create a company
2 Read a company
3 Update a company
4 Delete a company
5 List all companies

Enter an option:
> 2
Enter company name:
> go
0 Alphabet Inc (Google) Class C
1 Wells Fargo & Company
2 Goldman Sachs Group, Inc. (The)
Enter company number:
> 1
WFC Wells Fargo & Company
P/E = 7.41
P/S = 1.87
P/B = 0.08
ND/EBITDA = None
ROE = 0.12
ROA = 0.01
L/A = 0.91
```

```
MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> 1

CRUD MENU
0 Back
1 Create a company
2 Read a company
3 Update a company
4 Delete a company
5 List all companies

Enter an option:
> 3
Enter company name:
> go
0 Alphabet Inc (Google) Class C
1 Wells Fargo & Company
2 Goldman Sachs Group, Inc. (The)
Enter company number:
> 0
Enter ebitda (in the format '987654321'):
> 1000
Enter sales (in the format '987654321'):
> 1000
Enter net profit (in the format '987654321'):
> 250
Enter market price (in the format '987654321'):
> 2000
Enter net debt (in the format '987654321'):
> 100
Enter assets (in the format '987654321'):
> 2000
Enter equity (in the format '987654321'):
> 2500
Enter cash equivalents (in the format '987654321'):
> 2500
Enter liabilities (in the format '987654321'):
> 10
Company updated successfully!
```

```
Welcome to the Investor Program!

MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> 2

TOP TEN MENU
0 Back
1 List by ND/EBITDA
2 List by ROE
3 List by ROA

Enter an option:
> 1
TICKER ND/EBITDA
DUK 6.4
SO 6.02
CHTR 4.55
NEE 4.39
TMUS 4.19
DE 4.16
T 3.94
MCD 3.77
VZ 3.57
CAT 3.34

MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> 2

TOP TEN MENU
0 Back
1 List by ND/EBITDA
2 List by ROE
3 List by ROA

Enter an option:
> 2
TICKER ROE
AMGN 6.43
AAPL 1.4
MA 1.22
UPS 0.84
ABBV 0.7
QCOM 0.68
LMT 0.63
ADP 0.62
LLY 0.59
TXN 0.55

MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> 2

TOP TEN MENU
0 Back
1 List by ND/EBITDA
2 List by ROE
3 List by ROA

Enter an option:
> 3
TICKER ROA
TXN 0.31
AAPL 0.27
FB 0.24
MA 0.23
HD 0.23
AMAT 0.23
NVDA 0.22
PM 0.22
GOOG 0.21
QCOM 0.2

MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria

Enter an option:
> 0
Have a nice day!
```
