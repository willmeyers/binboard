from django.urls import reverse

from rest_framework import test, status

from .models import User


class UserAuthTests(test.APITestCase):
    def setUp(self):
        u = User.objects.create(
                username='alice',
                email='alice@example.com',
                real_name=' Alice',
        )
        u.set_password('aSecurePa55word?')
        u.save()

    def test_obtain_token(self):
        data = {
            'username': 'alice',
            'password': 'aSecurePa55word?'
        }

        url = reverse('users:token_obtain_pair')
        
        resp = self.client.post(url, data=data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        token = resp.json()
        self.assertTrue('refresh' in token)
        self.assertTrue('access' in token)

    def test_refresh_token(self):
        data = {
            'username': 'alice',
            'password': 'aSecurePa55word?'
        }

        obtain_url = reverse('users:token_obtain_pair')
        refresh_url = reverse('users:token_refresh')

        resp = self.client.post(obtain_url, data=data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        token = resp.json()
        self.assertTrue('refresh' in token)
        self.assertTrue('access' in token)

        data = {
            'refresh': token['refresh']
        }

        resp = self.client.post(refresh_url, data=data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        refresh = resp.json()
        self.assertTrue('access' in refresh)


class UserTests(test.APITestCase):
    def setUp(self):
        u = User.objects.create(
                username='alice',
                email='alice@example.com',
                real_name='Alice',
        )
        u.set_password('aSecurePa55word?')
        u.save()

    def test_user_signup(self):
        data = {
            'username': 'bob',
            'email': 'bob@example.com',
            'real_name': 'Bob',
            'password': 'aSecurePa55word?'
        }

        url = reverse('users:user-list')

        resp = self.client.post(url, data=data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(username='bob').username, 'bob')

    def test_user_list(self):
        url = reverse('users:user-list')

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_me_action(self):
        me_url = reverse('users:user-me')

        resp = self.client.get(me_url)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        data = {
            'username': 'alice',
            'password': 'aSecurePa55word?'
        }

        tk_url = reverse('users:token_obtain_pair')
        
        resp = self.client.post(tk_url, data=data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        token = resp.json()
        self.assertTrue('refresh' in token)
        self.assertTrue('access' in token)

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token['access']}")
        
        resp = self.client.get(me_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        user = resp.json()
        self.assertDictEqual(user, {'username': 'alice', 'email': 'alice@example.com', 'real_name': 'Alice'})

    def test_user_change_password_action(self):
        uid = User.objects.get(real_name='Alice').id

        change_pwd_url = reverse('users:user-change-password', kwargs={'pk': uid})

        resp = self.client.get(change_pwd_url)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        data = {
            'username': 'alice',
            'password': 'aSecurePa55word?'
        }

        tk_url = reverse('users:token_obtain_pair')
        
        resp = self.client.post(tk_url, data=data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        token = resp.json()
        self.assertTrue('refresh' in token)
        self.assertTrue('access' in token)

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token['access']}")
        
        data = {
            'new_password': 'anotherSecurePa55word?',
            'confirm_new_password': 'anotherSecurePa55word?'
        }

        resp = self.client.post(change_pwd_url, data=data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        data = {
            'username': 'alice',
            'password': 'anotherSecurePa55word?'
        }
        
        resp = self.client.post(tk_url, data=data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        token = resp.json()
        self.assertTrue('refresh' in token)
        self.assertTrue('access' in token)
