from django.test import TestCase
from django.contrib.auth import get_user_model


def sample_user(email='rohitjose@voice.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'rohitjose@voice.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            role='mentor'
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'rohitjose@VOICE.COM'
        user = get_user_model().objects.create_user(email,
                                                    'test123',
                                                    role='candidate')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'admin@voice.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
