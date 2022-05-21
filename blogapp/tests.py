from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse 
from .models import Post 

# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'default',
            )
        self.post = Post.objects.create(
            title = 'test title',
            body = 'test body',
            author = self.user,
            )
    def test_str_representation(self):
        post = Post(title='boy')
        #print(str(post))
        #print(post.title)
        self.assertEqual(str(post), post.title)
    def test_post_content(self):
        #print(self.post.title)
        self.assertEqual(f'{self.post.title}', 'test title')
        self.assertEqual(f'{self.post.body}', 'test body')
        self.assertEqual(f'{self.post.author}', 'testuser')
    def test_post_list_view(self):
        response = self.client.get(reverse('blogapphome'))
        #print(str(response))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')
        self.assertTemplateUsed(response, 'home.html')
    def test_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/270/')
        #print(str(response))
        #print (str(no_response))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'post_detail.html')