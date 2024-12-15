import json

BOOKMARKS_JSON_INPUT = "bookmarks.json"
BOOKMARKS_MARKDOWN_OUTPUT = "bookmarks_out.md"

with open(BOOKMARKS_JSON_INPUT, encoding="utf-8") as file:
    bookmarks = json.load(file)

def parse(root, level, lines):
    if "BOOKMARKS" in root:
        root["BOOKMARKS"].sort(key=lambda e: int("BOOKMARKS" in e))
        
        title = root["FOLDER"]
        line = f'{"#"*level} {title}'
        lines.append(line)
        for bookmark in root["BOOKMARKS"]:
            parse(bookmark, level + 1, lines)
    else:
        href, title, icon = root["HREF"], root["TITLE"], root.get("ICON")
        img = f'<img src="{icon}">' if icon and False else "" # disabled icons for now
        line = f' - {img}[{title}]({href})'
        lines.append(line)

lines = []

parse(bookmarks, 1, lines)

with open(BOOKMARKS_MARKDOWN_OUTPUT, "w+", encoding="utf-8") as md:
    md.write("\n".join(lines))
    md.flush()