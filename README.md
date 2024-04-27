# Python Stopwatch by Cyber Nerd using Tkinter

A simple stopwatch application built with Python's tkinter library.

## Features

- Start/Stop functionality to control the stopwatch.
- Restart button to reset the stopwatch to 00:00:00.00.
- Close button to exit the application.

## Requirements

- Python 3.x
- tkinter library (usually comes pre-installed with Python)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/cybernerdmax/Python-StopWatch.git
    ```

2. Navigate to the directory:

    ```bash
    cd Python-StopWatch
    ```

3. Run the stopwatch:

    ```bash
    python stopwatch.py
    ```

4. If you want to create a standalone executable using PyInstaller:

    ```bash
    pip install pyinstaller
    pyinstaller --onefile --windowed --icon=stopwatch.ico stopwatch.py
    ```

    This command will generate a single executable file (`stopwatch.exe` on Windows) in the `dist` directory.

    **Note:** Installing PyInstaller is only necessary if you want to create a standalone executable. If you only intend to run the script directly using Python, skip this step.

## How it Works

- The stopwatch starts counting time when the "Start" button is pressed.
- The "Stop" button halts the timer, and it resumes from the paused time when pressed again.
- The "Restart" button resets the stopwatch to 00:00:00.00.
- The "Close" button exits the application.

## Customization

- You can customize the appearance and behavior of the stopwatch by modifying the tkinter widgets and their properties in the `StopWatch` class.

## License

This project is licensed under the MIT License.
