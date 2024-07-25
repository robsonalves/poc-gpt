
import openai

# Set your OpenAI API key
openai.api_key = 'sk-****'

    # Make a request to the OpenAI API
response = openai.Completion.create(
    model="text-davinci-003",  # Use the correct model name
    prompt="Hello, how are you?",
    max_tokens=50
)
# Print the response
print(response.choices[0].text.strip())

