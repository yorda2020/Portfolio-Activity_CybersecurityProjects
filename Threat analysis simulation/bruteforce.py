'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

# Function to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        # Attempt to extract using the given password
        zf_handle.extractall(pwd=password.strip())
        return True
    except RuntimeError:  # Incorrect password
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("[+] Beginning brute force attack...")
    
    try:
        # Open the encrypted zip file
        with ZipFile('enc.zip') as zf:
            # Open the password list
            with open('rockyou.txt', 'rb') as f:
                for line in f:
                    password = line.strip()
                    if attempt_extract(zf, password):
                        print(f"[+] Password found: {password.decode()}")
                        return
                    else:
                        print(f"[-] Incorrect password: {password.decode()}")
        print("[+] Password not found in list")
    except FileNotFoundError as e:
        print(f"Error: {e}. Make sure 'enc.zip' and 'rockyou.txt' exist.")

if __name__ == "__main__":
    main()