# '''
# Forage AIG Cybersecurity Program
# Bruteforce starter template
# '''


from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode())
        return True
    except Exception as e:
        return False

def main(): 
    print("[+] Beginning bruteforce")
    with ZipFile('enc.zip') as zf:
        with open('./rockyou.txt', 'r', errors='ignore') as f:
            # Iterate through password entries in rockyou.txt
            for line in f:
                password = line.strip()

                # Attempt to extract the zip file using each password
                if attempt_extract(zf, password):
                    print(f"[+] Password found: {password}")
                    break
                else:
                    print(f"[-] Incorrect password: {password}")

    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
