#IMPORTANT : In order to fully engage with this crackme and make the most of it to improve your skills, do not read the source code and try known cracking methods to find the password
#Thank you for considering this and good luck

import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


encrypted_password = "fcfbb5e9c8d1a2120e1e752ffaf7b3adf8f76e7c9d9bcd746b6e50c5e9b0cf29"  

def main():
    user_name = input("Name ? :")
    user_input = input("Log ? :")
    user_hashed = hash_password(user_input)
    
    if user_hashed == encrypted_password:
        print("Access")
    else:
        print("Fail")
    
    input("Press Enter to exit...")  

if __name__ == "__main__":
    main()
