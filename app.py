import streamlit as st

st.set_page_config(page_title="Viral Hook & Script Generator v2", page_icon="🚀", layout="centered")

st.title("🚀 Viral Hook & Script Generator v2")
st.caption("Whop Clipping aur Short-form creators ke liye premium scripts generator.")

# Step 1: User Inputs
topic = st.text_input("Enter your Video Topic/Niche (e.g., Tech, Crypto, Motivation):")
category = st.selectbox("Choose Content Category:", ["Tech & AI", "Finance & Crypto", "Self-Improvement & Motivation"])
tone = st.radio("Select Script Tone:", ["Aggressive/Bold", "Mysterious/Curious"], horizontal=True)

# Step 2: Dynamic Template Logic based on Category & Tone
hooks_dict = {
    "Tech & AI": {
        "Aggressive/Bold": [
            f"If you are not using AI for {topic} in 2026, you are falling behind.",
            f"Stop wasting hours on {topic}. This new tool does it in 5 seconds."
        ],
        "Mysterious/Curious": [
            f"This hidden {topic} tool feels illegal to know...",
            f"The dark truth about {topic} that developers hide from you."
        ]
    },
    "Finance & Crypto": {
        "Aggressive/Bold": [
            f"You are losing money every second you ignore this {topic} strategy.",
            f"I tried {topic} for 7 days, and here is the exact profit."
        ],
        "Mysterious/Curious": [
            f"The elite 1% are using this secret {topic} loophole...",
            f"Why traditional {topic} advice is keeping you broke."
        ]
    },
    "Self-Improvement & Motivation": {
        "Aggressive/Bold": [
            f"Stop crying about {topic} and fix your routine today.",
            f"The brutal reality of {topic} nobody wants to face."
        ],
        "Mysterious/Curious": [
            f"The psychological trick behind {topic} success...",
            f"I changed my life in 7 days using this weird {topic} habit."
        ]
    }
}

if st.button("Generate Premium Content 🔥"):
    if topic:
        st.subheader("🎯 CUSTOM SCROLL-STOPPING HOOKS")
        selected_hooks = hooks_dict[category][tone]
        for i, hook in enumerate(selected_hooks, 1):
            st.code(f"{i}. {hook}", language="text")

        st.subheader("📝 30-SECOND DYNAMIC VIDEO SCRIPT")
        script_body = f"""
- [0:00 - 0:05] [Hook Phase]: [INSERT HOOK FROM ABOVE]
- [0:05 - 0:15] [The Problem/Lie]: Most internet gurus tell you that {topic} is easy, but they are selling you a lie just for views.
- [0:15 - 0:25] [The Solution/Action]: To actually win in {category}, you need to build a system, use sharp hooks, and act fast.
- [0:25 - 0:30] [High-Converting CTA]: Comment "STREAM" below and I'll send you the exact {topic} framework for free.
        """
        st.text_area(label="Copy Script:", value=script_body.strip(), height=220)
    else:
        st.error("Topic daalo pehle, bhai!")
