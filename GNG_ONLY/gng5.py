#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
F:\gng5.py - Root Quick Trigger for @gng5 (Gemini Sovereign Epistemic Apex Gate & Cognitive Dual-Engine)
"""
import os
import sys
import runpy

target_script = r"F:\GNG5_STANDALONE\gng5.py"

if not os.path.exists(target_script):
    print(f"Error: Target script not found at {target_script}")
    sys.exit(1)

target_dir = os.path.dirname(target_script)
if target_dir not in sys.path:
    sys.path.insert(0, target_dir)

runpy.run_path(target_script, run_name="__main__")
