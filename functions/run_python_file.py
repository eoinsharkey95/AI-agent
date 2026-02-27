import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_dir = os.path.commonpath([ target_file, working_dir_abs]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        #print(f'target_file[-3:] = {target_file[-3:]}')
        target_file_type = target_file.split(".", maxsplit=1)
        if target_file_type[1] != "py":
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args != None:
            command.extend(args)
        
        results = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30
        )

        return_code = f'Process exited with code {results.returncode}\n'
        
        if results.stdout == "" and results.stderr == "":
            output = "No output produced\n"
        else:
            output = f'STDOUT: "{results.stdout}"\nand\nSTDERR: "{results.stderr}"\n'

        return return_code + output +'\n--------------------\n'
    
    except Exception as e:
        return f'Error: executing Python file: {e}'

# Declare the available "run_python_file" function for the LLM to use in a type format    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=f"Runs specified python function file in specified directory in relation to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File name of target file",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description='Additional arguments needed to run a function. (e.g. for calculator function ["3 + 5"])',
            ),
        },
    ),
)