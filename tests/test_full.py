from datetime import datetime
from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

from accounts.models import Profile
from events.models import Event
from groups.models import Group
from hobbies.models import Hobby
from interactions.models import Comment

User = get_user_model()


class HobbyHiveTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@test.com', password='password123')

        self.client.login(username='testuser', password='password123')


        self.hobby = Hobby.objects.create(name='Chess', description='Play chess', owner=self.user)

        self.group = Group.objects.create(
            name='Chess Club',
            description='Chess group',
            owner=self.user,
            hobby=self.hobby
        )

        event_date = timezone.make_aware(datetime(2026, 5, 1))

        self.event = Event.objects.create(
            title='Chess Tournament',
            description='Annual chess tournament',
            date=event_date,
            group=self.group,
            organizer=self.user
        )

    @patch('events.tasks.send_mail')
    def test_event_email(self, mock_send):
        self.event = Event.objects.create(
            title='Chess Tournament',
            description='Annual chess tournament',
            date='2026-05-01',
            group=self.group,
            organizer=self.user
        )
        mock_send.assert_not_called()

    def test_login_logout(self):
        response = self.client.get(reverse('accounts:profile-detail', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.client.post(reverse('accounts:logout'))
        response = self.client.get(reverse('common:home'))
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'newuser', 'email': 'new@test.com',
            'password1': 'Password123!', 'password2': 'Password123!'
        })
        self.assertEqual(User.objects.filter(username='newuser').exists(), True)

    def test_profile_detail_shows_user_info(self):
        response = self.client.get(reverse('accounts:profile-detail', args=[self.user.pk]))
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.email)

    def test_hobby_list_and_detail(self):
        response = self.client.get(reverse('hobbies:hobby-list'))
        self.assertContains(response, self.hobby.name)
        response = self.client.get(reverse('hobbies:hobby-detail', args=[self.hobby.pk]))
        self.assertContains(response, self.hobby.description)

    def test_hobby_join_leave(self):
        self.client.get(reverse('hobbies:hobby-join', args=[self.hobby.pk]))
        self.assertIn(self.user, self.hobby.participants.all())
        self.client.get(reverse('hobbies:hobby-leave', args=[self.hobby.pk]))
        self.assertNotIn(self.user, self.hobby.participants.all())

    def test_hobby_edit_permission(self):
        response = self.client.get(reverse('hobbies:hobby-edit', args=[self.hobby.pk]))
        self.assertEqual(response.status_code, 200)

    def test_group_creation_and_detail(self):
        response = self.client.get(reverse('groups:group-list'))
        self.assertContains(response, self.group.name)
        response = self.client.get(reverse('groups:group-detail', args=[self.group.pk]))
        self.assertContains(response, self.group.description)

    def test_event_creation_and_detail(self):
        response = self.client.get(reverse('events:event-list'))
        self.assertContains(response, self.event.title)
        response = self.client.get(reverse('events:event-detail', args=[self.event.pk]))
        self.assertContains(response, self.event.description)

    def test_comment_creation_for_group(self):
        response = self.client.post(reverse('interactions:comment-create') + f'?group={self.group.pk}', {
            'content': 'Nice group!'
        })
        self.assertEqual(Comment.objects.filter(group=self.group, user=self.user).count(), 1)

    def test_comment_creation_for_event(self):
        response = self.client.post(reverse('interactions:comment-create') + f'?event={self.event.pk}', {
            'content': 'Excited for this event!'
        })
        self.assertEqual(Comment.objects.filter(event=self.event, user=self.user).count(), 1)

    def test_comment_requires_authentication(self):
        self.client.logout()
        response = self.client.post(reverse('interactions:comment-create') + f'?event={self.event.pk}', {
            'content': 'Should fail'
        })
        self.assertEqual(response.status_code, 302)  # redirected to login

    def test_404_page(self):
        response = self.client.get('/nonexistent-url/')
        self.assertEqual(response.status_code, 404)

    def test_403_page(self):
        self.client.logout()
        self.client.login(username='otheruser', password='password123')
        response = self.client.get(reverse('hobbies:hobby-edit', args=[self.hobby.pk]))
        self.assertEqual(response.status_code, 403)

    def test_simple_placeholder(self):
        self.assertTrue(True)