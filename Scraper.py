import scrapetube


def get_newest_videos_from_channel(channel_url, count=10):
    videos = scrapetube.get_channel(channel_url=channel_url, limit=count)
    results = [(video["title"]["runs"][0]["text"],
                convert_text_to_timestamp(video["publishedTimeText"]["simpleText"].split(" ", 1)[1]),
                "https://www.youtube.com/watch?v=" + str(video["videoId"]),
                video["thumbnail"]["thumbnails"][1]["url"]) for video in videos]
    return results


def convert_text_to_timestamp(upload_date):
    nr = int(upload_date.split(" ", 1)[0])
    if "Stunde" in upload_date:
        return nr * 3600
    elif "Woche" in upload_date:
        return nr * 604800
    elif "Monat" in upload_date:
        return nr * 2592000
    elif "Tag" in upload_date:
        return nr * 86400
    elif "Minute" in upload_date:
        return nr * 60
    elif "Jahr" in upload_date:
        return nr * 31536000
    elif "Sekunde" in upload_date:
        return nr


if __name__ == "__main__":
    with open("subscriptions.txt") as file:
        videos = get_newest_videos_from_channel(file.readline())
    for video in videos:
        print(video)
