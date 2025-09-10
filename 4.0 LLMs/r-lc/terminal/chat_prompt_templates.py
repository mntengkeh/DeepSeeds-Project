from langchain_core.prompts import ChatPromptTemplate
from config import load_google_chat_model

chat_model = load_google_chat_model()

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "you are an {expert} in {domain}, please break down any questions the user is going to ask you i na clear and conncise manner with real world analogies)"),
    ("user", "please {expert} help me with my questions"),
    ("ai", "sure {name}, i can do just that"),
    ("user", "{user_input}")
])

prompt = chat_prompt.format_messages(
    expert="Gen Ai Engineer",
    domain="Artificial Intelligence",
    name="Tasha",
    user_input="Please explain Transformers in GenAI to me as though i was 5 years old, but in not more than 300 words"
)


print("Thinking...")
response = chat_model.invoke(prompt)

print(f"\n{response.content}\n")