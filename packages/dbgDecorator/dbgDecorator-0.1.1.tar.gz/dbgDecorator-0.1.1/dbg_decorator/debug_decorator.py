import inspect
import os
import functools

# 定义颜色代码
DEBUG_BLACK = "\033[30m"
DEBUG_RED = "\033[31m"
DEBUG_GREEN = "\033[32m"
DEBUG_YELLOW = "\033[33m"
DEBUG_BLUE = "\033[34m"
DEBUG_MAGENTA = "\033[35m"
DEBUG_CYAN = "\033[36m"
DEBUG_WHITE = "\033[37m"
DEBUG_RESET = "\033[0m"
DEBUG_END = "\033[0m"

DEBUG_BYPASS = True


def universal_exception_logger(obj):
    if inspect.isclass(obj):
        return ExceptionLoggerForAllMethods(obj)

    elif inspect.isfunction(obj):
        @functools.wraps(obj)
        def wrapper(*args, **kwargs):
            class_name = ''
            if args:
                class_name = args[0].__class__.__name__
            return exception_logger_decorator(class_name, obj)(*args, **kwargs)

        return wrapper

    else:
        raise TypeError("Decorated object must be a function or a class")


def exception_logger_decorator(class_name, func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"方法 {class_name}.{func.__name__} 异常终止，原因是：{DEBUG_RED}{str(e)}{DEBUG_END}")
            raise  # 重新抛出捕获的异常
    return wrapper


def ExceptionLoggerForAllMethods(cls):
    for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
        setattr(cls, name, exception_logger_decorator(cls.__name__, method))
    return cls


def debug_trace_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        caller_frame = inspect.currentframe().f_back
        frame_info = inspect.getframeinfo(caller_frame)

        # 获取调用者信息
        if 'self' in caller_frame.f_locals:
            caller_self = caller_frame.f_locals['self']
            caller_info = f"{caller_self.__class__.__name__}.{frame_info.function}"
        else:
            caller_info = frame_info.function

        print(f"--> {caller_info} 调用 {func.__name__}")

        result = func(*args, **kwargs)

        print(f"<-- {func.__name__} 由 {caller_info} 返回")

        return result

    return wrapper


def debug_trace_calls_all(depth=0, max_depth=10, use_class_method_format=True):
    """装饰器工厂，用于跟踪函数调用"""
    def actual_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal depth
            if depth > max_depth:
                return func(*args, **kwargs)

            # 获取调用方的帧信息
            caller_frame = inspect.currentframe().f_back.f_back
            frame_info = inspect.getframeinfo(caller_frame)

            indent = ' ' * depth  # 使用空格来表示当前调用的深度

            # 获取调用方信息
            if 'self' in caller_frame.f_locals:
                caller_self = caller_frame.f_locals['self']
                caller_info = f"{caller_self.__class__.__name__}.{frame_info.function}"
            else:
                caller_info = frame_info.function

            method_info = func.__name__

            print(f"{indent}--> {caller_info} 调用 {method_info}")

            depth += 4
            result = func(*args, **kwargs)
            depth -= 4

            print(f"{indent}<-- {method_info} 由 {caller_info} 返回")

            return result
        return wrapper
    return actual_decorator

# 装饰整个类的所有方法
def debug_trace_class(cls):
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value):
            setattr(cls, attr_name, debug_trace_calls_all()(attr_value))
    return cls


def debug_decorator(color=None, show_full_path=False, show_path=False, show_class_name=True):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            if not DEBUG_BYPASS:
                color_code = {
                    "black": DEBUG_BLACK,
                    "red": DEBUG_RED,
                    "green": DEBUG_GREEN,
                    "yellow": DEBUG_YELLOW,
                    "blue": DEBUG_BLUE,
                    "magenta": DEBUG_MAGENTA,
                    "cyan": DEBUG_CYAN,
                    "white": DEBUG_WHITE
                }.get(color, "")
                class_name = ""
                if show_class_name and args:
                    class_name = f"{args[0].__class__.__name__}."
                frame_info = inspect.getframeinfo(inspect.currentframe().f_back)
                func_line_no = inspect.getsourcelines(func)[1]
                file_path = frame_info.filename if show_full_path else os.path.basename(frame_info.filename)
                file_path_str = f"文件名: {file_path }" if show_path else ""
                print(f"{color_code}" + file_path_str + f" 进入函数: {class_name}{func.__name__}" + f" 行号: {func_line_no}" + DEBUG_END)
                result = func(*args, **kwargs)
                print(f"{color_code}" + file_path_str + f" 退出函数: {class_name}{func.__name__}" + DEBUG_END)
            else:
                result = func(*args, **kwargs)
            return result

        return wrapper

    return actual_decorator


def decorate_all_in_class(color=None):
    def actual_decorator(cls):
        for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
            setattr(cls, name, debug_decorator(color)(method))
        return cls

    return actual_decorator


def decorate_skip_inside_fun_in_class(color=None):
    def actual_decorator(cls):
        for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
            if not name.startswith('__'):
                setattr(cls, name, debug_decorator(color)(method))
        return cls

    return actual_decorator


def decorate_in_class(color=None):
    def actual_decorator(cls):
        for name, method in cls.__dict__.items():  # 只获取当前类定义的方法
            if inspect.isfunction(method):
                setattr(cls, name, debug_decorator(color)(method))
        return cls

    return actual_decorator


def universal_decorator(color=None, class_decorator_type='current_class_only'):
    def choose_decorator(obj):
        if inspect.isfunction(obj):
            return debug_decorator(color)(obj)
        elif inspect.isclass(obj):
            if class_decorator_type == 'all':
                return decorate_all_in_class(color)(obj)
            elif class_decorator_type == 'skip_inside':
                return decorate_skip_inside_fun_in_class(color)(obj)
            elif class_decorator_type == 'current_class_only':
                return decorate_in_class(color)(obj)
        return obj
    return choose_decorator

'''
class MyClass:
    def method1(self):
        print("Inside method1")

    def method2(self):
        print("Inside method2")

@decorate_in_class(color="red")
class MyDerivedClass(MyClass):
    def method3(self):
        print("Inside method3")


obj = MyDerivedClass()
obj.method1()
obj.method2()
obj.method3()
'''
'''
# 使用装饰器
def my_function():
    print("Inside my_function")
    another_function()

@debug_trace_calls()
def another_function():
    print("Inside another_function")


def another_function3():
    my_function()

def another_function4():
    another_function3()


another_function4()
'''