import subprocess
import os

def get_wifi_profiles():
    """Fetches Wi-Fi profiles and their passwords."""
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    wifi_data = []

    for i in profiles:
        password_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        password = [b.split(":")[1][1:-1] for b in password_data if "Key Content" in b]
        wifi_data.append((i, password[0] if password else ""))

    return wifi_data

def display_wifi_profiles(wifi_data):
    """Displays Wi-Fi profiles and passwords."""
    print("{:<30}|  {:<}".format("Wi-Fi Name", "Password"))
    print("-" * 50)
    for wifi_name, password in wifi_data:
        print("{:<30}|  {:<}".format(wifi_name, password))

def save_to_file(wifi_data, filename="wifi_passwords.txt"):
    """Saves Wi-Fi profiles and passwords to a file."""
    with open(filename, "w") as file:
        file.write("{:<30}|  {:<}\n".format("Wi-Fi Name", "Password"))
        file.write("-" * 50 + "\n")
        for wifi_name, password in wifi_data:
            file.write("{:<30}|  {:<}\n".format(wifi_name, password))

    print(f"\nWi-Fi details have been saved to {filename}")

def main():
    while True:
        print("\nWi-Fi Password Viewer")
        print("1. Display Wi-Fi Profiles and Passwords")
        print("2. Save Wi-Fi Profiles and Passwords to File")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            wifi_data = get_wifi_profiles()
            display_wifi_profiles(wifi_data)
        elif choice == '2':
            wifi_data = get_wifi_profiles()
            filename = input("Enter the filename to save (default: wifi_passwords.txt): ") or "wifi_passwords.txt"
            save_to_file(wifi_data, filename)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
