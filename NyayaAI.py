import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# ==================================================
# CONFIGURATION
# ==================================================

GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]


st.markdown(
    """
    <style>
    .stApp {
        background-color: #cd5c5c;

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
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3
)

# ==================================================
# APP HEADER
# ==================================================


st.markdown("""
<h1 style='color:#ffc0cb;
           font-family:Garamond;
           text-align:center;
           font-size: 60px'>
    NyayaAI ݁₊ ⚖️ .📜 ݁˖ 
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='color:#fffaf0;
           font-family:Garamond;
           text-align:center;
           font-size: 23px'>
   One stop solution for citizens being denied basic rights, dignity, or simply questioning the constitutional provisions.
</h1>
""", unsafe_allow_html=True)

# ==================================================
# FEATURE SELECTION
# ==================================================

st.markdown("""
<h1 style='color:#fffaf0;
           font-family:Garamond;
           text-align:center;
           font-size: 17px'>
  Welcome to NyayaAI! 
  This is a tool that will help you overcome any challenge- be it related to basic digity or complex provisional rights.
There are different modes that will help you with different problems. All you need to do is just share whatever you feel like has been done to harm your fundamental rights, dignity or respect, and NyayaAI will suggest the best solution! 

Give it a try!

</h1>
""", unsafe_allow_html=True)

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
    <div style='color:#fffaf0;
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
