def count_by_extension(paths):
    extension = {}
    for path in paths:
        parts = path.split('.')
        if len(parts) == 1:
            ext = ''
        elif len(parts) == 2:
            ext = parts[-1].lower()
        else:
            ext = '.'.join(parts[:-2]).lower()
        extension[ext] = extension.get(ext, 0) + 1
    return extension