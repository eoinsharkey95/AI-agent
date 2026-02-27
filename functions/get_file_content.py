import os
from config import *
from google.genai import types

def get_file_content(working_directory, file_path):
    
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        #print(f'working_dir = {working_dir_abs}')
        #print(f'target_file = {target_file}')

        valid_target_dir = os.path.commonpath([target_file, working_dir_abs]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            # e.g. passing file_path = "/bin/cat" or "../test_get_files_info.py"

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
            # if the target_file is not a file or not in the folder 

        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    
    except Exception as e:
        return f'Error: {e}'
    
    return content

# Declare the available "get_file_content" function for the LLM to use in a type format 
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Returns content of a specified in directory relative to the working directory, as string truncated to {MAX_CHARS} characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File name of target file",
            ),
        },
    ),
)