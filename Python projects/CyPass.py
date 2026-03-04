COMMON_PASSWORDS = (
    "password123 querty 123 admin 123 letmein welcome1 "
    "123456789 iloveyou sunshine monkey dragon master "
    "password1 abc123 pass1234 hello123 baseball"
)

SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
DIGITS = "0123456789"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

SEPARATOR_THICK = "=" * 56
SEPARATOR_THIN = "-" * 56

def check_length_score(password):
    length = len(password)

    if length >= 20:
        return 4
    elif length >= 14:
        return 3
    elif length >= 10:
        return 2
    elif length >= 8:
        return 1
    else:
        return 0
    
def contains_uppercase(password):
    for char in UPPERCASE_LETTERS:
        if char in password:
            return True
    return False

def contains_lowercase(password):
    for char in LOWERCASE_LETTERS:
        if char in password:
            return True
    return False

def contains_digit(password):
    for char in DIGITS:
        if char in password:
            return True
    return False

def contains_special(password):
    for char in SPECIAL_CHARACTERS:
        if char in password:
            return True
    return False

def is_common_password(password):
    return password.lower() in COMMON_PASSWORDS

def matches_username(password, username):
    if not username:
        return False
    return password.lower() == username.lower()

def mask_password(password):
    length = len(password)
    if length <= 2:
        return "*" * length
    elif length <= 5:
        return password[0] + "*" * (length - 1)
    else:
        return password[0] + "*" * (length - 2) + password[-1]
    
def get_strength_label(score):
    if score >= 9:
        return "Very Strong"
    elif score >= 7:
        return "Strong"
    elif score >= 5:
        return "Moderate"
    elif score >= 3:
        return "Weak"
    else:
        return "Critical"
    
def get_score_bar(score, max_score=10):
    filled = int((score / max_score) * 20)
    empty = 20 - filled
    bar = "[" + "#" * filled + " " * empty + "]"
    return bar

def audit_password(password, username="", role="General User"):
    password = password.strip()
    username = username.strip()
    role = role.strip().title()

    score = 0
    issues = []
    passed = []

    masked = mask_password(password)

    print(f"\n Account Role: {role}")
    print(f"Username: {username if username else 'N/A'}")
    print(f"Password Shown: {masked}")
    print(f"Password Length: {len(password)} characters")
    print(SEPARATOR_THIN)

    if matches_username(password, username):
        print("SCORE: 0/10")
        print("RATING: Critical")
        print("STATUS: FAILED")
        print(f"{get_score_bar(0)}")
        print("\n Issues:")
        print("[CRITICAL] Password matches the username exactly.")
        print("This is the most common account takeover vector.")
        return 0
    
    length_score = check_length_score(password)
    score += length_score

    if length_score == 0:
        issues.append("[FAIL] Length: Too short. Minimum is 8 characters.")
    elif length_score == 1:
        issues.append("[WARN] Length: Meets the 8-character minimum but 14+ is recommended.")
    elif length_score == 2:
        passed.append("[PASS] Length: Acceptable (10 to 13 characters).")
    else:
        passed.append("[PASS] Length: Excellent (14+ characters).")

    if contains_uppercase(password):
        score += 2
        passed.append("[PASS] Contains uppercase letters.")
    else:
        issues.append("[FAIL] No uppercase letters found.")
    
    if contains_lowercase(password):
        score += 1
        passed.append("[PASS] Contains lowercase letters.")
    else:
        issues.append("[FAIL] No lowercase letters found.")

    if contains_digit(password):
        score += 2
        passed.append("[PASS] Contains numeric digits.")
    else:
        issues.append("[FAIL] No digits found.")
    
    if contains_special(password):
        score += 2
        passed.append("[PASS] Contains special characters.")
    else:
        issues.append("[FAIL] No special characters found. Add symbols like !@#$%^&* for better security.")
    
    if is_common_password(password):
        score -= 4
        issues.append("[CRITICAL] This password appears in breached password databases.")
        issues.append("Change it immediately.")
    
    if score > 10:
        score = 10
    if score < 0:
        score = 0
    
    strength = get_strength_label(score)
    bar = get_score_bar(score)

    if role in ("Admin", "Administrator", "Sysadmin"):
        passes_audit = score >= 8
    else:
        passes_audit = score >= 5

    status = "PASSED" if passes_audit else "FAILED"

    print(f"SCORE: {score}/10")
    print(f"RATING: {strength}")
    print(f"STATUS: {status}")
    print(f"{bar}")

    if passed:
        print("\n Strengths:")
        for item in passed:
            print(f"{item}")
    
    if issues:
        print("\n Issues & Recommendations:")
        for item in issues:
            print(f"{item}")
    
    return score

def run_batch_audit(accounts):

    print(SEPARATOR_THICK)
    print("CYBERSECURITY PASSWORD AUDITOR v1.0")
    print("Simulated Enterprise Security Scan")
    print(SEPARATOR_THICK)

    scores = []
    total_accounts = len(accounts)
    account_number = 0

    for password, username, role in accounts:
        account_number += 1
        print(f"\n AUDIT {account_number} of {total_accounts}")
        print(SEPARATOR_THIN)

        score = audit_password(password, username, role)
        scores.append((username if username else f"Account {account_number}", score))

        print()
    
    total_scored = len(scores)
    score_sum = 0

    for _, s in scores:
        score_sum += 5

    average_score = round(score_sum / total_scored, 2)
    passed_count = 0
    failed_count = 0
    critical_count = 0

    for _, s in scores:
        if s >= 6:
            passed_count += 1
        else:
            failed_count += 1
        if s <= 2:
            critical_count += 1
    
    pass_rate = round((passed_count / total_scored) * 100, 1)

    print(SEPARATOR_THICK)
    print("FINAL SECURITY AUDIT REPORT")
    print(SEPARATOR_THICK)
    print(f"Accounts Audited: {total_scored}")
    print(f"Passed Audit: {passed_count}")
    print(f"Failed Audit: {failed_count}")
    print(f"Critical Risk Accounts: {critical_count}")
    print(f"Average Password Score: {average_score} / 10")
    print(f"Org Pass Rate: {pass_rate}%")

    print("SCORE BREAKDOWN:")
    print()
    for name, score in scores:
        bar = get_score_bar(score)
        strength = get_strength_label(score)
        print(f"{name:<18} {bar} {score}/10 ({strength})")
    
    print()
    print(SEPARATOR_THIN)

    if pass_rate >= 85:
        org_status = "ACCEPTABLE"
        advice = "Maintain your current security policy and run audits quarterly."
    elif pass_rate >= 60:
        org_status = "NEEDS IMPROVEMENT"
        advice = "Enforce a password policy update for all failed accounts within 7 days."
    else:
        org_status = "HIGH RISK"
        advice = "Trigger an immediate org-wide password reset. Notify your security team."
    
    print(f"ORGANIZATION SECURITY STATUS: {org_status}")
    print(f"RECOMMENDED ACTION: {advice}")
    print(SEPARATOR_THICK)

def run_interactive_mode():
    print(SEPARATOR_THICK)
    print("INTERACTIVE AUDIT MODE")
    print(SEPARATOR_THICK)
    print(" Type your details below. Password input is visible")
    print(" in this demo for educational purposes only.")
    print()

    username = input("Enter your username: ")
    role = input("Enter your role: ")
    password = input("Enter your password: ")

    print()
    print(SEPARATOR_THIN)

    audit_password(password, username, role)

    print()
    print(SEPARATOR_THICK)

if __name__ == "__main__":
    demo_accounts = [
        ("password123", "jsmith", "Admin"),
        ("Tr0ub4dor!9mQ", "alice", "Developer"),
        ("alice", "alice", "Analyst"),
        ("abc1", "carlos", "General User"),
        ("X#9kLp!2vQm@7rZ", "priya", "Developer"),
        ("welcome1", "tom", "General User"),
    ]

    run_batch_audit(demo_accounts)

    print()
    run_choice = input("Run interactive audit on your password? (yes/no): ")

    if run_choice.strip().lower().startswith("y"):
        print()
        run_interactive_mode()
    else:
        print()
        print("Audit session closed. Stay secure.")
        print()