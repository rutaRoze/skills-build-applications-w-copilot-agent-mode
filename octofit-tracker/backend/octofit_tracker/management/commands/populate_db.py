from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='pass', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='pass', team=dc)

        # Create Activities
        Activity.objects.create(user=ironman, type='run', duration=30)
        Activity.objects.create(user=captain, type='cycle', duration=45)
        Activity.objects.create(user=batman, type='swim', duration=25)
        Activity.objects.create(user=superman, type='run', duration=60)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=50)

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=superman, score=120)
        Leaderboard.objects.create(user=batman, score=90)
        Leaderboard.objects.create(user=captain, score=110)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
