#!/usr/bin/python3

#############################################################################
# This is a firewall manager written in Python with a GUI that has          #
# the ability to give users a interface to block services/ports, IP         #
# addresses, and to manage the Firewall. The Firewall manager relies on     #
# IPtables and the package ufw. This program has been tested on             #
# Parrot OS a Ubuntu Distro and Kali a Debian Distro which leads me         #
# to believe that this software will work on most Debian and Ubuntu Distros.#
# Created by Jacob Silva                                                    #
#############################################################################

# Needed Libraries
from tkinter import *
import tkinter as tk
from tkinter import Tk, scrolledtext, Menu, filedialog, messagebox, Text, simpledialog, filedialog
import os

# Quit Function
def quit():
	# Asks user to quit
	quit_app = tk.messagebox.askquestion ('Quit','Would you like to close the application?')
    
	# If yes brake loop
	if quit_app == 'yes':
		root.destroy()

	# Else tell them they will return to main menu
	else:
		tk.messagebox.showinfo('Return','You will now return to the main menu')
	
# Check Dependencies function
def check_Dependencies():

	# Ask user if they would like to install dependencies
	dependencies = tk.messagebox.askquestion ('Check Dependencies','Would you like to check and install dependencies?')
    
	# If yes install ufw on Debian/Ubuntu Distros
	if dependencies == 'yes':
		os.system("sudo apt-get update && sudo apt-get install ufw")
		tk.messagebox.showinfo('Dependencies','All dependencies are now installed!')

	# Else prompt user to return to main menu
	else:
		tk.messagebox.showinfo('Return','You will now return to the main menu')
 
# Mange Firewall function 
def manage_Firewall():
	
	# Ask user if they would like to View, Reset, Enable, or Disable the firewall
	firewall = simpledialog.askstring("Manage Firewall", "Would you like to (View|Reset|Enable|Disable) the firewall")
	
	# If View copy check status to output file so it can be processed in show info message box 
	if firewall == "View":
		# Do sudo ufw status command on terminal and output to /tmp/
		view = os.system("sudo ufw status > /tmp/output.txt")
		# Open output file
		f = open('/tmp/output.txt', 'r')
		# Read in variable
		file_contents = f.read() 
		tk.messagebox.showinfo('View', file_contents)
		f.close()
		# Remove file residue 
		os.system('rm /tmp/output.txt')
		 
	# If Reset do sudo ufw --force reset command
	if firewall == "Reset":
		os.system('sudo ufw --force reset')
		tk.messagebox.showinfo('Reset','Your firewall is now reset')
		
		
	# If enable do ufw --force enable command
	if firewall == "Enable":
		os.system("sudo ufw --force enable")
		tk.messagebox.showinfo('Enabled','Your firewall is now enabled')
	
	# If disable do ufw --force disable command
	if firewall == "Disable":	
		os.system("sudo ufw --force disable")
		tk.messagebox.showinfo('Disabled','Your firewall is now Disabled')
	
# Manage IPS function
def manage_IPS():

	# Ask user if they would like to Allow or Deny an IP address
	ips = simpledialog.askstring("Manage IPS", "Allow or Deny an IP address (Allow|Deny):")
	
	# If allow allow user input IP
	if ips == 'Allow':
		allow = simpledialog.askstring("Manage IPs", "Enter an IP to allow")
		
		allow1 = "sudo ufw allow from "
		allow2 = " to any"
		# allow3 var puts the whole command together
		allow3 = allow1 + allow + allow2
		os.system(allow3)
		
		# message2 var puts message var and allow together 
		message = " is now Allowed"
		message2 = allow + message
		tk.messagebox.showinfo('Allowed', message2)
		
	# If deny bloc user input IP  
	if ips == 'Deny':
		deny = simpledialog.askstring("Manage IPs", "Enter an IP to deny")
		
		deny1 = "sudo ufw deny from "
		deny2 = " to any"
		
		# deny3 var puts all variables together
		deny3 = deny1 + deny + deny2
		os.system(deny3)
		
		message = " is now denied"
		# message2 var puts deny and message var together
		message2 = deny + message
		tk.messagebox.showinfo('Denied', message2)

# Manage Rules function
def manage_Rules():

	# Asks user if they would like to Allow or  Block a Service
	rules = simpledialog.askstring("Manage Rules", "Allow or Block Service (Allow|Block)")

	# If allow ask user to enter port or service to allow 
	if rules == 'Allow':
		allow = simpledialog.askstring("Manage Rules", "Enter the port or service to allow")
		part1 = "sudo ufw allow "
		# part2 var puts commands together
		part2 = part1 + allow 
		os.system(part2)
		message = " is now allowed"
		message2 = "Servce/Port: "
		# Message 3 var puts message2, allow, and message vars into one for info box
		message3 = message2 + allow + message
		messagebox.showinfo('Allowed', message3)
		
	# If block ask user to enter port or service to block 
	if rules == 'Block':
		block = simpledialog.askstring("Manage Rules", "Enter the port or service to block")
		part1 = "sudo ufw deny "
		# part2 var puts command together
		part2 = part1 + block 
		os.system(part2)
		message = " is now blocked"
		message2 = "Servce/Port: "
		
		# message3 puts message together
		message3 = message2 + block + message
		messagebox.showinfo('Blocked', message3)

# Changelog function prints added features		
def change_Log():
		messagebox.showinfo('Changelog', 
'''
Version 0.1:
-Implemented Manage Rules
-Implemented Manage IPs
-Implemented Manage Firewall
-Implemented Check Dependencies
-Implemented Quit 
-Added About tab
-Added Credits in About tab
-Added About Us in About tab
-Added Changelog in About tab
''')
	
# Credits function displays the contributor of the project
def credits():
	messagebox.showinfo('Credits', 'The only contributor to this Firewall Manager is Jacob Silva')

# AboutUs function gives some backstory to the program
def aboutUS():
	messagebox.showinfo('About Us', "I first started off learning Python in my second semester at UAT with the course Professor Stephen Gose taught. I'm currently in my fifth semester moving on to my sixth semester. The last GUI I wrote was for my Python final back in my second semester I wrote a notepad text editor in Python. This project I've started is for my Shell Scripting For Hackers final which is being taught by Professor Greg Miles.")

# Starts loop
root = Tk()

# Gives project a title
root.title("Linux Firewall Manager")

# Potitions first label along with font text and placement
label1 = Label(root, text="Linux Firewall Manager", font='Helvetica 18 bold')
label1.place(x=65, y=0)

# Potitions second label along with font text and placement
label2 = Label(root, text="Manage Rules", font='Helvetica 9 bold')
label2.place(x=80, y=70)

# Potitions manageRules button along with font text and placement and call manage_Rules function
manageRules = Button(text="        OK        ", font='Helvetica 9', command=manage_Rules)
manageRules.place(x=220, y=70)

# Potitions third label along with font text and placement
label3 = Label(root, text="Manage IPs", font='Helvetica 9 bold')
label3.place(x=80, y=110)

# Potitions manageIPs button along with font text and placement and calls manage_IPS function
manageIPs = Button(text="        OK        ", font='Helvetica 9', command=manage_IPS)
manageIPs.place(x=220, y=110)

# Potitions fourth label along with font text and placement
label4 = Label(root, text="Manage Firewall", font='Helvetica 9 bold')
label4.place(x=80, y=150)

# Potitions manageFirewall button along with font text and placement and calls manage_Firewall function
manageFirewall = Button(text="        OK        ", font='Helvetica 9', command=manage_Firewall)
manageFirewall.place(x=220, y=150)

# Potitions Fifth label along with font text and placement
label5 = Label(root, text="Check Dependencies", font='Helvetica 9 bold')
label5.place(x=80, y=190)

# Potitions checkDependencies button along with font text and placement and calls checkDependencies function
checkDependencies = Button(text="        OK        ", font='Helvetica 9', command=check_Dependencies)
checkDependencies.place(x=220, y=190)

# Potitions sixth label along with font text and placement
label6 = Label(root, text="Quit", font='Helvetica 9 bold')
label6.place(x=80, y=230)

# Potitions quit button along with font text and placement and calls quit function
quit = Button(text="        OK        ", font='Helvetica 9', command=quit)
quit.place(x=220, y=230)


menu = Menu(root)
root.config(menu=menu)

# Creats dopdown menu
subMenu = Menu(menu)
menu.add_cascade(label="About",menu=subMenu)
# Creates Credits tab and calls credits function
subMenu.add_command(label="Credits", command=credits)
# Creates About Us tab and calls aboutUS function
subMenu.add_command(label="About Us", command=aboutUS)
# Creates Changelog tab and calls change_Log function
subMenu.add_command(label="Changelog", command=change_Log)

# Creates the size of the application
root.geometry("400x350")

# End of Loop
root.mainloop()