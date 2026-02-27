import os
from google.genai import types

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
        
        
        parent_dir = os.path.dirname(target_file)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
        
        with open(target_file, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        

        
    except Exception as e:
        return f'Error: {e}'

# Declare the available "write_file" function for the LLM to use in a type format
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=f"Write new or overwrite existing file in a specified directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File name of target file",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description='Contents to be written to target file',
            ),
        },
    ),
)