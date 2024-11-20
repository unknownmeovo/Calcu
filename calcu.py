import tkinter as tk
from tkinter import ttk, messagebox
from sympy import symbols, Eq, simplify, solve, sympify

# History for past calculations
history = []

def preprocess_input(user_input):
    """Preprocess user input to handle implicit multiplication."""
    processed_input = ""
    for i in range(len(user_input)):
        if i > 0 and user_input[i] == '(' and user_input[i - 1].isalnum():
            # Add multiplication before parentheses (e.g., "2(x+1)" -> "2*(x+1)")
            processed_input += "*("
        elif i > 0 and user_input[i] == 'x' and user_input[i - 1].isdigit():
            # Add multiplication for implicit multiplication with 'x' (e.g., "2x" -> "2*x")
            processed_input += "*x"
        elif i > 0 and user_input[i] == 'y' and user_input[i - 1].isdigit():
            # Add multiplication for implicit multiplication with 'y' (e.g., "3y" -> "3*y")
            processed_input += "*y"
        elif i > 0 and user_input[i] == '-' and user_input[i - 1].isdigit():
            # Handle negative numbers (e.g., "-3x" -> "-3*x")
            processed_input += "*-"
        else:
            processed_input += user_input[i]
    return processed_input

def extract_variables(expression):
    """Extract variables from the expression."""
    return list(set(char for char in expression if char.isalpha()))

def evaluate_expression():
    """Evaluates the entered algebraic expression."""
    user_input = entry.get().strip()
    try:
        # Preprocess input for implicit multiplication
        user_input = preprocess_input(user_input)
        
        # Extract variables and define them as symbolic
        variables = extract_variables(user_input)
        symbols_dict = {var: symbols(var) for var in variables}
        
        if "=" in user_input:
            # Handle equations
            lhs, rhs = user_input.split("=")
            equation = Eq(sympify(lhs, symbols_dict), sympify(rhs, symbols_dict))
            solution = solve(equation, list(symbols_dict.values()))
            result_text.set(f"Solution: {solution}")
            add_to_history(user_input, f"Solution: {solution}")
        else:
            # Handle expressions
            expression = sympify(user_input, symbols_dict)
            result = simplify(expression)
            result_text.set(f"Result: {result}")
            add_to_history(user_input, f"Result: {result}")
    except SyntaxError:
        messagebox.showerror("Syntax Error", "Please check your input for valid syntax.")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def clear_input():
    """Clears the input field and result label."""
    entry.delete(0, tk.END)
    result_text.set("")

def add_to_history(input_text, result):
    """Adds the calculation to history."""
    if len(history) >= 10:  # Keep history limited to 10 items
        history.pop(0)
    history.append(f"{input_text} → {result}")
    update_history()

def update_history():
    """Updates the history display."""
    history_text.config(state=tk.NORMAL)  # Enable editing to update
    history_text.delete(1.0, tk.END)  # Clear existing content
    history_text.insert(tk.END, "\n".join(history))  # Insert updated history
    history_text.config(state=tk.DISABLED)  # Disable editing

def toggle_theme():
    """Toggles between light and dark themes."""
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.config(bg="#2E2E2E")
        result_label.config(readonlybackground="#3E3E3E", fg="white")
        entry.config(bg="#3E3E3E", fg="white", insertbackground="white")
        history_frame.config(bg="#2E2E2E")
        history_text.config(bg="#3E3E3E", fg="white")
        theme_button.config(text="Switch to Light Mode", style="Rounded.TButton")
    else:
        root.config(bg="white")
        result_label.config(readonlybackground="white", fg="blue")
        entry.config(bg="white", fg="black", insertbackground="black")
        history_frame.config(bg="white")
        history_text.config(bg="white", fg="black")
        theme_button.config(text="Switch to Dark Mode", style="Rounded.TButton")

# Create the main window
root = tk.Tk()
root.title("Simple Algebraic Calculator")
root.geometry("600x500")
root.resizable(False, False)
dark_mode = False  # Default theme

# Styling
style = ttk.Style()
style.theme_use("clam")

# Custom button styling for rounded edges
style.configure("Rounded.TButton", 
                font=("Arial", 12),
                padding=6,
                borderwidth=1,
                relief="flat")
style.map("Rounded.TButton", background=[("active", "#cce7ff")])

# Header Section
header = ttk.Label(root, text="Simple Algebraic Calculator", font=("Arial", 20, "bold"))
header.pack(pady=15)

instruction = ttk.Label(root, text="Enter an algebraic expression or equation (e.g., 23x - 8y = 99):")
instruction.pack(pady=5)

entry = ttk.Entry(root, width=50, font=("Arial", 14))
entry.pack(pady=10)

# Result Section
result_text = tk.StringVar()
result_label = tk.Entry(root, textvariable=result_text, font=("Arial", 14), state="readonly", readonlybackground="white", fg="blue", bd=0)
result_label.pack(pady=10)

# Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

calculate_button = ttk.Button(button_frame, text="Calculate", style="Rounded.TButton", command=evaluate_expression)
calculate_button.grid(row=0, column=0, padx=10)

clear_button = ttk.Button(button_frame, text="Clear", style="Rounded.TButton", command=clear_input)
clear_button.grid(row=0, column=1, padx=10)

exit_button = ttk.Button(button_frame, text="Exit", style="Rounded.TButton", command=root.quit)
exit_button.grid(row=0, column=2, padx=10)

# Dark Mode Toggle
theme_button = ttk.Button(root, text="Switch to Dark Mode", style="Rounded.TButton", command=toggle_theme)
theme_button.pack(pady=10)

# History Section
history_frame = tk.Frame(root, bg="white")
history_frame.pack(pady=20, fill=tk.BOTH, expand=True)

history_text = tk.Text(history_frame, font=("Arial", 10), bg="white", fg="black", state=tk.DISABLED, wrap=tk.WORD)
history_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)

# Scrollbar for history
scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, command=history_text.yview)
history_text.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()
