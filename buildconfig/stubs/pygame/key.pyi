"""Pygame module to work with the keyboard.

This module contains functions for dealing with the keyboard.

The :mod:`pygame.event` queue gets ``pygame.KEYDOWN`` and ``pygame.KEYUP``
events when the keyboard buttons are pressed and released. Both events have
``key`` and ``mod`` attributes.

   * ``key``: an :ref:`integer ID <key-constants-label>` representing every key
     on the keyboard
   * ``mod``: a bitmask of all the :ref:`modifier keys <key-modifiers-label>`
     that were in a pressed state when the event occurred

The ``pygame.KEYDOWN`` event has the additional attributes ``unicode`` and
``scancode``.

   * ``unicode``: a single character string that is the fully translated
     character entered, this takes into account the shift and composition keys
   * ``scancode``: the platform-specific key code, which could be different from
     keyboard to keyboard, but is useful for key selection of weird keys like
     the multimedia keys

.. versionaddedold:: 2.0.0
    The ``pygame.TEXTINPUT`` event is preferred to the ``unicode`` attribute
    of ``pygame.KEYDOWN``. The attribute ``text`` contains the input.


.. _key-constants-label:

The following is a list of all the constants (from :mod:`pygame.locals`) used to
represent keyboard keys.

Portability note: The integers for key constants differ between pygame 1 and 2.
Always use key constants (``K_a``) rather than integers directly (``97``) so
that your key handling code works well on both pygame 1 and pygame 2.


::

      pygame
      Constant      ASCII   Description
      ---------------------------------
      K_BACKSPACE   \\b      backspace
      K_TAB         \\t      tab
      K_CLEAR               clear
      K_RETURN      \\r      return
      K_PAUSE               pause
      K_ESCAPE      ^[      escape
      K_SPACE               space
      K_EXCLAIM     !       exclaim
      K_QUOTEDBL    "       quotedbl
      K_HASH        #       hash
      K_DOLLAR      $       dollar
      K_AMPERSAND   &       ampersand
      K_QUOTE               quote
      K_LEFTPAREN   (       left parenthesis
      K_RIGHTPAREN  )       right parenthesis
      K_ASTERISK    *       asterisk
      K_PLUS        +       plus sign
      K_COMMA       ,       comma
      K_MINUS       -       minus sign
      K_PERIOD      .       period
      K_SLASH       /       forward slash
      K_0           0       0
      K_1           1       1
      K_2           2       2
      K_3           3       3
      K_4           4       4
      K_5           5       5
      K_6           6       6
      K_7           7       7
      K_8           8       8
      K_9           9       9
      K_COLON       :       colon
      K_SEMICOLON   ;       semicolon
      K_LESS        <       less-than sign
      K_EQUALS      =       equals sign
      K_GREATER     >       greater-than sign
      K_QUESTION    ?       question mark
      K_AT          @       at
      K_LEFTBRACKET [       left bracket
      K_BACKSLASH   \\       backslash
      K_RIGHTBRACKET ]      right bracket
      K_CARET       ^       caret
      K_UNDERSCORE  _       underscore
      K_BACKQUOTE   `       grave
      K_a           a       a
      K_b           b       b
      K_c           c       c
      K_d           d       d
      K_e           e       e
      K_f           f       f
      K_g           g       g
      K_h           h       h
      K_i           i       i
      K_j           j       j
      K_k           k       k
      K_l           l       l
      K_m           m       m
      K_n           n       n
      K_o           o       o
      K_p           p       p
      K_q           q       q
      K_r           r       r
      K_s           s       s
      K_t           t       t
      K_u           u       u
      K_v           v       v
      K_w           w       w
      K_x           x       x
      K_y           y       y
      K_z           z       z
      K_DELETE              delete
      K_KP0                 keypad 0
      K_KP1                 keypad 1
      K_KP2                 keypad 2
      K_KP3                 keypad 3
      K_KP4                 keypad 4
      K_KP5                 keypad 5
      K_KP6                 keypad 6
      K_KP7                 keypad 7
      K_KP8                 keypad 8
      K_KP9                 keypad 9
      K_KP_PERIOD   .       keypad period
      K_KP_DIVIDE   /       keypad divide
      K_KP_MULTIPLY *       keypad multiply
      K_KP_MINUS    -       keypad minus
      K_KP_PLUS     +       keypad plus
      K_KP_ENTER    \\r      keypad enter
      K_KP_EQUALS   =       keypad equals
      K_UP                  up arrow
      K_DOWN                down arrow
      K_RIGHT               right arrow
      K_LEFT                left arrow
      K_INSERT              insert
      K_HOME                home
      K_END                 end
      K_PAGEUP              page up
      K_PAGEDOWN            page down
      K_F1                  F1
      K_F2                  F2
      K_F3                  F3
      K_F4                  F4
      K_F5                  F5
      K_F6                  F6
      K_F7                  F7
      K_F8                  F8
      K_F9                  F9
      K_F10                 F10
      K_F11                 F11
      K_F12                 F12
      K_F13                 F13
      K_F14                 F14
      K_F15                 F15
      K_NUMLOCK             numlock
      K_CAPSLOCK            capslock
      K_SCROLLOCK           scrollock
      K_RSHIFT              right shift
      K_LSHIFT              left shift
      K_RCTRL               right control
      K_LCTRL               left control
      K_RALT                right alt
      K_LALT                left alt
      K_RMETA               right meta
      K_LMETA               left meta
      K_LSUPER              left Windows key
      K_RSUPER              right Windows key
      K_MODE                mode shift
      K_HELP                help
      K_PRINT               print screen
      K_SYSREQ              sysrq
      K_BREAK               break
      K_MENU                menu
      K_POWER               power
      K_EURO                Euro
      K_AC_BACK             Android back button


.. _key-modifiers-label:

The keyboard also has a list of modifier states (from :mod:`pygame.locals`) that
can be assembled by bitwise-ORing them together.

::

      pygame
      Constant      Description
      -------------------------
      KMOD_NONE     no modifier keys pressed
      KMOD_LSHIFT   left shift
      KMOD_RSHIFT   right shift
      KMOD_SHIFT    left shift or right shift or both
      KMOD_LCTRL    left control
      KMOD_RCTRL    right control
      KMOD_CTRL     left control or right control or both
      KMOD_LALT     left alt
      KMOD_RALT     right alt
      KMOD_ALT      left alt or right alt or both
      KMOD_LMETA    left meta
      KMOD_RMETA    right meta
      KMOD_META     left meta or right meta or both
      KMOD_CAPS     caps lock
      KMOD_NUM      num lock
      KMOD_MODE     AltGr


The modifier information is contained in the ``mod`` attribute of the
``pygame.KEYDOWN`` and ``pygame.KEYUP`` events. The ``mod`` attribute is a
bitmask of all the modifier keys that were in a pressed state when the event
occurred. The modifier information can be decoded using a bitwise AND (except
for ``KMOD_NONE``, which should be compared using equals ``==``). For example:

::

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.mod == pygame.KMOD_NONE:
                print('No modifier keys were in a pressed state when this '
                      'event occurred.')
            else:
                if event.mod & pygame.KMOD_LSHIFT:
                    print('Left shift was in a pressed state when this event '
                          'occurred.')
                if event.mod & pygame.KMOD_RSHIFT:
                    print('Right shift was in a pressed state when this event '
                          'occurred.')
                if event.mod & pygame.KMOD_SHIFT:
                    print('Left shift or right shift or both were in a '
                          'pressed state when this event occurred.')
"""

from typing import NoReturn

from pygame.typing import RectLike

class ScancodeWrapper(tuple[bool, ...]):
    def __iter__(self) -> NoReturn: ...

def get_focused() -> bool:
    """True if the display is receiving keyboard input from the system.

    Returns ``True`` when the display window has keyboard focus from the
    system. If the display needs to ensure it does not lose keyboard focus, it
    can use :func:`pygame.event.set_grab()` to grab all input.
    """

def get_pressed() -> ScancodeWrapper:
    """Get the state of all keyboard buttons.

    Returns a sequence of boolean values representing the state of every key on
    the keyboard. Use the key constant values to index the array. A ``True``
    value means that the button is pressed.

    .. note::
       Getting the list of pushed buttons with this function is not the proper
       way to handle text entry from the user. There is no way to know the order
       of keys pressed, and rapidly pushed keys can be completely unnoticed
       between two calls to ``pygame.key.get_pressed()``. There is also no way to
       translate these pushed keys into a fully translated character value. See
       the ``pygame.KEYDOWN`` events on the :mod:`pygame.event` queue for this
       functionality.

    .. versionchanged:: 2.1.4
       The collection of bools returned by ``get_pressed`` can not be iterated
       over because the indexes of the internal tuple does not correspond to the
       keycodes.
    """

def get_just_pressed() -> ScancodeWrapper:
    """Returns a ScancodeWrapper containing the most recent key presses.

    Returns a mapping from key codes to booleans indicating which keys were
    newly pressed as of the last time events were processed. This can be used
    as a convenience function to detect keys that were pressed "this frame."

    The result of this function is updated when new events are processed,
    e.g. in :func:`pygame.event.get()` or :func:`pygame.event.pump()`.

    A key can be marked as "just pressed" even if it is not currently pressed
    according to :func:`pygame.key.get_pressed()`, if it was pressed and released
    again during the same frame. Multiple presses and releases of the same key
    are not distinguished from a single press with this function.

    .. seealso:: :func:`pygame.key.get_just_released()`

    .. note::
       If you require getting the key presses in order, use the event queue
       ``KEYDOWN`` events

    ::

       if pygame.key.get_just_pressed()[pygame.K_b]:
          print("B key just pressed")

    .. versionadded:: 2.4.0
    """

def get_just_released() -> ScancodeWrapper:
    """Returns a ScancodeWrapper containing the most recent key releases.

    Returns a mapping from key codes to booleans indicating which keys were
    newly released as of the last time events were processed. This can be used
    as a convenience function to detect keys that were released "this frame."

    The result of this function is updated when new events are processed,
    e.g. in :func:`pygame.event.get()` or :func:`pygame.event.pump()`.

    .. seealso:: :func:`pygame.key.get_just_pressed()`

    .. note::
       If you require getting the key releases in order, use the event queue
       ``KEYUP`` events.

    ::

       if pygame.key.get_just_released()[pygame.K_b]:
          print("B key just released")

    .. versionadded:: 2.4.0
    """

def get_mods() -> int:
    """Determine which modifier keys are being held.

    Returns a single integer representing a bitmask of all the modifier keys
    being held. Using bitwise operators you can test if specific
    :ref:`modifier keys <key-modifiers-label>` are pressed.
    """

def set_mods(mods: int, /) -> None:
    """Temporarily set which modifier keys are pressed.

    Create a bitmask of the :ref:`modifier key constants <key-modifiers-label>`
    you want to impose on your program.
    """

def set_repeat(delay: int = 0, interval: int = 0, /) -> None:
    """Control how held keys are repeated.

    When the keyboard repeat is enabled, keys that are held down will generate
    multiple ``pygame.KEYDOWN`` events. The ``delay`` parameter is the number of
    milliseconds before the first repeated ``pygame.KEYDOWN`` event will be sent.
    After that, another ``pygame.KEYDOWN`` event will be sent every ``interval``
    milliseconds. If a ``delay`` value is provided and an ``interval`` value is
    not provided or is 0, then the ``interval`` will be set to the same value as
    ``delay``.

    To disable key repeat call this function with no arguments or with ``delay``
    set to 0.

    When pygame is initialized the key repeat is disabled.

    :raises ValueError: if ``delay`` or ``interval`` is < 0

    .. versionchangedold:: 2.0.0 A ``ValueError`` is now raised (instead of a
       ``pygame.error``) if ``delay`` or ``interval`` is < 0.
    """

def get_repeat() -> tuple[int, int]:
    """See how held keys are repeated.

    Get the ``delay`` and ``interval`` keyboard repeat values. Refer to
    :func:`pygame.key.set_repeat()` for a description of these values.

    .. versionaddedold:: 1.8
    """

def name(key: int, use_compat: bool = True) -> str:
    """Get the name of a key identifier.

    Get the descriptive name of the button from a keyboard button id constant.
    Returns an empty string (``""``) if the key is not found.

    If ``use_compat`` argument is ``True`` (which is the default), this function
    returns the legacy name of a key where applicable. The return value is
    expected to be the same across different pygame versions (provided the
    corresponding key constant exists and is unique). If the return value is
    passed to the ``key_code`` function, the original constant will be returned.

    If this argument is ``False``, the returned name may be prettier to display
    and may cover a wider range of keys than with ``use_compat``, but there are
    no guarantees that this name will be the same across different pygame
    versions. If the name returned is passed to the ``key_code`` function, the
    original constant is returned back (this is an implementation detail which
    may change later, do not rely on this)

    .. versionchanged:: 2.1.3 Added ``use_compat`` argument and guaranteed API stability for it
    """

def key_code(name: str) -> int:
    """Get the key identifier from a key name.

    Get the key identifier code from the descriptive name of the key. This
    returns an integer matching one of the K_* keycodes. For example:

    ::

         >>> pygame.key.key_code("return") == pygame.K_RETURN
         True
         >>> pygame.key.key_code("0") == pygame.K_0
         True
         >>> pygame.key.key_code("space") == pygame.K_SPACE
         True

    :raises ValueError: if the key name is not known.

    .. versionaddedold:: 2.0.0
    """

def start_text_input() -> None:
    """Start handling Unicode text input events.

    Start receiving ``pygame.TEXTEDITING`` and ``pygame.TEXTINPUT``
    events. If applicable, show the on-screen keyboard or IME editor.

    For many languages, key presses will automatically generate a
    corresponding ``pygame.TEXTINPUT`` event. Special keys like
    escape or function keys, and certain key combinations will not
    generate ``pygame.TEXTINPUT`` events.

    In other languages, entering a single symbol may require multiple
    key presses, or a language-specific user interface. In this case,
    ``pygame.TEXTINPUT`` events are preferable to ``pygame.KEYDOWN``
    events for text input.

    A ``pygame.TEXTEDITING`` event is received when an IME composition
    is started or changed. It contains the composition ``text``, ``length``,
    and editing ``start`` position within the composition (attributes
    ``text``, ``length``, and ``start``, respectively).
    When the composition is committed (or non-IME input is received),
    a ``pygame.TEXTINPUT`` event is generated.

    Text input events handling is on by default.

    .. versionaddedold:: 2.0.0
    """

def stop_text_input() -> None:
    """Stop handling Unicode text input events.

    Stop receiving ``pygame.TEXTEDITING`` and ``pygame.TEXTINPUT``
    events. If an on-screen keyboard or IME editor was shown with
    ``pygame.key.start_text_input()``, hide it again.

    Text input events handling is on by default.

    To avoid triggering the IME editor or the on-screen keyboard
    when the user is holding down a key during gameplay, text input
    should be disabled once text entry is finished, or when the user
    clicks outside of a text box.

    .. versionaddedold:: 2.0.0
    """

def set_text_input_rect(rect: RectLike, /) -> None:
    """Controls the position of the candidate list.

    This sets the rectangle used for typing with an IME.
    It controls where the candidate list will open, if supported.

    .. versionaddedold:: 2.0.0
    """
