# 🔐 Introductory Ciphers - Encrypt & Decrypt in Python

## 📜 About This Repository
This repository is dedicated to **introductory cryptographic ciphers**, focusing on classical encryption techniques. The goal is to provide easy-to-understand implementations of historical ciphers, allowing users to explore encryption and decryption through interactive Python scripts.

### ✅ **Currently Available Ciphers**
- **Caesar Cipher** - A simple substitution cipher that shifts letters in the alphabet.
  
### 🚀 **Coming Soon**
- **Vigenère Cipher** - A more advanced cipher that uses a repeating key to encrypt text.

---

## 🏛 Caesar Cipher - The Basics
The **Caesar Cipher** is one of the earliest known encryption techniques, used by Julius Caesar to send secure messages. It works by shifting each letter in the plaintext forward by a fixed number (`shift value`) in the alphabet.

For example, with a shift of **3**:  
`HELLO WORLD` → `KHOOR ZRUOG`

If the shift is unknown, we can **brute force decrypt** by trying all possible shifts.

---

## 🖥 How to Use

### 🔹 **Run the Python Script**
The script is designed to be executed directly in the **terminal**. It takes user inputs to either encrypt or decrypt messages.