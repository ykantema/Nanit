# Streaming Integration Tests

## Purpose
Validate mobile and backend streaming states agree:
- Mobile: Login, navigate to stream, verify visibility.
- Backend: `/health` reports `status = streaming`.
- Validation: Both layers agree.

## Test Flow
1. Mobile: Login → Navigate to stream → Check visibility.
2. Backend: Poll `/health` for `status = streaming`.
3. Validator: Compare mobile and backend states.

## Execution Modes
- Mobile-only: `pytest -k mobile --platform-name android --layer ui` or `pytest -k mobile --platform-name ios --layer ui`
  - `--layer ui`: Runs only mobile UI tests.
- Backend-only: `pytest -k backend --layer api`
  - `--layer api`: Runs only backend API tests.
- Both: `pytest -k integrated --platform-name android --layer both` or `pytest -k integrated --platform-name ios --layer both`
  - `--layer both`: Runs both mobile UI and backend API tests.

## Key Classes
- `MobileSession`: Manages mobile actions (login, navigation, visibility checks).
- `StreamingValidator`: Polls backend `/health` endpoint.

## Environment Overrides
- Use environment variables to override test parameters:
  - `TEST_PLATFORM_NAME`: Set platform (e.g., `android`, `ios`).
  - `TEST_RUN_BACKEND`: Enable backend checks (e.g., `true`, `false`).

## Example Command
Run integrated test:
```bash
TEST_PLATFORM_NAME=android TEST_RUN_BACKEND=true pytest tests/test_streaming_integration.py
TEST_PLATFORM_NAME=ios TEST_RUN_BACKEND=true pytest tests/test_streaming_integration.py
```
