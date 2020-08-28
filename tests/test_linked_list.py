# from data_structures_and_algorithms.challenges.linked_list.linked_list import LinkedList
# # import pytest

# # @pytest.fixture
# # def test_prepare_info():
# #     books = LinkedList()
# #     a = books.append_info("History")
# #     b = books.append_info("Kids")
# #     c = books.append_info("Horror")
# #     d = books.includes("Novel")
# #     e = books.insert_between("Novel","Two_City")
# #     return {"a":a,"b":b,"c":c,"d":d,"e":e,"books":books}

# def test_first():
#     books = LinkedList()
#     books.append_info("History")
#     books.append_info("Horror")
#     books.includes("Novel")
#     expected = 'History -> Horror -> Novel -> None'
#     actual = books.__str__()
#     assert expected == actual

# def test_second(prepare_info):
#     prepare_info['books']
#     prepare_info['a']
#     prepare_info['b']
#     prepare_info['c']
#     expected = True
#     actual = prepare_info['books'].includes("Novel")
#     assert expected == actual

# def test_third(prepare_info):
#     prepare_info['books']
#     prepare_info['a']
#     prepare_info['b']
#     prepare_info['c']
#     expected = False
#     actual = prepare_info['books'].includes("since")
#     assert expected == actual

# def test_fourth(prepare_info):
#     prepare_info['books']
#     prepare_info['a']
#     prepare_info['b']
#     prepare_info['c']
#     expected = 'This function doesn\'t have been initialized yet'
#     actual = prepare_info['books'].insert_between("Novel")
#     assert expected == actual

# def test_fifth(prepare_info):
#     new_book = prepare_info['books'].insert('Advanture')
#     expected = 'Advanture -> History -> Horror -> Novel -> None'
#     actual = prepare_info['books'].__str__()
#     assert expected == actual