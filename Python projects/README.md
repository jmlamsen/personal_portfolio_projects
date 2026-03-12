# CyPass v1.0

A command-line cybersecurity password auditing tool built with pure Python. Evaluates individual passwords against 7 security criteria, assigns a score out of 10, and generates a full organizational security report across multiple accounts.

Built as a lab project to apply Python fundamentals to a real cybersecurity use case.

---

## What It Does

- Scores each password from 0 to 10 based on length, character variety, and breach history
- Detects passwords that match the account username (the most common account takeover vector)
- Flags passwords found in known breach databases sourced from NCSC and HaveIBeenPwned reports
- Applies a stricter pass threshold for Admin and Sysadmin roles (8/10 required vs. 6/10 for general users)
- Masks passwords in all output to protect sensitive data during review
- Runs batch audits across a full list of accounts
- Produces a final report with pass rate, average score, critical risk count, and a recommended org-level action
- Offers an interactive mode where you audit your own password live from the terminal

---

## Sample Output

```
========================================================
              CYPASS  v1.0
       Simulated Enterprise Security Scan
========================================================

  AUDIT 1 of 6
--------------------------------------------------------

  Account Role  : Admin
  Username      : jsmith
  Password Shown: p*********3
  Password Length: 11 characters
--------------------------------------------------------
  SCORE  : 1 / 10
  RATING : Critical
  STATUS : FAILED
  [##..................]

  Strengths:
    [PASS] Length: Acceptable (10 to 13 characters).
    [PASS] Contains lowercase letters.
    [PASS] Contains numeric digits.

  Issues & Recommendations:
    [FAIL] No uppercase letters found.
    [WARN] No special characters. Add symbols like !@#$%.
    [CRITICAL] This password appears in breached password databases.
               Change it immediately.

...

========================================================
  FINAL SECURITY AUDIT REPORT
========================================================
  Accounts Audited      : 6
  Passed Audit          : 2
  Failed Audit          : 4
  Critical Risk Accounts: 4
  Average Password Score: 3.33 / 10
  Org Pass Rate         : 33.3%
--------------------------------------------------------
  SCORE BREAKDOWN:

    jsmith             [##..................]  1/10  (Critical)
    alice              [##################..]  9/10  (Very Strong)
    alice              [....................]  0/10  (Critical)
    carlos             [....................]  0/10  (Critical)
    priya              [####################]  10/10  (Very Strong)
    tom                [....................]  0/10  (Critical)

--------------------------------------------------------
  ORGANIZATION SECURITY STATUS: HIGH RISK
  RECOMMENDED ACTION: Trigger an immediate org-wide password reset. Notify your security team.
========================================================
```

---

## Scoring Breakdown

| Criterion              | Points  | Notes                                              |
|------------------------|---------|-----------------------------------------------------|
| Length (8 chars)       | +1      | Minimum standard per NIST SP 800-63B               |
| Length (10-13 chars)   | +2      | Acceptable                                          |
| Length (14-19 chars)   | +3      | Very good                                           |
| Length (20+ chars)     | +4      | Excellent                                           |
| Uppercase letters      | +2      |                                                     |
| Lowercase letters      | +1      |                                                     |
| Numeric digits         | +2      |                                                     |
| Special characters     | +2      | Any of: !@#$%^&*()_+-=[]{}|;:,.<>?                |
| Common/breached password | -4    | Instant heavy penalty                               |
| Matches username       | 0/10   | Overrides all other criteria, immediate fail        |

Pass threshold: 6/10 for general users, 8/10 for Admin / Administrator / Sysadmin roles.

---

## Python Concepts Covered

This project was built using Python fundamentals only. No external libraries were used.

- Variables and data types: str, int, float, bool, None
- String methods: strip(), lower(), upper(), title(), find(), count(), startswith(), len(), in operator
- f-strings and string concatenation
- Functions with parameters and default values
- if / elif / else statements with nested conditions
- Boolean operators: and, or, not
- Truthy and falsy value evaluation
- Comparison operators
- Arithmetic and augmented assignment operators (+=, -=)
- Built-in functions: print(), input(), len(), round(), abs(), isinstance(), type()

---

## How to Run

You need Python 3.8 or higher. No pip installs required.

Clone the repository:

```
git clone https://github.com/your-username/cypass.git
cd cypass
```

Run the script:

```
python cypass.py
```

The program runs the batch audit on 6 demo accounts automatically. When it finishes, it asks if you want to run an interactive audit on your own password.

---

## Project Structure

```
cypass/
│
├── cypass.py     # Main script, all logic self-contained
└── README.md
```

---

## Security Note

This tool is built for educational and portfolio purposes. It does not connect to any external API or database. The breach list is a hardcoded sample drawn from publicly documented common passwords. Do not use this as a substitute for a production security tool.

---

## Roadmap

Features planned for future versions:

- Read account data from a CSV file instead of a hardcoded list
- Export the audit report to a .txt file
- Expand the breach list by loading from an external file
- Add entropy-based scoring as a supplementary metric

---

## Author

Built by J.M. Lamsen as a Python Basics lab project. CyPass stands for Cybersecurity Password Auditor.


Connect on LinkedIn: https://www.linkedin.com/in/jonathan-matthew-lamsen-2063b7285/
