''' A library for wrapping sync functions in async coroutines. '''

# Standard library imports.
import asyncio

def syncwrap(asyncfunc=None, timeout=None):
    ''' Decorator to wrap a sync function and either run in the current
        event loop, or run in a new loop and wait for the result.
        optional timeout parameter to wait for the result.
    '''
    # Note: nested decorator function is required to pass parameters like timeout.
    def _syncwrap(asyncfunc):
        def wrapper(*args, **kwargs):
            try:
                # will raise a RuntimeError if no loop is running
                loop = asyncio.get_running_loop()
                return asyncio.wait_for(asyncfunc(*args, **kwargs), timeout)                 
            except RuntimeError:
                # Loop is not running, so create a new one.
                loop = asyncio.new_event_loop()
                return loop.run_until_complete(asyncio.wait_for(asyncfunc(*args, **kwargs), timeout))

        if not asyncio.iscoroutinefunction(asyncfunc):
            # If the function is not a coroutine, just return it.
            if timeout is None:
                return asyncfunc
            else:
                raise ValueError("timeout parameter can only be used with async functions")
        return wrapper
    if asyncfunc is None:
        return _syncwrap
    else:
        return _syncwrap(asyncfunc)
