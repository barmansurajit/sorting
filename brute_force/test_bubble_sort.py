from unittest import TestCase
from brute_force import bubble_sort


class Test(TestCase):
    def test_two_items_sort(self):
        lst = [3, 2]
        sorted_lst = bubble_sort.bubble_sort(lst)
        self.assertEqual([2, 3], sorted_lst)

    def test_single_item_sort(self):
        lst = [1]
        sorted_lst = bubble_sort.bubble_sort(lst)
        self.assertEqual([1], sorted_lst)

    def test_empty_list_sort(self):
        lst = []
        sorted_lst = bubble_sort.bubble_sort(lst)
        self.assertEqual([], sorted_lst)

    def test_zero_in_list_sort(self):
        lst = [10, 0]
        sorted_lst = bubble_sort.bubble_sort(lst)
        self.assertEqual([0, 10], sorted_lst)

    def test_odd_number_of_items_sort(self):
        lst = [13, 7, 5]
        sorted_lst = bubble_sort.bubble_sort(lst)
        self.assertEqual([5, 7, 13], sorted_lst)

    def test_even_number_of_items_sort(self):
        lst = [23, 7, 13, 5]
        sorted_lst = bubble_sort.bubble_sort(lst)
        self.assertEqual([5, 7, 13, 23], sorted_lst)

    def test_duplicate_integers_in_list(self):
        lst = [1, 2, 2, 1, 0, 0, 15, 15]
        sorted_lst = bubble_sort.bubble_sort(lst)
        self.assertEqual([0, 0, 1, 1, 2, 2, 15, 15], sorted_lst)
