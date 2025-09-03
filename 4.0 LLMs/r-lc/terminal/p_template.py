from langchain_core.prompts import PromptTemplate
from config import load_google_llm

llm = load_google_llm()

prompt_template = PromptTemplate.from_template(
    "Given the book title {title} and author {author} summarize it in a clear and concise manner"
)

# acceting the input
print("\nWELCOME TO MY LEARNING APP")
print("_"*70)

book_title = input("\nEnter book title: ")
book_author = input("\nAuthor for the book above: ")

prompt = prompt_template.format(title=book_title, author=book_author)

print("Thinking...")
print(f"\n{llm.stream(prompt)}")