from typing import List

import customtkinter
import groq

from key.groq_api_key import API_KEY


class AIModel():
    def __init__(self):
        self.client = groq.Client(api_key=API_KEY)

    # Initialize Groq API client
    def get_ai_response(self, user_input_, model_input_):
        '''Get AI response from Groq API'''
        try:
            response_ = self.client.chat.completions.create(
                model=model_input_,
                messages=[{"role": "user", "content": user_input_}]
            )
            return response_.choices[0].message.content  # Corrected access
        except Exception as e:
            return f"Error: {e}"


class ConversationsButtonsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.past_conversations = []

        for i, value in enumerate(self.values):
            button = customtkinter.CTkButton(self, text=value, command=lambda v=value: self.open_page(v))
            button.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.past_conversations.append(button)

    def open_page(self, page):
        print(f"Opening conversation: {page}")  # Example functionality





class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("MultAIple")
        self.geometry("600x300")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
        self.past_conversations_frame = ConversationsButtonsFrame(self, title="Past Conversations", values=values)
        self.past_conversations_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")


# Main loop for user input
if __name__ == "__main__":
    app = App()
    app.mainloop()
    # print("Welcome to your AI chatbot! Type 'exit' to quit.")
    # while True:
    #     user_input = input("\nYou: ")
    #     if user_input.lower() in ["exit", "quit", "see you later"]:
    #         print("\nGoodbye! 👋")
    #         break
    #     response = get_ai_response(user_input)
    #     print("AI:", response)
