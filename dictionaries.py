# dictionary creation

albums = {
    'Abbey Road': 1969,
    'Revolver': 1966,
    'Let It Be': 1970,
}

key_value_pairs = (
    ('Abbey Road', 1969),
    ('Revolver', 1966),
    ('Let It Be', 1970)
)
albums = dict(key_value_pairs)


# basic operations

albums['Abbey Road']
# access the value
# 1969

albums['Help'] = 1965
# add the key-value pair

del albums['Revolver']
# remove the value

'Abbey Road' in albums
# check existence
# True

'Revolver' in albums
# check existence
# False

for key in albums:
    print(key)
# iterate over albums' keys(!)
# 'Abbey Road'
# 'Let It Be'
# 'Help'

for key in albums:
    print(f'Album {key} was released in {albums.key}')
# Album 'Abbey Road' was released in 1969
# Album 'Let It Be' was released in 1970
# Album 'Help' was released in 1965


# methods

albums.items()
# return the dict_items
# dict_items([('Abbey Road', 1969), ('Revolver', 1966), ('Let It Be', 1970)])

for title, year in albums.items():
    print(f'Album {title} was released in {year}')
# Album 'Abbey Road' was released in 1969
# Album 'Let It Be' was released in 1970
# Album 'Help' was released in 1965

albums[14] = 'albums\' amount'
# another type of dict key
# ONLY IMMUTABLE KEYS ALLOWED!!!

album = {
    'title': 'Help',
    'year': 1965,
    'songs': {
        1: ("Help!", "2:18"),
        2: ("The Night Before", "2:34"),
        3: ("You've Got to Hide Your Love Away", "2:09"),
        4: ("I Need You", "2:28"),
        5: ("Another Girl", "2:05"),
        6: ("You're Going to Lose That Girl", "2:18"),
        7: ("Ticket to Ride", "3:09"),
        8: ("Act Naturally", "2:30"),
        9: ("It's Only Love", "1:56"),
        10: ("You Like Me Too Much", "2:36"),
        11: ("Tell Me What You See", "2:37"),
        12: ("I've Just Seen a Face", "2:05"),
        13: ("Yesterday", "2:05"),
        14: ("Dizzy Miss Lizzy", "2:54"),
    }
}
album['songs'][4][0]
# nested dictionary
# "I Need You"





