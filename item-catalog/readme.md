### Intro

This project requires you to run a VM to run a web server and a web app called project.py
The project uses vagrant software to configure and manage the VM. Here are the tools needed to install and get everything running


### Git

If you don't already have Git installed, [download Git from git-scm.com.](http://git-scm.com/downloads) Install the version for your operating system.

On Windows, Git will provide you with a Unix-style terminal and shell (Git Bash).  
(On Mac or Linux systems you can use the regular terminal program.)

You will need Git to install the configuration for the VM.



### VirtualBox

VirtualBox is the software that actually runs the VM. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads)  Install the *platform package* for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

**Ubuntu 14.04 Note:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a [reported bug](http://ubuntuforums.org/showthread.php?t=2227131), installing VirtualBox from the site may uninstall other software you need.



### Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.  [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.

**Windows Note:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this. In some cases you may need to configure the BIOS to allow VM's.



## copy Source Code

Copy all files and folders from the attached item-catalog folder to your vagrant directory:

static directory
templates directory

client_secrets.json
database_setup.py
fb_client_secrets.json
lotsofitems.py
pg_config.sh
project.py
sportinggoodscatalogwithusers.db


#Install dependencies (python, postgresql, sqlalchemy, flask etc)

in the vagrant directory run the pg_config.sh file (this may take several minutes)



## Run the virtual machine

Using the terminal, within the vagrant directory type "vagrant up" to launch your virtual machine.



## Running the Sporting Goods Catalog App
Once it is up and running, type **vagrant ssh**. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type **exit** at the shell prompt.  To turn the virtual machine off (without deleting anything), type **vagrant halt**. If you do this, you'll need to run **vagrant up** again before you can log into it.


Now that you have Vagrant up and running type "vagrant ssh" to log into your VM.  change to the /vagrant directory by typing "cd /vagrant". This will take you to the shared folder between your virtual machine and host machine.


Type **ls** to ensure that you are inside the directory that contains project.py, database_setup.py, and two directories named 'templates' and 'static'.


Now type **python database_setup.py** to initialize the database.


Type **python lotsofitems.py** to populate the database with departments and category items. 


Type **python project.py** to run the Flask web server.


In your browser visit **http://localhost:5000** to view the sporting goods catalog app. 
 

click the login button at the top left and login with your google plus or facebook account.


You should be able to view all items's but you are not authorized to add, edit or delete any of the Department category item's except those you create. 


Create a new Department and name it what you would like.


Add, edit and delete items within your new Department Category to test out CRUD functionality


Use the logout button at the top right to logout of the app and then see if you can add any items to the department you created.

