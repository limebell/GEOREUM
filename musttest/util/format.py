

def print_formatter(inner_func):
    def wrapper_func(formatting, *args, **kwargs):
        tmp_str = "="*102
        func_name = inner_func.__name__
        tmp_str = tmp_str[:len(tmp_str)-len(func_name)//2-1]
        tmp_str = f'{tmp_str} {func_name} {tmp_str}'
        print(tmp_str)
        for item in formatting:
            print(item)
        inner_func(*args, **kwargs)
    return wrapper_func
