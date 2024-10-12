import random
import string

# Kullanıcı bilgilerini tutacak basit bir sözlük (dictionary)
users = {}

# Rastgele şifre üretici fonksiyon
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Kullanıcı kaydetme fonksiyonu
def register_user(username):
    if username in users:
        print("This username is already taken. Please choose another.")
    else:
        # Rastgele şifre atama
        password = generate_password(8)  # 8 karakterlik rastgele şifre
        users[username] = password
        print(f"User '{username}' registered successfully!")
        print(f"Assigned password: {password}")

# Şifre güncelleme fonksiyonu
def update_password(username):
    if username in users:
        new_password = input("Enter your new password: ")
        users[username] = new_password
        print(f"Password for user '{username}' has been updated.")
    else:
        print("Username not found. Please register first.")

# Kullanıcı arayüzü
def user_menu():
    while True:
        print("\n1. Register New User")
        print("2. Update Password")
        print("3. View Users and Passwords (Admin only)")
        print("4. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            username = input("Enter a username to register: ")
            register_user(username)
        elif choice == '2':
            username = input("Enter your username to update password: ")
            update_password(username)
        elif choice == '3':
            print("Users and their passwords: ")
            for user, password in users.items():
                print(f"{user}: {password}")
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

# Programı çalıştır
user_menu()
