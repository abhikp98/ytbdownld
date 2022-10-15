from flask import Flask, request
from pytube import YouTube

app = Flask(__name__)


@app.route('/test')
def val():
    link = str(request.args.get('link'))
    key, vall, lis = [], [], []
    ttl = YouTube(link).title
    tnu = YouTube(link).thumbnail_url
    for i in YouTube(link).streams.filter(type="video").order_by("resolution"):
        if i.resolution not in key:
            key.append(i.resolution)
            vall.append(i.url)
    for i, j in zip(range(len(key)), range(len(vall))):
        a = {"name": key[i], "link": vall[j]}
        lis.append(a)
    last = {"data": lis, "title": ttl, "qualitylist": key, "thumbnail": tnu}
    return last


if __name__ == "__main__":
    app.run(debug=True)
