"""
Mobile locator configuration for different platforms.
This module centralizes element IDs/attributes so automation code can pick
platform-specific locators from a single place.
"""

from typing import Dict, Any, Optional

LOCATORS: Dict[str, Dict[str, Dict[str, Any]]] = {
    "android": {

        "login_button": {
            "element_id": "login_button_android",
            "text": "Login",
            "attributes": {"accessibility_id": "login_button"},
        },
        "welcome_label": {
            "element_id": "welcome_label",
            "text": "Welcome",
            "attributes": {"accessibility_id": "welcome_label"},
        },
        "get_started": {
            "element_id": "get_started_button",
            "text": "Get Started",
            "attributes": {"accessibility_id": "get_started"},
        },
        "live_stream_label": {
            "element_id": "live_stream_label",
            "text": "Live Stream",
            "attributes": {"accessibility_id": "live_stream_label"},
        },
        "bitrate_label": {
            "element_id": "bitrate_label",
            "text": "1080p",
            "attributes": {"accessibility_id": "bitrate_label"},
        },
        "play_button": {
            "element_id": "play_button",
            "text": "Play",
            "attributes": {"accessibility_id": "play_button"},
        },
    },
    "ios": {
        "login_button": {
            "element_id": "login_button_ios",
            "text": "Login",
            "attributes": {"accessibility_id": "login_button"},
        },
        "username_input": {
            "element_id": "username_input_ios",
            "text": "",
            "attributes": {"accessibility_id": "username_input"},
        },
        "password_input": {
            "element_id": "password_input_ios",
            "text": "",
            "attributes": {"accessibility_id": "password_input"},
        },
        "welcome_label": {
            "element_id": "welcome_label_ios",
            "text": "Welcome",
            "attributes": {"accessibility_id": "welcome_label"},
        },
        "get_started": {
            "element_id": "get_started_button_ios",
            "text": "Get Started",
            "attributes": {"accessibility_id": "get_started"},
        },
        "live_stream_label": {
            "element_id": "live_stream_label_ios",
            "text": "Live Stream",
            "attributes": {"accessibility_id": "live_stream_label"},
        },
        "bitrate_label": {
            "element_id": "bitrate_label_ios",
            "text": "1080p",
            "attributes": {"accessibility_id": "bitrate_label"},
        },
        "play_button": {
            "element_id": "play_button_ios",
            "text": "Play",
            "attributes": {"accessibility_id": "play_button"},
        },
    },
    "default": {},
}


def get_screen(screen_name: str, platform: Optional[str] = None, session: Optional[object] = None) -> Dict[str, Any]:
    """Return locator info for a logical screen/element.

    If `platform` is provided, return the locator mapping for that platform.
    If `platform` is None and a `session` is provided, infer the platform from
    `getattr(session, 'platform_name', None)` and use that. Raises ValueError if
    no platform can be inferred. Raises KeyError when the platform is unknown or
    when the locator is missing for the platform.
    """
    # Infer platform from session if not explicitly provided
    if platform is None:
        if session is not None:
            platform = getattr(session, "platform_name", None)
        if platform is None:
            raise ValueError(
                "get_screen requires an explicit platform or a session with 'platform_name' set"
            )

    p = platform.lower()
    if p not in LOCATORS:
        raise KeyError(f"Unknown platform: {platform!r}")
    info = LOCATORS[p].get(screen_name)
    if info is None:
        # attempt to fall back to explicit default
        info = LOCATORS.get("default", {}).get(screen_name)
    if info is None:
        raise KeyError(f"No locator for '{screen_name}' on platform '{p}'")
    return info
