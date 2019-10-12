import pprint
import urllib.request, json
from firebase import firebase

google_autocomplete = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
key="AIzaSyC8cn_tgtIiNErOM5S5pVj8Eu9Y8gUkiXY"
db = firebase.FirebaseApplication("https://touradvisorapp.firebaseio.com/", None)

def user_auth(user, pwd):
    users = db.get('/users', user)
    secure_token = list(users)[0]
    if list(db.get('/users', None)).count(user) > 0 and users[secure_token] == pwd:
        return True
    return False

def user_register(user, pwd, confirm_pwd):
    try:
        if pwd == confirm_pwd:
            db.post('/users/' + user, pwd)
            return True
    except:
        pass
    return False

def add_plan(destination, budget):
    global google_autocomplete
    choice = []
    google_autocomplete += '&key=' + key + '&input=' + destination.replace(' ', '+')
    with urllib.request.urlopen(google_autocomplete) as url:
        data = json.loads(url.read().decode())['predictions']
        pprint.pprint(data)
        for i in data:
            for j in i:
                if j == 'description':
                    choice.append(i[j])
    return choice

