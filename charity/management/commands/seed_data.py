import os
import urllib.request
from django.core.management.base import BaseCommand
from django.conf import settings
from charity.models import Cause, Event, News

class Command(BaseCommand):
    help = 'Seed initial data for Causes, Events, and News'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Cause.objects.all().delete()
        Event.objects.all().delete()
        News.objects.all().delete()

        # Create sample Causes
        Cause.objects.create(
            title='Clean Water Initiative',
            description='Providing clean water to communities in need.',
            is_active=True,
            icon='fas fa-tint'
        )
        Cause.objects.create(
            title='Education for All',
            description='Supporting education for underprivileged children.',
            is_active=True,
            icon='fas fa-book'
        )
        Cause.objects.create(
            title='Healthcare Access',
            description='Improving healthcare facilities in rural areas.',
            is_active=True,
            icon='fas fa-heartbeat'
        )

        # Create sample Events
        Event.objects.create(
            title='Charity Run 2024',
            description='Annual charity run to raise funds for education.',
            date='2024-09-15',
            location='Central Park',
        )
        Event.objects.create(
            title='Health Camp',
            description='Free health checkup camp for local communities.',
            date='2024-10-10',
            location='Community Center',
        )

        # Download image for news item
        image_url = 'https://images.yourstory.com/cs/5/f02aced0d86311e98e0865c1f0fe59a2/rural-education-1640238389356.png?fm=png&auto=format&blur=500'
        image_dir = os.path.join(settings.MEDIA_ROOT, 'news')
        os.makedirs(image_dir, exist_ok=True)
        image_path = os.path.join(image_dir, 'new_school_built.png')

        # Use urllib.request with headers to avoid 403 error
        req = urllib.request.Request(
            image_url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
            }
        )
        with urllib.request.urlopen(req) as response, open(image_path, 'wb') as out_file:
            out_file.write(response.read())

        # Download image for Successful Fundraiser news item
        fundraiser_image_url = 'https://payu.in/blog/wp-content/uploads/2022/08/NGO.png'
        fundraiser_image_path = os.path.join(image_dir, 'successful_fundraiser.png')

        # Use urllib.request with headers to avoid 403 error
        req_fundraiser = urllib.request.Request(
            fundraiser_image_url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
            }
        )
        with urllib.request.urlopen(req_fundraiser) as response, open(fundraiser_image_path, 'wb') as out_file:
            out_file.write(response.read())

        # Create sample News
        News.objects.create(
            title='Successful Fundraiser',
            content='We successfully raised funds for the clean water project.',
            author='Admin',
            date='2024-05-01',
            image='news/successful_fundraiser.png',
        )
        News.objects.create(
            title='New School Built',
            content='A new school has been built in the rural area.',
            author='Admin',
            date='2024-06-15',
            image='news/new_school_built.png',
        )

        self.stdout.write(self.style.SUCCESS('Sample data seeded successfully.'))
