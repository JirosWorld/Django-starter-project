from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Send a test notification to verify if notifications are properly configured"

    def add_arguments(self, parser):
        parser.add_argument(
            "username", help="Specifies the username for the superuser.",
        )
        parser.add_argument(
            "email", help="Specifies the email for the superuser.",
        )

    def handle(self, *args, **options):
        User = get_user_model()
        username = options["username"]
        email = options["email"]

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING("Initial superuser already exists, doing nothing")
            )
            return

        call_command(
            "createsuperuser",
            username=username,
            email=email,
            no_input=True,
            interactive=False,
        )

        user = User.objects.get(username=username)

        password = User.objects.make_random_password(length=20)
        user.set_password(password)
        user.save()

        send_mail(
            f"Credentials for {settings.PROJECT_NAME}",
            f"Credentials for project: {settings.PROJECT_NAME}\n\nUsername: {username}\nPassword: {password}",
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        self.stdout.write(self.style.SUCCESS("Initial superuser successfully created"))
