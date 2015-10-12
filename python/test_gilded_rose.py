# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def tests_update_quality_should_decrement_days_and_quality(self):
        items = [Item("foo", 2, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(2, items[0].quality)
    
    def tests_update_quality_should_degrade_quality_twice_as_fast_once_the_sell_by_date_has_passed(self):
        items = [Item("foo", 0, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(2, items[0].quality)

    def tests_update_quality_shouldnt_degrades_quality_under_0(self):
        items = [Item("foo", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_update_quality_should_increases_the_quality_of_aged_brie_the_older_it_gets(self):
        items = [Item("Aged Brie", 2, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(5, items[0].quality)

    def test_update_quality_shouldnt_increase_the_quality_over_50(self):
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_update_should_never_decrease_sulfuras_quality_or_days(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)
        self.assertEquals(2, items[0].sell_in)

    def test_update_should_increase_quality_of_backstage_pass_by_2_when_sell_in_is_10_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_update_should_increase_quality_of_backstage_pass_by_3_when_sell_in_is_5_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 23)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(26, items[0].quality)

    def test_update_should_drops_quality_of_backstage_to_0_after_the_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 23)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
