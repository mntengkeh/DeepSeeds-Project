def environmental_variables():
    import os
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def load_google_llm():
    from langchain_google_genai import GoogleGenerativeAI
    environmental_variables()
    google_llm = GoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.6
    )
    return google_llm

def load_google_chat_model():
    from langchain_google_genai import ChatGoogleGenerativeAI
    environmental_variables()
    google_chat_model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7
    )
    return google_chat_model