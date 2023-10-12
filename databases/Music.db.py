import sqlite3

conn = sqlite3.connect('Music_data.sqlite')

conn.execute('Create a table for the song the user decides to input (Song Release date,artest name,song title)')

conn.execute('insert year of Release', ("2015"))
conn.execute('insert artest data', ("The Oh hellos"))
conn.execute('insert the song data', ("Soldier, Poet, King"))
conn.commit()
for row in conn.execute('select * From Music data'):
    print(row)


def Music_data(data):
    print('Here its time to store your data')
    return 'Hi its loaded in all of your data usage.'
