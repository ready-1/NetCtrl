# Testing Guide for NetCtrl CMS Backend

## Test Types

1. **Sync Tests**: Direct tests using TestClient from FastAPI
2. **Async Tests**: Tests using AsyncClient with pytest.mark.asyncio

## Known Issues

Some tests using async fixtures have been skipped due to issues with coroutines and async generators.
See `../ASYNC_TEST_FIXING_GUIDE.md` for more information on how to fix these issues.

## Running Tests

Run all tests:
```bash
pytest -v
```

Run only synchronous tests:
```bash
pytest -v -k "not asyncio"
```

## Test Files

- `test_minimal.py`: Basic health check tests
- `test_working_auth.py`: Authentication tests (sync-only)
- `test_skipped_suite.py`: Placeholder for skipped complex async tests

## Fixtures

Most fixtures are defined in `conftest.py` and include:
- Database session management
- User creation
- Token generation

## Adding New Tests

When adding new tests:
1. Prefer synchronous tests when possible
2. For async tests, properly handle async generators and coroutines
3. Always use `await` with async functions
4. Consider using the helpers from `ASYNC_TEST_FIXING_GUIDE.md`
