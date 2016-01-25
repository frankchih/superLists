from django.test import TestCase

from lists.models import Item, List
from django.core.exceptions import ValidationError


class ListAndItemModelTest(TestCase):
    
    def test_save_and_retrieving_items(self):
        list_ = List()
        list_.save()
        
        firstItem = Item()
        firstItem.text = '第一個清單項目'
        firstItem.list = list_
        firstItem.save()
        
        secondItem = Item()
        secondItem.text = '第二個清單項目'
        secondItem.list = list_
        secondItem.save()

        savedLists = List.objects.first()
        self.assertEqual(savedLists, list_)
        
        savedItems = Item.objects.all()
        self.assertEqual(savedItems.count(), 2)
        
        firstSavedItem = savedItems[0]
        secondSavedItem = savedItems[1]
        self.assertEqual(firstSavedItem.text, '第一個清單項目')
        self.assertEqual(firstItem.list, list_)
        self.assertEqual(secondSavedItem.text, '第二個清單項目')
        self.assertEqual(secondItem.list, list_)
        
    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.full_clean()
            item.save()
            
            
            