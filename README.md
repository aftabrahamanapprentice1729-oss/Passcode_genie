# Passcode_genie

A lightweight, modern desktop application built in Python for generating secure, randomized passwords. The tool features an intuitive graphical user interface (GUI) allowing users to customize password length and character constraints dynamically.

---

## Features

- **Custom Length Slider:** Generate passwords anywhere from 6 to 30 characters long.
- **Granular Character Pools:** Toggle uppercase letters, numeric digits, and special symbols on or off based on security requirements.
- **Modern UI:** Built using a responsive dark-themed design with native window scaling.
- **One-Click Generation:** Instantly outputs the password string to a selectable text field for quick copying.
- **Local-Only Execution:** Password generation occurs entirely on-device with no external API calls or cloud storage.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or higher
- `pip` package manager

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/aftabrahamanapprentice1729-oss/ Passcode_genie.git
cd  Passcode_genie
```

### 2. Install Dependencies

Install the required packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main application script from your terminal:

```bash
python password_gen.py
```

---

## How It Works

The application dynamically generates passwords based on the selected GUI options.

### Internal Workflow

1. Reads the state of the checkbox controls:
   - Uppercase letters
   - Numbers
   - Symbols

2. Builds a dynamic character pool using the enabled categories.

3. Uses Python's pseudo-random selection mechanism to generate a password matching the exact slider-defined length.

4. Displays the generated password directly inside the GUI for instant copying.

---

## Project Structure

```plaintext
 Passcode_genie/
│
├── password_gen.py   # Main application logic and GUI layout
├── requirements.txt          # External dependencies
└── README.md                 # Project documentation
```

---

## Example Passwords

```txt
N8@qL2!xPa
vR7#tZ1$Km
Q2&wXp9!Ld
```

---

## Security Notes

- All password generation is performed locally.
- No generated password is stored or logged.
- No internet connection is required.
- No telemetry or tracking is included.

---

## Dependencies

Primary dependency:

```txt
customtkinter
```

---

## License

This project is open-source and available under the MIT License.

---
