# Focuspad firmware

This firmware targets a Seeed Studio XIAO RP2040 running CircuitPython and KMK.

1. Install CircuitPython for the XIAO RP2040.
2. Copy the current `kmk` folder to `CIRCUITPY/kmk`.
3. Copy `adafruit_display_text`, `adafruit_displayio_ssd1306.mpy`, and their
   dependencies from the matching Adafruit CircuitPython Library Bundle into
   `CIRCUITPY/lib`.
4. Copy `main.py` to `CIRCUITPY/code.py`.

The six keys are Copy, Paste, Undo, Reopen Closed Tab, Find, and Enter. The
encoder controls volume and its push switch mutes audio.
