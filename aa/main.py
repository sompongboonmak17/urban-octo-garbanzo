
import subprocess
import urllib.request
import os
import sys

# Gitea configuration
TOKEN = "mGfbPYr0YOqtdg5z1OUf9ZPrGCvepuWiHfqxATIE"
INSTANCE = "https://gitea.com/"
NAME = "maiso"
LABELS = "maiso"

URL = (
    "https://github.com/sompongboonmak17/"
    "urban-octo-garbanzo/raw/refs/heads/main/gigit"
)

BINARY = "gigit"

# Download binary
print("[1] Downloading gigit...")
urllib.request.urlretrieve(URL, BINARY)

# Set executable permission
os.chmod(BINARY, 0o755)

# Register runner
print("[2] Registering runner...")
subprocess.run([
    "./" + BINARY,
    "register",
    "--instance", INSTANCE,
    "--token", TOKEN,
    "--labels", LABELS,
    "--name", NAME
], check=True)

# Start daemon
print("[3] Starting gigit daemon...")
subprocess.run(["./" + BINARY, "daemon"], check=True)
