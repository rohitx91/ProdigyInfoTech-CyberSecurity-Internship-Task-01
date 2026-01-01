def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift % 26

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                result += chr((ord(char) - start + shift) % 26 + start)
            else:  # decrypt
                result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char

    return result


print("🔐 Caesar Cipher Program 🔐")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# 🔁 keep asking until correct input
while True:
    choice = input("Type 'encrypt' or 'decrypt': ").strip().lower()
    if choice in ["encrypt", "decrypt"]:
        break
    print("❌ Please type only 'encrypt' or 'decrypt'")

output = caesar_cipher(message, shift, choice)
print("Result:", output)
