### Building an Authentication System with Flask and SQLAlchemy

#### Overview

In this project, you'll build a simple authentication system using Flask and SQLAlchemy. While it's recommended to use established modules like Flask-User for production, this exercise is intended for learning purposes. You'll gain hands-on experience with API routes, cookies, request data, and HTTP status codes.

#### Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Requests Module Documentation](https://docs.python-requests.org/en/master/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

#### Learning Objectives

By the end of this project, you should be able to:

- Declare API routes in a Flask app
- Get and set cookies
- Retrieve request form data
- Return various HTTP status codes

#### Requirements

- **Editors**: `vi`, `vim`, `emacs`
- **Interpreter/Compiler**: Ubuntu 18.04 LTS with Python 3.7
- **File Standards**:
  - Files end with a new line
  - First line: `#!/usr/bin/env python3`
  - Code style: `pycodestyle` version 2.5
  - SQLAlchemy version 1.3.x
  - Executable files
  - Length tested using `wc`
- **Documentation**:
  - Modules: `python3 -c 'print(__import__("my_module").__doc__)'`
  - Classes: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
  - Functions: `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
  - Use full sentences to explain the purpose of modules, classes, and methods

#### Setup

To begin, ensure you have `bcrypt` installed:

```sh
pip3 install bcrypt
```
