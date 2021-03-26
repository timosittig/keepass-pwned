# keepass-pwned
A python script for KeePass files to prove if they were pwned.



## INSTALLATION

You can install the script as usual with git:
```
git clone https://github.com/timosittig/keepass-pwned
```

If there are any problems you can still just copy the source code from [GitHub](https://github.com/timosittig/keepass-pwned/blob/main/keepass_pwned.py) and save it ie next to your KeePass .kdbx file.






## HOW TO USE

The script takes up to three parameters from the command line:

```
keepass-pwned.py database.kdbx --password="1234" --keyfile="keyfile.keyx;"
```

It takes the following parameters:
* `database` as the path to the KeePass file.
* `--password` as the password to the KeePass file. (optional)
* `--keyfile` as the keyfile to the KeePass file. (optional)

After hitting **[ENTER]** it will print out every entry that has been pwned.

### Example 1: using a KeePass file and a password

![20210322190108219_pw](https://user-images.githubusercontent.com/47139230/112037086-a9a17d00-8b41-11eb-8bf7-21862ec7be38.gif)



### Example 2: using a KeePass file and a keyfile

![20210322185908144_keyfile](https://user-images.githubusercontent.com/47139230/112037028-9a223400-8b41-11eb-9792-ad1f2aaca6ed.gif)



### Example 3: using a KeePass file and both a password and a keyfile!

![20210322185426383_pw+keyfile](https://user-images.githubusercontent.com/47139230/112037040-9c848e00-8b41-11eb-940a-666746c55479.gif)






## HOW DOES IT WORK

To access your KeePass .kdbx file I am using the [PyKeePass module](https://pypi.org/project/pykeepass/) from pip.

To prove if your password is beeing compromised I am using the API of haveibeenpwned.com: https://haveibeenpwned.com/API/v3

It does not transfer your password in plain text. But it will send the first 5 letters of it's SHA-1 hash to [https://api.pwnedpasswords.com/range/](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange). Afterwards the API will send an HTTP response with a list of SHA-1 hashes. If one of them matches the SHA-1 hash of your password, your password was leaked in the past.

This will all work automatically. You only have to follow the [HOW TO USE](https://github.com/timosittig/keepass-pwned/blob/main/README.md#how-to-use).






## ROADMAP / TO DO

The next milestones on my to do list are:
- [x] finished PyKeePass implementation
- [x] finished implementation of API communication
- [x] finished implementing command line support for .kdbx file with password
- [x] implementing command line support for .kdbx file with key file
- [x] implementing command line support for .kdbx file with password and key file
- [ ] adding --export-csv argument and CSV export implementation
- [ ] adding --export-json argument and JSON export implementation
- [ ] adding --export-xml argument and XML export implementation
