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


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_name():
    item1 = Item.all[0]
    item1.name = 'Тест'
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'
