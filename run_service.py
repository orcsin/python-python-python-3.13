import subprocess  # nosec
import sys

if __name__ == "__main__":
    subprocess.Popen([sys.executable, "server.py"])  # nosec
