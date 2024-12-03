import tkinter as tk
from tkinter import messagebox
import pyperclip
from openai import OpenAI

# Set up your OpenAI client
client = OpenAI(api_key="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")  # Replace with your actual API key

def chat_with_gpt():
    """
    Sends the user's question to OpenAI's GPT API and displays the response.
    """
    user_input = user_input_field.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showerror("Error", "Please enter a question.")
        return

    try:
        # Updated API call using the new client structure
        response = client.chat.completions.create(
            model="gpt-4",  # Use "gpt-4" if you have access
            messages=[
                {"role": "user", "content": user_input}
            ],
        )

        # Extract the response content
        answer = response.choices[0].message.content.strip()

        # Display the response in the text area
        response_field.delete("1.0", tk.END)
        response_field.insert(tk.END, answer)

        # Copy response to clipboard
        pyperclip.copy(answer)
        messagebox.showinfo("Copied", "The response has been copied to your clipboard.")

    except Exception as e:
        response_field.delete("1.0", tk.END)
        response_field.insert(tk.END, f"Error: {str(e)}")

# Create the main Tkinter window
app = tk.Tk()
app.title("ChatGPT GUI (Updated)")

# Set the window size
app.geometry("600x500")
app.resizable(False, False)

# Create a frame for user input
input_frame = tk.Frame(app)
input_frame.pack(pady=10)

# Label for input
input_label = tk.Label(input_frame, text="Ask a question:")
input_label.pack(anchor="w")

# Text area for user input
user_input_field = tk.Text(input_frame, height=5, width=70)
user_input_field.pack()

# Button to send question to ChatGPT
submit_button = tk.Button(app, text="Ask ChatGPT", command=chat_with_gpt)
submit_button.pack(pady=10)

# Label for response
response_label = tk.Label(app, text="ChatGPT Response:")
response_label.pack(anchor="w", pady=5)

# Text area for ChatGPT response
response_field = tk.Text(app, height=15, width=70, state="normal", bg="#f4f4f4")
response_field.pack()

# Run the Tkinter main loop
app.mainloop()
