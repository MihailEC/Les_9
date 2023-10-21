import unittest
from loto_classes import Player

class TestPlayer(unittest.TestCase):
	"""Тестирование класса Player"""
	def setUp(self):
		self.player = Player(1, 'ч', 'Max')
		self.player.card_list = [1, 4, 2, 67, 15, 46, 17, 8, 10, 45, 11, 89, 24, 14, 80]

	def test_init(self):
		self.assertEqual(self.player.type, 'ч')
		self.assertEqual(self.player.name, 'Max')
		self.assertEqual(self.player.number_player, 1)

	def test_change_card(self):
		choice_dice = 15
		self.player.change_card(choice_dice)
		self.assertIn('-', self.player.card_list)

	def test_check_number_in_card_True(self):
		choice_dice = 80
		self.assertTrue(self.player.check_number_in_card(choice_dice))

	def test_check_number_in_card_Fals(self):
		choice_dice = 60
		self.assertFalse(self.player.check_number_in_card(choice_dice))

	def test_check_type_True(self):
		self.assertTrue(self.player.check_type())

	def test_check_type_Fals(self):
		self.player.type = 'к'
		self.assertFalse(self.player.check_type())

	# def test_check_win_Fals(self):
	# 	win_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
	# 	self.assertFalse(self.player.check_win(win_list))

	# def test_check_win_True(self):
	# 	self.player.card_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
	# 	win_list = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
	# 	self.assertTrue(self.player.check_win(win_list))

	def test_str(self):
		player_str = str(self.player)
		compare_str = f'Игрок {self.player.number_player}: {self.player.name}'
		self.assertEqual(player_str, compare_str)

	def test_eq_True(self):
		other = [1, 4, 2, 67, 15, 46, 17, 8, 10, 45, 11, 89, 24, 14, 80]
		self.assertTrue(self.player.__eq__(other))

	def test_eq_False(self):
		other = ['-', '-', 2, 67, 15, 46, 17, 8, 10, 45, 11, 89, 24, 14, 80]
		self.assertFalse(self.player.__eq__(other))

