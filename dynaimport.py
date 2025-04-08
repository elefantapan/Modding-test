import os
import importlib.util
import sys

# Function to dynamically import a Python file as a module
def dynamic_import(module_name, module_path):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# Function to discover and import all Python files in a directory and subdirectories
def discover_and_import_modules(base_path, command_list):
    for dirpath, dirnames, filenames in os.walk(base_path):  # Walk through all directories and files
        for filename in filenames:
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = os.path.splitext(filename)[0]
                module_path = os.path.join(dirpath, filename)
                print(f"Importing module: {module_name}")
                module = dynamic_import(module_name, module_path)

                # After importing the module, check if it has a 'commands' list
                if hasattr(module, 'commands'):
                    for cmd in module.commands:
                        command_list.append(cmd)
