import os
import shutil

def sync_folders(source, destination):

    # Check source folder
    if not os.path.isdir(source):
        print("Source folder not found!")
        return

    # Create backup folder if missing
    os.makedirs(destination, exist_ok=True)

    # Read files from source
    for file in os.listdir(source):

        source_path = os.path.join(source, file)
        destination_path = os.path.join(destination, file)

        # Copy only files
        if os.path.isfile(source_path):

            if not os.path.exists(destination_path):
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {file}")

            elif os.path.getmtime(source_path) > os.path.getmtime(destination_path):
                shutil.copy2(source_path, destination_path)
                print(f"Updated: {file}")

    print("Synchronization Completed!")