import streamlit as st
from openai import OpenAI
import anthropic
client = OpenAI(api_key=st.secrets["open_ai"])

def get_openai_response(user_input):
       print(user_input)
       """
       This function sends the user input to OpenAI's Chat API and returns the model's response.
       """
       try:
           response = client.chat.completions.create(
               model="gpt-4o",  # Specify the model for chat applications
               messages=[
                   {"""role": "system", "content": "You are playfully protecting a secret. My wife is going to guess what her gift is for our 10 year anniversary. Your job is to answer her questions and guide her to the correct answer, but not too quickly.
                    If she asks for a hint, first make her answer a trivia question before you provide the hint.
                    My wife's name is Julie. Here is some context about our 10 years together, feel free to weave it into your responses. 
                    We had a long distance relationship for the beginning of our relationship. I was in China, she was in Pennsylvania.
                    We were engaged on Amelia Island. We were married on a very hot day in Georgia. It was also Bob Dylan's birthday.
                    We have two boys.
                    We are deeply in love.

                    The gift is two tickets to see Meghan Trainor in September. Don't be too easy. Make it kind of hard for her to guess. And try to suggest little games or force her to answer trivia questions sometimes to get a hint.
                    """},
                   {user_input},
               ]
           )
           print(f"response: {response}")
           # Extracting the text from the last response in the chat
           if response.choices:
               print(response)
               return response.choices[0].message['content'].strip()
           else:
               return "No response from the model."
       except Exception as e:
           return f"An error occurred: {str(e)}"
    
def toast(tone):
    with st.spinner("I'd like to propose a toast..."):
        result = anthropic.Anthropic(api_key=st.secrets["claudeAPI"]).messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            temperature=1,
            messages=[
                {"role": "user", "content": f"""My name is Julie. Today is my ten year anniversary. My husband, Wesley and I have had a decade of happy marriage. 
                 Here is some context about our relationship:
                 We had a long distance relationship for the beginning of our relationship. Wesley was in China, I was in Pennsylvania.
                    We were engaged on Amelia Island. We were married on a very hot day in Georgia. It was also Bob Dylan's birthday.
                    We have two boys.
                    We are deeply in love.
                 Propose an anniversary toast adopting the persona of {tone} and tell me what to hope for in my next 10 years with my husband. Don't make it rhyme unless I explicitly ask you to. 
                 Don't explicitly tell me who you are. No need to do so, it will become apparent by the words you include in your toast.
                 Start with the phrase, 'I'd like to propose a toast' and don't make it longer than 3 sentences. Really get into the part and include details
                 from our relationship."""}
            ]
        )
    st.success(f"a toast from {tone}")
    return result.content[0].text


def imageMaker(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"funny realistic photograph of {prompt} proposing a toast",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    return response.data[0].url
