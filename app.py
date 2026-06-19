import streamlit as st

st.title("🔍 Phishing URL Detector")

url = st.text_input("Enter a URL")

if url:

    score = 0
    reasons = []

    # Rule 1: Length
    if len(url) > 50:
        score += 1
        reasons.append("URL is unusually long")

    # Rule 2: @ symbol
    if "@" in url:
        score += 1
        reasons.append("Contains @ symbol")

    # Rule 3: Suspicious words
    suspicious_words = ["login", "verify", "secure", "update", "bank"]

    for word in suspicious_words:
        if word in url.lower():
            score += 1
            reasons.append(f"Contains suspicious word: {word}")

    # Rule 4: Hyphens
    if url.count("-") >= 2:
        score += 1
        reasons.append("Contains multiple hyphens")

    # Output section
    st.subheader("Analysis Result")

    if score >= 4:
        st.error("🚨 HIGH RISK: Likely Phishing Site")
    elif score >= 2:
        st.warning("⚠️ MEDIUM RISK: Be careful")
    else:
        st.success("✅ LOW RISK: Looks safe")

    st.write("Score:", score)

    if reasons:
        st.write("### Reasons Detected:")
        for r in reasons:
            st.write("- ", r)