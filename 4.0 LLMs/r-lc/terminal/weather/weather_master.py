from config import load_google_llm, weatherContext
from langchain_core.prompts import ChatPromptTemplate
from pprint import pprint

llm = load_google_llm()


messages = [
    ("system", "you are a weather expert providing answers based on {context}"
    "I need you to advice me on what to wear, what to eat, and thow to prepare the day"
    "based on the context given. Only answer questions on weather"
    "Please your response should be precise and never more than 100 tokens")
]
prompt_template = ChatPromptTemplate.from_messages(messages)


while True:
    user_input = input("\nEnter your city: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Exiting chat...")
        break
    messages.append(("human", user_input))
    weather = weatherContext(user_input)
    promt = prompt_template.format_messages(context=weather)
    print("\nLoading...\n")
    response = llm.invoke(promt)
    messages.append(("ai", response))
    pprint(response)