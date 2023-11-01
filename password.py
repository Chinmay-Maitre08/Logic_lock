import shutil
import os
import time

# Source and destination folder paths
source_folder = 'files'
destination_folder = 'backups'

# Check if the "backups" folder exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print("Destination folder created.")

# Change folder permissions to read-write
os.chmod(destination_folder, 0o755)

# List all files in the source folder
files = os.listdir(source_folder)

# Copy files to the destination folder
for file in files:
    source_file = os.path.join(source_folder, file)
    destination_file = os.path.join(destination_folder, file)

    if os.path.exists(destination_file):
        print(f"Updating file: {file}")
    else:
        print(f"Copying file: {file}")

    shutil.copy(source_file, destination_file)

print("Files copied to the destination folder.")

# Set file permissions to read-only
for file in files:
    destination_file = os.path.join(destination_folder, file)
    os.chmod(destination_file, 0o444)

# Set a password for the folder (you can change this password)
correct_password = "1234"

# Initialize a variable to track elapsed time
start_time = time.time()

# Initialize a variable to track the number of attempts
attempts = 0

# Loop until the correct password is entered or 60 seconds are exceeded
while time.time() - start_time < 60:
    password_attempt = input("Enter the password to make changes to the 'backups' folder: ")
    attempts += 1

    if password_attempt == correct_password:
        break
    else:
        print("Incorrect password. Please try again.")

if time.time() - start_time >= 60:
    print("Time exceeded. You are not allowed to make changes to the files.")
    exit(1)

# If the correct password is entered, allow making changes
# Remove read-only permission from the files
for file in files:
    destination_file = os.path.join(destination_folder, file)
    os.chmod(destination_file, 0o644)  # This grants read-write permissions to the owner of the file

# Here, you can perform any edit operations you need on the files in the "backups" folder.
print("Password accepted. You can now make changes to the files in the 'backups' folder.")
print(f"Number of attempts: {attempts}")

# After performing the operations, you can set the files back to read-only if needed.

# Restore folder permissions to read-only
os.chmod(destination_folder, 0o555)
