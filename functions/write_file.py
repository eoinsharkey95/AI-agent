import os

def write_file(working_directory, file_path, content):
    
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        #print(f'working_dir = {working_dir_abs}')
        #print(f'target_file = {target_file}')

        valid_target_dir = os.path.commonpath([target_file, working_dir_abs]) == working_dir_abs
        
        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            # e.g. passing file_path = "/bin/cat" or "../test_get_files_info.py"

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(file_path, exist_ok=True)
        with open(target_file, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        

        
    except Exception as e:
        return f'Error: {e}'
    