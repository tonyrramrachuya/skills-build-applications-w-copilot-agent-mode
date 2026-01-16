from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Team, User, Activity, Workout, Leaderboard

class APIRootTest(APITestCase):
	def test_api_root(self):
		url = reverse('api-root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class TeamTests(APITestCase):
	def test_create_team(self):
		url = reverse('team-list')
		data = {'name': 'Test Team'}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserTests(APITestCase):
	def setUp(self):
		self.team = Team.objects.create(name='Test Team')
	def test_create_user(self):
		url = reverse('user-list')
		data = {'username': 'testuser', 'email': 'test@example.com', 'team_id': self.team.id}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
	def setUp(self):
		self.team = Team.objects.create(name='Test Team')
		self.user = User.objects.create_user(username='testuser', email='test@example.com', team=self.team)
	def test_create_activity(self):
		url = reverse('activity-list')
		data = {'user_id': self.user.id, 'type': 'run', 'duration': 30, 'distance': 5}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
	def setUp(self):
		self.team = Team.objects.create(name='Test Team')
		self.user = User.objects.create_user(username='testuser', email='test@example.com', team=self.team)
	def test_create_workout(self):
		url = reverse('workout-list')
		data = {'user_id': self.user.id, 'name': 'Chest Day', 'description': 'Bench press'}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(APITestCase):
	def setUp(self):
		self.team = Team.objects.create(name='Test Team')
		self.user = User.objects.create_user(username='testuser', email='test@example.com', team=self.team)
	def test_create_leaderboard(self):
		url = reverse('leaderboard-list')
		data = {'user_id': self.user.id, 'points': 100}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
