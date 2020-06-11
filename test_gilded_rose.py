# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_sulfuras_maintains_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 15, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_aged_brie_ripens(self):
        items = [Item("Aged Brie", 15, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(31, items[0].quality)

    def test_aged_brie_peaks_at_50(self):
        items = [Item("Aged Brie", 15, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_normal_items_lose_quality(self):
        items = [Item("Golden Apples", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)

    def test_normal_items_min_0_quality(self):
        items = [Item("Glass Sword", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_normal_items_lose_quality_2x_after_date(self):
        items = [Item("Pear Cider", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_back_stage_pass_gains_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 30, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(29, items[0].sell_in)

    def test_back_stage_pass_gains__2_quality_within_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_back_stage_pass_gains__3_quality_within_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_back_stage_pass_loses_all_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_back_stage_pass_max_50_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(2, items[0].sell_in)

    # def test_conjured_item_after_sell_by_date(self):
    #     items = [Item("Conjured Mana Potion", 35, 40)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEqual(38, items[0].quality)
    #
    # def test_conjured_item_degraces_twice_as_fast(self):
    #     items = [Item("Conjured Mana Potion", 0, 15)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEqual(11, items[0].quality)
    #

if __name__ == '__main__':
    unittest.main()
