from pykeepass import PyKeePass
import sys
import urllib.request
import hashlib

def check_pwned(entry):
    pw = entry.password

    result = hashlib.sha1(pw.encode())
    result = result.hexdigest()
    result_five = result[0:5]

    api_url = 'https://api.pwnedpasswords.com/range/' + result_five

    with urllib.request.urlopen(api_url) as response:
        html = (response.read()).decode('ascii').lower().split('\r\n')
        for line in html:
            current_hash=result_five+line.split(':')[0]
            if result==current_hash:
                print('Your ' + entry.title + ' account has been pwned. Password ' + entry.password + ' was found ' + line.split(':')[1] + ' times in the data set of haveibeenpwned.com')
                return True

    return False

def main():
    if 1 < len(sys.argv):
        file = str(sys.argv[1])
        
        if 2 < len(sys.argv):
            password = str(sys.argv[2])
            
            kp = PyKeePass(file, password=password)
            
            groups = kp.groups
            pwned_entries = []
            
            for group in groups:
                entries = group.entries

                for entry in entries:
                    if str(entry.password)=='None':
                        pass
                    elif check_pwned(entry):
                        pwned_entries.append(entry)

if __name__=='__main__':
    main()
