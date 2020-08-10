# Python Password Locker
On Average, a person has at least 7 different accounts he or she has signed into, be it email, social media, entertainment or job portal accounts. It becomes really hard to remember all those passwords and even create new ones.

Python Password Locker is an application that will help a user to manage their passwords and even generate new passwords for them.

# Features
* User is able to create a password locker account with his/her details, a login username and password.
* User is able to store their already existing account credentials in the application. Assuming I already have a [Twitter](https://twitter.com) account, I want to store my already existing Twitter username and password in the application.
* User is able to create new account credentials in the application. For example, If I have not yet signed up for [Instagram](https://instagram.com), the user is able to create credentials account for Instagram in the application and application generates a password for me to use when I sign up for Instagram.
* User has the option of putting in a password that they want to use for new credential account. For example, when creating my Instagram credential account, I have the option of putting in the password I want to use instead of having the application generate a password for me.
* User can be able to view various account credentials and their passwords in the application.
* User has the ability to delete a credentials account that they no longer need in the application.
* User is able to copy their credentials to the clipboard.
* User is also able to dictate the length of the password to be generated.

# Usage
## Requirements
1. Create a Docker Hub account [here](https://kirr.co/ud0sxn)
2. In case you don't have Docker installed, you can get instructions on how to download Docker [here](https://docs.docker.com/docker-hub/)

Bringing Python Password Locker application stack is as easay as running a *docker run* command with the name of the image. Running the below command, for example, allows you to run an instance Python Password Locker on the Docker host

```
docker run -it kwairore/python_password_locker
```

## Bug / Feature 
If you find a bug, kindly open an issue [here](https://github.com/lwairore/python-password-locker/issues/new).

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/lwairore/python-password-locker/issues/new).



# Buit with
1. [Python 3.6](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language.
2. [Docker](https://www.docker.com/) - Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels.
3. [Pyperclip](https://pyperclip.readthedocs.io/en/latest/) - Pyperclip is a cross-platform Python module for copy and paste clipboard functions.



# Team 
### Karangu Lucas Wairore 
#### Aspiring full-stack developer

# [License](README.md)
MIT License

Copyright (c) 2019 [Karangu Lucas Wairore](https://github.com/lwairore)


