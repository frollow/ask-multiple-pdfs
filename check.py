import openai

# Замените 'your-api-key' на ваш ключ API
openai.api_key = "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"

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Translate the following English text to French: '{}'",
    max_tokens=60,
)

print(response.choices[0].text.strip())
