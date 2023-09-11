# Define ANSI escape codes for color formatting
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
GREEN = '\033[92m'
ENDC = '\033[0m'

# Header box
print(f"{BLUE}***********************************************{ENDC}")
print(f"{GREEN}*              Bob the Assistant              *{ENDC}")
print(f"{BLUE}***********************************************{ENDC}")
print("\n\n")  # Add two empty lines

from langchain.llms import CTransformers
from langchain.memory import ConversationBufferMemory

# Initialize chat history memory
memory = ConversationBufferMemory(memory_key="chat_history")

# Load the model
def load_model():
    llm = CTransformers(
        model="path\to\the\model\",  # Replace with your local path
        model_type="llama",
        max_new_tokens=1026,
        temperature=0.7,
        repetition_penalty=1.5
    )
    return llm

# Function to get the bot's response
def llm_function(user_input):
    # Add user's message to memory
    memory.chat_memory.add_user_message(user_input)
    
    # Get chat history from memory
    chat_history = memory.load_memory_variables({})["chat_history"]
    
    # Generate the prompt using the system_prompt method
    system_prompt = f"### System:\nYou are an AI assistant named Bob. Help as much as you can.\n\n{chat_history}"
    prompt = f"{system_prompt}### User: {user_input}\n\n### Assistant:\n"
    
    llm = load_model()
    llm_response = llm(prompt)
    
    # Add Bob's response to memory
    memory.chat_memory.add_ai_message(llm_response)
    
    return llm_response

# Continuous user input loop
while True:
    message = input(f"{RED}You:{ENDC} ")  # Red color for "You: "
    if message.lower() == 'bye':
        break
    response = llm_function(message)
    print(f"{YELLOW}Bob:{ENDC} {response}")  # Yellow color for "Bob: "
    print()  # Add an empty line after each message
