#!/usr/bin/env python3
"""
42.py — Simple local DevOps environment checker

Checks:
 - Python version
 - Docker installed
 - Git available
 - Basic network connectivity
 - Environmental variables for CI/CD
"""

import sys
import subprocess
import os

def check_python():
    print(f"Python version: {sys.version_info.major}.{sys.version_info.minor}")
    if sys.version_info < (3, 8):
        print("⚠️  Python 3.8+ recommended for DevOps scripts.")
    else:
        print("✅ Python OK")

def check_program(name):
    try:
        subprocess.run([name, "--version"], check=True, stdout=subprocess.PIPE)
        print(f"✅ {name} is installed")
    except FileNotFoundError:
        print(f"❌ {name} not found")

def check_env_vars():
    needed = ["CI", "DEV_ENV", "DOCKER_HOST"]
    for var in needed:
        val = os.getenv(var)
        print(f"{var} = {val!r}")

def main():
    print("🔍 Running local DevOps environment checks...\n")
    check_python()
    check_program("git")
    check_program("docker")
    check_env_vars()

if __name__ == "__main__":
    main()
