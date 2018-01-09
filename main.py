from analizer import analise2

from editdistance import eval

test_cases = [
    ('resources/test/roman/test_roman_eng_10.png', 'roman',
     'How do you talk to your new coworkers? What do you talk about? How can you impress your boss?\n' +
     'Sometimes the most difficult questions have the simplest solutions!\nWhere can I find the bathroom?\n' +
     'I love your shoes. Where did you get them?\nExcuse me, can you please speak up?\n'),
    ('resources/test/roman/test_roman_eng_15.png', 'roman',
     'How do you talk to your new coworkers? What do you talk about? How can\nyou impress your boss?\n' +
     'Sometimes the most difficult questions have the simplest solutions!\nWhere can I find the bathroom?\n' +
     'I love your shoes. Where did you get them?\nExcuse me, can you please speak up?\n'),
    ('resources/test/roman/test_roman_eng_20.png', 'roman',
     'How do you talk to your new coworkers? What do you talk\nabout? How can you impress your boss?\n' +
     'Sometimes the most difficult questions have the simplest\nsolutions!\nWhere can I find the bathroom?\n' +
     'I love your shoes. Where did you get them?\nExcuse me, can you please speak up?\n'),

    ('resources/test/roman/test_roman_eng1_40.png', 'roman',
     'How do you talk to your new\ncoworkers? What do you talk\nabout? How can you impress\nyour boss?\n'),
    ('resources/test/roman/test_roman_eng2_40.png', 'roman',
     'Sometimes the most difficult\nquestions have the simplest\nsolutions!\nWhere can I find the\nbathroom?\n'),
    ('resources/test/roman/test_roman_eng3_40.png', 'roman',
     'I love your shoes. Where did\nyou get them?\nExcuse me, can you please\nspeak up?\n'),

    ('resources/test/roman/test_roman_lat_10.png', 'roman',
     'Mama je gruz!\nPiernik jest z Afryki.\nKukurydza to nie robak, a jej facet ma metr i trzy.\n' +
     'Kalafior jest zielony i ma wszystkie spory tam, gdzie mam je i ja.\nProducent tworzy filmy, a w nich jest masa rozbieranych scen.\n' +
     'Julia jest jak wieloryb i ubiera rozmiar XXL.\nPartner Julii rzuca w wieloryba talerzem, bo akurat betoniarki przy sobie nie ma.\n'),
    ('resources/test/roman/test_roman_lat_15.png', 'roman',
     'Mama je gruz!\nPiernik jest z Afryki.\nKukurydza to nie robak, a jej facet ma metr i trzy.\n' +
     'Kalafior jest zielony i ma wszystkie spory tam, gdzie mam je i ja.\nProducent tworzy filmy, a w nich jest masa rozbieranych scen.\n' +
     'Julia jest jak wieloryb i ubiera rozmiar XXL.\nPartner Julii rzuca w wieloryba talerzem, bo akurat betoniarki przy sobie nie\nma.\n'),
    ('resources/test/roman/test_roman_lat_20.png', 'roman',
     'Mama je gruz!\nPiernik jest z Afryki.\nKukurydza to nie robak, a jej facet ma metr i trzy.\n' +
     'Kalafior jest zielony i ma wszystkie spory tam, gdzie mam\nje i ja.\nProducent tworzy filmy, a w nich jest masa rozbieranych\nscen.\n' +
     'Julia jest jak wieloryb i ubiera rozmiar XXL.\nPartner Julii rzuca w wieloryba talerzem, bo akurat\nbetoniarki przy sobie nie ma.\n'),

    ('resources/test/roman/test_roman_lat1_40.png', 'roman',
     'Mama je gruz!\nPiernik jest z Afryki.\nKukurydza to nie robak, a jej\nfacet ma metr i trzy.\n'),
    ('resources/test/roman/test_roman_lat2_40.png', 'roman',
     'Kalafior jest zielony i ma\nwszystkie spory tam, gdzie\nmam je i ja.\nProducent tworzy filmy, a w\nnich jest masa rozbieranych\nscen.\n'),
    ('resources/test/roman/test_roman_lat3_40.png', 'roman',
     'Julia jest jak wieloryb i\nubiera rozmiar XXL.\nPartner Julii rzuca w\nwieloryba talerzem, bo akurat\nbetoniarki przy sobie nie ma.\n'),

    ('resources/test/roman/test_roman_pl_10.png', 'roman',
     'Ręczne robótki na działce Pana Zdzisława przynoszą więcej szkód niż pożytku.\n' +
     'Analfabeta, który nie jest w stanie pokonać innego analfabety, jest głupszy od całej reszty społeczeństwa.\n' +
     'Gubić klucze każdy może, należy pamiętać żeby zamykać mieszkania zawsze po wyjściu z nich.\n' +
     'Źdźbło trawy delikatnie kłuje mnie w pośladek.\nZerżnąć wszystko od kolegi na sprawdzianie każdy potrafi.\n'),
    ('resources/test/roman/test_roman_pl_15.png', 'roman',
     'Ręczne robótki na działce Pana Zdzisława przynoszą więcej szkód niż pożytku.\n' +
     'Analfabeta, który nie jest w stanie pokonać innego analfabety, jest głupszy od\ncałej reszty społeczeństwa.\n' +
     'Gubić klucze każdy może, należy pamiętać żeby zamykać mieszkania zawsze\npo wyjściu z nich.\n' +
     'Źdźbło trawy delikatnie kłuje mnie w pośladek.\nZerżnąć wszystko od kolegi na sprawdzianie każdy potrafi.\n'),
    ('resources/test/roman/test_roman_pl_20.png', 'roman',
     'Ręczne robótki na działce Pana Zdzisława przynoszą więcej\nszkód niż pożytku.\n' +
     'Analfabeta, który nie jest w stanie pokonać innego\nanalfabety, jest głupszy od całej reszty społeczeństwa.\n' +
     'Gubić klucze każdy może, należy pamiętać żeby zamykać\nmieszkania zawsze po wyjściu z nich.\n' +
     'Źdźbło trawy delikatnie kłuje mnie w pośladek.\nZerżnąć wszystko od kolegi na sprawdzianie każdy potrafi.\n'),

    ('resources/test/roman/test_roman_pl1_40.png', 'roman',
     'Ręczne robótki na działce\nPana Zdzisława przynoszą\nwięcej szkód niż pożytku.\n'),
    ('resources/test/roman/test_roman_pl2_40.png', 'roman',
     'Analfabeta, który nie jest w\nstanie pokonać innego\nanalfabety, jest głupszy od\ncałej reszty społeczeństwa.\n'),
    ('resources/test/roman/test_roman_pl3_40.png', 'roman',
     'Gubić klucze każdy może,\nnależy pamiętać żeby\nzamykać mieszkania zawsze\npo wyjściu z nich.\n'),
    ('resources/test/roman/test_roman_pl4_40.png', 'roman',
     'Źdźbło trawy delikatnie kłuje\nmnie w pośladek.\nZerżnąć wszystko od kolegi\nna sprawdzianie każdy\npotrafi.\n'),

    ('resources/test/arial/test_arial_eng_10.png', 'arial',
     'How do you talk to your new coworkers? What do you talk about? How can you impress your boss?\n' +
     'Sometimes the most difficult questions have the simplest solutions!\nWhere can I find the bathroom?\n' +
     'I love your shoes. Where did you get them?\nExcuse me, can you please speak up?\n'),
    ('resources/test/arial/test_arial_eng_15.png', 'arial',
     'How do you talk to your new coworkers? What do you talk about? How\ncan you impress your boss?\n' +
     'Sometimes the most difficult questions have the simplest solutions!\nWhere can I find the bathroom?\n' +
     'I love your shoes. Where did you get them?\nExcuse me, can you please speak up?\n'),
    ('resources/test/arial/test_arial_eng_20.png', 'arial',
     'How do you talk to your new coworkers? What do you\ntalk about? How can you impress your boss?\n' +
     'Sometimes the most difficult questions have the\nsimplest solutions!\nWhere can I find the bathroom?\n' +
     'I love your shoes. Where did you get them?\nExcuse me, can you please speak up?\n'),

    ('resources/test/arial/test_arial_eng1_40.png', 'arial',
     'How do you talk to your\nnew coworkers? What do\nyou talk about? How can\nyou impress your boss?\n'),
    ('resources/test/arial/test_arial_eng2_40.png', 'arial',
     'Sometimes the most\ndifficult questions have the\nsimplest solutions!\nWhere can I find the\nbathroom?\n'),
    ('resources/test/arial/test_arial_eng3_40.png', 'arial',
     'I love your shoes. Where\ndid you get them?\nExcuse me, can you\nplease speak up?\n'),

    ('resources/test/arial/test_arial_lat_10.png', 'arial',
     'Mama je gruz!\nPiernik jest z Afryki.\nKukurydza to nie robak, a jej facet ma metr i trzy.\n' +
     'Kalafior jest zielony i ma wszystkie spory tam, gdzie mam je i ja.\nProducent tworzy filmy, a w nich jest masa rozbieranych scen.\n' +
     'Julia jest jak wieloryb i ubiera rozmiar XXL.\nPartner Julii rzuca w wieloryba talerzem, bo akurat betoniarki przy sobie nie ma.\n'),
    ('resources/test/arial/test_arial_lat_15.png', 'arial',
     'Mama je gruz!\nPiernik jest z Afryki.\nKukurydza to nie robak, a jej facet ma metr i trzy.\n' +
     'Kalafior jest zielony i ma wszystkie spory tam, gdzie mam je i ja.\nProducent tworzy filmy, a w nich jest masa rozbieranych scen.\n' +
     'Julia jest jak wieloryb i ubiera rozmiar XXL.\nPartner Julii rzuca w wieloryba talerzem, bo akurat betoniarki przy sobie\nnie ma.\n'),
    ('resources/test/arial/test_arial_lat_20.png', 'arial',
     'Mama je gruz!\nPiernik jest z Afryki.\nKukurydza to nie robak, a jej facet ma metr i trzy.\n' +
     'Kalafior jest zielony i ma wszystkie spory tam, gdzie\nmam je i ja.\nProducent tworzy filmy, a w nich jest masa\nrozbieranych scen.\n' +
     'Julia jest jak wieloryb i ubiera rozmiar XXL.\nPartner Julii rzuca w wieloryba talerzem, bo akurat\nbetoniarki przy sobie nie ma.\n'),

    ('resources/test/arial/test_arial_lat1_40.png', 'arial',
     'Mama je gruz!\nPiernik jest z Afryki.\nKukurydza to nie robak, a\njej facet ma metr i trzy.\n'),
    ('resources/test/arial/test_arial_lat2_40.png', 'arial',
     'Kalafior jest zielony i ma\nwszystkie spory tam, gdzie\nmam je i ja.\nProducent tworzy filmy, a\nw nich jest masa\nrozbieranych scen.\n'),
    ('resources/test/arial/test_arial_lat3_40.png', 'arial',
     'Julia jest jak wieloryb i\nubiera rozmiar XXL.\nPartner Julii rzuca w\nwieloryba talerzem, bo\nakurat betoniarki przy\nsobie nie ma.\n'),

    ('resources/test/arial/test_arial_pl_10.png', 'arial',
     'Ręczne robótki na działce Pana Zdzisława przynoszą więcej szkód niż pożytku.\n' +
     'Analfabeta, który nie jest w stanie pokonać innego analfabety, jest głupszy od całej reszty społeczeństwa.\n' +
     'Gubić klucze każdy może, należy pamiętać żeby zamykać mieszkania zawsze po wyjściu z nich.\n' +
     'Źdźbło trawy delikatnie kłuje mnie w pośladek.\nZerżnąć wszystko od kolegi na sprawdzianie każdy potrafi.\n'),
    ('resources/test/arial/test_arial_pl_15.png', 'arial',
     'Ręczne robótki na działce Pana Zdzisława przynoszą więcej szkód niż\npożytku.\n' +
     'Analfabeta, który nie jest w stanie pokonać innego analfabety, jest\ngłupszy od całej reszty społeczeństwa.\n' +
     'Gubić klucze każdy może, należy pamiętać żeby zamykać mieszkania\nzawsze po wyjściu z nich.\n' +
     'Źdźbło trawy delikatnie kłuje mnie w pośladek.\nZerżnąć wszystko od kolegi na sprawdzianie każdy potrafi.\n'),
    ('resources/test/arial/test_arial_pl_20.png', 'arial',
     'Ręczne robótki na działce Pana Zdzisława przynoszą\nwięcej szkód niż pożytku.\n' +
     'Analfabeta, który nie jest w stanie pokonać innego\nanalfabety, jest głupszy od całej reszty\nspołeczeństwa.\n' +
     'Gubić klucze każdy może, należy pamiętać żeby\nzamykać mieszkania zawsze po wyjściu z nich.\n' +
     'Źdźbło trawy delikatnie kłuje mnie w pośladek.\nZerżnąć wszystko od kolegi na sprawdzianie każdy\npotrafi.\n'),

    ('resources/test/arial/test_arial_pl1_40.png', 'arial',
     'Ręczne robótki na działce\nPana Zdzisława przynoszą\nwięcej szkód niż pożytku.\n'),
    ('resources/test/arial/test_arial_pl2_40.png', 'arial',
     'Analfabeta, który nie jest w\nstanie pokonać innego\nanalfabety, jest głupszy od\ncałej reszty\nspołeczeństwa.\n'),
    ('resources/test/arial/test_arial_pl3_40.png', 'arial',
     'Gubić klucze każdy może,\nnależy pamiętać żeby\nzamykać mieszkania\nzawsze po wyjściu z nich.\n'),
    ('resources/test/arial/test_arial_pl4_40.png', 'arial',
     'Źdźbło trawy delikatnie\nkłuje mnie w pośladek.\nZerżnąć wszystko od\nkolegi na sprawdzianie\nkażdy potrafi.\n'),
]

for i, test in enumerate(test_cases):
    anal = analise2(test[0], test[1])
    print('Test nr: {} from {} file\n'.format(i, test[0]))
    print('Desired:')
    print(test[2])
    print('Actual:')
    print(anal)
    print('Distance: {}'.format(eval(test[2], anal)))
    print('---------------------------------------\n')
