# AsyncSyncWrap: A Library for Wrapping Synchronous Functions 
AsyncSyncWrap is a Python library that simplifies the process of integrating Asynchronous functions into synchronous codebases. It provides a decorator, syncwrap, that allows you to seamlessly use asynchronous functions within synchronous environments. This library is particularly useful when you need to work with legacy code or external libraries where one requires async and the other does not.


# Installation
You can easily install AsyncSyncWrap via pip:

```bash
pip install syncwrap
```  

## Usage
The core feature of AsyncSyncWrap is the syncwrap decorator:  

```python
from syncwrap import syncwrap

#wrap a given function
@syncwrap
async def my_sync_function():
    # call asyncronous code etc.
    await ...
    return 1

#within standard syncrounous code use without needing to await
result = my_sync_function()
```

Option timeout:
```python
@syncwrap(timeout=2.0)
def my_slow_sync_function():
    ...
```

Alternativly with an external library to avoid extra wrapper functions:
```python
# Wrap and call the external asynchronous function inline for testing
result = syncwrap(external_async_function)(*args, **kwargs)
```
