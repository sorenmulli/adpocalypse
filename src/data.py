import os
import datetime as dt

import pandas as pd
from tqdm import tqdm
from psaw import PushshiftAPI

from pelutils import log

def download_submissions(sub: str, q: str, start: int, end: int):
    r = PushshiftAPI()
    search = r.search_submissions(subreddit=sub, after=start, before=end, q=q,
        filter=["id", "title", "created_utc", "num_comments", "score", "author"]
    )
    results = list(tqdm(search))
    log("Number of videos", len(results))

    df = pd.DataFrame({
        "id":       [res.id for res in results],
        "title":    [res.title for res in results],
        "created":  [dt.datetime.utcfromtimestamp(res.created_utc) for res in results],
        "comments": [int(res.num_comments) for res in results],
        "score":    [res.score for res in results],
        "author":   [res.author for res in results],
    })

    df.to_csv(os.path.join("local_data", "r_videos_posts.csv"))
    log(df.tail())
    log(df.describe())
    return df

if __name__ == '__main__':
    log.configure(os.path.join("local_data", "download.log"), "Download Reddit data")

    sub, q = "videos", "YouTube"
    start_date, end_date = int(dt.datetime(2016, 1, 1).timestamp()), int(dt.datetime(2021, 1, 1).timestamp())
    download_submissions(sub, q, start_date, end_date)
