

def get_human_readable_size(size, precision=2):
    if size == 0:
        return "0B"

    suffixes = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    index = 0
    while size > 1024 and index < len(suffixes):
        index += 1
        size = size / 1024

    return f"{size:.{precision}f} {suffixes[index]}"
