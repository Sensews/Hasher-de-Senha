# Python Password Strength Checker And Hasher

Welcome to the **Python Password Strength Checker And Hasher** project! This repository contains a Python application developed as part of a cybersecurity course at Pontifícia Universidade Católica do Paraná (PUCPR). The application is designed to evaluate the strength of passwords and securely hash them using industry-standard cryptographic algorithms.

## Features

- **Password Strength Evaluation**: Analyzes passwords based on various criteria such as length, use of uppercase and lowercase letters, digits, and special characters.
- **Hashing**: Securely hashes passwords using algorithms like SHA-256 and bcrypt, ensuring they are stored safely.
- **User Management**: Stores usernames and their corresponding hashed passwords in a text file (`usuarios.txt`).

## Installation

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/Sensews/Python-Password-Strength-Checker-With-Hasher.git
cd Python-Password-Strength-Checker-With-Hasher
```

Ensure you have Python 3.6 or higher installed. There are no additional dependencies required for this project.

## Usage

To evaluate the strength of a password, hash it, and store the user information, run the following command:

```bash
python Main.py
```

Follow the prompts to:
1. Enter your username.
2. Enter your password.

The application will provide feedback on the password's strength and store the username and hashed password in `usuarios.txt`.

## File Descriptions

- `Main.py`: The main script that runs the password strength checker and hasher.
- `usuarios.txt`: A text file that stores usernames along with their hashed passwords.

## Contributing

We welcome contributions from the community. If you'd like to contribute, please fork the repository and submit a pull request with your changes. Ensure your code follows our coding standards and include appropriate tests.

## Acknowledgements

This project was developed as part of the cybersecurity curriculum at PUCPR. We thank our professors and peers for their support and guidance.

---

Feel free to reach out if you have any questions or suggestions. Happy coding!

---
*This README was created for a course project at Pontifícia Universidade Católica do Paraná (PUCPR).*
