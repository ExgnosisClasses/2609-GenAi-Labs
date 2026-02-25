# Lab 4 - Code Generation

The focus of this lab is to investigate prompting as technical specification writing.

In this lab, you will
- Understand how vague prompts produce weak code
- Learn to write a structured engineering specification
- Include error handling requirements
- Include secure coding standards
- Reference PEP and Python standards
- Generate a high-quality Flask "Hello World" app

You can continue to use the same conda environment you used in lab 3/

## Part 1: Unstructured

Just like in the previous lab, run the following scrip `lab4a.py` in the conda console

```python

from openai import OpenAI

# Create client
client = OpenAI()

prompt="Write a simple Python Flask hello world application."
# Simple prompt
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)

```
The model cannot implement requirements you did not specify

Look at the output and determine
- Does it specify Python version?
- Does it include error handling?
- Does it mention security?
- Does it follow PEP standards?
- Does it pin dependencies?
- Does it include input validation?


## Part 2: Clear Statement of the Programming Problem

Add a clear statement of the programming problem

```Python
from openai import OpenAI

# Create client
client = OpenAI()

prompt="""Create a minimal but production-quality Python 3.11 Flask web application
        that exposes a single HTTP GET endpoint at the root path ("/")
        and returns the text "Hello, World!"."""

# Simple prompt
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)

```

## Part 3: Error Handling Requirements

Now we add in the explicit error handling requirements

```Python

from openai import OpenAI

# Create client
client = OpenAI()

prompt="""Create a minimal but production-quality Python 3.11 Flask web application
        that exposes a single HTTP GET endpoint at the root path ("/")
        and returns the text "Hello, World!".

        The application must:

        - Return HTTP 405 for unsupported HTTP methods.
        - Return HTTP 404 for unknown routes.
        - Include a global error handler for unhandled exceptions.
        - Avoid exposing stack traces to the client.
        - Log errors using Python's logging module.

        """

# Simple prompt
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)
```

## Part 4: Secure Coding Requirements

Now we add into the specification the secure coding requirements.