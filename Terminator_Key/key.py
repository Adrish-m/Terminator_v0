# Mapping of special keys in msvcrt (second byte of extended keys)
EXTENDED_KEYS = {
    # Arrow keys
    b'H': "UP",
    b'P': "DOWN",
    b'K': "LEFT",
    b'M': "RIGHT",

    # Home / End / Insert / Delete / PageUp / PageDown
    b'G': "HOME",
    b'O': "END",
    b'R': "INSERT",
    b'S': "DELETE",
    b'I': "PAGE_UP",
    b'Q': "PAGE_DOWN",

    # Function keys F1-F12
    b';': "F1",
    b'<': "F2",
    b'=': "F3",
    b'>': "F4",
    b'?': "F5",
    b'@': "F6",
    b'A': "F7",
    b'B': "F8",
    b'C': "F9",
    b'D': "F10",
    b'\x85': "F11",  # may vary depending on keyboard
    b'\x86': "F12",
}

# Normal keys mapping
NORMAL_KEYS = {
    b'\x1b': "ESC",
    b'\r': "ENTER",
    b'\t': "TAB",
    b'\x08': "BACKSPACE",
    b' ': "SPACE",
    # letters, numbers, symbols will default to decoded character
}

import msvcrt
import g_vars as g_vars

def iskeypressed():
    '''
    Returns True if any key is pressed or else returns False
    '''
    return msvcrt.kbhit()

def get_key():
    """
    Return a friendly key name or character.
    Returns None if no key is pressed (non-blocking).
    """
    if not msvcrt.kbhit():
        return None

    key = msvcrt.getch()

    # Handle extended keys (arrows, F-keys, Home, etc.)
    if key in (b'\x00', b'\xe0'):
        key2 = msvcrt.getch()
        return EXTENDED_KEYS.get(key2, f"SPECIAL_{key2.hex()}")

    # Normal keys
    return NORMAL_KEYS.get(key, key.decode(errors="ignore"))