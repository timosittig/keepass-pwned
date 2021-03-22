# keepass-pwned
A python script for KeePass files to prove if they were pwned.



## INSTALLATION

You can install the script as usual with git:
```
git clone https://github.com/timosittig/keepass-pwned
```



## HOW TO USE

The script takes two parameters from the command line:

```
keepass-pwned.py file.kdbx mypassword
```

After hitting **[ENTER]** it will print out every entry 



## HOW DOES IT WORK

To prove if your password is beeing compromised I am using the API of haveibeenpwned.com: https://haveibeenpwned.com/API/v3

