# gui-password-manager
Simple Python Password Manager (Tkinter)  A lightweight desktop password manager built with Python and Tkinter.   It lets you:  - Generate strong random passwords - Copy passwords directly to your clipboard - Save website credentials (website, email/username, password) to a local text file

## 🧩 Features

- 🎲 **Random Password Generator**
  - Mix of letters (upper & lower case), numbers, and symbols
  - Automatically copies the generated password to your clipboard via `pyperclip`

- 💾 **Save Credentials**
  - Store website, email/username, and password in `data.txt`
  - Each entry is stored in the format:
    ```text
    website|email|password
    ```

- 🖥️ **Graphical User Interface (GUI)**
  - Built with Tkinter
  - Simple and minimal layout:
    - Website input
    - Email/Username input (pre-filled with a default email)
    - Password field + “Generate Password” button
    - “Add” button to save credentials
  - Displays confirmation dialogs before saving

---

## 📦 Requirements

- Python 3.x
- The following Python modules:
  - `tkinter` (usually comes with Python on most systems)
  - `pyperclip`
  - `random` (part of Python standard library)

