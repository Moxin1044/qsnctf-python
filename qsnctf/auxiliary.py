def js_from_file(file_name):
    # 没啥用，我就是简单的读个文件
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()
        return result