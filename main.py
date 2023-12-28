from openai import OpenAI
import streamlit as st

image_path = "fortune_teller.webp"


def chat_with_gpt(prompt):
    client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key = st.secrets['OPEN_AI_KEY']
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f'''Act as an expert on Taylor Swift song lyrics.  I’m going to pass you a problem and situation, you will respond with only responding with a return prompt and song quote in the format “In the words of Ta-ta the great: <song-quote here>. For example:
User:  my boyfriend just broke up with me
Bot: In the words of Ta-ta the great: “Shake it off” (put song name and year song was released).  Act as the fortune teller described abover for {prompt}''',
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

# Streamlit app starts here
st.title('Ta-Ta the Great Will Solve All Your Problems')

# Display the image at the top of the app
st.image(image_path, width=300)  # Adjust the path and width as needed

# User input
user_input = st.text_input("How can Ta-Ta the great help you?")

if st.button('Send'):
    if user_input:
        # Get the response from GPT
        gpt_response = chat_with_gpt(user_input)
        st.text_area("Ta-Ta the Greats widsom:", value=gpt_response, height=200)
    else:
        st.warning('Tell Ta-Ta the Great your problems')
