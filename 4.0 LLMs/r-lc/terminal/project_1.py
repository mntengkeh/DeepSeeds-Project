from config import load_google_chat_model
import time

chat_model = load_google_chat_model()
# print(f"Model: {chat_model}")

# terminal header
print("\nPERSONAL TUTOR ASSISTANT")
print("_"*70)

""""creating messages array, which will help AI format chats"""

messages = [
    ("system", "You are a helpful assistant and you play the role of a personal tutor. Be friendly, but strict."),
    ""
]

while True: 
   user_input = input("\n>>>  ")
   if user_input.lower() in ["exit", "quit"]:
     print("\nI had fun talking with you...\n")
     break
   else:
    #  print("\n")
     messages[1] = ("user", f"{user_input}")
     print("\nThinking...")
     for part in chat_model.stream(messages):
       print(f"\n{part.content}", end="", flush=True)
     print("\n")
 