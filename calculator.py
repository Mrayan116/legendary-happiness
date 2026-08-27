import tkinter as tk

def on_button_click(value):
    # Get the current text in the entry widget.
    current = entry.get()
    # Clear the entry widget.
    entry.delete(0, tk.END)
    
    if value == 'Clear':
        # Clear button pressed, reset the entry widget.
        entry.insert(tk.END, '')
    elif value == 'C':
        # C button pressed, handle special case 'C=12'
        if current == '12':
            entry.insert(tk.END, 'C=12')
        else:
            entry.insert(tk.END, 'C')
    elif value in 'ABCDEF':
        # If the button clicked is A, B, C, D, E, or F
        entry.insert(tk.END, current + str(value))
    else:
        # Other buttons pressed, update the entry widget
        entry.insert(tk.END, current + value)

def clear_entry():
    # Clear the entry widget
    entry.delete(0, tk.END)

def calculate():
    try:
        # Evaluate the expression and display the result
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        # Handle exceptions and display an error message
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_conversion(conversion_type):
    try:
        input_value = entry.get()
        if conversion_type == "BinToDec":
            # Convert binary to decimal
            if all(bit in '01' for bit in input_value):
                result = str(int(input_value, 2))
            else:
                result = "Error"
        elif conversion_type == "DecToBin":
            # Convert decimal to binary
            if input_value.isdigit():
                result = bin(int(input_value))[2:]
            else:
                result = "Error"
        elif conversion_type == "HexToBin":
            # Convert hexadecimal to binary
            try:
                result = bin(int(input_value, 16))[2:].zfill(len(input_value) * 4)
            except ValueError:
                result = "Error"
        elif conversion_type == "BinToHex":
            # Convert binary to hexadecimal
            if all(bit in '01' for bit in input_value):
                result = hex(int(input_value, 2))[2:].upper()
            else:
                result = "Error"
        elif conversion_type == "DecToHex":
            # Convert decimal to hexadecimal
            if input_value.isdigit():
                result = hex(int(input_value))[2:].upper()
            else:
                result = "Error"
        elif conversion_type == "HexToDec":
            # Convert hexadecimal to decimal
            try:
                result = str(int(input_value, 16))
            except ValueError:
                result = "Error"
        else:
            result = "Error"
        
        # Update the entry widget with the conversion result
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        # Handle exceptions and display an error message
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Conversion Calculator")
root.configure(bg='black')  # Set background color

# Entry widget for user input and display
entry = tk.Entry(root, width=20, font=('Arial', 14), bg='orange', fg='black')
entry.grid(row=0, column=0, columnspan=5, pady=10)

# Define button layout
button_layout = [
    ['7', '8', '9', '/',],['4', '5', '6', '*'], ['1', '2', '3', '-',], ['0', '.', '=', '+'], ['A', 'B', 'C', 'Clear'],['D', 'E', 'F'],['BinToDec', 'DecToBin',  'HexToBin',],['BinToHex', 'DecToHex', 'HexToDec'],
]

# Create and place the buttons with different colors
row_counter = 0
for row in button_layout:
    col_counter = 0
    for button in row:
        if button == '=':
            # '=' button for calculations
            tk.Button(root, text=button, width=5, height=2, command=calculate,
                      bg='green', fg='black').grid(row=row_counter + 1, column=col_counter, pady=5, padx=5)
        elif button in ['BinToDec', 'DecToBin', 'HexToBin', 'BinToHex', 'DecToHex', 'HexToDec']:
            # Buttons for base conversions
            tk.Button(root, text=button, width=8, height=2, command=lambda b=button: calculate_conversion(b),
                      bg='blue', fg='white').grid(row=row_counter + 1, column=col_counter, pady=5, padx=5)
        elif button == 'Clear':
            # Clear button
            tk.Button(root, text=button, width=5, height=2, command=clear_entry,
                      bg='red', fg='black').grid(row=row_counter + 1, column=col_counter, pady=5, padx=5)
        else:
            # Numeric and operator buttons
            tk.Button(root, text=button, width=5, height=2, command=lambda b=button: on_button_click(b),
                      bg='orange', fg='black').grid(row=row_counter + 1, column=col_counter, pady=5, padx=5)
        col_counter += 1
    row_counter += 1

# Run the Tkinter event loop
root.mainloop()



