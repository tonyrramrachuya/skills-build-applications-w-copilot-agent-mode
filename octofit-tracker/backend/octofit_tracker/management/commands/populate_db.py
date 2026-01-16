
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark', team=marvel),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', first_name='Steve', last_name='Rogers', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='password', first_name='Diana', last_name='Prince', team=dc),
        ]

        # Create activities
        activities = [
            Activity.objects.create(user=users[0], type='run', duration=30, distance=5),
            Activity.objects.create(user=users[1], type='cycle', duration=60, distance=20),
            Activity.objects.create(user=users[2], type='swim', duration=45, distance=2),
            Activity.objects.create(user=users[3], type='yoga', duration=50, distance=0),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(user=users[0], name='Chest Day', description='Bench press, pushups'),
            Workout.objects.create(user=users[1], name='Leg Day', description='Squats, lunges'),
            Workout.objects.create(user=users[2], name='Cardio', description='Running, cycling'),
            Workout.objects.create(user=users[3], name='Flexibility', description='Yoga, stretching'),
        ]

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=90)
        Leaderboard.objects.create(user=users[2], points=95)
        Leaderboard.objects.create(user=users[3], points=85)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
