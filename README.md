# Project Title
File locker using python

## Getting Started

File Locker is a desktop software tool that helps you secure your important files (e.g. images, audio, and video) and folders from unauthorized access, with as little effort as possible. It encrypts your file using RSA algorithm. 

### Prerequisites

you need to install the software.

```
Python
or 
Anocanda
```
### Main functionality

1. Login and Register (multiuser system)
2. Encrypt and decrypt option. You can encrypt any file and decrypt this file. Here, we use the RSA algorithm to encrypt and decrypt files.
3. When any file is encrypted, it deletes from this computer and only encrypted files can exist.
4. When any user login his/her id and open a file to decrypt, he/she can access only his/her folder.
5. Use a read-write file database to store the user data. We store the user data in a text file. Further, I encrypt those text data using the Elgamal algorithm. As a result, no one can read those user register data. Its shows like this.(fig:1)

![](https://github.com/shahidul034/File-locker-using-python/blob/master/image/image001.png)

### Description

![](https://github.com/shahidul034/File-locker-using-python/blob/master/image/image002.png)

They have a login and register button.

**Register**

This button used for registering any user. When any user registers, it’s corresponding private and private key are generated using the RSA algorithm. This private and public key helps the user to encrypt and decrypt their files.

![](https://github.com/shahidul034/File-locker-using-python/blob/master/image/image003.jpg)

If the user already exists, it shows the user already exists.

![](https://github.com/shahidul034/File-locker-using-python/blob/master/image/image004.jpg)

**Login**

This button helps the user to log in his account. After login, we are going to encrypt and decrypt page.

![](https://github.com/shahidul034/File-locker-using-python/blob/master/image/image005.jpg)

**Encrypt and decrypt**

This page has three buttons. The first button helps the user to encrypt his files using the private key. The second button helps the user to decrypt the files. The third button helps the user to show his files and save this file in the desktop.

![](https://github.com/shahidul034/File-locker-using-python/blob/master/image/image006.jpg)

### Conclusion

Here, we use python language to build the program. We use the RSA algorithm for encryption and decryption. In a graphical user interface, we use the tkinter library.




