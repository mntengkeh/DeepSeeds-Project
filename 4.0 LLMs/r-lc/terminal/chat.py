from config import load_google_chat_model

chat_model = load_google_chat_model()
# print(f"My chat model is: {chat_model}")

messages = [
    ("system","you are a helpful assistant that translates English to French."),
    ("user", "translate the following sentence to French. I love programming languae for llms")
]

# response = chat_model.invoke(messages)
# print(f"\nResponse: {response.content}\n")

# stream responses
for part in chat_model.stream("Yo! Tell me the basics of basketball"):
    print(part.content, end="", flush=True)
print("\n")