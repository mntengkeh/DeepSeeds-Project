from config import load_google_llm
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate

llm = load_google_llm()

parser = StrOutputParser()
j_parse = JsonOutputParser()

prompt_temp = PromptTemplate.from_template("""
    Give me information about football team {team}. Format the output as 
                                           
    {{
        "number_of_players": str,
        "team_captain": str,
        "key_player": str,
        "top_5_players": list(str)
    }}
""")

team = input("Team: ")
prompt = prompt_temp.format(team=team)

info = llm.invoke(prompt)

formatted_out = j_parse.parse(info)

print(formatted_out)