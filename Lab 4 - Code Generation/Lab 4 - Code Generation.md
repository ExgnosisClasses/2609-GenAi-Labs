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


## Refinement 1

Add a clear statement of the programming problem

```Python


```

