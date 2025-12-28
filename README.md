# SQL Injection Security & Performance Analysis

This repository contains the experimental code for the SEG2102 Final Assessment. The project demonstrates the impact of SQL Injection attacks on data integrity and evaluates the performance trade-off of using Prepared Statements.

## Project Structure
- `database_setup.sql`: SQL script to initialize the testing database.
- `vulnerable.php`: Implementation of a login page vulnerable to SQL Injection.
- `secure.php`: Implementation of a secure login page using Parameterized Queries.
- `benchmark_test.py`: Python script to automate attack simulation and latency measurement.

## How to Run the Experiment

### 1. Database Setup
1. Install XAMPP and start Apache & MySQL.
2. Import `database_setup.sql` into phpMyAdmin.

### 2. Deployment
1. Place the PHP files in `C:\xampp\htdocs\sql_test\`.
2. Configure `config.php` if your database credentials differ from default.

### 3. Execution
Run the Python benchmark script:
```bash
pip install requests
python benchmark_test.py
Experimental Results
The script tests for:

Security/Integrity: Verifies if ' OR '1'='1 bypasses login.

Latency: Compares response time (ms) between vulnerable and secure implementations.

(If you uploaded a screenshot, keep this line; otherwise delete it)

Author
[你的名字/学号] Sunway University
