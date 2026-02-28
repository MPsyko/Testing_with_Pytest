import pytest
from cards import Card


class TestEquality:
	def test_equality(self):
		c1 = Card("something", "Dom", "todo", 123)
		c2 = Card("something", "Dom", "todo", 123)
		assert c1 == c2

	def test_equality_with_diff_ids(self):
		c1 = Card("something", "Dom", "todo", 123)
		c2 = Card("something", "Dom", "todo", 4567)
		assert c1 == c2

	def test_inequality(self):
		c1 = Card("something", "Dom", "todo", 123)
		c2 = Card("something else", "Dum", "done", 123)
		assert c1 != c2

