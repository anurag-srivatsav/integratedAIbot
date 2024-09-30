
import os
import google.generativeai as genai
from google.generativeai import configure, GenerativeModel
from langchain.prompts import PromptTemplate
import streamlit as st
import time

# Set your API key as an environment variable (Replace with your actual API key)
os.environ['GENAI_API_KEY'] = 'AIzaSyDzeATPLWRenJGapH8wOCtKEs_QFf6FPR0'  # Make sure to replace this with your actual API key

# Configure the SDK with the API key
api_key = os.getenv('GENAI_API_KEY')
configure(api_key=api_key)

# Define the generation configuration
generation_config = {
    "temperature": 1,                  
    "top_p": 0.95,                     
    "top_k": 64,                       
    "max_output_tokens": 8192,         
    "response_mime_type": "text/plain" 
}

# Initialize the model with the configuration
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  
    generation_config=generation_config
)

# Define chatbot persona variables
name = "Anurag Srivatsav"
age = 20
he_or_she = "he"
university = "KL University Hyderabad"
gpa = "8.8/10"
graduation_date = "July 2025"

# Contact information
contact_phone = "9581403857"
contact_email = "anuragsrivatsav4@gmail.com"
contact_linkedin = "https://linkedin.com/in/anuragsrivatsav"
contact_github = "https://github.com/anurag-srivatsav"
credly="https://www.credly.com/users/anurag-srivatsav"
accredible="https://www.credential.net/profile/anuragsrivastavthammera403031/wallet#gs.f8ewcq"
google_cloud_profile="https://www.cloudskillsboost.google/public_profiles/af9d1c52-af78-4f77-8e27-47f02007a0d9"


# Skills summary
skills = ", ".join([
    "Python", "Java", "R", "C",
    "Django", "React.js", "Node.js", "TensorFlow",
    "MySQL", "MongoDB", "Oracle",
    "HTML", "CSS", "JavaScript", "Tableau", "Power BI",
    "Google Cloud", "Azure", "AWS",
    "Machine Learning", "Artificial Intelligence",
    "Git", "Jupyter Notebook", "Docker","hugging face"
])

# Projects summary
projects = """
1. [Task Manager Application with MongoDB](https://github.com/anurag-srivatsav/MongoDb-UserManagement) - A web app for task management. Live site: [View here](https://mongousermanagement.streamlit.app/).
2. [AI Voice Clone](https://github.com/anurag-srivatsav/EchoClone-AI) - An AI voice clone application. Live site: [View here](https://echoclone-ai.streamlit.app/).
3. [TEXT to HTML Converter](https://github.com/anurag-srivatsav/Text2Html) - Converts text input into HTML format. Live site: [View here](https://anuragportfoli04.netlify.app/).
4. [Image Classification (Cat vs. Dog)](https://github.com/anurag-srivatsav/image-classification) - A deep learning model to classify cat and dog images. Live site: [View here](https://anuragportfoli04.netlify.app/).
5. [My Portfolio Website](https://github.com/anurag-srivatsav/MyPortfolio) - Showcases my education, skills, projects, and certifications. Live site: [View here](https://anuragportfoli04.netlify.app/).
"""

# Define the chatbot persona template
template = """
Meet Nani, your friendly personal assistant driven by a passion for technology, coding, and AI, ready to help with programming issues, AI projects, or general questions; this interactive AI profile bot will provide answers about Anurag Srivatsav based on a preloaded knowledge base or generate responses using AI



Anurag Srivastav Thammera is currently pursuing a B.Tech in Artificial Intelligence and Data Science at {university},
with a GPA of {gpa} and expected graduation in {graduation_date}.
{he_or_she}'s experiences include participating in the Amazon ML Summer School (sept 2023 to oct 2023) and facilitating Google Cloud Ready session  (feb 2022 to present)
also completed AICTE  virtual internships such as Google Generative AI Virtual Internship(jul 2024 to sept 2024) and Alteryx Data Analytics Process Virtual Internship.(july 2024 to sept 2024)

You can aslo view my google cloud skill badges on {credly}
note that all the certfications links are not present in credly. so its better if u provide links and certification name next to each other.

I have successfully developed and deployed multiple interactive AI applications on Hugging Face Spaces. 
Leveraging this platform, I showcase advanced machine learning models and solutions, enabling seamless user
interactions and real-time AI-driven responses. this is my hugging face profile(https://huggingface.co/anurag04)


In my free time, I enjoy watching movies and series, particularly in the sci-fi and mind-bending thriller genres.
I also listen to music and have written several sci-fi stories, which I’ve published on the Notion app

tell them about this following one if your asks me about projects or what r u working on.

I am currently working on an AI personalized music application that begins by collecting initial user data at the start of the day. 
It gathers information from various sources, including sensors, APIs, and user inputs, to understand the user's context. Once the data is collected, 
it analyzes this information to accurately determine the user's current mood. Based on the detected mood, the application decides whether to use existing 
music from a database or generate new music. If it opts for existing music, it retrieves mood-specific tracks from a platform like Spotify or a local collection. 
Alternatively, if it generates new music, it creates personalized lyrics using models like GPT-3/4 and generates unique tunes with tools like MusicVAE or MuseNet. 
These elements are then combined to form a complete song, which is added to a personalized playlist. The application plays the music while continuously updating the 
playlist in real-time, adapting to the user's ongoing activities and mood changes. Throughout the process, it collects feedback from the user to refine and improve 
the music selection and generation. At the end of the day, it concludes the activities and summarizes the user experience for future enhancements. I am just in a half way there, i am facing many compicate challanges but its okay i am learning alot.

If you wanna take a look into what i have done in my google cloud skill boost {google_cloud_profile}
Here’s a bit more about Anurag:
- **Contact**:
  - Phone: {contact_phone}
  - Email: {contact_email}
  - LinkedIn: {contact_linkedin}
  - GitHub: {contact_github}
  - Credly: {credly}

- **Skills**: {skills}

- **Projects**: {projects}

- **Certifications**:
    - [Google Cloud Data Analytics Certificate](https://www.credly.com/badges/97a889b4-6069-4118-9b29-3f7de7a3cc23)
    - [Google TensorFlow Developer Certificate](https://www.credential.net/d81c83e2-673f-475f-a6dc-bf5ffafc81b7#gs.ak34mm)
    - [Oracle Cloud Infrastructure 2024 Generative AI Certified Professional](https://catalog-education.oracle.com/pls/certview/sharebadge?id=B10032C2F707BD514D547D772A9983B3BBAE0554318278F137B99606886BC7FC)
    - [Microsoft Certified: Azure AI Fundamentals](https://learn.microsoft.com/en-us/users/anuragsrivatsav-6772/credentials/b42af8fa0151a887?ref=https%3A%2F%2Fwww.linkedin.com%2F)
    - [Advanced Automation Certification](https://certificates.automationanywhere.com/a02047c5-a380-4ebb-a15e-44da8fd0a097)
    - [Oracle Cloud Infrastructure 2023 Certified Architect Associate](https://catalog-education.oracle.com/pls/certview/sharebadge?id=B10032C2F707BD514D547D772A9983B33C5B29DDB470072B0A3CDB447E72BBE0)
    - [Google AI Essentials](https://www.credly.com/badges/2e2258c6-8d4b-4be0-ba97-8dfaea5f5116)
    - [CS50’s Introduction to Programming with Python](https://certificates.cs50.io/c54c3ae3-1816-42b1-b3db-316da4b49055.pdf)
    - [NoSQL - MongoDB](https://courses.etrain.skillsnetwork.site/certificates/8a07367606c641cfa29e468a11de8179)

{chat_history}
User {user_name}: {user_message}
Chatbot:"""

# Create a PromptTemplate using the template
prompt = PromptTemplate(
    input_variables=["chat_history", "user_name", "user_message", "name", "age", "he_or_she", "university", "gpa", "graduation_date",
                     "contact_phone", "contact_email", "contact_linkedin", "contact_github", "skills", "projects"],
    template=template
)

# Initialize chat history as an empty list
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Start a new chat session
chat_session = model.start_chat(history=[])

# Streamlit app UI
st.title('Questions about me? Shoot—I\'m here with all the answers!') 


st.sidebar.header("About the App:")

st.sidebar.write("""
This is an interactive AI profile bot. \n
Ask any questions about Anurag Srivatsav, and the bot will provide answers based on the preloaded knowledge base or generate responses using AI.
""")



st.sidebar.image('https://res.cloudinary.com/dvlgixtg8/image/upload/v1721021639/chatbot.png', use_column_width=True)

# URL to redirect to
url = 'https://anuragsrivatsav.netlify.app/'  # Replace with your desired URL

# Adding a button to redirect to another URL
if st.sidebar.button('Back to Portfolio'):
    st.sidebar.markdown(f'You are being redirected to: [{url}]({url})', unsafe_allow_html=True)
    # Redirect using Streamlit's write function with HTML link and target="_blank"
    st.sidebar.write(f'<meta http-equiv="refresh" content="0;URL={url}" target="_blank">', unsafe_allow_html=True)



url = 'https://echoclone-ai.streamlit.app/'  # Replace with your desired URL

st.markdown(
    """
    <style>
    .styled-text {
        font-size: 18px; /* Change font size */
        color: skyblue; /* Change text color */
        font-weight: bold; /* Make the text bold */
        
        margin-bottom: 20px; /* Add space below */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Use markdown to display the styled text in the sidebar
st.sidebar.markdown('<p class="styled-text">Wanna explore my Unique Voice Assistant? Check it out now!</p>', unsafe_allow_html=True)
# Adding a button to redirect to another URL
if st.sidebar.button('EchoClone AI🎧'):
    st.sidebar.markdown(f'You are being redirected to: [{url}]({url})', unsafe_allow_html=True)
    # Redirect using Streamlit's write function with HTML link and target="_blank"
    st.sidebar.write(f'<meta http-equiv="refresh" content="0;URL={url}" target="_blank">', unsafe_allow_html=True)










user_name = st.text_input('Enter your name here to enhance your interaction before posing your query: 📝🧑‍💼', value="", key="user_name")

if user_name:
    st.write(f"Hello, {st.session_state['user_name']}! Ask me anything.")
    user_message = st.text_input("Now, go ahead and enter your query: 🔍", key="user_message")

    # Add a Send button
    if st.button("Send"):
        if user_message.lower() in ["exit", "quit"]:
            st.write("Nani: Goodbye! Come again.")
        
        
        elif user_message:
            with st.spinner('Nani is typing...'):
                time.sleep(2)  # Simulate chatbot thinking

                # Render the prompt using the template with dynamic values
                filled_prompt = prompt.format(
                    chat_history="\n".join(st.session_state.chat_history),
                    user_name=user_name,
                    user_message=user_message,
                    name=name,
                    age=age,
                    he_or_she=he_or_she,
                    university=university,
                    gpa=gpa,
                    graduation_date=graduation_date,
                    contact_phone=contact_phone,
                    contact_email=contact_email,
                    contact_linkedin=contact_linkedin,
                    contact_github=contact_github,
                    skills=skills,
                    projects=projects,
                    credly=credly,
                    accredible=accredible,
                    google_cloud_profile=google_cloud_profile
                    
                    
                )

                # Send the prompt to the chatbot model and get a response
                response = chat_session.send_message(filled_prompt)

                # Update chat history for future context
                chat_entry = f" **{user_name}**: {user_message}\n\n **Nani**: {response.text}"
                st.session_state.chat_history.append(chat_entry)

                # Display the chatbot's response
                st.markdown(f"**Nani**: {response.text}")

    st.write('')
    st.subheader("Chat History:")
    st.markdown("""<hr style="border-top: 3px solid #bbb;">""", unsafe_allow_html=True)

    # Print chat history at the bottom
    for entry in st.session_state.chat_history:
        st.write(entry)
        st.write("---")  # Add a line to differentiate entries


# Markdown with HTML for footer
st.markdown("""
<br><br>
<div style="text-align:center;">
    <p>&copy; 2024 Anurag Srivatsav. All rights reserved.</p>
    <p>Meet Nani: Your AI-Driven Profile Assistant 🤖🧠</p>
    <p>Connect with me on LinkedIn: <a href="https://linkedin.com/in/anuragsrivatsav" target="_blank">Anurag Srivatsav</a></p>
</div>
""", unsafe_allow_html=True)
