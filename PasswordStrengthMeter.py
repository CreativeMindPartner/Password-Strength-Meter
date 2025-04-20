import streamlit as st
import re

# Custom CSS for dark theme styling
st.markdown("""
    <style>     
    .main {
        background-color: #1c2800;
        padding: 30px;
        border-radius: 12px;
        max-width: 750px;
        margin: auto;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        border: 2px solid #3aafa9;
    }

    h1 {
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
        text-align: center;
        font-size: 2.8em;
        margin-bottom: 15px;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    h2 {
        color: #3aafa9;
        font-family: 'Roboto', sans-serif;
        font-size: 1.6em;
        text-align: center;
        margin-bottom: 25px;
    }

    .stTextInput > div > div {
        background-color: #2d3839;
        border: 2px solid #3aafa9;
        border-radius: 10px;
        padding: 12px;
        margin-bottom: 20px;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.2);
    }

    .stTextInput label {
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
        font-size: 1.1em;
    }
    
    .stButton > button {
        background-color: #3aafa9;
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
        font-size: 1.2em;
        padding: 12px 25px;
        border-radius: 10px;
        border: 2px solid #2d3839;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .stButton > button:hover {
        background-color: #2d3839;
        border-color: #3aafa9;
        color: #3aafa9;
        transform: translateY(-2px);
        cursor: pointer;
    }

    .stAlert {
        background-color: #2d3839;
        color: #ffffff;
        border: 2px solid #3aafa9;
        border-radius: 10px;
        padding: 15px;
        font-family: 'Roboto', sans-serif;
        font-size: 1.1em;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.2);
    }

    .stMarkdown {
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
        font-size: 1.1em;
    }

    .footer {
        text-align: center;
        color: #3aafa9;
        font-family: 'Roboto', sans-serif;
        font-size: 1em;
        margin-top: 30px;
        padding-top: 20px;
        border-top: 2px solid #3aafa9;
    }

    @media (max-width: 600px) {
        h1 {
            font-size: 2.2em;
        }
        h2 {
            font-size: 1.3em;
        }
        .stButton > button {
            font-size: 1em;
            padding: 10px 20px;
        }
        .main {
            padding: 20px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# 🎉 Title
st.title("🔐 Ultimate Password Strength Checker")

# 📝 Description
st.markdown("""
Welcome to the **Ultimate Password Strength Checker!**  
Ensure your password is secure by checking:
- ☑ Length
- ✅ Upper & Lowercase letters
- ✅ Numbers
- ✅ Special Characters

> ⚡ *Improve your online security by creating strong passwords!*  
""")

# 🏷️ Input Field
password = st.text_input("🔑 Enter your password:", type="password")

# 🔍 Password Strength Check
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters** long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include **both uppercase and lowercase** letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least **one number (0-9)**.")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least **one special character (!@#$%^&*)**.")

    return score, feedback

# ✅ Button to Check Password
if st.button("🔍 Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)

        st.subheader("🔒 Password Strength Result:")

        if score == 4:
            st.success("✅ Strong Password! Your password is secure.")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")

        if feedback:
            st.info("💡 Suggestions to improve your password:")
            for tip in feedback:
                st.write(tip)
    else:
        st.error("🚨 Please enter a password to check.")

# 🌟 Footer
st.markdown("""
<div class="footer">
🌟 Built with Streamlit | Stay Secure! 🔒
</div>
""", unsafe_allow_html=True)
