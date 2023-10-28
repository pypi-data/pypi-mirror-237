# Python Debugging Decorators / Python调试装饰器

## 概览 / Overview

这个Python库提供了一系列用于调试的装饰器，用于追踪函数和方法调用，记录异常，以及注释代码流程。可用的装饰器有：

- `universal_exception_logger`: 记录由装饰的函数或类的方法抛出的任何异常。
- `universal_decorator`: 一个可配置的装饰器，可用于各种调试注释。
- `debug_trace_class`: 为类的所有可调用方法添加追踪。

This Python library provides a collection of debugging decorators to assist you in tracing function and method calls, logging exceptions, and annotating code flow. The available decorators are:

- `universal_exception_logger`: Logs any exceptions that are thrown by the decorated function or methods of the decorated class.
- `universal_decorator`: A configurable decorator that can be used for various debug annotations.
- `debug_trace_class`: Adds tracing to all callable methods of a class.

## 安装 / Installation

克隆仓库或下载源代码。在你的Python脚本中导入装饰器。

Clone the repository or download the source code. Import the decorators into your Python script.

## 使用方法 / Usage

### 通用异常记录器 / Universal Exception Logger

要记录函数或类的所有方法抛出的异常，使用`universal_exception_logger`。

```python
from your_library import universal_exception_logger

@universal_exception_logger
def your_function():
    # Your code here
```

对于类：

```
@universal_exception_logger
class YourClass:
    # Your methods here
```

To log exceptions thrown by a function or all methods of a class, use `universal_exception_logger`.

```
from your_library import universal_exception_logger

@universal_exception_logger
def your_function():
    # Your code here
```

For classes:

```
@universal_exception_logger
class YourClass:
    # Your methods here
```

### 通用装饰器 / Universal Decorator

`universal_decorator`可以使用各种选项进行自定义。这里有一个简单的示例：

```
from your_library import universal_decorator

@universal_decorator(color="red")
def another_function():
    # Your code here
```

The `universal_decorator` can be customized using various options. Here is a simple example:

```
from your_library import universal_decorator

@universal_decorator(color="red")
def another_function():
    # Your code here
```

### 调试追踪类 / Debug Trace Class

要为类的所有可调用方法添加追踪，使用`debug_trace_class`。

```
from your_library import debug_trace_class

@debug_trace_class
class YourClass:
    # Your methods here
```

To add tracing to all callable methods of a class, use `debug_trace_class`.

```
from your_library import debug_trace_class

@debug_trace_class
class YourClass:
    # Your methods here
```

## 调试颜色代码 / Debugging Color Codes

在某些装饰器中，你可以指定颜色。可用选项有：

- 黑色 / black
- 红色 / red
- 绿色 / green
- 黄色 / yellow
- 蓝色 / blue
- 品红 / magenta
- 青色 / cyan
- 白色 / white

## 示例 / Examples

源代码中包含了一些注释掉的示例。取消注释它们以查看装饰器的效果。

A few examples are included as comments in the source code. Uncomment them to see the decorators in action.

## 许可 / License

本项目根据MIT许可证进行许可 - 有关详细信息，请参阅[LICENSE.md](https://chat.openai.com/c/LICENSE.md)文件。

This project is licensed under the MIT License - see the [LICENSE.md](https://chat.openai.com/c/LICENSE.md) file for details.

```
你可以根据需要进行适当的修改或添加其他信息。这个README应该为使用你的库的人提供足够的信息。
```