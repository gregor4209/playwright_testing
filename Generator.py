import random
import string

def generate_password(length=8):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

passwords = []
while True:
    passwords.append(generate_password())
    content = ", ".join(passwords)
    if len(content.encode('utf-8')) >= 65 * 2048:  # 65 KB
        break

with open("passwords_65kb.txt", "w") as f:
    f.write(content[:65 * 2048])  # Обрезаем до точного размера