import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def create_coding_assistant():
    # Initialize the model
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    # Start the conversation with a system prompt
    chat = model.start_chat(history=[
        {
            "role": "user",
            "parts": ["You are a helpful coding assistant. Provide clear, concise code examples, explain programming concepts, help debug issues, and suggest best practices."]
        },
        {
            "role": "model",
            "parts": ["I'll help you with coding tasks, provide examples, explain concepts, assist with debugging, and suggest best practices. What would you like help with today?"]
        }
    ])
    
    print("🤖 Coding Assistant Bot - Your AI programming partner")
    print("Type '###' to exit the conversation")
    
    while True:
        # Get user input
        user_input = input("\nYou: ")
        
        # Check exit condition
        if user_input == "###":
            print("Goodbye! Happy coding!")
            break
        
        try:
            # Get response from Gemini
            response = chat.send_message(user_input)
            
            # Display the response
            print(f"\nAssistant: {response.text}")
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            
if __name__ == "__main__":
    create_coding_assistant()
