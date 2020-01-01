# falah

## Setup with [Vagrant](https://www.vagrantup.com/)

### Dependencies:
- Install VirtualBox
- Install Vagrant

### Bringing up the website:

- clone the repository.
- Navigate to it (ex. ```cd falah```).
- Run this command:
```
vagrant up
```

A virtual machine (VM) is now active (using VirtualBox). It's running Ubuntu 18.04.3 
and has all needed python modules and system configuration to run the website.

- Login to the VM using ssh:

```
vagrant ss
```

- Run Django server on ```0.0.0.0``` port ```8000```:
  
```
python manage.py runserver 0.0.0.0:8000
```

You can reach to the website on [localhost:8000/](localhost:8000/)

This directory is synced with the VM so any changes you make here will affect 
the VM.