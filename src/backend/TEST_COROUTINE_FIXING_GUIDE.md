# Test Suite Coroutine Fixing Guide

This guide documents the key issues fixed in the CMS backend test suite to resolve coroutine and syntax errors.

## Main Issues Fixed

1. **Missing SQLAlchemy User Database Extension**
   - Added `SQLAlchemyUserDatabaseWithUsername` class in `app/db/user_db.py` to implement the `get_by_username` method
   - Properly handled async generator sessions within queries

2. **Improved UserManager Class**
   - Added proper exception handling for async generator sessions
   - Added missing `not_exists_exception` attribute 
   - Fixed robustness in `create` and `authenticate` methods

3. **Syntax Errors in Test Files**
   - Fixed missing commas in function parameters
   - Fixed missing commas in dictionary literals
   - Fixed missing commas in API calls
   - Fixed f-string API paths

4. **Coroutine Handling in Tests**
   - Added `anext` helper function to handle async generators
   - Fixed `await` usage for async generators (`await anext(client)`)
   - Removed stray awaits outside of functions
   - Handled mock coroutines properly

5. **MockDB Improvements**
   - Better handling of mock user fixtures
   - Proper AsyncMock configuration
   - Proper side_effect usage

## Common Error Patterns

### "Coroutine was never awaited" Warnings

These warnings indicate that an async function was called but its results were not awaited with `await`. Fix by ensuring:

```python
# Bad:
result = async_function()  # Warning: coroutine was never awaited

# Good:
result = await async_function()
```

### "'async_generator' object has no attribute 'execute'" Errors

These errors occur when trying to call a method on an async generator instead of awaiting it first:

```python
# Bad:
result = session.execute(query)  # Error if session is an async generator

# Good:
session_value = await anext(session) if hasattr(session, "__anext__") else session
result = await session_value.execute(query)
```

### SQLAlchemy Async Session Handling

When using FastAPI dependency injection with `yield`, sessions may be async generators:

```python
async def get_async_session():
    """This returns an async generator"""
    async with async_session_maker() as session:
        yield session  # This makes it an async generator

# When using the session, always handle both cases:
async def use_session(session):
    if hasattr(session, "__anext__"):
        session = await anext(session)
    # Now use the session normally
    result = await session.execute(...)
```

## Tools Used for Fixing

1. **fix_all_tests.py** - Python script that automatically fixes syntax and coroutine usage in all test files
2. **fix_syntax_errors.py** - Python script that fixes syntax errors in test files
3. **fix_test_files.sh** - Bash script to fix common patterns with sed

## Async Testing Best Practices

1. Always use `pytest.mark.asyncio` for async tests
2. Handle async generators with `await anext(generator)`
3. Properly mock async functions with `AsyncMock`
4. Make assertions adaptable to both sync and async contexts
5. Set up proper override patterns for FastAPI dependencies

## Related Files

- `app/db/user_db.py` - Extends SQLAlchemy user database with username support
- `app/auth/users.py` - Implements user authentication and management
- `app/tests/conftest.py` - Provides fixtures for all tests
- `app/tests/test_minimal.py` - Contains minimal tests that work without complex fixtures
