import os
import json




def write_to_protectremote_file(data, file_name=".protectremote"):
    try:
        home_directory = os.path.expanduser("~")
        file_path = os.path.join(home_directory, file_name)
        if not os.path.isfile(file_path):
            # Create the file if it doesn't exist
            with open(file_path, 'w') as file:
                file.write('')
                print(f"Created {file_path} because it didn't exist.")

        with open(file_path, 'w') as file:
            file.write(json.dumps(data))
        print(f"Data written to {file_name}")
    except Exception as e:
        print(f"Error writing to {file_name}: {e}")

def read_protectremote_file(file_name=".protectremote"):
    try:
        home_directory = os.path.expanduser("~")
        file_path = os.path.join(home_directory, file_name)
        with open(file_path, 'r') as file:
            content = file.read()
            content = json.loads(content) 
            print(f"Read from {file_name}: {content}")
            return content
    except Exception as e:
        print(f"Error reading from {file_name}: {e}")
        return None