from questions_three.lib import try_me

def test_try_me_type():
    assert(type(try_me(name='henry', quest='grail', answer='hello')) == dict)
