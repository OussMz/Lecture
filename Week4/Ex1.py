from collections import defaultdict

login_attempts = [
    ("alice", "success"),
    ("bob", "failed"),
    ("bob", "failed"),
    ("charlie", "success"),
    ("hailey", "failed"),
    ("alice", "failed"),
]
false_users = []
record = defaultdict(int)
for user, status in login_attempts:
    if status == "failed":
        record[user] += 1
        if record[user] == 3:
            false_users.append(user)

print(f"Checking login attempts:")
if len(false_users):
    for u in false_users:
        print(f"ALERT: User '{u}' has 3 failed login attempts")
    print("Security check complete.")
else:
    print("No failed logins. Security check complete.")

    

