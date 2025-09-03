from config import load_google_llm, load_google_chat_model
import time

llm = load_google_llm()
chat_llm = load_google_chat_model()
print("\nAsk AI anything...!")
while True:
    prompt = input("\n>>>  ")
    if prompt == "exit":
        print(f"\n{chat_llm.invoke("short goodbye message expressing how you enjoyed the ending session. Respond with a maximum of 6 words").content}\n\n")
        break
    else:
        print("\nThinking...\n")
        print(f"\n{chat_llm.invoke(f"{prompt}.  Respond with a maximum of 30 words.").content}\n")
