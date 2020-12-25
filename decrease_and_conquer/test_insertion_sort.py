from unittest import TestCase
from decrease_and_conquer import insertion_sort


class Test(TestCase):
    def test_even_number_of_items_sort_1(self):
        lst = [23, 7, 13, 5]
        insertion_sort.insertion_sort_recursive(lst, len(lst))
        self.assertEqual([5, 7, 13, 23], lst)

    def test_duplicate_integers_in_list_1(self):
        lst = [1, 2, 2, 1, 0, 0, 15, 15]
        insertion_sort.insertion_sort_recursive(lst, len(lst))
        self.assertEqual([0, 0, 1, 1, 2, 2, 15, 15], lst)

    def test_even_number_of_items_sort_2(self):
        lst = [23, 7, 13, 5]
        insertion_sort.insertion_sort_recursive_2(lst, len(lst))
        self.assertEqual([5, 7, 13, 23], lst)

    def test_duplicate_integers_in_list_2(self):
        lst = [1, 2, 2, 1, 0, 0, 15, 15]
        insertion_sort.insertion_sort_recursive_2(lst, len(lst))
        self.assertEqual([0, 0, 1, 1, 2, 2, 15, 15], lst)

    def test_two_items_sort_2(self):
        lst = [3, 2]
        insertion_sort.insertion_sort_recursive_2(lst, len(lst))
        self.assertEqual([2, 3], lst)

    def test_single_item_sort_2(self):
        lst = [1]
        insertion_sort.insertion_sort_recursive_2(lst, len(lst))
        self.assertEqual([1], lst)

    def test_empty_list_sort_2(self):
        lst = []
        insertion_sort.insertion_sort_recursive_2(lst, len(lst))
        self.assertEqual([], lst)

    def test_zero_in_list_sort_2(self):
        lst = [10, 0]
        insertion_sort.insertion_sort_recursive_2(lst, len(lst))
        self.assertEqual([0, 10], lst)

    def test_odd_number_of_items_sort_2(self):
        lst = [13, 7, 5]
        insertion_sort.insertion_sort_recursive_2(lst, len(lst))
        self.assertEqual([5, 7, 13], lst)

    def test_even_number_of_items_sort_3(self):
        lst = [23, 7, 13, 5]
        insertion_sort.insertion_sort_iterative(lst)
        self.assertEqual([5, 7, 13, 23], lst)

    def test_two_items_sort_3(self):
        lst = [3, 2]
        insertion_sort.insertion_sort_iterative(lst)
        self.assertEqual([2, 3], lst)

    def test_single_item_sort_3(self):
        lst = [1]
        insertion_sort.insertion_sort_iterative(lst)
        self.assertEqual([1], lst)

    def test_empty_list_sort_3(self):
        lst = []
        insertion_sort.insertion_sort_iterative(lst)
        self.assertEqual([], lst)

    def test_zero_in_list_sort_3(self):
        lst = [10, 0]
        insertion_sort.insertion_sort_iterative(lst)
        self.assertEqual([0, 10], lst)

    def test_odd_number_of_items_sort_3(self):
        lst = [13, 7, 5]
        insertion_sort.insertion_sort_iterative(lst)
        self.assertEqual([5, 7, 13], lst)
