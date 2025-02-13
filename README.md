# 🔐 Introductory Ciphers - Encrypt & Decrypt in Python

## 📜 About This Repository
This repository provides implementations of **introductory cryptographic ciphers**, offering a beginner-friendly way to explore encryption. These Python scripts allow users to **encrypt and decrypt** messages directly from the terminal, supporting both simple substitution and polyalphabetic ciphers.

### ✅ **Currently Available Ciphers**
- **Caesar Cipher** - A basic shift-based substitution cipher.
- **Vigenère Cipher** - A more advanced cipher using an alphabetic keyword for encryption.
- **Gronsfeld Cipher** - A variant of the Vigenère Cipher that uses a numeric keyword for encryption.

### ❗️ **Ciphers Coming Soon**
- **TBD**

---

## 🏛 Cipher Overview

### 🔹 **Caesar Cipher**
The **Caesar Cipher** is one of the earliest known encryption techniques, famously used by Julius Caesar to secure military communications. It works by shifting each letter in the plaintext forward by a fixed number (**shift value**).  

For example, with a shift of **3**:  
`HELLO WORLD` → `KHOOR ZRUOG`

If the shift is unknown, brute force can be used to try all possible shifts.

### 🔹 **Vigenère Cipher**
The **Vigenère Cipher** improves upon the Caesar Cipher by using a repeating **alphabetic keyword** to determine different shift values for each letter. This makes it more resistant to brute-force attacks.

For example, using the key **"KEY"**:  
Plaintext: `HELLO WORLD`  
Key: `KEYKEYKEYK`  
Ciphertext: `RIJVS UYVJN`

The shift for each letter is based on the corresponding letter in the keyword, making the pattern more complex than a simple Caesar shift.

### 🔹 **Gronsfeld Cipher**
The **Gronsfeld Cipher** is a variant of the **Vigenère Cipher**, but instead of using an alphabetic keyword, it uses a **numeric key** for shifting letters. This makes it similar in structure but slightly more restrictive, as it only allows numbers in the key.

For example, using the key **"132"**:  
Plaintext: `HELLO WORLD`  
Key: `1321321321`  
Ciphertext: `IHNMR YPUNE`

The shift for each letter is based on the corresponding number in the keyword.

---

## 📜 History & Background
### **Caesar Cipher**
- Used by Julius Caesar for secure military communication.
- Vulnerable to frequency analysis and brute-force attacks (only 25 possible shifts).

### **Vigenère Cipher**
- First described in the 16th century by Giovan Battista Bellaso, but often attributed to Blaise de Vigenère.
- Considered unbreakable for centuries until Charles Babbage and Friedrich Kasiski developed techniques to crack it.
- More secure than the Caesar Cipher but still vulnerable to cryptanalysis with long ciphertexts.

### **Gronsfeld Cipher**
- First introduced by Johann Franz von Gronsfeld, a 17th-century Bavarian diplomat and military leader.
- A simplified version of the Vigenère Cipher, using digits (0-9) instead of letters as a key.
- Used in historical European diplomatic communications due to its ease of use.
- While stronger than the Caesar Cipher, it is still vulnerable to frequency analysis if the key length is short.

---

## 🔒 Constraints & Limitations
- Only supports encryption of **alphabetic characters (A-Z, a-z)**. Special characters and numbers remain unchanged.
- The **Caesar Cipher** is vulnerable to brute-force attacks due to its small keyspace.
- The **Vigenère Cipher** and **Gronsfeld Cipher** is stronger but can be broken with frequency analysis if the key is short and the text is long.

---


### **Install Requirements**
No external libraries are required. This script runs with **Python 3.x**.

---

## 📌 Future Plans
✅ Research & Implement Other Introductory Ciphers
✅ Create a **GUI version** for easier usability.  

Stay tuned for updates! ⭐ If you find this useful, consider **starring** the repository!