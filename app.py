import streamlit as st

# App title
st.set_page_config(page_title="Agent Kisha - Tax Software Assistant", layout="centered")
st.title("🤖 Meet Agent Kisha – Your Tax Software Assistant")

# Introduction
st.markdown("""
Welcome! I'm **Agent Kisha**, your right hand when it comes to navigating our tax software platform.  
I'm here to help with:
- Onboarding & setup
- Troubleshooting issues
- Closing sales & upsells
- Finding the right target audience for your ads
- Recruiting and onboarding new tax preparers

How can I help you today?
""")

# User input
user_input = st.text_input("Type your question or request below:")

# Predefined responses
def get_response(message):
    message = message.lower()
    
    if "onboard" in message or "setup" in message:
        return "Let’s get your onboarding started! Please make sure you have your EFIN, ID, and bank info ready."
    elif "troubleshoot" in message or "error" in message:
        return "No worries, I got you! Can you describe the issue you're having with the software?"
    elif "sale" in message or "buy" in message or "upgrade" in message:
        return "Ready to make a move? Let me break down your options and help you choose the best software package."
    elif "ads" in message or "audience" in message:
        return "Looking to reach the right people? I can help you define your audience and research what works best in your area."
    elif "recruit" in message or "tax preparer" in message:
        return "We love growth! Let's go over the steps to recruit and onboard new preparers under your office."
    elif "help" in message:
        return "Here’s what I can help with: onboarding, tech issues, sales, marketing research, and team building. Ask me anything!"
    elif message.strip() == "":
        return ""
    else:
        return "I'm going to send this to the team so we can get back to you with the best solution. Hang tight—we got you!"

# Display response
if user_input:
    response = get_response(user_input)
    st.markdown(f"**Agent Kisha:** {response}")
