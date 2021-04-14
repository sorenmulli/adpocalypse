import os
from socialreaper import YouTube

from pelutils import log

def download_comments(yt: YouTube):
    coms = yt.video_comments(
        "VqkgQdzmQBk",
        count=20,
        order="relevance",
        text_format="plainText",
    )
    for c in coms:
        log(c["snippet"]["topLevelComment"]["snippet"]["textOriginal"])

if __name__ == '__main__':
    log.configure(os.path.join("local_data", "download_yt.log"), "Download YouTube data")
    with open("secret", "r") as s:
        key = s.readlines()[0]
    yt = YouTube(key)

    download_comments(yt)
