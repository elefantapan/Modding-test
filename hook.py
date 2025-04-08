import sys

command_instances = []

def HOOK(func_name, hook_code, position='before'):
    """
    Hooks a method of the Command class and injects custom code either before, after, or completely replaces the original function.
    
    func_name: The name of the method to hook (e.g., 'callontick').
    hook_code: The code (function) to inject or replace with.
    position: 'before', 'after', or 'replace' to determine where to place the hook.
    """
    def apply_hook_to_method(command_instance):
        target_func = getattr(command_instance, func_name, None)

        if not target_func:
            print(f"Method '{func_name}' not found in Command instance!")
            return

        # Define a wrapper function to inject custom code
        def wrapper(*args, **kwargs):
            if position == 'before':
                hook_code(*args, **kwargs)
                return target_func(*args, **kwargs)
            elif position == 'after':
                result = target_func(*args, **kwargs)
                hook_code(*args, **kwargs)
                return result
            elif position == 'replace':
                return hook_code(*args, **kwargs)
            else:
                print(f"Invalid position: {position}")
                return target_func(*args, **kwargs)

        setattr(command_instance, func_name, wrapper if position != 'replace' else hook_code)

    for command_instance in command_instances:
        apply_hook_to_method(command_instance)

def track_command_instances(frame, event, arg):
    if event == "call" and frame.f_code.co_name == "__init__":
        if "Command" in frame.f_globals:
            command_instances.append(frame.f_locals.get('self'))
    return track_command_instances

sys.settrace(track_command_instances)
