#!/usr/bin/python3
import subprocess

import build

if build.build():
    print("Running")
    subprocess.run(["build/src/main/main"])