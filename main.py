import openai

# Set your OpenAI API key here
openai.api_key = "sk-YVwTY8eVVHO0d2uzzUppTNKNqsym48qHn0oSTElogVT3BlbkFJTfUHaiCrSLbwSqMBEYlpijlnkAbVM1k83v7lHDCEsA"

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, something went wrong."

if __name__ == "__main__":
    print("Welcome to OpenAI Chatbot! Type 'quit', 'exit', or 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
