# 🔐 Password Strength Analyzer

> A simple Python-based cybersecurity tool that analyzes password strength, detects commonly used passwords, provides improvement suggestions, and prevents password reuse using password hashing and SQLite.

---

## 🛡️ About The Project

**Password Strength Analyzer** is a beginner-friendly cybersecurity project developed using Python.

The main purpose of this project is to evaluate whether a password is **Weak, Medium, or Strong** based on different security criteria such as:

- 🔢 Numbers
- 🔠 Uppercase letters
- 🔡 Lowercase letters
- 🔣 Special characters
- 📏 Password length
- 🚫 Common password detection
- 🔁 Password reuse detection

The project also provides suggestions to help users create stronger passwords.

For password reuse detection, the application stores **hashed passwords** rather than storing passwords in plain text.

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Understand basic password security concepts.
2. Learn how password strength can be evaluated.
3. Understand regular expressions in Python.
4. Learn the basics of password hashing.
5. Work with SQLite databases.
6. Understand how password reuse can be detected.
7. Provide users with useful password improvement suggestions.
8. Build a practical cybersecurity-focused Python application.

---

## ✨ Features

### 🔍 1. Password Strength Analysis

The application evaluates the password based on multiple criteria.

It checks:

| Security Criteria | Description |
|---|---|
| 📏 Length | Checks whether the password has enough characters |
| 🔠 Uppercase | Checks for uppercase letters |
| 🔡 Lowercase | Checks for lowercase letters |
| 🔢 Numbers | Checks for numeric characters |
| 🔣 Special Characters | Checks for symbols |
| 🚫 Common Password | Checks whether the password is commonly used |
| 🔁 Password Reuse | Checks whether the password was used previously |

---

### 💪 2. Strength Rating

The password receives one of three ratings:

```text
🔴 WEAK
🟡 MEDIUM
🟢 STRONG