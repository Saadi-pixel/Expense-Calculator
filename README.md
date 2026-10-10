# DAILY AND MONTHLY EXPENSE CALCULATOR
#### Video Demo: https://youtu.be/YOUR_VIDEO_ID_HERE

#### Description:
Welcome to the **Daily and Monthly Expense Calculator**, a robust and user-friendly command-line application built in Python for Harvard’s CS50p final project. 

Managing personal finances is a crucial everyday task, yet many people struggle to keep clear records without complex software. This project provides a lightweight, terminal-based solution that allows users to seamlessly log, review, search, and analyze their daily expenditures. Data persistence is handled via a local CSV file (`expenses.csv`), and output data is formatted cleanly using the `tabulate` library for an enhanced user interface.

---

### Project Structure & Design Architecture

The project is split into modular components to ensure separation of concerns, testability, and clean code practices:

1. **`project.py` (Core Application):**
   - **`main()`:** Serves as the primary control loop, presenting a clear numerical menu system (1 through 6) with input validation.
   - **`add_expense()`:** Prompts the user for category, item name, date, and amount. It features robust input error handling to ensure monetary values are successfully captured as integers before appending the entry safely to the CSV file.
   - **`show_expenses()`:** Reads all recorded entries from the database and renders them in a styled tabular grid (`fancy_grid`) using `tabulate`.
   - **`search_expense()`:** Allows users to query specific spending categories, filtering matching records and displaying them dynamically.
   - **`calculate_total()`:** Computes and outputs the cumulative lifetime spending across all recorded items.
   - **`calculate_categorywise_spendings()`:** Aggregates and reports total expenditures for a user-specified category.

2. **`test_project.py` (Automated Testing Suite):**
   - Written for `pytest`, this file validates core application logic without altering production data. It uses `capsys` to verify terminal output and `monkeypatch` to simulate user inputs, ensuring high test coverage for functions like `calculate_total`, `calculate_categorywise_spendings`, and `search_expense`.

3. **`expenses.csv` (Data Storage):**
   - Automatically created upon the first successful expense entry, serving as a persistent lightweight flat-file database.

---

### Getting Started & Installation

To run this project locally on your machine, follow these simple steps:

1. Clone or download the project files into a single directory.
2. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python project.py
   ```

---

### Running the Tests

To execute the automated test suite using `pytest`, run the following command in your terminal:
```bash
pytest test_project.py
```

---

### Design Choices & Challenges

- **Why CSV?** A comma-separated values file was chosen for its simplicity, speed, and lack of heavy database dependencies, making the tool instantly portable.
- **Error Handling:** Extensive use of `try-except` blocks for `FileNotFoundError` ensures that users attempting to run reports before creating any expenses receive a friendly message instead of a program crash.
- **User Experience:** Incorporating the `tabulate` package transforms raw data into a clean, easy-to-read financial dashboard right inside the command line.