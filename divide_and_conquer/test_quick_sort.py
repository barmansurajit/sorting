from unittest import TestCase
from divide_and_conquer import quick_sort


class Test(TestCase):
    def test_two_items_sort(self):
        lst = [3, 2]
        quick_sort.quick_sort_lomuto(lst)
        self.assertEqual([2, 3], lst)

    def test_single_item_sort(self):
        lst = [1]
        quick_sort.quick_sort_lomuto(lst)
        self.assertEqual([1], lst)

    def test_empty_list_sort(self):
        lst = []
        quick_sort.quick_sort_lomuto(lst)
        self.assertEqual([], lst)

    def test_zero_in_list_sort(self):
        lst = [10, 0]
        quick_sort.quick_sort_lomuto(lst)
        self.assertEqual([0, 10], lst)

    def test_odd_number_of_items_sort(self):
        lst = [13, 7, 5]
        quick_sort.quick_sort_lomuto(lst)
        self.assertEqual([5, 7, 13], lst)

    def test_even_number_of_items_sort(self):
        lst = [4, 2, 8, 7, 1, 3, 5, 6]
        quick_sort.quick_sort_lomuto(lst)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], lst)

    def test_duplicate_integers_in_list(self):
        lst = [1, 2, 2, 1, 0, 0, 15, 15]
        quick_sort.quick_sort_lomuto(lst)
        self.assertEqual([0, 0, 1, 1, 2, 2, 15, 15], lst)
