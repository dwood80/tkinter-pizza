# Auther: Darien Wood
# Date made: 5/2/2023
# Purpose: tkinter final project
# Program: this tkinter program is used for oredering a pizza

import tkinter as tk

class PizzaOrderApp:
    def clear_fields(self):
    # Reset the order details variables to their default values
        self.size_var.set("Medium")
        self.type_var.set("Cheese")
        self.toppings_var.set("")
        self.toppings_entry.delete(0, tk.END)

    def __init__(self, master):
        # Set the main window and title
        self.master = master
        master.title("Pizza Order App")

        # Create variables to hold pizza order details
        self.size_var = tk.StringVar(value="Medium")  # default size is Medium
        self.type_var = tk.StringVar(value="Cheese")  # default type is Cheese
        self.toppings_var = tk.StringVar(value="")    # default toppings is empty

        # Create the size selection option menu
        size_label = tk.Label(master, text="Select size:")
        size_label.grid(row=0, column=0)
        sizes = ["Small", "Medium", "Large"]
        self.size_menu = tk.OptionMenu(master, self.size_var, *sizes)  # create the option menu with sizes
        self.size_menu.grid(row=0, column=1)

        # Create the pizza type selection radio buttons
        type_label = tk.Label(master, text="Select pizza type:")
        type_label.grid(row=1, column=0)
        types = [("Cheese", "Cheese"), 
                 ("Pepperoni", "Pepperoni"), 
                 ("Veggie", "Veggie")]
        for i, (text, value) in enumerate(types):
            button = tk.Radiobutton(master, text=text, variable=self.type_var, value=value)  # create a radio button for each type
            button.grid(row=i+2, column=1, sticky="W")

        # Create the toppings entry field
        toppings_label = tk.Label(master, text="Enter toppings (separated by commas):")
        toppings_label.grid(row=5, column=0)
        self.toppings_entry = tk.Entry(master, textvariable=self.toppings_var)  # create an entry field for toppings
        self.toppings_entry.grid(row=5, column=1)

        # Create the order button
        order_button = tk.Button(master, text="Order now", command=self.show_confirmation)  # create the order button
        order_button.grid(row=6, column=1)

          # Create the clear button
        clear_button = tk.Button(master, text="Clear", command=self.clear_fields)  # create the clear button
        clear_button.grid(row=6, column=0)

        # Create the exit button
        exit_button = tk.Button(master, text="Exit", command=master.quit)
        exit_button.grid(row=7, column=1)

    def show_confirmation(self):
        # Get the order details from the variables
        size = self.size_var.get()
        pizza_type = self.type_var.get()
        toppings = self.toppings_var.get().split(",")
        toppings = [t.strip() for t in toppings if t.strip()]

        # Create the confirmation message
        confirmation_message = f"Thank you for ordering a {size} {pizza_type} pizza"
        if toppings:
            confirmation_message += f" with {', '.join(toppings)}"

        # Show the confirmation message in a new window
        confirmation_window = tk.Toplevel(self.master)
        confirmation_label = tk.Label(confirmation_window, text=confirmation_message)  # create a new window with the confirmation message
        confirmation_label.pack(padx=20, pady=20)

# Create the main window and run the app
root = tk.Tk()
app = PizzaOrderApp(root)
root.mainloop()
