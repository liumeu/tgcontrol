# Telegram Linux Control Bot

A Telegram bot built with [aiogram 3.0](https://docs.aiogram.dev/en/latest/) that allows you to execute Linux terminal commands remotely, send system notifications, retrieve system status, and log all executed commands. The bot also allows you to download a log file that contains all command execution details.

## Features

- **Execute Linux Commands**: Run shell commands directly from Telegram.
- **System Notifications**: Send notifications to your Linux system via Telegram.
- **System Status**: Get real-time CPU, memory, disk usage, and uptime information.
- **Command Logging**: All commands executed via the bot are logged with the user's Telegram username, timestamp, command, and output.
- **Log File Download**: Download the log file containing all executed commands and results.

## Requirements

- Python 3.7+
- Linux-based system
- Aiogram 3.0+
- A Telegram bot token (from [BotFather](https://core.telegram.org/bots#botfather))

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/lmeusz/tgcontrol.git
    cd tgcontrol
    ```
2. **First, create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
    ```bash
    pip install aiogram
    pip install psutil
    ```

4. **Set your Telegram Bot API Token**:
   Open the `telegram_bot.py` file and replace `YOUR_TELEGRAM_BOT_API_TOKEN_HERE` with your actual bot token:
    ```python
    API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN_HERE'
    ```

5. **Run the bot**:
    ```bash
    python telegram_bot.py
    ```

## Usage

### Commands
Every displayed result use a Telegram Bot API Markdown.

- **/start**: Greets the user and provides a brief introduction.
- **/exec `<command>`**: Executes a shell command on the Linux system.
  - Example: `/exec ls -la`
- **/notify `<message>`**: Sends a notification to the Linux system.
  - Example: `/notify Backup completed!`
- **/status**: Retrieves the current system status, including CPU, memory, disk usage, and uptime.
- **/logfile**: Sends the log file (`command_log.txt`) containing all executed commands and their results.

### Logging Details

Every time a command is executed, the following information is logged:

- **User**: Telegram username of the user who executed the command.
- **Timestamp**: Date and time when the command was executed.
- **Command**: The command that was executed.
- **Result**: The output or error message resulting from the command.

The log file is stored as `command_log.txt` in the same directory as the bot script.

## Support

If you find this project helpful, consider supporting its development. Your donations help me continue working on this and other open-source projects.

### Donate via Cryptocurrency

- **Bitcoin (BTC)**: `114fkG3qBefonYVRRFnUTaJtqjT7EWvwtY`
- **USDT (TRC20)**: `TQFMncGsk9zuU2hkT2ej66TQhtjxYH2Nbe`
- **TON (TON)**: `UQBarZqcWiAqE1JpDt9XhmI5l5awH2ghE87gKFacvGzTnx6O`
