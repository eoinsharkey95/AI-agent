from google.genai import types
from functions.get_files_info import *
from functions.get_file_content import *
from functions.write_file import *
from functions.run_python_file import *

# Pull schemas for each function from their relevant .py file
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content, 
        schema_run_python_file,
        schema_write_file 
        ],
)

function_map = {
    "get_files_info" : get_files_info,
    "get_file_content" : get_file_content,
    "run_python_file" : run_python_file,
    "write_file" : write_file,
}

def call_function(function_call, verbose=False):
    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")

    # Assign the function name. If bool(function_call.name)=False, assign "" 
    function_name = function_call.name or ""

    # Error handling for unkown functions called, ensuring types.content variable returned 
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    # creates shallow copy, or empty dict if no args
    args = dict(function_call.args) if function_call.args else {}
    # Hard-code set the working_directory(?)
    args.update({"working_directory" : "./calculator"})

    # Call the specified function, returning a string output
    function_result = function_map[function_name](**args)
    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )




    