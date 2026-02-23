import os

def get_files_info(working_directory, directory="."):
    
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([target_dir, working_dir_abs]) == working_dir_abs
    #print(f'working_dir_abs: {working_dir_abs} \ntarget_dir: {target_dir} \nvalid_target_dir: {valid_target_dir}')


    if valid_target_dir == False:
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    if os.path.isdir(target_dir) == False:
        return(f'Error: "{directory}" is not a directory')

    content_lst = os.listdir(target_dir)
    content_str = []
    
    for item in content_lst:
        item_path = os.path.normpath(os.path.join(target_dir, item))

        file_size = os.path.getsize(item_path)
        is_dir = os.path.isdir(item_path)
        content_str.append(f'- {item}: file_size={file_size}, is_dir={is_dir}')

    return( '\n'.join(content_str))
    
