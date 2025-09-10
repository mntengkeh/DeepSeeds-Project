from langchain_community.document_loaders import WebBaseLoader
import streamlit as st


urls_data = [
    "https://www.linkedin.com/in/mntengkeh/"
]

loader = WebBaseLoader(urls_data)
docs = loader.load()

print(docs)

# for page in docs:
#     print(f"SCRAPE CONTENT for {page.metadata} IS: ", page.page_content[:300],  "\n\n")
#     # st.write(page.page_content[:300]    # st.write(page.page_content[:300]))