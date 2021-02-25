from parser_for_term import two_stek_parser

def test_parser_good():
    assert two_stek_parser('1+1') == 2.0

def test_parser_good_one_more():
    assert two_stek_parser('(1+1)*2-3') == 1.0

def test_parser_good_one_more_again():
    assert two_stek_parser('(1.+1))*2-3') == None