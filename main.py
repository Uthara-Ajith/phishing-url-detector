url = input("Enter a URL: ")

score = 0
reasons = []

# 1. Length check
if len(url) > 50:
    score += 1
    reasons.append("URL is unusually long")

# 2. @ symbol check
if "@" in url:
    score += 1
    reasons.append("Contains @ symbol (can hide real domain)")

# 3. Suspicious words
suspicious_words = ["login", "verify", "secure", "update", "bank"]

for word in suspicious_words:
    if word in url.lower():
        score += 1
        reasons.append(f"Contains suspicious keyword: {word}")

# 4. Hyphen check
if url.count("-") >= 2:
    score += 1
    reasons.append("Too many hyphens in URL")

# -----------------------------
# RISK CLASSIFICATION
# -----------------------------

print("\n==============================")
print("   PHISHING URL ANALYZER")
print("==============================\n")

print("URL:", url)
print("Risk Score:", score, "/ 5")

# simple visual bar
print("Risk Level:", "█" * score + "░" * (5 - score))

if score >= 4:
    print("\n🚨 HIGH RISK: Likely Phishing Site")

elif score >= 2:
    print("\n⚠️ MEDIUM RISK: Be careful")

else:
    print("\n✅ LOW RISK: Looks safe")

# -----------------------------
# REASONS
# -----------------------------

if reasons:
    print("\nReasons detected:")
    for r in reasons:
        print("-", r)