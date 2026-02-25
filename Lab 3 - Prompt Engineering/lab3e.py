from openai import OpenAI

# Create client
client = OpenAI()

prompt= "List 5 programming languages:\n1."

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
    stop=["4."]

)

print(response.output_text)