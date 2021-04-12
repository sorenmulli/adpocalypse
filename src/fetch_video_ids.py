from __future__ import annotations
import os
import urllib
from urllib import request
import json

from pelutils import log

def get_channel_vid_urls(channel_id: str, key: str) -> list[str]:
    # Credit: https://stackoverflow.com/a/47290790
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(key, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_links

if __name__ == '__main__':
    log.configure(os.path.join("local_data", "yt_ids.log"), "Fetch youtube video ids")
    out = "data/video_ids.json"

    with open("secret", "r") as s:
        key = s.readlines()[0].strip()
    with open("data/youtubers.json", "r") as f:
        youtubers = json.load(f)

    vids = dict()
    for name, c_id in youtubers.items():
        try:
            log(f"Fetching vids for {name} ...")
            vids[name] = [url.split("=")[-1] for url in get_channel_vid_urls(c_id, key)]
            log(f"Fetched {len(vids[name])}")
        except urllib.error.HTTPError as e:
            log.error(e, f"Error fetching videos for {name}. You might have used up your quota.")
    if vids:
        with open(out, "w") as f:
            json.dump(vids, f, indent=4)
        log(f"Saved video ids to {out}")
