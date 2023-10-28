# pkd-chikku-cli


# Chikku - Python Code Assistant

## Introduction

Chikku is a Python code assistant that helps you with various coding tasks and provides assistance with Python code snippets. This document provides an overview of some of the available commands and how to use them.

## Commands

### Command 1: Fix Code

This command is used to fix code issues. You can provide a code snippet and specify what you want to fix. For example:

```bash
python3 app.py --fix "without using urllib.request rewrite the code" --filename example.txt
```

This command will attempt to fix the code in the "example.txt" file by rewriting it without using `urllib.request`.

### Command 2: Prompt for Code

Use this command to prompt Chikku to provide Python code that accomplishes a specific task. For example, to request code for downloading a file from a URL:

```bash
python3 app.py prompt "write python code that downloads a file from a URL" --filename example.txt
```

Chikku will generate Python code that downloads a file from a URL and save it in the "example.txt" file.

### Output

When running the Chikku application with Python, you will receive output based on the commands you provided. The output will depend on the specific task you requested or the code you asked to be fixed.

## Conclusion

Chikku is a valuable Python code assistant that can help you write code, fix issues, and automate coding tasks. Explore the various commands to make your coding experience more efficient and productive.
