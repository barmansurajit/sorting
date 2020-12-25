from unittest import TestCase
from others import counting_sort


class Test(TestCase):
    def test_two_items_sort(self):
        lst = [3, 2]
        result = counting_sort.counting_sort(lst)
        self.assertEqual([2, 3], result)

    def test_single_item_sort(self):
        lst = [1]
        result = counting_sort.counting_sort(lst)
        self.assertEqual([1], result)

    def test_empty_list_sort(self):
        lst = []
        result = counting_sort.counting_sort(lst)
        self.assertEqual([], result)

    def test_zero_in_list_sort(self):
        lst = [10, 0]
        result = counting_sort.counting_sort(lst)
        self.assertEqual([0, 10], result)

    def test_odd_number_of_items_sort(self):
        lst = [2, 1, 1, 0, 2, 5, 4, 0, 2, 8, 7, 7, 9, 2, 0, 1, 9]
        result = counting_sort.counting_sort(lst)
        self.assertEqual([0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 4, 5, 7, 7, 8, 9, 9], result)

    def test_even_number_of_items_sort(self):
        lst = [4, 2, 8, 7, 1, 3, 5, 6]
        result = counting_sort.counting_sort(lst)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], result)

    def test_duplicate_integers_in_list(self):
        lst = [1, 2, 2, 1, 0, 0, 15, 15]
        result = counting_sort.counting_sort(lst)
        self.assertEqual([0, 0, 1, 1, 2, 2, 15, 15], result)
