import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier

# Load and prepare the dataset (Same as before)
df = pd.read_csv("iriss.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Label Encoding and Scaling
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the model (MLPClassifier)
model = MLPClassifier(hidden_layer_sizes=(16, 8), activation='relu', max_iter=1000, solver='adam', random_state=42)
model.fit(X_scaled, y_encoded)

# Create the GUI window
window = tk.Tk()
window.title("Flower Type Predictor")
window.geometry("400x400")  # Set the size of the window
window.config(bg="#f0f8ff")  # Set a light blue background color

# Add a title label with some styling
title_label = tk.Label(window, text="Flower Type Prediction", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#2e8b57")
title_label.pack(pady=20)

# Create a frame to hold the input fields and labels (for better organization)
input_frame = tk.Frame(window, bg="#f0f8ff")
input_frame.pack(pady=10)

feature_labels = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
entries = []

# Create labels and entry widgets for the features
for i, label in enumerate(feature_labels):
    label_widget = tk.Label(input_frame, text=label, font=("Arial", 12), bg="#f0f8ff", fg="#333")
    label_widget.grid(row=i, column=0, padx=20, pady=5, sticky="w")

    entry = tk.Entry(input_frame, font=("Arial", 12), width=20, relief="solid", borderwidth=2)
    entry.grid(row=i, column=1, padx=20, pady=5)
    entries.append(entry)

# Function to make predictions when the button is clicked
def predict():
    try:
        # Get the input values and convert them into a NumPy array
        features = np.array([float(entry.get()) for entry in entries]).reshape(1, -1)
        
        # Scale the input features using the same scaler as the training data
        features_scaled = scaler.transform(features)
        
        # Predict using the trained model
        prediction = model.predict(features_scaled)
        
        # Convert the predicted class index back to the original label
        predicted_label = label_encoder.inverse_transform(prediction)
        
        # Show the result in a messagebox
        messagebox.showinfo("Prediction", f"Predicted Flower Type: {predicted_label[0]}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for all features.")

# Create a button to trigger the prediction
predict_button = tk.Button(window, text="Predict Flower Type", command=predict, font=("Arial", 14), bg="#4caf50", fg="white", relief="solid", width=20)
predict_button.pack(pady=20)

# Footer Label with Credits
footer_label = tk.Label(window, text="Developed by AI Lab", font=("Arial", 10, "italic"), bg="#f0f8ff", fg="#555")
footer_label.pack(side="bottom", pady=10)

# Run the GUI event loop
window.mainloop()
