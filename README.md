# keepass-pwned
A python script for KeePass files to prove if they were pwned.



## INSTALLATION

You can install the script as usual with git:
```
git clone https://github.com/timosittig/keepass-pwned
```

If there are any problems you can still just copy the source code from [GitHub](https://github.com/timosittig/keepass-pwned/blob/main/keepass_pwned.py) and save it ie next to your KeePass .kdbx file.



## HOW TO USE

The script takes two parameters from the command line:

```
keepass-pwned.py file.kdbx mypassword
```

After hitting **[ENTER]** it will print out every entry 



## HOW DOES IT WORK

To prove if your password is beeing compromised I am using the API of haveibeenpwned.com: https://haveibeenpwned.com/API/v3

