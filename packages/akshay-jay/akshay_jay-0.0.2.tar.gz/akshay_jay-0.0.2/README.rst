=========
Blessings
=========

Coding with Blessings looks like this... ::

    from blessings import Terminal

    t = Terminal()

    print t.bold('Hi there!')
    print t.bold_red_on_bright_green('It hurts my eyes!')

    with t.location(0, t.height - 1):
        print 'This is at the bottom.'

Or, for byte-level control, you can drop down and play with raw terminal
capabilities::

    print '{t.bold}All your {t.red}bold and red base{t.normal}'.format(t=t)
    print t.wingo(2)

`Full API Reference <https://blessings.readthedocs.io/>`_

The Pitch
=========

Blessings lifts several of curses_' limiting assumptions, and it makes your
code pretty, too:

* Use styles, color, and maybe a little positioning without necessarily
  clearing the whole
  screen first.
* Leave more than one screenful of scrollback in the buffer after your program
  exits, like a well-behaved command-line app should.
* Get rid of all those noisy, C-like calls to ``tigetstr`` and ``tparm``, so
  your code doesn't get crowded out by terminal bookkeeping.
* Act intelligently when somebody redirects your output to a file, omitting the
  terminal control codes the user doesn't want to see (optional).

.. _curses: http://docs.python.org/library/curses.html

Before And After
----------------

Without Blessings, this is how you'd print some underlined text at the bottom
of the screen::

    from curses import tigetstr, setupterm, tparm
    from fcntl import ioctl
    from os import isatty
    import struct
    import sys
    from termios import TIOCGWINSZ

    # If we want to tolerate having our output piped to other commands or
    # files without crashing, we need to do all this branching:
    if hasattr(sys.stdout, 'fileno') and isatty(sys.stdout.fileno()):
        setupterm()
        sc = tigetstr('sc')
        cup = tigetstr('cup')
        rc = tigetstr('rc')
        underline = tigetstr('smul')
        normal = tigetstr('sgr0')
    else:
        sc = cup = rc = underline = normal = ''
    print sc  # Save cursor position.
    if cup:
        # tigetnum('lines') doesn't always update promptly, hence this:
        height = struct.unpack('hhhh', ioctl(0, TIOCGWINSZ, '\000' * 8))[0]
        print tparm(cup, height - 1, 0)  # Move cursor to bottom.
    print 'This is {under}underlined{normal}!'.format(under=underline,
                                                      normal=normal)
    print rc  # Restore cursor position.

That was long and full of incomprehensible trash! Let's try it again, this time
with Blessings::

    from blessings import Terminal

    term = Terminal()
    with term.location(0, term.height - 1):
        print 'This is', term.underline('pretty!')

Much better.

What It Provides
================

Blessings provides just one top-level object: ``Terminal``. Instantiating a
``Terminal`` figures out whether you're on a terminal at all and, if so, does
any necessary terminal setup. After that, you can proceed to ask it all sorts
of things about the terminal. Terminal terminal terminal.


    print 'All your {t.red}base {t.underline}are belong to us{t.normal}'.format(t=term)

Simple capabilities of interest include...

* ``bold``
* ``reverse``
* ``underline``
* ``no_underline`` (which turns off underlining)
* ``blink``
* ``normal`` (which turns off everything, even colors)