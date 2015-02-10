from django.test import TestCase


class HelloTestCase(TestCase):

    def test_page(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

        if resp.context is not None:  # if none it is cached
            self.assertEqual(resp.context['greet'], 'hello')

    def test_page_not_found(self):
        resp = self.client.get('/xxx/')
        self.assertEqual(resp.status_code, 404)