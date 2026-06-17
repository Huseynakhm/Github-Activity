# Github-Activity

A lightweight, zero-dependency command-line interface (CLI) tool built in Python that fetches and displays the recent public activity of any GitHub user directly in your terminal. 

This project is a complete solution for the [GitHub User Activity](https://roadmap.sh/projects/github-user-activity) challenge on roadmap.sh.

## Features

* **Zero Third-Party Dependencies:** Built entirely using Python's standard libraries (`urllib`, `json`, `sys`). No `pip install` required!
* **Smart Push Aggregation:** Automatically loops through the event stream, groups multiple consecutive `PushEvent` items targeting the same repository, and calculates total commit sums for a cleaner layout.
* **Comprehensive Event Support:** Dynamically tracks and beautifully prints Commits, Stars (`WatchEvent`), Issues, Pull Requests, Repository/Branch/Tag Creation, and provides a clean fallback for any other historical event types.
* **Defensive Error Handling:** Includes custom `try/except` safety blocks protecting against missing terminal arguments, profile 404 errors, API rate-limiting, and local network/Wi-Fi connection drops.

## How It Looks

$ github-activity Huseynakhm
Fetching recent data for Huseynakhm... 

- Created a brand new repository: Huseynakhm/Github-Activity
- Starred django/django
- Opened a pull request in Huseynakhm/TaskTracerCLI
- Pushed 5 commit(s) to Huseynakhm/TaskTracerCLI


## Installation & Global Setup

Follow these setup steps to configure the script so it can be run as a global shortcut (github-activity <username>) from any directory or project folder on your computer.

## For macOS Users

1. Open your terminal and create a dedicated folder for your custom CLI scripts (e.g., ~/bin):

```bash
mkdir -p ~/bin
mv github-activity.py ~/bin/github-activity.py

2. Open your shell configuration file using a terminal text editor (assuming you use the default Zsh):

```bash
nano ~/.zshrc

3. Add the following line at the very bottom of the file:

```bash
alias github-activity="python3 ~/bin/github-activity.py"

4.Save and exit (Press Ctrl+O, Enter, then Ctrl+X).
5.Reload your terminal settings to apply the shortcut immediately:

```bash
source ~/.zshrc


## For Windows Users

**Step 1: Set up the Script Directory**
1. Create a folder somewhere safe on your system to house your custom scripts, for example: C:\bin
2. Move your github-activity.py file into that folder.

**Step 2: Create a Batch Wrapper File**
To call this script directly without typing python or .py explicitly, create a companion batch file inside the same folder:

1. Inside C:\bin, create a new text file named github-activity.bat.
2. Open it in Notepad and paste the following line:

```bash
@python "C:\bin\github-activity.py" %*

3. Save and close the file. (The %* guarantees that any username arguments you pass in your terminal are fed down cleanly to Python).

**Step 3: Add to Environment Variables PATH**
1. Click the Windows Start menu, type "Environment Variables", and press Enter.
2. Under the System Properties window, click the Environment Variables... button at the bottom.
3. In the "User variables" box (the top box), find the row named Path and double-click it.
4. Click New on the right side and type: C:\bin
5. Click OK on all open windows to apply the updates.
6. Restart your terminal window (Command Prompt or PowerShell) for the system path configuration changes to take effect.


## Usage
Now you can check anyone's public timeline from any location across your command-line environment!

```bash
github-activity <github_username>

**Error Handling Examples**
If you run into missing data or network issues, the application handles them safely without breaking:

1. No Name Typed: User's name hasn't been typed, the right usage: github-activity <github_username>

2. Missing Profiles: Error: The username 'invalid_user' doesn't exist on GitHub.

3. No Connectivity: Error: Could not reach GitHub. Please check your internet connection.