from datetime import datetime

def generate_log(entries):
    if not isinstance(entries, list):
        raise ValueError("Input must be a list.")

    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    with open(filename, "w") as f:
        for i, entry in enumerate(entries):
            f.write(entry)
            if i < len(entries) - 1:
                f.write("\n")

    print(f"Log file created: {filename}")
    return filename
