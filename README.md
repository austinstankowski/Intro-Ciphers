# 🔐 Introductory Ciphers - Encrypt & Decrypt in Python

## 📜 About This Repository
This repository provides implementations of **introductory cryptographic ciphers**, offering a beginner-friendly way to explore encryption. These Python scripts allow users to **encrypt and decrypt** messages directly from the terminal, supporting both simple substitution and polyalphabetic ciphers.

### ✅ **Currently Available Ciphers**
- **Caesar Cipher** - A basic shift-based substitution cipher.
- **Vigenère Cipher** - A more advanced cipher using a keyword for encryption.

---

## 🏛 Cipher Overview

### 🔹 **Caesar Cipher**
The **Caesar Cipher** is one of the earliest known encryption techniques, famously used by Julius Caesar to secure military communications. It works by shifting each letter in the plaintext forward by a fixed number (**shift value**).  

For example, with a shift of **3**:  
`HELLO WORLD` → `KHOOR ZRUOG`

If the shift is unknown, brute force can be used to try all possible shifts.

### 🔹 **Vigenère Cipher**
The **Vigenère Cipher** improves upon the Caesar Cipher by using a repeating **keyword** to determine different shift values for each letter. This makes it more resistant to brute-force attacks.

For example, using the key **"KEY"**:  
Plaintext: `HELLO WORLD`  
Key: `KEYKEYKEYKE`  
Ciphertext: `RIJVS UYVJN`

The shift for each letter is based on the corresponding letter in the keyword, making the pattern more complex than a simple Caesar shift.

---

## 📜 History & Background
### **Caesar Cipher**
- Used by Julius Caesar for secure military communication.
- Vulnerable to frequency analysis and brute-force attacks (only 25 possible shifts).

### **Vigenère Cipher**
- First described in the 16th century by Giovan Battista Bellaso, but often attributed to Blaise de Vigenère.
- Considered unbreakable for centuries until Charles Babbage and Friedrich Kasiski developed techniques to crack it.
- More secure than the Caesar Cipher but still vulnerable to cryptanalysis with long ciphertexts.

---

## 🔒 Constraints & Limitations
- Only supports encryption of **alphabetic characters (A-Z, a-z)**. Special characters and numbers remain unchanged.
- The **Caesar Cipher** is vulnerable to brute-force attacks due to its small keyspace.
- The **Vigenère Cipher** is stronger but can be broken with frequency analysis if the key is short and the text is long.

---


### **Install Requirements**
No external libraries are required. This script runs with **Python 3.x**.

---

## 📌 Future Plans
✅ Add support for additional ciphers like **Affine Cipher** and **Rail Fence Cipher**.  
✅ Implement **automatic key length detection** for Vigenère Cipher decryption.  
✅ Create a **GUI version** for easier usability.  

Stay tuned for updates! ⭐ If you find this useful, consider **starring** the repository!