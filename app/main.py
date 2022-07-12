import os

import config


def scan_items(base: str, files_list: list[str]):
    f = open("films.html", "w")
    for path in files_list:
        absolute_path = base + "/" + path
        if os.path.isfile(absolute_path):
            path = '.'.join(path.split(".")[:-1])
            print(path)
            f.write("<a target=\"_blank\" href=\"https://www.google.com/search?q={}\">{}</a><br>\r\n".format(path.replace(".", "+"), path))


scan_items(config.library_dir, os.listdir(config.library_dir))
