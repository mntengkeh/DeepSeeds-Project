from langchain_core.prompts import PromptTemplate
from config import load_google_llm
import streamlit as st

llm = load_google_llm()


if "prompt" not in st.session_state:
    st.session_state["prompt"] = ""
    st.session_state["extracted"] = ""
    st.session_state["messages"] = []


prompt_template = PromptTemplate.from_template(
    "Given the book title {title} and author {author} summarize it in a clear and concise manner"
)


def get_info(prompt):
    st.session_state["extracted"] = llm.invoke(f"I need you to extract the book title and author from {prompt}. Your output should be formatted thus: title:<title>|author:<author>")
    st.session_state["messages"].append({"user":prompt})

def main():
    st.chat_input(placeholder="Book Title and Author", key="prompt", on_submit=lambda: get_info(st.session_state["prompt"]))
    
    with st.container(height=550, border=True):
        with st.chat_message("system"):
            st.write("Enter a book title and author, and i will generate the book summary for you!")
        with st.container(height=435, border=False):
            extracted: str = st.session_state["extracted"]
            if extracted:    
                title = extracted[6:extracted.index("|")]
                author = extracted[extracted.index("|")+8:]
                t_prompt = prompt_template.format(title=title, author=author)
                summary = llm.invoke(t_prompt)
                st.session_state["messages"][len(st.session_state["messages"])-1]["ai"] = summary
                
                if st.session_state.messages:
                    for message in st.session_state["messages"]:
                        with st.chat_message("user"):
                            st.write(message["user"])
                        with st.chat_message("ai"):
                            st.write(message["ai"])
                        

if __name__ == "__main__":
    main()