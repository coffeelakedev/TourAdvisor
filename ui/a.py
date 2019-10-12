
import urllib.request, json
from firebase import firebase



firebase = firebase.FirebaseApplication("https://touradvisorapp.firebaseio.com/", None)

print(firebase.get('/users', None))

google_url = "https://maps.googleapis.com/maps/api/place/autocomplete/json?key=AIzaSyC8cn_tgtIiNErOM5S5pVj8Eu9Y8gUkiXY&input=VIT+Chennai"
#with urllib.request.urlopen(google_url) as url:
#    data = json.loads(url.read().decode())
#    print(data)
DATA = {'predictions': [{'description': 'VIT Chennai, Chennai, Tamil Nadu, India', 'id': 'b28ddd84c5917e80aaf4f05e19504f4cf6b959b5', 'matched_substrings': [{'length': 11, 'offset': 0}], 'place_id': 'ChIJZx9Jjq9ZUjoRLX11GxNCS5Q', 'reference': 'ChIJZx9Jjq9ZUjoRLX11GxNCS5Q', 'structured_formatting': {'main_text': 'VIT Chennai', 'main_text_matched_substrings': [{'length': 11, 'offset': 0}], 'secondary_text': 'Chennai, Tamil Nadu, India'}, 'terms': [{'offset': 0, 'value': 'VIT Chennai'}, {'offset': 13, 'value': 'Chennai'}, {'offset': 22, 'value': 'Tamil Nadu'}, {'offset': 34, 'value': 'India'}], 'types': ['university', 'point_of_interest', 'establishment']}, {'description': 'VIT Chennai Basket Ball Court, Kelambakkam - Vandalur Road, Kovilancheri, Tamil Nadu, India', 'id': 'd2a1d2ab893a1053c2cb985f386594b6af33af6d', 'matched_substrings': [{'length': 11, 'offset': 0}], 'place_id': 'ChIJoat4b69ZUjoRE0QqLbslqyg', 'reference': 'ChIJoat4b69ZUjoRE0QqLbslqyg', 'structured_formatting': {'main_text': 'VIT Chennai Basket Ball Court', 'main_text_matched_substrings': [{'length': 11, 'offset': 0}], 'secondary_text': 'Kelambakkam - Vandalur Road, Kovilancheri, Tamil Nadu, India'}, 'terms': [{'offset': 0, 'value': 'VIT Chennai Basket Ball Court'}, {'offset': 31, 'value': 'Kelambakkam - Vandalur Road'}, {'offset': 60, 'value': 'Kovilancheri'}, {'offset': 74, 'value': 'Tamil Nadu'}, {'offset': 86, 'value': 'India'}], 'types': ['premise', 'establishment']}, {'description': 'VIT Chennai - Food Court, Kovilancheri, Tamil Nadu, India', 'id': '7ae490c8d4cba29d13a05c0b7ed708d75507c183', 'matched_substrings': [{'length': 11, 'offset': 0}], 'place_id': 'ChIJ-5ebq6hZUjoRsBPQMClNH38', 'reference': 'ChIJ-5ebq6hZUjoRsBPQMClNH38', 'structured_formatting': {'main_text': 'VIT Chennai - Food Court', 'main_text_matched_substrings': [{'length': 11, 'offset': 0}], 'secondary_text': 'Kovilancheri, Tamil Nadu, India'}, 'terms': [{'offset': 0, 'value': 'VIT Chennai - Food Court'}, {'offset': 26, 'value': 'Kovilancheri'}, {'offset': 40, 'value': 'Tamil Nadu'}, {'offset': 52, 'value': 'India'}], 'types': ['restaurant', 'food', 'point_of_interest', 'establishment']}, {'description': 'VIT Chennai Cricket Ground, Kovilancheri, Tamil Nadu, India', 'id': '60b38a1566bb727452247c3fb507353d274b5d1c', 'matched_substrings': [{'length': 11, 'offset': 0}], 'place_id': 'ChIJvXpfmqVZUjoR9YTY-z86lbY', 'reference': 'ChIJvXpfmqVZUjoR9YTY-z86lbY', 'structured_formatting': {'main_text': 'VIT Chennai Cricket Ground', 'main_text_matched_substrings': [{'length': 11, 'offset': 0}], 'secondary_text': 'Kovilancheri, Tamil Nadu, India'}, 'terms': [{'offset': 0, 'value': 'VIT Chennai Cricket Ground'}, {'offset': 28, 'value': 'Kovilancheri'}, {'offset': 42, 'value': 'Tamil Nadu'}, {'offset': 54, 'value': 'India'}], 'types': ['point_of_interest', 'establishment']}, {'description': 'VIT CHENNAI HEALTH CENTER, Kovilancheri, Tamil Nadu, India', 'id': 'ca765d688c0d1ffd0bdeffe1f0a0169e4c430774', 'matched_substrings': [{'length': 11, 'offset': 0}], 'place_id': 'ChIJGf3OAaVZUjoREksCgOsMZ0E', 'reference': 'ChIJGf3OAaVZUjoREksCgOsMZ0E', 'structured_formatting': {'main_text': 'VIT CHENNAI HEALTH CENTER', 'main_text_matched_substrings': [{'length': 11, 'offset': 0}], 'secondary_text': 'Kovilancheri, Tamil Nadu, India'}, 'terms': [{'offset': 0, 'value': 'VIT CHENNAI HEALTH CENTER'}, {'offset': 27, 'value': 'Kovilancheri'}, {'offset': 41, 'value': 'Tamil Nadu'}, {'offset': 53, 'value': 'India'}], 'types': ['point_of_interest', 'establishment']}], 'status': 'OK'}
import pprint
pprint.pprint(DATA['predictions'])
for i in DATA['predictions']:
    for j in i:
        if j == 'description':
            print(i[j])

