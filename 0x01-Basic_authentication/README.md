# Simple API with Basic Authentication

## Background Context

In this project, you will learn about the authentication process and implement Basic Authentication on a simple API.

In the industry, you should not implement your own Basic authentication system and use a module or framework that does it for you (such as Flask-HTTPAuth in Python-Flask). Here, for learning purposes, we will walk through each step of this mechanism to understand it by doing.

## Resources

Read or watch:

- [REST API Authentication Mechanisms](https://chatgpt.com/c/ef4dba1f-fed3-4b25-97a7-c53dae11e42c#)
- [Base64 in Python](https://chatgpt.com/c/ef4dba1f-fed3-4b25-97a7-c53dae11e42c#)
- [HTTP header Authorization](https://chatgpt.com/c/ef4dba1f-fed3-4b25-97a7-c53dae11e42c#)
- [Flask](https://chatgpt.com/c/ef4dba1f-fed3-4b25-97a7-c53dae11e42c#)
- [Base64 - concept](https://chatgpt.com/c/ef4dba1f-fed3-4b25-97a7-c53dae11e42c#)

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## Requirements

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)

## Project Structure

```
simple_api/
│
├── app.py                  # Main application file
├── auth.py                 # Authentication implementation
├── README.md               # Project documentation
└── requirements.txt        # List of dependencies
```

## Usage

1. Run the application:
    ```bash
    ./app.py
    ```
2. The API will be available at `http://localhost:5000`.

## Documentation

### Module: `auth`

This module handles the Basic Authentication.

### Class: `BasicAuth`

This class provides methods to authenticate users using Basic Authentication.

### Function: `encode_base64`

Encodes a string in Base64.
