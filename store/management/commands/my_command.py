from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'my first own command'

    def handle(self, *args, **options):
        print('this is my command exicuted')
        for i in range(10):
            print('#'*i)