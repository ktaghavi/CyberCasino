CARDS = {
    'K': (10, '''
     -------
    |K      |
    |       |
    |       |
    |       |
    |      K|
     ------- 
    '''),

    'Q': (10, '''
     -------
    |Q      |
    |       |
    |       |
    |       |
    |      Q|
     ------- 
    '''), 

    'J': (10, '''
     -------
    |J      |
    |       |
    |       |
    |       |
    |      J|
     ------- 
    '''), 

    '10': (10, '''
     -------
    |10     |
    |       |
    |       |
    |       |
    |     10|
     ------- 
    '''), 

    '9': (9, '''
     -------
    |9      |
    |       |
    |       |
    |       |
    |      9|
     ------- 
    '''), 

    '8': (8, '''
     -------
    |8      |
    |       |
    |       |
    |       |
    |      8|
     ------- 
    '''), 

    '7': (7, '''
     -------
    |7      |
    |       |
    |       |
    |       |
    |      7|
     ------- 
    '''), 

    '6': (6, '''
     -------
    |6      |
    |       |
    |       |
    |       |
    |      6|
     ------- 
    '''), 

    '5': (5, '''
     -------
    |5      |
    |       |
    |       |
    |       |
    |      5|
     ------- 
    '''), 

    '4': (4, '''
     -------
    |4      |
    |       |
    |       |
    |       |
    |      4|
     ------- 
    '''), 

    '3': (3, '''
     -------
    |3      |
    |       |
    |       |
    |       |
    |      3|
     ------- 
    '''), 

    '2': (2, '''
     -------
    |2      |
    |       |
    |       |
    |       |
    |      2|
     ------- 
    '''), 

    'A': (11, '''
     -------
    |A      |
    |       |
    |       |
    |       |
    |      A|
     ------- 
    ''')
}

BLANKCARD = '''
     -------
    |XXXXXXX|
    |XXXXXXX|
    |XXXXXXX|
    |XXXXXXX|
    |XXXXXXX|
     ------- 
    '''

def get_card_ascii(card_rank):
    return CARDS.get(card_rank, (0, 'Invalid Rank'))[1]

def get_blank_card_ascii():
    return BLANKCARD