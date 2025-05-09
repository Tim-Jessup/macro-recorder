# Macro Recorder

A lightweight Python-based macro recorder that captures mouse clicks and keyboard actions, then generates an editable Python script for playback using `pyautogui`.

## Features

- Records mouse clicks and basic keystrokes
- Detects hotkey combos like `Ctrl+Tab`
- Outputs readable, editable Python code
- Playback support via `pyautogui`
- Simple setup, no GUI required

## Getting Started

### Prerequisites

- Python 3.7+
- `pyautogui`
- `pynput`

Install dependencies:
```bash
pip install pyautogui pynput
```

## Recording a Macro
Run the recorder:

``` bash
python record_macro.py
```

* You'll get a 3-second countdown.
* The recorder runs for 20 seconds by default.
* Mouse clicks and keystrokes are saved to macro_playback.py.

### Playing Back the Macro
After recording:

``` bash
python macro_playback.py
```

This script waits 3 seconds, then replays your actions.

## Customization
* Adjust the recording duration in `record_macro.py (recording_time)`
* Modify delays or actions directly in `macro_playback.py`

## Known Limitations
* Mouse movements and scroll events are not recorded (yet)
* Complex modifier combos may need manual tuning
* Must be run from a system terminal (not inside VS Code's terminal)

## License
MIT License