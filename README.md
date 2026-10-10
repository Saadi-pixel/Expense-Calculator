# 📊 Daily & Monthly Expense Calculator

> *A lightweight, command-line expense tracking application built with Python for CS50P.*

![Python 3.13+](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CSV Database](https://img.shields.io/badge/Storage-CSV-green?style=for-the-badge&logo=datacamp&logoColor=white)
![Pytest Tested](https://img.shields.io/badge/Tested%20With-Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

---

## ⚡ Overview

The **Daily & Monthly Expense Calculator** is an intuitive CLI tool designed to streamline personal financial management. It allows users to log expenses, aggregate daily and monthly totals, search transaction logs, and format outputs cleanly using structured tables.

---

## ✨ Key Features

* 📝 **Log Transactions:** Quickly record expense category, description, date, and cost.
* 📈 **Instant Aggregations:** Calculate total spending broken down by day or month.
* 🔍 **Search & Filter:** Query logged expenses using custom search parameters.
* 📊 **Formatted Tables:** Renders clean ASCII tables powered by `tabulate`.
* 💾 **Persistent Storage:** Stores all financial entries securely in a local `expenses.csv` file.
* 🧪 **Automated Testing:** Fully verified via unit tests in `test_project.py` using `pytest`.

---

## 📁 Project Architecture

```text
├── project.py         # Main application source code & core CLI functions
├── test_project.py    # Pytest suit verifying project functions
├── requirements.txt   # Third-party dependencies (tabulate, pytest)
├── .gitignore         # Git tracking exclusion list
├── LICENSE            # MIT Open-Source License
└── README.md          # Project documentation
