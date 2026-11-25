import os


LINE = "My fitness tracker congratulated me for sleeping. I was awake, staring at the ceiling, doing nothing."


def write_entry(output_dir):
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
