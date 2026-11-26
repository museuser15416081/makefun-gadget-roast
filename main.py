import os

LINE = (
    "My phone spent all night updating to protect my privacy, then woke me "
    "asking permission to open my own photos, my own contacts, and — twice — itself."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
