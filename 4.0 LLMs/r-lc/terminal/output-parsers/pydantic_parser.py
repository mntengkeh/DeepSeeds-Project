from typing import List
from config import load_google_llm
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate

llm = load_google_llm()

print("LLM loaded!!")

# force llm to give output in a specific format

class Person(BaseModel):
    name: str = Field(description="full names here")
    age: int = Field(description="age in years")
    description: str = Field(description="a short description about the person")
    albums: List[str] = Field(description="a list of album names")


parser = PydanticOutputParser(pydantic_object=Person)
prompt_template = PromptTemplate.from_template(
    """Based on the nickname of your favorite artist: {artist}, give the real 
    name and the age inthe followiing json format: {{
        "name": string,
        "age": int,
        "description": string,
        "albums": Array of strings
    }}"""
)


fav_artist = input("Please enter the nickname of your favorite artist\n\t\t>>>  ")

prompt = prompt_template.format(artist=fav_artist)

response=llm.invoke(prompt)
print("Response: ", response)
try:
    parsed_result = parser.parse(response)
    print("THE PARSED RESULT IS: ", parsed_result)
    print("THE PARSED RESULT Name IS: ", parsed_result.name)
except Exception as e:
    print("Parsing failed! Raw response: ", response)
    print("Error: ", e)