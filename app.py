from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<p>Hello, World!</p><img class="lnXdpd" alt="Google" height="92" src="/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" srcset="/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png 1x, /images/branding/googlelogo/2x/googlelogo_color_272x92dp.png 2x" width="272" data-atf="1" data-frt="0">'

if __name__ == "__main__":
    app.run()
