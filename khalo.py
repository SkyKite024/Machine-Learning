import streamlit as st
import requests

# Set Cohere API key directly in the code (temporary approach)
cohere_api_key = "MtDvCJw9bASg879dnzhXsyH5skcHi6vmBEXl0pQO"  # Replace with your actual Cohere API key

# Function to get response from Cohere API
def get_cohere_response(input_text, no_words, blog_style):
    url = "https://api.cohere.ai/generate"
    
    headers = {
        "Authorization": f"Bearer {cohere_api_key}",
        "Content-Type": "application/json"
    }
    
    # Prepare the prompt template
    prompt = f"""
    Write a blog for a {blog_style} job profile on the topic: "{input_text}"
    within {no_words} words.
    """
    
    # Prepare the request data
    data = {
        "model": "command",  # Cohere's text generation model
        "prompt": prompt,
        "max_tokens": 300,  # Limit to 300 tokens (words + formatting)
        "temperature": 0.7,  # You can adjust this for more creativity or more deterministic output
        "stop_sequences": ["\n"]  # Stop when a newline is encountered
    }
    
    try:
        # Send request to Cohere API
        response = requests.post(url, json=data, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            response_data = response.json()
            if "text" in response_data:
                return response_data["text"].strip()
            else:
                return f"Error: 'text' key not found in response. Response: {response_data}"
        else:
            return f"Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"

# Initialize Streamlit app
st.set_page_config(page_title="Generate Blogs", page_icon="🤖", layout="centered", initial_sidebar_state="collapsed")

st.header("Generate Blogs 🤖")

# Input field for the blog topic
input_text = st.text_input("Enter the Blog Topic")

# Create two columns for additional inputs
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input("Number of Words")
with col2:
    blog_style = st.selectbox(
        "Writing the blog for",
        ("Researchers", "Data Scientist", "Common People"),
        index=0
    )

# Button to generate the blog
submit = st.button("Generate")

# Final response when the button is clicked
if submit:
    if input_text and no_words:
        # Call Cohere API to generate the response
        blog_response = get_cohere_response(input_text, no_words, blog_style)
        st.subheader("Generated Blog:")
        st.write(blog_response)
    else:
        st.warning("Please enter both the blog topic and the number of words.")
