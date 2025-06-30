import os
import pywhatkit
import time
def create_folder():
    folder_name = input("Enter folder name -> ")
    os.makedirs(folder_name, exist_ok = True)
    print(f"Folder '{folder_name}' created.")
    path = os.path.abspath(folder_name)
    os.startfile(path)
def create_file():
    file_name = input("Enter file name(with .txt) -> ")
    with open(file_name, "w") as f:
        f.write("This is a sample file.\n")
    print(f"File '{file_name}' created.")
    path = os.path.abspath(file_name)
    os.startfile(path)
def send_whatsapp_message():
    phone = input("Enter WhatsApp number with country code (e.g. +91xxxxxxxxxx): ")
    message = input("Enter message to send: ")
    print("Sending whatsapp message in few seconds...")
    pywhatkit.sendwhatmsg_instantly(phone, message)
def shutdown():
    confirm = input("Are you sure you want to shutdown? (yes/no): ").lower()
    if confirm == "yes":
        os.system("shutdown /s /t 5")
    else:
        print("Shutdown cancelled.")
while True:
    print("\nSelect an operation:")
    print("1. Create Folder")
    print("2. Create File")
    print("3. Send WhatsApp Message")
    print("4. Shutdown PC")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        create_folder()
    elif choice == "2":
        create_file()
    elif choice == "3":
        send_whatsapp_message()
    elif choice == "4":
        shutdown()
    elif choice == "5":
        print("👋 Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")

