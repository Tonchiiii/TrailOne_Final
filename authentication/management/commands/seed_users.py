from django.core.management.base import BaseCommand
from authentication.models import Users

class Command(BaseCommand):
    help = 'Seed the Users table with sample data'

    def handle(self, *args, **kwargs):
        users_data = [
            {
                'name': 'Lorelie Canete',
                'role': 'SUPER_ADMIN',
                'email': 'lorie@trailone.com',
                'password': 'password',
            },
            {
                'name': 'Charlie Brown',
                'role': 'ADMIN',
                'email': 'charlie@trailone.com',
                'password': 'password',
            },
            {
                'name': 'Bob Smith',
                'role': 'CLIENT',
                'email': 'bob@trailone.com',
                'password': 'password',
            },
            {
                'name': 'Rey Ban',
                'role': 'CLIENT',
                'email': 'rey@trailone.com',
                'password': 'password',
            },
            {
                'name': 'John Doe',
                'role': 'CLIENT',
                'email': 'john@trailone.com',
                'password': 'password',
            },
            {
                'name': 'Rhobby Calixtro',
                'role': 'CLIENT',
                'email': 'mrjcalixtro@tip.edu.ph',
                'password': 'password',
            },
            {
                'name': 'Anton Ramos',
                'role': 'CLIENT',
                'email': 'gerardramos0213@gmail.com',
                'password': 'password',
            },
        ]

        for user_data in users_data:
            # Create or update user using your manager's create_user method to handle password hashing
            Users.objects.update_or_create(
                email=user_data['email'],
                defaults={
                    'name': user_data['name'],
                    'role': user_data['role'],
                    # Call set_password later after getting or creating user
                },
            )
            # After update_or_create, get the user and set password properly
            user = Users.objects.get(email=user_data['email'])
            user.set_password(user_data['password'])
            user.save()

            self.stdout.write(f"Created/Updated user {user.email} with hashed password")

        self.stdout.write(self.style.SUCCESS('Successfully seeded Users table.'))
