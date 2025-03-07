# Homework

import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np

# Load the pretrained model
with open("model2.pkl", "rb") as file:
    model = pickle.load(file)

# Function to make predictions
def predict_edibility():
    try:
        # Get user inputs
        inputs = [
            float(entry_cap_diameter.get()),
            float(entry_cap_shape.get()),
            float(entry_gill_attachment.get()),
            float(entry_gill_color.get()),
            float(entry_stem_height.get()),
            float(entry_stem_width.get()),
            float(entry_stem_color.get()),
            float(entry_season.get())
        ]
        inputs = np.array(inputs).reshape(1, -1)

        # Predict using the loaded model
        prediction = model.predict(inputs)
        result = prediction[0]
        if result == 0:
            messagebox.showinfo("Prediction", f"The prediction is: {result} i.e. edible")
        else:
            messagebox.showinfo("Prediction", f"The prediction is: {result} i.e. poisonous")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI Setup
root = tk.Tk()
root.title("Mushroom Edible/Poisonous")

# Input Fields
tk.Label(root, text="Cap Diameter (cm):").grid(row=0, column=0, padx=10, pady=5)
entry_cap_diameter = tk.Entry(root)
entry_cap_diameter.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Cap Shape (cm):").grid(row=1, column=0, padx=10, pady=5)
entry_cap_shape = tk.Entry(root)
entry_cap_shape.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Gill Attachment (cm):").grid(row=2, column=0, padx=10, pady=5)
entry_gill_attachment = tk.Entry(root)
entry_gill_attachment.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Gill Color :").grid(row=3, column=0, padx=10, pady=5)
entry_gill_color = tk.Entry(root)
entry_gill_color.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Stem Height (cm):").grid(row=4, column=0, padx=10, pady=5)
entry_stem_height = tk.Entry(root)
entry_stem_height.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Stem Width (cm):").grid(row=5, column=0, padx=10, pady=5)
entry_stem_width = tk.Entry(root)
entry_stem_width.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Stem Color :").grid(row=6, column=0, padx=10, pady=5)
entry_stem_color = tk.Entry(root)
entry_stem_color.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Season :").grid(row=7, column=0, padx=10, pady=5)
entry_season = tk.Entry(root)
entry_season.grid(row=7, column=1, padx=10, pady=5)

# Predict Button
predict_button = tk.Button(root, text="Predict", command=predict_edibility)
predict_button.grid(row=8, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
