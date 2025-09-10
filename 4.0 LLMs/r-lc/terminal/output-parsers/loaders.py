from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.prompts import ChatPromptTemplate
from config import load_google_chat_model

loader = PyPDFLoader("./data/ai.pdf")
text_loader = TextLoader("./data/ai.txt")
load_data = text_loader.load()

llm = load_google_chat_model()

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "only answer questions from or directly related to {context}. Your responses should be short and straight to the point! If you get asked a question out of this context, decline to answer in a user friendly manner."),
    ("user", "{question}")
])

chain = prompt_template | llm

while True:
    question = input("Ask a question related to genai:\n\t\n>>>  ")
    if question == "exit":
        print("Goodebye!")
        break        

    else:
        print("\nThinking...\n")
        output = chain.invoke({
            "context": load_data,
            "question": question
        })
        print(output.content)
