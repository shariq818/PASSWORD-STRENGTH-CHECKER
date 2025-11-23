#!/usr/bin/env python3
# checker_v2.py — Password Strength Checker v2.0
# Shows password requirements first. Lets user choose visible or hidden input.
# Then evaluates strength and prints recommendations.

import re
from getpass import getpass

REQ_TEXT = """
Password requirements (recommended):
 - At least 8 characters (12+ preferred)
 - Mix of lowercase and uppercase letters
 - At least one digit
 - At least one symbol (e.g. ! @ # $ % ^ & *)
 - Avoid common words or sequences like "password", "1234", "qwerty", "admin"
"""

def score_password(pw: str):
    length = len(pw)
    score = 0
    reasons = []

    # length scoring
    if length >= 12:
        score += 3
    elif length >= 8:
        score += 2
    elif length >= 6:
        score += 1
    else:
        reasons.append("Too short (>=8 recommended)")

    # lowercase / uppercase
    if re.search(r"[a-z]", pw): score += 1
    else: reasons.append("No lowercase letters")

    if re.search(r"[A-Z]", pw): score += 1
    else: reasons.append("No uppercase letters")

    # digits
    if re.search(r"\d", pw): score += 1
    else: reasons.append("No digits")

    # symbols
    if re.search(r"[^\w\s]", pw): score += 2
    else: reasons.append("No symbols (e.g. !@#$...)")

    # common patterns check (simple)
    if re.search(r"(password|1234|qwerty|admin|letmein)", pw, re.I):
        reasons.append("Contains common pattern (avoid easily guessable text)")

    return score, reasons

def grade(score: int):
    if score >= 8:
        return "VERY STRONG"
    if score >= 6:
        return "STRONG"
    if score >= 4:
        return "MEDIUM"
    if score >= 2:
        return "WEAK"
    return "VERY WEAK"

def ask_visible_choice():
    while True:
        choice = input("Do you want the password to be visible while typing? (y/N): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("", "n", "no"):
            return False
        print("Please enter Y or N.")

def main():
    print("Password Strength Checker v2.0\n")
    print(REQ_TEXT)

    visible = ask_visible_choice()

    if visible:
        pw = input("Enter password (visible): ")
        print("\nYou entered (visible):", pw)
    else:
        pw = getpass("Enter password (hidden): ")
        # For hidden input we do NOT print back the characters, only confirm length
        print("\nPassword captured (hidden).")

    score, reasons = score_password(pw)
    print(f"\nScore: {score} / 10  => {grade(score)}")

    if reasons:
        print("\nRecommendations:")
        for r in reasons:
            print(" -", r)
    else:
        print("\nNo recommendations. Nice password — keep it secure.")

    # Simple note about reuse and storage
    print("\nNotes:")
    print(" - Do not reuse passwords across important accounts.")
    print(" - Consider a password manager to store strong unique passwords.")
    print(" - This is an educational tool, not production-grade credential storage.")

if __name__ == "__main__":
    main()