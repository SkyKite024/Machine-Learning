import cohere

# Initialize the Cohere client with your API key
cohere_api_key = 'MtDvCJw9bASg879dnzhXsyH5skcHi6vmBEXl0pQO'  # Replace with your Cohere API key
co = cohere.Client(cohere_api_key)

# The text you want to summarize
text_to_summarize = """
Cohere is an AI company that focuses on providing natural language processing (NLP) solutions for businesses and developers. 
Their language models can generate, analyze, and understand text to enable applications such as chatbots, sentiment analysis, 
and content generation. Cohere's APIs are designed to be easy to integrate into various platforms, and they provide models 
that are highly scalable and capable of understanding the nuances of human language. With a strong emphasis on privacy and 
data security, Cohere aims to make cutting-edge NLP technology accessible to all industries.
"""

# Use the Cohere API to generate a summary
response = co.summarize(
    model='xlarge',  # You can specify different models here, such as 'small', 'medium', or 'xlarge'
    text=text_to_summarize,
    length='short'  # You can specify 'short', 'medium', or 'long' for summary length
)

# Output the generated summary
print("Summary:", response.summary)
