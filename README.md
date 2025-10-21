# 🔐 Password Guessing Demo — Local Web + PyAutoGUI Automation

> Educational demo showing a simple local HTML page that prompts for a password and a Python automation script (PyAutoGUI) that programmatically types guesses and detects success. **This repository is for learning and testing only.** Do **not** use these tools against other people's systems or services.

---

## ⚠️ Safety & Ethics (Read first)
- **ONLY** run the HTML page and the automation script on a machine and browser you control (e.g., your local computer), or in an isolated virtual machine/test environment.
- Never point this automation at remote websites, services, or accounts that you do not own or do not have explicit permission to test.
- This project is intended for educational purposes: to learn about automation, GUI interaction, and basic scripting — not to break into systems.

---

## Project Overview
This project contains two main parts:

1. `index.html` — a tiny local web page (runs in your browser) that asks a user to set a password, then accepts guesses until the correct password is entered and displays the number of guesses.
2. `guesser.py` — a Python script using `pyautogui` that automates typing guesses into the web page's prompt and detects when the page indicates success. Includes a simple demo flow recorded as a video (link placeholder).

You can use this to experiment with GUI automation and to learn how automation can interact with modal dialogs and webpages.

---

## Files
