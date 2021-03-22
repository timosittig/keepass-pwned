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
keepass-pwned.py file.kdbx 'mypassword'
```

It takes the following parameters:
* `file.kdbx` as the path to the KeePass file.
* `mypassword` as the password to the KeePass file.

![20210322102410436](https://user-images.githubusercontent.com/47139230/111967942-eb5a0580-8af8-11eb-876f-d6833bed072d.gif)

After hitting **[ENTER]** it will print out every entry that has been pwned.



## HOW DOES IT WORK

To access your KeePass .kdbx file I am using the [PyKeePass module](https://pypi.org/project/pykeepass/) from pip.

To prove if your password is beeing compromised I am using the API of haveibeenpwned.com: https://haveibeenpwned.com/API/v3

It does not transfer your password in plain text. But it will send the first 5 letters of it's SHA-1 hash to [https://api.pwnedpasswords.com/range/](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange). Afterwards the API will send an HTTP response with a list of SHA-1 hashes. If one of them matches the SHA-1 hash of your password, your password was leaked in the past.

This will all work automatically. You only have to follow the [HOW TO USE](https://github.com/timosittig/keepass-pwned/blob/main/README.md#how-to-use).
