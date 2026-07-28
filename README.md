# Dreaming Spanish Sync

Automatically imports activities tracked with the **Simple Time Tracker** app (exported as a CSV file) and enters them into your **Dreaming Spanish** account using the "Add time outside the platform" feature.

This tool was created to simplify tracking Spanish listening hours and avoid manually entering every activity into Dreaming Spanish.

## Features

- Import activities from Simple Time Tracker CSV exports
- Filter activities by category
- Convert tracked durations into Dreaming Spanish entries
- Automatically open Dreaming Spanish and enter listening hours
- Reuse an existing Chrome profile to stay logged in

## How it works

1. Export your activities from Simple Time Tracker as a CSV file.
2. Select the date from which activities should be synchronized.
3. The script filters relevant activities.
4. The browser automation enters them into Dreaming Spanish.

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) for dependency management
- Google Chrome
- A Dreaming Spanish account
- Exported CSV data from Simple Time Tracker

## Installation

### Install uv

If you don't have uv installed yet, follow the official installation guide:

https://docs.astral.sh/uv/getting-started/installation/

### Clone the repository

```bash
git clone https://github.com/marcovanzuiden/dreaming-spanish-sync.git
cd dreaming-spanish-sync
```

### Install dependencies

```bash
uv sync
```

## Usage

Run the application:

```bash
uv run python main.py
```

`uv` automatically creates and uses the virtual environment and installs the required dependencies.

Follow the instructions shown in the terminal.

## Configuration

Before running the script, make sure your CSV file is available and configure the required paths.

Personal data such as CSV exports and browser profiles should not be uploaded to GitHub.

## Limitations

- This tool depends on the current Dreaming Spanish website structure.
- Changes to the website may require updates to the automation logic.
- The tool is intended for personal use.

## License

No license has been added yet.