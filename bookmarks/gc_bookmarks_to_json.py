import re
import json

BOOKMARKS_FILE = "bookmarks_12_15_24.html"
JSON_EXPORT_FILE = "bookmarks.json"

lines = []

with open(BOOKMARKS_FILE, encoding="utf-8") as file:
    for i, line in enumerate(file):
        if i < 7: 
            continue
        lines.append(line)

TITLE_RE = re.compile(r'<DT><(A|H3) (.+)>(.+)<\/(A|H3)>')
ENTRY_RE = re.compile(r'([A-Z_]+)="([^"]+)"')

def parse(root, lines, state):
    prev = root

    while state["index"] < len(lines):
        line: str = lines[state["index"]].strip()
        if line == "<DL><p>": #indicates that we're about to enter a folder
            state["index"] += 1
            parse(prev, lines, state)
        elif line == "</DL><p>": #indicates that we're about to exit a folder
            state["index"] += 1
            return
        else:
            current = {}
            _, kw, title, _ = TITLE_RE.findall(line)[0]
            for match in ENTRY_RE.finditer(kw):
                current[match.group(1)] = match.group(2)
            
            if "HREF" not in current:
                current["FOLDER"] = title
                current["BOOKMARKS"] = []
            else:
                current["TITLE"] = title
            
            root["BOOKMARKS"].append(current)
            prev = current
            state["index"] += 1

## parsing
root = {
    "FOLDER": "Exported Bookmarks",
    "BOOKMARKS": []
}

state = {
    "index": 0
}

parse(root, lines, state)

with open(JSON_EXPORT_FILE, "w+", encoding="utf-8") as f:
    json.dump(root, f, indent=4)