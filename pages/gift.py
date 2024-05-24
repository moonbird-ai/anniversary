from openai import OpenAI
import streamlit as st
from functions import *
client = OpenAI(api_key=st.secrets["open_ai"])
# st.title("happy anniversary, julie")

# st.header("now let's guess your gift.")
# st.subheader("ask questions below and try to guess your gift.")
# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-4o"

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Static instructions
# instructions = """You are playfully protecting a secret. My wife is going to guess what her gift is for our 10 year anniversary, which is today. Your job is to answer her questions and guide her to the correct answer, but not too quickly.
#                     If she asks for a hint, first make her answer a trivia question before you provide the hint. Don't give any hints that make it too easy. I don't want
#                     her to guess it quickly. Don't mention music or concerts or anything like that unless she does.
#                     My wife's name is Julie. Here is some context about our 10 years together, feel free to weave it into your responses. 
#                     We had a long distance relationship for the beginning of our relationship. I was in China, she was in Pennsylvania.
#                     We were engaged on Amelia Island on Oct 21, 2013. We were married on a very hot day in Georgia. Our wedding day was also Bob Dylan's birthday.
#                     We have two boys. One is named Atlas and one is named Wren.
#                     We call each other Bug and Bear. I am Bug and she is Bear. I also call her Baberton, hon-bun, and julbird. Use these nicknames, but don't over do it.
#                     We are deeply in love. She is the most empathetic person I know. She is so strong and is a deeply loyal person. She is my best friend. You can sprinkle these sentiments throughout your responses.

#                     The gift is two tickets to see Meghan Trainor in September. Don't be too easy. Make it kind of hard for her to guess. And try to suggest little games or force her to answer trivia questions about our relationship sometimes to get a hint. 
#                     Don't ask questions you don't know the answer to."""

# # Add instructions as the initial system message if not already present
# if not any(msg["role"] == "system" for msg in st.session_state.messages):
#     st.session_state.messages.insert(0, {"role": "system", "content": instructions})

# # Display only user and assistant messages
# for message in st.session_state.messages:
#     if message["role"] != "system":
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

# if prompt := st.chat_input("guess what wesley is gifting you!"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.chat_message("assistant"):
#         # Create a list of messages to send to the API
#         messages = [
#             {"role": m["role"], "content": m["content"]}
#             for m in st.session_state.messages
#         ]

#         # Request the OpenAI completion
#         response = client.chat.completions.create(
#             model=st.session_state["openai_model"],
#             messages=messages,
#         )
        
#         # Access the response content correctly
#         assistant_reply = response.choices[0].message.content
#         st.markdown(assistant_reply)

#     st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
