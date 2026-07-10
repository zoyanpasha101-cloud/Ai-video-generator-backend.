import streamlit as st

st.set_page_config(page_title="Viral Hook & Script Generator", page_icon="🚀", layout="centered")

st.title("🚀 Viral Hook & Script Generator")
st.caption("Whop Clipping aur LinkedIn/Instagram reels ke liye fast scripts banao.")

# User Input
topic = st.text_input("Enter your Video Topic/Niche (e.g., AI Tools, Crypto, Coding):")

if st.button("Generate Content 🔥"):
    if topic:
        st.subheader("🎯 SECTION 1: 5 SCROLL-STOPPING HOOKS")
        hooks = [
            f"1. This hidden {topic} tool feels illegal to know...",
            f"2. Stop wasting hours on {topic}. Do this instead.",
            f"3. I tried {topic} for 7 days, and here is what happened.",
            f"4. The ugly truth about {topic} nobody wants you to know.",
            f"5. If you are not using AI for {topic} in 2026, you are falling behind."
        ]
        for hook in hooks:
            st.code(hook, language="text")

        st.subheader("📝 SECTION 2: 30-SECOND DYNAMIC VIDEO SCRIPT")
        script_body = f"""
- [0:00 - 0:05] [Hook Phase]: [INSERT CHOSEN VIRAL HOOK]
- [0:05 - 0:15] [The Problem/Lie]: Traditional {topic} advice is slow, recycled, and built to keep you stuck while everyone else wins attention.
- [0:15 - 0:25] [The Solution/Action]: Use one fast system: grab the angle, cut the fluff, and post a sharp hook that makes people stop scrolling.
- [0:25 - 0:30] [High-Converting CTA]: Comment "STREAM" below and I'll send you the exact {topic} playbook.
        """
        st.text_area(label="Copy Script:", value=script_body.strip(), height=220)
    else:
        st.error("Please enter a topic first, bhai!")
