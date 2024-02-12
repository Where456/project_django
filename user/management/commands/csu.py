from django.core.management import BaseCommand
from user.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = CustomUser.objects.create(
            email='admin@sky.pro',
            avatar='main_app/products/2023-12-27_14.00.53.jpg',
            phone='1234567890',
            country='Country Name',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123qwe456rty')
        user.save()
