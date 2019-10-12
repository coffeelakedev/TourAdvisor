import pprint
import urllib.request, json
from firebase import firebase

db = firebase.FirebaseApplication("https://touradvisorapp.firebaseio.com/", None)
AUTH = False

def post_review(location, user, review):
    try:
        db.post('/reviews/' + location + '/' + user + '/' + review)
        return True
    except:
        pass
    return False

def post_rating(location, user, rating):
    try:
        db.post('/ratings/' + location + '/' + user + '/' + rating)
        return True
    except:
        pass
    return False