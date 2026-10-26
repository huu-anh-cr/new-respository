#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
F:\gng6.py - Root Quick Trigger for @gng6 (Gemini Fast / Direct Pass-Through, Port 5007)
"""
import os
import sys
import runpy

candidates = [
    r"F:\GNG_PORTABLE_ALL_AGENTS\02_GNG2_DIRECT\gng2.py",
    r"F:\GNG2_STANDALONE\gng2.py",
    r"F:\GNG_PORTABLE_ALL_AGENTS\00_BRIDGE_DAEMON\gemini_client.py"
]

target_script = None
for p in candidates:
    if os.path.exists(p):
        target_script = p
        break

if not target_script:
    print(f"Error: Target script not found in {[c for c in candidates]}")
    sys.exit(1)

target_dir = os.path.dirname(target_script)
if target_dir not in sys.path:
    sys.path.insert(0, target_dir)

runpy.run_path(target_script, run_name="__main__")
