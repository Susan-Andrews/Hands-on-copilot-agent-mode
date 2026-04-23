from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User.objects.create(email='captain@marvel.com', name='Captain Marvel', team='marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc'),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=date(2024, 4, 1))
        Activity.objects.create(user=users[1], type='walk', duration=45, date=date(2024, 4, 2))
        Activity.objects.create(user=users[2], type='cycle', duration=60, date=date(2024, 4, 3))
        Activity.objects.create(user=users[3], type='swim', duration=50, date=date(2024, 4, 4))

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Upper body', suggested_for='marvel')
        Workout.objects.create(name='Squats', description='Lower body', suggested_for='dc')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
