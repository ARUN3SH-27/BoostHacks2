import tkinter as tk
import time
import random

# Sentences for the typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "Sphinx of black quartz, judge my vow.",
    "Mr. Jock, TV quiz PhD, bags few lynx.",
    "Jackdaws love my big sphinx of quartz.",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.configure(bg="light blue")  # Set background color
        
        # Select a random sentence
        self.sentence = random.choice(sentences)
        
        # Create GUI elements
        self.label = tk.Label(root, text="Type the following sentence:", font=("Arial", 14), bg="light blue", fg="black")
        self.label.pack(pady=10)
        
        self.sentence_label = tk.Label(root, text=self.sentence, font=("Arial", 14, "italic"), bg="light blue", fg="black", wraplength=500)
        self.sentence_label.pack(pady=10)
        
        self.text_entry = tk.Entry(root, font=("Arial", 14), width=50, bg="light yellow", fg="black")
        self.text_entry.pack(pady=10)
        self.text_entry.config(state=tk.DISABLED)  # Disable the text entry initially
        
        self.start_button = tk.Button(root, text="Start", font=("Arial", 14), command=self.start_test, bg="light yellow", fg="black")
        self.start_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 14), bg="light blue", fg="black")
        self.result_label.pack(pady=10)
        
        self.start_time = None

    def start_test(self):
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)  # Disable the start button
        self.text_entry.config(state=tk.NORMAL)  # Enable the text entry widget
        self.text_entry.focus()  # Focus on the text entry widget

    def calculate_speed(self):
        if self.start_time is None:
            return
        
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        time_in_minutes = elapsed_time / 60
        
        # Get the user's input and calculate WPM and accuracy
        user_input = self.text_entry.get()
        words_typed = len(user_input.split())
        wpm = words_typed / time_in_minutes if time_in_minutes > 0 else 0

        accuracy = sum(1 for a, b in zip(self.sentence.lower(), user_input.lower()) if a == b) / len(self.sentence) * 100
        
        # Display the results
        self.result_label.config(text=f"Time: {elapsed_time:.2f} seconds\nWPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}%")
        
        # Reset the test
        self.start_button.config(state=tk.NORMAL)  # Re-enable the start button
        self.text_entry.config(state=tk.DISABLED)  # Disable the text entry widget
        self.text_entry.delete(0, tk.END)
        self.sentence = random.choice(sentences)
        self.sentence_label.config(text=self.sentence)
        self.start_time = None

def main():
    root = tk.Tk()
    app = TypingSpeedTest(root)
    
    # Bind Enter key to calculate speed
    root.bind("<Return>", lambda event: app.calculate_speed())
    
    root.mainloop()

if __name__ == "__main__":
    main()
