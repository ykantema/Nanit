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
- Mobile-only: `pytest -k mobile --platform-name android` or `pytest -k mobile --platform-name ios`
- Backend-only: `pytest -k backend --run-backend-only`
- Integrated: `pytest -k integrated --platform-name android --run-backend` or `pytest -k integrated --platform-name ios --run-backend`

## Key Classes
- `MobileSession`: Manages mobile actions (login, navigation, visibility checks).
- `StreamingValidator`: Polls backend `/health` endpoint.

## Example Command
Run integrated test:
```bash
pytest tests/test_streaming_integration.py --platform-name android --run-backend
pytest tests/test_streaming_integration.py --platform-name ios --run-backend
```
