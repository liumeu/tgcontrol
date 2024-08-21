import logging
import os
import subprocess
import psutil
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
from aiogram.types import FSInputFile

API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN_HERE'
LOG_FILE = "command_log.txt"

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def log_command(user: str, command: str, result: str):
    """Logs the executed command to a file with the user, timestamp, command, and result."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"[{timestamp}] User: {user}\n")
        log_file.write(f"Command: {command}\n")
        log_file.write(f"Result:\n{result}\n")
        log_file.write("-" * 50 + "\n")

@dp.message(Command(commands=["start"]))
async def start_command(message: Message):
    user_first_name = message.from_user.first_name
    await message.reply(
        f"*Welcome, {user_first_name}!* 👋\n"
        "I can send notifications and execute commands on your Linux system.",
        parse_mode="Markdown"
    )

@dp.message(Command(commands=["exec"]))
async def exec_command(message: Message):
    command = message.text.strip().split(" ", 1)
    if len(command) == 2:
        try:
            output = subprocess.check_output(command[1], shell=True, stderr=subprocess.STDOUT, text=True)
            result_message = f"✅ *Command executed successfully*:\n```\n{output}\n```"
            await message.reply(result_message, parse_mode="Markdown")
        except subprocess.CalledProcessError as e:
            result_message = f"❌ *Command failed with error*:\n```\n{e.output}\n```"
            await message.reply(result_message, parse_mode="Markdown")
        log_command(message.from_user.username, command[1], output if 'output' in locals() else e.output)
    else:
        await message.reply("⚠️ *Please provide a command to execute.*\nUsage: `/exec <command>`", parse_mode="Markdown")

@dp.message(Command(commands=["notify"]))
async def notify_command(message: Message):
    notification = message.text.strip().split(" ", 1)
    if len(notification) == 2:
        await message.reply(f"🔔 *Notification sent*:\n_{notification[1]}_", parse_mode="Markdown")
        os.system(f'notify-send "{notification[1]}"')
    else:
        await message.reply("⚠️ *Please provide a message to notify.*\nUsage: `/notify <message>`", parse_mode="Markdown")

@dp.message(Command(commands=["status"]))
async def status_command(message: Message):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    uptime = subprocess.check_output('uptime -p', shell=True, text=True).strip()

    status_report = (
        f"📊 *System Status*:\n"
        f"🖥 **CPU Usage**: `{cpu_usage}%`\n"
        f"💾 **Memory Usage**: `{memory_info.percent}%` (Used: `{memory_info.used // (1024 ** 2)}MB` / Total: `{memory_info.total // (1024 ** 2)}MB`)\n"
        f"📂 **Disk Usage**: `{disk_info.percent}%` (Used: `{disk_info.used // (1024 ** 3)}GB` / Total: `{disk_info.total // (1024 ** 3)}GB`)\n"
        f"⏳ **Uptime**: `{uptime}`"
    )

    await message.reply(status_report, parse_mode="Markdown")
    log_command(message.from_user.username, "/status", status_report)

@dp.message(Command(commands=["logfile"]))
async def logfile_command(message: Message):
    try:
        log_file = FSInputFile(LOG_FILE)
        await message.reply_document(document=log_file, caption="📄 *Here is the command log file.*", parse_mode="Markdown")
    except FileNotFoundError:
        await message.reply("⚠️ *Log file not found. No commands have been executed yet.*", parse_mode="Markdown")

@dp.message(F.text)
async def echo_message(message: Message):
    await message.reply(f"🗣 *You said*: _{message.text}_", parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
