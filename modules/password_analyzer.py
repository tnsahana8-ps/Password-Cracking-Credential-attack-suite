import re
import math

def analyze_password(password):

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Include uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Include lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Include special characters.")

    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^A-Za-z0-9]", password):
        charset += 32

    entropy = 0
    if charset > 0:
        entropy = len(password) * math.log2(charset)

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "strength": strength,
        "score": score,
        "entropy": round(entropy, 2),
        "suggestions": suggestions
    }
