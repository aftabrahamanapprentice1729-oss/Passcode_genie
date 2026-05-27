import random
import customtkinter as ctk

# Set the overall theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PasswordGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simple Password Generator")
        self.geometry("450x420")
        self.resizable(False, False)

        # Title
        self.title_label = ctk.CTkLabel(self, text="🛠️ Easy Password Generator", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=20)

        # Password Display Box
        self.result_var = ctk.StringVar(value="Your password will appear here")
        self.result_entry = ctk.CTkEntry(self, textvariable=self.result_var, font=ctk.CTkFont(size=15), width=350, height=45, justify="center")
        self.result_entry.pack(pady=10)

        # Slider for Length
        self.length_label = ctk.CTkLabel(self, text="Length: 12", font=ctk.CTkFont(size=14))
        self.length_label.pack(pady=5)
        self.slider = ctk.CTkSlider(self, from_=6, to=30, number_of_steps=24, command=self.update_label)
        self.slider.set(12)
        self.slider.pack(pady=5)

        # Checkboxes for choices
        self.cb_caps = ctk.CTkCheckBox(self, text="Include Capital Letters (A-Z)")
        self.cb_caps.select()
        self.cb_caps.pack(pady=8, anchor="w", padx=80)

        self.cb_numbers = ctk.CTkCheckBox(self, text="Include Numbers (0-9)")
        self.cb_numbers.select()
        self.cb_numbers.pack(pady=8, anchor="w", padx=80)

        self.cb_symbols = ctk.CTkCheckBox(self, text="Include Symbols (@#$%)")
        self.cb_symbols.select()
        self.cb_symbols.pack(pady=8, anchor="w", padx=80)

        # Generate Button
        self.generate_btn = ctk.CTkButton(self, text="Generate", font=ctk.CTkFont(size=15, weight="bold"), height=40, width=200, command=self.make_password)
        self.generate_btn.pack(pady=20)

    def update_label(self, value):
        self.length_label.configure(text=f"Length: {int(value)}")

    def make_password(self):
        # 1. Define our basic building blocks
        lower_letters = "abcdefghijklmnopqrstuvwxyz"
        upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "!@#$%^&*()_+-="

        # Start our character pool with just lowercase letters
        character_pool = lower_letters

        # 2. Look at the GUI checkboxes and add to the pool accordingly
        if self.cb_caps.get() == 1:
            character_pool += upper_letters
            
        if self.cb_numbers.get() == 1:
            character_pool += numbers
            
        if self.cb_symbols.get() == 1:
            character_pool += symbols

        # 3. Get the length from the slider
        password_length = int(self.slider.get())

        # 4. Randomly pick characters from our pool and join them into a string
        generated_password = "".join(random.choices(character_pool, k=password_length))

        # 5. Send the final string straight back to the GUI entry box!
        self.result_var.set(generated_password)

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()