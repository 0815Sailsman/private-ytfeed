import scrapetube


def get_newest_videos_from_channel(channel_url, count=25):
    videos = scrapetube.get_channel(channel_url=channel_url, limit=count)

    results = [(video["title"]["runs"][0]["text"],
                "https://www.youtube.com/watch/" + str(video["videoId"])) for video in videos]
    return results


if __name__ == "__main__":
    with open("subscriptions.txt") as file:
        videos = get_newest_videos_from_channel(file.readline())
    for video in videos:
        print(video)
