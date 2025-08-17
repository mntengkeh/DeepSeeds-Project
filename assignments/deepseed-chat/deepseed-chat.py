import streamlit as st
import google.generativeai as genai
from auth import GEMINI_API_KEY

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.responses = []
    st.session_state.sent = ''

# if len(st.session_state.messages) > 0:
#     st.session_state.response = "🤖 🌱 Based on your message, I can provide some insights on this. 💡"


genai.configure(api_key=GEMINI_API_KEY)
model=genai.GenerativeModel("gemini-2.5-flash")


st.markdown("""
    <style>
        .block-container {
            padding-top: 3rem !important;
            padding-bottom: 1rem !important;
            padding-left: 4rem !important;
            padding-right: 4rem !important;
            max-width: 100% !important;
        }

        .stSidebar hr, .stSidebar h2, .stSidebar h3 {
            margin: 0.2rem 0 !important;
        }

        .nb table, .nb th, .nb td {
            border: none !important;
        }

        .cc {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .cc p:nth-child(odd) {
            align-self: flex-end;
            background-color: #071e26;
            border-radius: 8px;
            width: 60%;
            max-width: 60%;
            padding: 8px 12px;
            margin: 0;
            font-size: 1rem;
        }

        .cc p:nth-child(even) {
            align-self: flex-start;
            margin: 0;
            width: 60%;
            max-width: 60%;
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title(":seedling: DEEPSEED")
    st.write("One seed at a time")
    "---"
    st.subheader(":bar_chart: Session Stats")
    st.markdown(f"""
        <div class="nb" style="width:100%">
            <table style="width:100%;">
                <tr>
                    <th>Messages</th>
                    <th>Total</th>
                </tr>
                <tr>
                    <td>{len(st.session_state.messages)}</td>
                    <td>{len(st.session_state.messages) * 2}</td>
                </tr>
            </table>
        </div>
    """, unsafe_allow_html=True)
    "---"
    st.subheader(":rocket: Quick Actions")
    st.button(":bulb: Tell me a joke", use_container_width=True)
    st.button(":bulb: Explain AI", use_container_width=True)
    st.button(":bulb: Help brainstorm", use_container_width=True)
    st.button(":bulb: Writing tips", use_container_width=True)
    st.button(":bulb: Book recommendations", use_container_width=True)
    "---"
    st.subheader(":gear:  Controls")

st.subheader(":speech_balloon: Chat with DEEPSEED")

def clear_input():
    st.session_state['sent'] = ''

def send_message(message):
    clear_input()
    if message:
        st.session_state.messages.append(message)
        response = model.generate_content(f"{message}. Your response should be fairly short and straight to the point, but very sufficient for good user experience")
        st.session_state.responses.append(response.text)
    message=''

with st.container(height=260, border=True):
    for i  in range(len(st.session_state.messages)):
        st.markdown(f"""
            <div class="cc">
                <p>{st.session_state.messages[i]}</p>
                <p>{st.session_state.responses[i]}</p>
            </div>
        """, unsafe_allow_html=True)

"---"
with st.container(height=100, border=True, horizontal=True, horizontal_alignment="distribute"):
    message = st.text_input("Message DEEPSEED", placeholder="Ask deepsiid anything...!", key='sent')
    st.button("Send :rocket:", on_click=send_message, args=(message,))
    
            

st.write(f":speech_balloon: {len(st.session_state.messages)} messages in this conversation Session")
