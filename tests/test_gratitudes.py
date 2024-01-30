from lib.gratitudes import *

def test_add_multiple_items_to_list():
    grat_list = Gratitudes()
    grat_list.add('family')
    grat_list.add('friends')
    grat_list.add('health')
    grat_list.add('knowledge')
    assert grat_list.format() == 'Be grateful for: family, friends, health, knowledge'
