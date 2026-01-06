# backup-check.py
# Lists files modified in last 7 days + checks if 'backup/' folder exists
# Run: python backup-check.py

import os
from datetime import datetime, timedelta

print("🔍 Recent files (last 7 days):")
week_ago = datetime.now() - timedelta(days=7)

for root, dirs, files in os.walk('.'):
    for f in files:
        path = os.path.join(root, f)
        try:
            mtime = datetime.fromtimestamp(os.path.getmtime(path))
            if mtime > week_ago:
                print(f"  {path} [{mtime.strftime('%Y-%m-%d')}]")
        except:
            pass  # skip unreadable files

if os.path.exists('./backup'):
    print("\n✅ Backup folder found.")
else:
    print("\n⚠️  No 'backup' folder — consider making one!")
