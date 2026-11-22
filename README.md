<<<<<<< HEAD
# Password-Cracking-Credential-attack-suite
A Python-based cybersecurity toolkit for password strength analysis, dictionary generation, hash generation and offline attack simulation.
=======
# Password Cracking & Credential Attack Suite

## 1. Project Overview

The Password Cracking & Credential Attack Suite is a Python-based cybersecurity toolkit designed for password policy testing and credential security assessment.

It provides educational demonstrations of password strength analysis, dictionary generation, hash processing, and offline credential attack simulation using synthetic test data.

## 2. Objectives

- Generate custom password dictionaries.
- Generate and examine password hashes.
- Simulate dictionary-based password testing.
- Analyze password strength using complexity and estimated entropy.
- Generate security audit reports.
- Understand password security risks and preventive measures.

## 3. Features

### Password Strength Analyzer
Evaluates passwords based on length, uppercase letters, lowercase letters, digits, and special characters.

### Dictionary Generator
Generates a sample dictionary containing predefined test words and variations.

### Hash Generator
Generates SHA-256 hashes and provides basic hash-format identification.

### Attack Simulator
Demonstrates offline dictionary-based password testing using synthetic sample data.

### Security Audit Report
Generates a downloadable JSON report containing audit results.

## 4. Technologies Used

- Programming Language: Python
- Framework: Streamlit
- Libraries: hashlib, pandas, matplotlib
- Development Environment: Kali Linux
- Code Editor: GNU Nano

## 5. Project Structure

```text
Password-Cracking-Credential-Attack-Suite/
│
├── app.py
├── README.md
├── modules/
│   ├── __init__.py
│   ├── password_analyzer.py
│   ├── dictionary_generator.py
│   ├── hash_generator.py
│   └── attack_simulator.py
│
├── reports/
├── sample_data/
├── screenshots/
└── venv/
>>>>>>> 6fe71fb (Initial commit - Password Cracking and Credential Attack Suite)
