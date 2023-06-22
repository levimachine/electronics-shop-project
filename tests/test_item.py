"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item_calculate_total_price():
    example_item = Item('Кабачок', 100, 5)
    assert example_item.calculate_total_price() == 500


def test_item_apply_discount():
    example_item = Item('Кабачок', 100, 5)
    Item.pay_rate = 2
    example_item.apply_discount()
    assert example_item.price == 200
