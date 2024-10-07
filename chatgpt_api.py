import openai

# Set your OpenAI API key here
openai.api_key = 'your-api-key'

def chat_with_gpt(prompt, model="gpt-4", temperature=0.7, max_tokens=150):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Example usage
    user_input = input("Enter your prompt: ")
    response = chat_with_gpt(user_input)
    print("GPT-4 Response:")
    print(response)
