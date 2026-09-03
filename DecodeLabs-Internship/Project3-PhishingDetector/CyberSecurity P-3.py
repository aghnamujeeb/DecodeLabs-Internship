def check_phishing(msg):
    msg_lower = msg.lower()
    bad_words = ["urgent", "verify", "click here", "winner", "suspended",
    "act now", "limited time", "confirm your account", "password", "login"]
    found_words = [word for word in bad_words if word in msg_lower]
    link_flag = False
    if "bit.ly" in msg_lower or "http://" in msg_lower or "tinyurl" in msg_lower:
        link_flag = True
    greeting_flag = False
    if "dear customer" in msg_lower or "dear user" in msg_lower:
        greeting_flag = True
    red_flags = []
    if found_words:
        red_flags.append("Suspicious keywords found: " + ", ".join(found_words))
    if link_flag:
        red_flags.append("Suspicious/shortened link detected")
    if greeting_flag:
        red_flags.append("Generic/informal greeting used instead of your name")
    if red_flags:
        print("⚠️ This message looks UNSAFE. Red flags:")
        for flag in red_flags:
            print("-", flag)
    else:
        print("✅ No obvious red flags found. Message looks safe.")

sample_msg = input("Paste the email/message text: ")
check_phishing(sample_msg)

