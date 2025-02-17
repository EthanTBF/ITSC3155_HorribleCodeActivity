# Simple Calculator - Good vs. Bad Coding Practices

## Overview
This project demonstrates good and bad coding practices using a simple calculator program. The calculator supports four operations: addition, subtraction, multiplication, and division.

## Programs

### 1. **Good Coding Practices (`good_calculator.py`)**
This version follows best coding practices, including:
- **KISS (Keep It Simple, Stupid):** Uses a clean and minimal structure.
- **DRY (Don't Repeat Yourself):** Eliminates redundant code by using a reusable function for number input validation.
- **Single Responsibility Principle:** Each function performs a single task.
- **Separation of Concerns:** The code is modular, separating user input handling, calculations, and program execution.

### 2. **Bad Coding Practices (`bad_calculator.py`)**
This version demonstrates poor coding habits, such as:
- Long and repetitive `if-else` statements instead of a clean function-based approach.
- Input validation duplicated for every operation, violating **DRY**.
- Lack of modular functions, making maintenance difficult.
- No proper error handling, leading to potential crashes.
