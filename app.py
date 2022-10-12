from flask import Flask, request
from pytube import YouTube

app = Flask(__name__)


@app.route('/test')
def val():
    link = str(request.args.get('link'))
    key, vall, = [], []
    ttl = YouTube(link).title
    for i in YouTube(link).streams.filter(type="video").order_by("resolution"):
        if i.resolution not in key:
            key.append(i.resolution)
            vall.append(i.url)
    ab = dict(zip(key, vall))
    ab["title"] = ttl
    ab["qualitylist"] = key
    return ab


if __name__ == "__main__":
    app.run(debug=True)
