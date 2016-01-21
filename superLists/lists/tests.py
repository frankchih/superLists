from django.core.urlresolvers import resolve, reverse
from django.http.request import HttpRequest
from django.test import TestCase

from lists.models import Item, List
from lists.views import homePage


class HomePageTest(TestCase):
    
    
    def test_root_url_to_homePage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homePage)
        
    
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


class ListViewTest(TestCase):
    
    def test_displays_only_items_for_that_list(self):
        correntList = List.objects.create()
        Item.objects.create(text='itemey 1', list=correntList)
        Item.objects.create(text='itemey 2', list=correntList)
        otherList = List.objects.create()
        Item.objects.create(text='other list item 1', list=otherList)
        Item.objects.create(text='other list item 2', list=otherList)
        response = self.client.get(reverse('lists:viewList', args=(correntList.id, )))
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'itemey 1')
        self.assertNotContains(response, 'itemey 2')

    def test_use_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(reverse('lists:viewList', args=(list_.id, )))
        self.assertTemplateUsed(response, 'lists/list.html')
    
    def test_saving_a_POST_request(self):
        self.client.post('/lists/new/', data={'itemText':'新的項目'})
        self.assertEqual(Item.objects.count(), 1)
        newItem = Item.objects.first()
        self.assertEqual(newItem.text, '新的項目')


    def test_redirect_after_POST(self):
        response = self.client.post('/lists/new/', data={'itemText':'新的項目'})
        self.assertRedirects(response, reverse('lists:viewList'))        
        
        
        
        