import os
import shutil
import subprocess
import sys

print("🚀 FitPals GitHub Setup Starting...")

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create templates folder
templates_dir = os.path.join(script_dir, "templates")
os.makedirs(templates_dir, exist_ok=True)
os.makedirs(os.path.join(script_dir, "static", "uploads"), exist_ok=True)

# Move all html files into templates/
html_files = [f for f in os.listdir(script_dir) if f.endswith('.html')]
for f in html_files:
    src = os.path.join(script_dir, f)
    dst = os.path.join(templates_dir, f)
    shutil.move(src, dst)
    print(f"✅ Moved {f} → templates/{f}")

print("\n🎉 DONE! All HTML files moved to templates/ folder!")
print("\nNow go to GitHub and upload everything in this folder!")
input("\nPress Enter to close...")
