# GitHub Activity CLI

A lightweight, zero-dependency command-line tool built with Python that fetches and displays the recent public activity of any GitHub user directly in your terminal.

This project is a complete solution for the **GitHub User Activity** challenge on roadmap.sh.

## Features

* **Zero Third-Party Dependencies** – Built entirely using Python's standard library (`urllib`, `json`, and `sys`). No `pip install` required.
* **Smart Push Aggregation** – Consecutive `PushEvent` entries targeting the same repository are automatically grouped together, providing a cleaner and more readable output.
* **Comprehensive Event Support** – Supports commits, stars (`WatchEvent`), issues, pull requests, repository creation, branch/tag creation, and includes fallback handling for additional event types.
* **Defensive Error Handling** – Gracefully handles missing arguments, invalid usernames, GitHub API errors, rate limiting, and network connectivity issues.

## Example Output

```bash
$ github-activity Huseynakhm

Fetching recent activity for Huseynakhm...

- Created a new repository: Huseynakhm/Github-Activity
- Starred django/django
- Opened a pull request in Huseynakhm/TaskTracerCLI
- Pushed 5 commit(s) to Huseynakhm/TaskTracerCLI
```

## Installation

### macOS

#### 1. Create a directory for custom scripts

```bash
mkdir -p ~/bin
mv github-activity.py ~/bin/github-activity.py
```

#### 2. Create a shell alias

Open your Zsh configuration file:

```bash
nano ~/.zshrc
```

Add the following line at the bottom:

```bash
alias github-activity="python3 ~/bin/github-activity.py"
```

#### 3. Reload your shell configuration

```bash
source ~/.zshrc
```

You can now run:

```bash
github-activity <github_username>
```

---

### Windows

#### 1. Create a script directory

Create a folder to store your custom scripts, for example:

```text
C:\bin
```

Move `github-activity.py` into this folder.

#### 2. Create a batch wrapper

Inside `C:\bin`, create a file named:

```text
github-activity.bat
```

Add the following content:

```bat
@python "C:\bin\github-activity.py" %*
```

#### 3. Add the directory to PATH

1. Open **Environment Variables**.
2. Under **User Variables**, locate and edit **Path**.
3. Click **New** and add:

```text
C:\bin
```

4. Save the changes and restart your terminal.

You can now run:

```bash
github-activity <github_username>
```

## Usage

```bash
github-activity <github_username>
```

### Example

```bash
github-activity torvalds
```

## Error Handling

The application handles common errors gracefully:

### Missing Username

```text
Usage: github-activity <github_username>
```

### Invalid Username

```text
Error: The username 'invalid_user' does not exist on GitHub.
```

### No Internet Connection

```text
Error: Could not reach GitHub. Please check your internet connection.
```

### Contributing

```text
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements.
```

## Challenge

This project was built as a solution to the GitHub User Activity challenge on roadmap.sh:

https://roadmap.sh/projects/github-user-activity
