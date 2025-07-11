#IMPORTANT : In order to fully engage with this crackme and make the most of it to improve your skills, do not read the source code and try known cracking methods to find the password
#Thank you for considering this and good luck

import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_credentials(secret_key):
    name = "Esther"  
    password = "a2KR*xKmp2N4O0t496"   
    return hash_password(name + secret_key), hash_password(password + secret_key)

def main():
    secret_key = "the_special_one"   
    expected_name_hash, expected_password_hash = generate_credentials(secret_key)

    while True:
        user_name = input("Name ? :")
        user_input = input("Log ? :")
        
         
        if hash_password(user_name + secret_key) == expected_name_hash:
            if hash_password(user_input + secret_key) == expected_password_hash:
                print("Access")
                break   
            else:
                print("Fail")
        else:
            print("Invalid Name")

          
        retry = input("Try again? Press y or n (y/n): ").lower()
        if retry != 'y':
            break  

    input("Press Enter to exit...")  

if __name__ == "__main__":
    main()
