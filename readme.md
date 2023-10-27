"# pythonOOP" 
## python object orientation programing tutorial
Followed Youtube video: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

oop1.py  Tutorial 1: Classes and instances
oop2_classMethod.py 

## video followed by code

| video           |    code    |
|-----------------|:----------:|
| 1： Classes and Instances.mp4 | oop1.py  |
| 2： Class Variables.mp4 |    |
| 3： classmethods and staticmethods.mp4 |  oop2_classMethod.py   |
| 4： Inheritance - Creating Subclasses.mp4 |    oop3_inheritance.py     |
| 5： Special (Magic⧸Dunder) Methods.mp4 |   oop4_special(magic)Method.py    |
| 6： Property Decorators - Getters, Setters, and Deleters.en.vtt | oop5_propertyDecorator.py | 



## Manage Multiple Github Accounts on One Computer with SSH
Reference:
https://www.youtube.com/watch?v=ap56ivm0dhw
https://stackoverflow.com/questions/18683092/how-to-run-ssh-add-on-windows
```
Open Manage optional features from the start menu and make sure you have Open SSH Client in the list. If not, you should be able to add it.

Open Services from the start Menu

Scroll down to OpenSSH Authentication Agent > right click > properties

Change the Startup type from Disabled to any of the other 3 options. I have mine set to Automatic (Delayed Start)

Open cmd and type where ssh to confirm that the top listed path is in System32. Mine is installed at C:\Windows\System32\OpenSSH\ssh.exe. If it's not in the list you may need to close and reopen cmd.
```
## Config file used in the video
```
# Default Account (main account)
Host github.com
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa


# Other Account (other account)
Host github-other
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_ed25519
```

## "error: remote origin already exists."
git remote rm origin

Reference:
https://stackoverflow.com/questions/1221840/remote-origin-already-exists-on-git-push-to-a-new-repository