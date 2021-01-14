ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

def countFriends(dict):
    new_ramit = ramit
    new_ramit['friends_count'] = 0
    for friend in new_ramit['friends']:
        new_ramit['friends_count'] += 1
    return new_ramit

print(countFriends(ramit))


