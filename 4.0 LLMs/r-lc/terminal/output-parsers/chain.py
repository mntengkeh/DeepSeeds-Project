from typing import List
from config import load_google_llm
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# one runnable
# why -> it receive a prompt and send out output

llm = load_google_llm()

chat_template = ChatPromptTemplate.from_messages([
    ("system", "you are a football analyst"),
    ("user", "Consider {player} playing for {club}. Provide a short and straight forward answer to {question}")
])


player_input = input("Enter your favorite player: ")
club_input = input(f"Enter {player_input.title()}'s club: ")
question_input = input(f"Ask a question about {player_input}\n\t>>>  ")

parser = StrOutputParser()

chain = chat_template | llm | parser

output = chain.invoke({
    "question": question_input,
    "player": player_input,
    "club": club_input
})

print(f"\n{output}\n")