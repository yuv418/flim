import sys
import os
import getpass
import json

from termcolor import colored

# Add path that is required to import things from the flim app.
sys.path.append(os.getcwd() + "/app")


print(colored("Install Flim", "green"))

# Create a user

print("First, let's create an administrator for the forum.\n")

firstname = input(colored("First Name: ", "blue"))
lastname = input(colored("Last Name: ", "blue"))
email = input(colored("E-Mail Address: ", "blue"))

print()

username = input(colored("Username: ", "red"))
password = getpass.getpass(colored("Password: ", "red"))

# Get database information

print("\nNext, let's get some info about your database.")

db_hostname = input(colored("Hostname: ", "blue"))
db_name = input(colored("Database Name: ", "blue"))

print()

db_username = input(colored("Username: ", "red"))
db_password = getpass.getpass(colored("Password: ", "red"))

print()

# We want the port, it must be an integer

port_is_invalid = True

while port_is_invalid:
	try:
		db_port = int(input(colored("Port: ", "blue")))
		port_is_invalid = False
	except ValueError:
		print(colored("That is not a valid port. Please try again.", "red"))

# We are now going to create the dictionary and write the JSON file.

config = {}

config['database'] = {}

config['database']['hostname'] = db_hostname
config['database']['username'] = db_username
config['database']['password'] = db_password
config['database']['port'] = db_port
config['database']['name'] = db_name

# Write the JSON file in app/config.json

with open(os.path.join(os.getcwd(), "app", "config.json"), 'w+') as config_file:
	json.dump(config, config_file, indent=4, sort_keys=True)

# Print a status message about this

print(f"({colored('i:conf', 'green')}) wrote config file")


# Set environment variables so that the db can connect

os.environ["FLIM_DB_NAME"] = db_name
os.environ["FLIM_DB_HOST"] = db_hostname
os.environ["FLIM_DB_PORT"] = str(db_port)
os.environ["FLIM_DB_PROVIDER"] = "mysql"
os.environ["FLIM_DB_USERNAME"] = db_username
os.environ["FLIM_DB_PASSWORD"] = db_password

# Import the db module and and create the database

from app import db
db.create_all() # We need to handle the sqlalchemy.exc.OperationError here

print(f"({colored('i:db', 'green')}) populated database")

# Create the administrator group

from app.models import Group

admin_group = Group(name="Administrators")
db.session.add(admin_group)
db.session.commit()

print(f"({colored('i:admin', 'green')}) created admin group")

# Create the admin user

from app.models import Users

admin_user = Users(first_name=firstname, last_name=lastname, email=email, username=username)
admin_user.set_password(password)
admin_user.add_to_group(Group.admin_group())

db.session.add(admin_user)
db.session.commit()

print(f"({colored('i:admin', 'green')}) created admin user")

print(colored('Flim was installed successfully.', 'green'))



















