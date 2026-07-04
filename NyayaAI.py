import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# ==================================================
# CONFIGURATION
# ==================================================

GOOGLE_API_KEY = "AQ.Ab8RN6L1vQaJpA4C5t4sHB01SAxEwegG17eQa5Z0zjvZibptTQ"

st.markdown(
    """
    <style>
    .stApp {
        background-color:#faf0e6;

    }
    </style>
    """,
    unsafe_allow_html=True
)
st.set_page_config(
    page_title="NyayaAI ݁",
    page_icon= "📄",
    layout="centered"
)


# ==================================================
# GEMINI MODEL
# ==================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key= GOOGLE_API_KEY,
    temperature=0.3
)

# ==================================================
# APP HEADER
# ==================================================


st.markdown("""
<h1 style='color:#2F4F4F;
           font-family:Garamond;
           text-align:center;
           font-size: 60px'>
    NyayaAI ݁⚖️📜 ݁ 
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='color:#1B1B1B;
           font-family:Garamond;
           text-align:center;
           font-size: 23px'>
   One stop solution for citizens being denied basic rights, dignity, or simply questioning the constitutional provisions.
</h1>
""", unsafe_allow_html=True)

# ==================================================
# FEATURE SELECTION
# ==================================================



@st.dialog("About Rights Explainer")
def rights_info():
    st.markdown("""
    <div style='color:#000000;
                font-family:Garamond;
                text-align:center;
                font-size:17px;'>

    <b>Rights Explainer</b><br><br>

    • Understand your Fundamental Rights under the Constitution of India<br>
    • Learn which Constitutional Articles apply to your situation<br>
    • Discover relevant laws and legal protections<br>
    • Explore possible remedies and next steps<br><br>

    <b>Best for:</b> Understanding your rights before taking action.

    </div>
    """, unsafe_allow_html=True)


@st.dialog("About Complaint Draft")
def complaint_info():
    st.markdown("""
    <div style='color:#000000;
                font-family:Garamond;
                text-align:center;
                font-size:17px;'>

    <b>Complaint Draft</b><br><br>

    • Generate a professional complaint letter<br>
    • Clearly describe your grievance<br>
    • Request appropriate action from authorities<br>
    • Use respectful and formal language<br><br>

    <b>Best for:</b> Preparing complaints for schools, police stations, government offices, workplaces, or other organizations.

    </div>
    """, unsafe_allow_html=True)


@st.dialog("About Legal Simplifier")
def simplifier_info():
    st.markdown("""
    <div style='color:#000000;
                font-family:Garamond;
                text-align:center;
                font-size:17px;'>

    <b>Legal Simplifier</b><br><br>

    • Convert complex legal language into simple English<br>
    • Understand difficult Constitutional Articles and laws<br>
    • Get student-friendly explanations<br>
    • Learn key points without legal jargon<br><br>

    <b>Best for:</b> Understanding legal documents, legal explanations, and official notices.

    </div>
    """, unsafe_allow_html=True)

st.info(
    """

📍 Report a Crime:     File an FIR or incident report.




📚 Know Your Rights:       Simple legal information in your language.



🚨 Emergency Help:      Police • Ambulance • Women's Helpline.



👾 Ask NyayaAI :      Get instant legal guidance."""
)

import streamlit as st

st.set_page_config(page_title="NyayaAI", layout="wide")

st.title("🧑‍⚖️ NyayaAI")
st.subheader("How can we help you today?")

def generate_prompt(feature, user_input):

    if feature == "Rights Explainer":
        return f"""
        Explain the Indian constitutional and legal rights relevant to the following issue.

        Issue:
        {user_input}

        Requirements:
        - Use simple language
        - Mention relevant Constitutional Articles
        - Mention important laws if applicable
        - Explain possible remedies
        """

    elif feature == "Complaint Draft":
        return f"""
        Draft a formal complaint letter based on the issue below.

        Issue:
        {user_input}

        Requirements:
        - Professional format
        - Respectful tone
        - Clear description of grievance
        - Requested action
        """

    elif feature == "Legal Simplifier":
        return f"""
        Simplify the following legal rights explanation into plain, easy-to-understand language.

        Legal Explanation:
        {user_input}

        Requirements:
        - Explain like you are speaking to a student or ordinary citizen
        - Avoid legal jargon and complex terminology
        - Simplify references to Constitutional Articles and laws
        - Clearly explain:
          * What rights are involved
         * What the law says
         * What actions the person can take
        - Use short sentences
        - Use bullet points where helpful
        - Keep the explanation practical and easy to understand
        """

    elif feature == "Rights Explainer":
        return f"""
        Explain the Indian constitutional and legal rights relevant to the following issue.

        Issue:
        {user_input}

        Requirements:
        - Use simple language
        - Mention relevant Constitutional Articles
        - Mention important laws if applicable
        - Explain possible remedies
        """

    elif feature == "Complaint Draft":
        return f"""
        Draft a formal complaint letter based on the issue below.

        Issue:
        {user_input}

        Requirements:
        - Professional format
        - Respectful tone
        - Clear description of grievance
        - Requested action
        """

    elif feature == "Bhavya":
        return f"""
        Simplify the following legal rights explanation into plain, easy-to-understand language.

        Legal Explanation:
        {user_input}

        Requirements:
        - Explain like you are speaking to a student or ordinary citizen
        - Avoid legal jargon and complex terminology
        - Simplify references to Constitutional Articles and laws
        - Clearly explain:
          * What rights are involved
         * What the law says
         * What actions the person can take
        - Use short sentences
        - Use bullet points where helpful
        - Keep the explanation practical and easy to understand
        """
def generate_prompt(feature, user_input):

    if feature == "📚 Know Your Rights":
       return f"""
        Explain the Indian constitutional and legal rights relevant to the following issue.

        Issue:
        {user_input}

        Requirements:
        - Use simple language
        - Mention relevant Constitutional Articles
        - Mention important laws if applicable
        - Explain possible remedies
        - In case of invalid input, say "Invalid Input"
        """ 

    elif feature == "📝 Write a Report":
      return f"""
        Draft a formal complaint letter based on the issue below.

        Issue:
        {user_input}

        Requirements:
        - Professional format
        - Respectful tone
        - Clear description of grievance
        - Requested action
        """

    elif feature == "📄 Understand Legal Documents":
       return f"""
        Simplify the following legal rights explanation into plain, easy-to-understand language.

        Legal Explanation:
        {user_input}

        Requirements:
        - Explain like you are speaking to a student or ordinary citizen
        - Avoid legal jargon and complex terminology
        - Simplify references to Constitutional Articles and laws
        - Clearly explain:
          * What rights are involved
         * What the law says
         * What actions the person can take
        - Use short sentences
        - Use bullet points where helpful
        - Keep the explanation practical and easy to understand
        """
    elif feature == "🚨 Emergency Contacts":
       
       return {user_input}
    

    feature = st.radio(
    "Choose a Feature",
    [
        
    ]
    )


# ------------------------------
# Know Your Rights
# ------------------------------
with st.expander("📚 Know Your Rights"):
    st.write("Ask any question about your legal rights.")


    rights_query = st.text_area(
        "Type your question",
        placeholder="e.g. Can police refuse to register my FIR?"
    )

    rights_files = st.file_uploader(
        "Upload supporting documents",
        accept_multiple_files=True,
        type=["pdf","docx","jpg","jpeg","png"]
    )

    rights_audio = st.file_uploader(
        "Upload voice memo",
        type=["mp3","wav","m4a"]
    )

    if st.button("Submit Question", key="rights"):
        prompt = generate_prompt("📚 Know Your Rights", rights_query)

        try:
            with st.spinner("Analyzing..."):

                response = llm.invoke([
                    HumanMessage(content=prompt)
                ])
            st.markdown(
    f"""
    <div style='color:#964B00;
                font-family:Garamond;
                text-align:center;
                font-size:17px;'>
    {response.content}
    </div>
    """,
    unsafe_allow_html=True
)
        except Exception as e:
            st.error(f"Error: {e}")

           ## st.success("Analysis Complete")
            ##st.success("Your question has been submitted.")

# ------------------------------
# Write a Report
# ------------------------------
with st.expander("📝 Write a Report"):
    report = st.text_area(
        "Describe what happened",
        height=180,
        placeholder="Write your report here..."
    )

    photos = st.file_uploader(
        "Upload Photos",
        type=["jpg","jpeg","png"],
        accept_multiple_files=True,
        key="photos"
    )

    documents = st.file_uploader(
        "Upload Documents",
        type=["pdf","doc","docx"],
        accept_multiple_files=True,
        key="documents"
    )

    audio = st.file_uploader(
        "Upload Voice Memo",
        type=["mp3","wav","m4a"],
        key="audio"
    )
    if st.button("Submit Question", key="report"):
        prompt = generate_prompt("📝 Write a Report", report)
        try:
            with st.spinner("Analyzing..."):

                response = llm.invoke([
                    HumanMessage(content=prompt)
                ])
                st.markdown(
    f"""
    <div style='color:#964B00;
                font-family:Garamond;
                text-align:center;
                font-size:17px;'>
    {response.content}
    </div>
    """,
    unsafe_allow_html=True
)
        except Exception as e:
            st.error(f"Error: {e}")
    #if st.button("Submit Report", key="report"):
        #st.success("Report saved successfully.")

# ------------------------------
# Understand Legal Documents
# ------------------------------
with st.expander("📄 Understand Legal Documents"):
    legal_doc = st.file_uploader(
        "Upload your legal document",
        type=["pdf","doc","docx"],
        key="legal"
    )

    question = st.text_area(
        "Ask a question about the document",
        placeholder="Explain this notice in simple language."
    )
    if st.button("Submit Question", key="legal language"):
        prompt = generate_prompt("📄 Understand Legal Documents", legal_doc)
        try:
            with st.spinner("Analyzing..."):

                response = llm.invoke([
                    HumanMessage(content=prompt)
                ])
                st.markdown(
    f"""
    <div style='color:#964B00;
                font-family:Garamond;
                text-align:center;
                font-size:17px;'>
    {response.content}
    </div>
    """,
    unsafe_allow_html=True
)
        except Exception as e:
            st.error(f"Error: {e}")
    

# ------------------------------
# Emergency Contacts
# ------------------------------
with st.expander("🚨 Emergency Contacts"):

    st.markdown("""
    ### One-tap Emergency Numbers

    🚓 Police: **100**

    🚑 Ambulance: **108**

    🚒 Fire: **101**

    👩 Women's Helpline: **181**

    👶 Child Helpline: **1098**
    """)

    emergency_notes = st.text_area(
        "Describe your emergency (optional)"
    )



    if st.button("Submit Question", key="emergency"):
        prompt = generate_prompt("🚨Emergency Contacts", emergency_notes)
        try:
            with st.spinner("Analyzing..."):

                response = llm.invoke([
                    HumanMessage(content=prompt)
                ])
                st.markdown(
    f"""
    <div style='color:#964B00;
                font-family:Garamond;
                text-align:center;
                font-size:17px;'>
    {response.content}
    </div>
    """,
    unsafe_allow_html=True
)
        except Exception as e:
            st.error(f"Error: {e}")

feature = st.radio(
    
    "Choose a Feature",
    [
        "Rights Explainer",
        "Complaint Draft",
        "Legal Simplifier"

    ]
    )


if feature == "Rights Explainer":
    if st.button("ℹ️ What does this mode do?"):
        rights_info()

elif feature == "Complaint Draft":
    if st.button("ℹ️ What does this mode do?"):
        complaint_info()

elif feature == "Legal Simplifier":
    if st.button("ℹ️ What does this mode do?"):
        simplifier_info()

user_input = st.text_area(
    "Describe your issue or paste text here",
    height=200
)

# ==================================================
# PROMPT BUILDER
# ==================================================

def generate_prompt(feature, user_input):

    if feature == "Rights Explainer":
        return f"""
        Explain the Indian constitutional and legal rights relevant to the following issue.

        Issue:
        {user_input}

        Requirements:
        - Use simple language
        - Mention relevant Constitutional Articles
        - Mention important laws if applicable
        - Explain possible remedies
        """

    elif feature == "Complaint Draft":
        return f"""
        Draft a formal complaint letter based on the issue below.

        Issue:
        {user_input}

        Requirements:
        - Professional format
        - Respectful tone
        - Clear description of grievance
        - Requested action
        """

    elif feature == "Legal Simplifier":
        return f"""
        Simplify the following legal rights explanation into plain, easy-to-understand language.

        Legal Explanation:
        {user_input}

        Requirements:
        - Explain like you are speaking to a student or ordinary citizen
        - Avoid legal jargon and complex terminology
        - Simplify references to Constitutional Articles and laws
        - Clearly explain:
          * What rights are involved
         * What the law says
         * What actions the person can take
        - Use short sentences
        - Use bullet points where helpful
        - Keep the explanation practical and easy to understand
        """

# ==================================================
# ANALYZE BUTTON
# ==================================================

if st.button("Analyze"):

    if not user_input.strip():
        st.warning("Please enter some text.")
    else:

        prompt = generate_prompt(feature, user_input)

        try:
            with st.spinner("Analyzing..."):

                response = llm.invoke([
                    HumanMessage(content=prompt)
                ])

            st.success("Analysis Complete")
            st.markdown(
    f"""
    <div style='color:#964B00;
                font-family:Garamond;
                text-align:center;
                font-size:17px;'>
    {response.content}
    </div>
    """,
    unsafe_allow_html=True
)

        except Exception as e:
            st.error(f"Error: {e}")
