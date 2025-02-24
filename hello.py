import os
from datetime import datetime
 
# Specify the directory where the files are located
directory = 'files'
 
# Get a list of all filenames in the specified directory
filenames = os.listdir(directory)
 

for filename in filenames:
    
    filepath = os.path.join(directory, filename)
 
    
    current_date = datetime.now().strftime("%Y-%m-%d")
 
    
    new_filename = f'{filename[:-4]}-{current_date}.txt'
 
    
    new_filepath = os.path.join(directory, new_filename)
    
    
    os.rename(filepath, new_filepath)
    
    
    print(f"Renamed {filename} to {new_filename}")
 
print("File renaming completed!")