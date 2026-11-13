def count_by_extension(paths):
    extension = {}
    for path in paths:
        filename = path.split('/')[-1]
        cnt = -1
        for i in range(len(filename)-1, -1, -1):
            if filename[i] == ".":
                cnt = i
                break
        if cnt == -1 or (filename[0] == '.' and filename.count(".") == 1):
            ext = ""
        else:
            ext = filename[cnt + 1:].lower()

        extension[ext] = extension.get(ext, 0) + 1
    return extension


def deepest_path(paths):
    if not paths:
        return ""
    sorted_paths = sorted(paths)
    return max(sorted_paths, key=lambda x: x.count('/'))


def human_size(n_bytes):
    velichina = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ', 'ПБ']
    size = float(n_bytes)
    cnt = 0
    while size >= 1024 and cnt < len(velichina) - 1:
        size /= 1024
        cnt += 1

    if cnt == 0:
        return f'{int(size)} Б'

    formatted = f'{size:.1f}'
    if formatted[-1] == '.0':
        formatted = formatted[:-2]
    return f'{formatted} {velichina[cnt]}'