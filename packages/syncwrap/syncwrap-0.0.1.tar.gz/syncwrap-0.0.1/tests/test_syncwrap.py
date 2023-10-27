import asyncio
from syncwrap import syncwrap

def test_import_syncwrap():
    assert syncwrap

def test_standard_function():

    @syncwrap
    def standard_function(a, b=2):
        return a + b

    assert standard_function(1, 2) == 3
    
def test_standard_function_kwargs():

    @syncwrap
    def standard_function(a, b=2):
        return a + b

    assert standard_function(a=1, b=2) == 3

def test_async_function():

    @syncwrap
    async def async_function(a, b=2):
        return a + b

    # call
    result = async_function(1, 2)
    assert result == 3

    # call using await
    async def temp_awaiter():
        return await async_function(1, 2)
    result = asyncio.run(temp_awaiter())

    assert result == 3

def test_within_main_loop():
    async def main():
        @syncwrap
        async def async_function(a, b=2):
            return a + b

        result = await async_function(1, 2)
        assert result == 3

    asyncio.run(main())

# Chat GPT generated tests :
def test_standard_function_without_arguments():
    @syncwrap
    def standard_function():
        return 42

    assert standard_function() == 42

def test_async_function_without_arguments():
    @syncwrap
    async def async_function():
        return 42

    result = async_function()
    assert result == 42

def test_standard_function_with_exception():
    @syncwrap
    def standard_function():
        raise ValueError("An error occurred")

    try:
        result = standard_function()
    except Exception as e:
        assert isinstance(e, ValueError)
        assert str(e) == "An error occurred"
    else:
        assert False, "Expected an exception, but none was raised"

def test_async_function_with_exception():
    @syncwrap
    async def async_function():
        raise ValueError("An error occurred")

    try:
        result = async_function()
    except Exception as e:
        assert isinstance(e, ValueError)
        assert str(e) == "An error occurred"
    else:
        assert False, "Expected an exception, but none was raised"

def test_standard_function_with_multiple_decorators():
    def decorator1(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * 2
        return wrapped

    def decorator2(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            return result + 1
        return wrapped

    @decorator1
    @decorator2
    @syncwrap
    def standard_function(a, b=2):
        return a + b

    result = standard_function(1, 2)
    expected = ((1 + 2) + 1) * 2
    assert result == expected

def test_async_function_with_multiple_decorators():
    def decorator1(func):
        async def wrapped(*args, **kwargs):
            result = await func(*args, **kwargs)
            return result * 2
        return wrapped

    def decorator2(func):
        async def wrapped(*args, **kwargs):
            result = await func(*args, **kwargs)
            return result + 1
        return wrapped

    @syncwrap
    @decorator1
    @decorator2
    async def async_function(a, b=2):
        return a + b

    result = async_function(1, 2)
    expected = ((1 + 2) + 1) * 2
    assert result == expected


def test_standard_function_with_return_value():
    @syncwrap
    def standard_function():
        return "Hello, World!"

    result = standard_function()
    assert result == "Hello, World!"

def test_async_function_with_return_value():
    @syncwrap
    async def async_function():
        return "Hello, World!"

    result = async_function()
    assert result == "Hello, World!"

def test_nested_standard_function_calls():
    @syncwrap
    def add(a, b):
        return a + b

    @syncwrap
    def multiply(x, y):
        return x * y

    result = multiply(add(2, 3), 4)
    assert result == 20

def test_nested_async_function_calls():
    @syncwrap
    async def add(a, b):
        return a + b

    @syncwrap
    async def multiply(x, y):
        return x * y

    @syncwrap
    async def nested():
        return await multiply(await add(2, 3), 4)

    result = nested()
    assert result == 20

def test_async_function_with_timeout():
    @syncwrap(timeout=1)  # Set a 1-second timeout
    async def async_function():
        await asyncio.sleep(2)  # Sleep for 2 seconds
    try:
        result = async_function()
    except asyncio.TimeoutError:
        assert True
    except Exception as e:
        print(f'Exception: {e}')
        assert False, "Expected a TimeoutError, but none was raised"
    else:
        print(f'No exception raised, result: {result}')
        assert False, "Expected a TimeoutError, but none was raised"

def test_sync_function_with_timeout():
    # timeouts cannot be used with sync functions,
    # so the timeout parameter should be raised
    try:
        @syncwrap(timeout=1)  # Set a 1-second timeout
        def sync_function():
            import time
            time.sleep(10)  # Sleep for 2 seconds
        
        result = sync_function()
    except ValueError:
        assert True
    except Exception as e:
        assert False, "Expected a ValueError, but {e} was raised"
    else:
        assert False, "Expected a ValueError, but none was raised"
        

def test_inline_function():
    # Suppose you have an asynchronous function from an external library
    async def external_async_function(a, b):
        await asyncio.sleep(2)
        return a + b

    # Wrap and call the external asynchronous function inline for testing
    result = syncwrap(external_async_function)(1, 2)

    # Assert the result to perform the unit test
    assert result == 3
    
def test_recusive_call():
    #the first call will be sync, the rest will be async

    @syncwrap
    async def recursive_function(n):
        if n == 0:
            return 0
        else:
            return n + await recursive_function(n - 1)

    result = recursive_function(10)
    assert result == 55

