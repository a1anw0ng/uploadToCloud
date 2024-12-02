import os

# Get the folder path from the user
folder_path = input("Enter the path to the folder: ")

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Construct the full file path
    file_path = os.path.join(folder_path, filename)
    
    # Check if it's a file (not a directory)
    if os.path.isfile(file_path):
        # Remove the last 10 characters from the filename, including the file extension
        new_name = filename[:-11]

        # Construct the new full file path
        new_file_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(file_path, new_file_path)
        print(f'Renamed: {filename} -> {new_name}')