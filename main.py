# import things
from gmusicapi import Mobileclient
from flask import Flask

# initialise stuff
app = Flask(__name__)
api = Mobileclient()
logged_in = api.login('', '', api.FROM_MAC_ADDRESS)


# start an http listener and login to the service

@app.route("/logout")
def logout():
    logged_out = api.logout()
    return str(logged_out)

@app.route("/")
def hello():
    string_of_songs = 'Songs:'
    for x in api.get_all_songs():
        string_of_songs = string_of_songs + str(x['id'])
    return string_of_songs

@app.route("/bohemian")
def bohemian():
    return api.get_stream_audio('Tpawnjwgej55fonuti6ydllabou')[0]

@app.route("/playlist_create")
def playlist_create():
    return api.create_playlist('tester')

if __name__ == "__main__":
    app.run()
