# 🔐 Caesar Cipher - Encryption & Brute Force Decryption

## 📜 History of the Caesar Cipher
The **Caesar Cipher** is one of the oldest known encryption techniques, dating back to around 45 B.C. Julius Caesar used it to securely communicate with his generals by shifting each letter in a message by a fixed number of positions in the alphabet. While simple by today’s cryptographic standards, it laid the foundation for modern techniques.

## 🔍 How It Works
The Caesar Cipher operates by shifting each letter in the plaintext by a given number (`shift value`). For example, with a shift of **3**, `"HELLO"` becomes `"KHOOR"`. 

Decryption is simply shifting in the opposite direction. If the shift is unknown, **brute force** can be used to try all possible shifts (0-25) to find the original text.

## 🛠 Features
✅ **Encrypt** a message using a custom shift value.  
✅ **Decrypt** a message using brute force, displaying all possible shifts.