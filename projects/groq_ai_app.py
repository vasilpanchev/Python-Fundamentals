import groq
import customtkinter as ctk

# Initialize Groq API client
client = groq.Client(api_key="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")


# Function to get AI response from Groq API
def get_ai_response(user_input_):
    try:
        response_ = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": user_input_}]
        )
        return response_.choices[0].message.content  # Corrected access
    except Exception as e:
        return f"Error: {e}"


# Main loop for user input
if __name__ == "__main__":
    print("Welcome to your AI chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\nGoodbye! 👋")
            break
        response = get_ai_response(user_input)
        print("AI:", response)
