import os

roast_line = "Overnight privacy update brags about protecting your privacy, but now it asks permission to open your own photos, contacts, and even itself. Some protection."

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
entry_path = os.path.join(output_dir, 'entry.txt')

os.makedirs(output_dir, exist_ok=True)

with open(entry_path, 'w', encoding='utf-8') as f:
    f.write(roast_line)

print(roast_line)
