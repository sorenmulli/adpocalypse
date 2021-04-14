import os

import pandas as pd

from build import get_names, find_names

BOOK_PATHS = [
    "book1.txt",
    "book2.txt",
    "book3.txt",
    "book4.txt",
    "book5.txt",
]

def read(path: str) -> list[str]:
    docs = list()
    for b in BOOK_PATHS:
        with open(os.path.join(path, b), "r") as f:
            docs.append(
                f.read()
            )
    return docs

def build_df(books: list[str]) -> pd.DataFrame:
    chapters = list()
    chap_num = -1
    for i, book in enumerate(books):
        lines = list(book.splitlines())
        for j, line in enumerate(lines):
            # Chapter criterion: Upper case and followed by empty line
            if line and line.isupper() and not lines[j+1]:
                chap_num += 1
                chapters.append({
                    "book": i,
                    "title": line.strip(),
                    "lines": [line]
                })
                # Set up previous chapter
                if (old_num := chap_num - 1) >= 0:
                    chapters[old_num]["text"] = "\n".join(chapters[old_num]["lines"])
                    chapters[old_num].pop("lines")
            else:
                chapters[chap_num]["lines"].append(line)
    # Clean up last chapter
    chapters[-1]["text"] = "\n".join(chapters[-1]["lines"])
    chapters[-1].pop("lines")
    return pd.DataFrame(chapters)

def mentioned_chars(df: pd.DataFrame) -> pd.DataFrame:
    names = get_names()
    row_name_finder = lambda row: find_names(row["text"], names)
    df["names"] = df.apply(row_name_finder, axis=1)
    return df

if __name__ == '__main__':
    datapath = "local_data"
    books = read(datapath)
    chapter_df = build_df(books)
    chapter_df = mentioned_chars(chapter_df)

    chapter_df.to_csv(os.path.join(datapath, "chapters.csv"))
    print(chapter_df.head())
    print(chapter_df.tail(), "\n")
    print(chapter_df.describe())
