from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime

User = get_user_model()

class ProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='pass1234')
        # profile créé par signal

    def login(self):
        self.client.login(username='testuser', password='pass1234')

    def test_profile_edit_driver_fields(self):
        self.login()
        url = reverse('profile_edit')
        # définir conducteur + infos véhicule + trajet
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'new@example.com',
            'is_driver': 'on',  # coche la checkbox
            'vehicle_type': 'voiture',
            'seats': '4',
            'brand': 'Toyota',
            'model': 'Corolla',
            'departure_time': '08:30',
            'departure_lat': '6.3703',  # ex. Cotonou
            'departure_lng': '2.3912',
        }
        image = SimpleUploadedFile("avatar.jpg", b"file_content", content_type="image/jpeg")
        resp = self.client.post(url, {**data, 'photo': image}, follow=True)
        self.assertContains(resp, "Ton profil a bien été mis à jour.")
        self.user.refresh_from_db()
        profile = self.user.profile
        self.assertTrue(profile.is_driver)
        self.assertEqual(profile.vehicle_type, 'voiture')
        self.assertEqual(profile.seats, 4)
        self.assertEqual(profile.brand, 'Toyota')
        self.assertEqual(profile.model, 'Corolla')
        self.assertEqual(profile.departure_time, datetime.time(8, 30))
        self.assertAlmostEqual(profile.departure_lat, 6.3703, places=4)
        self.assertAlmostEqual(profile.departure_lng, 2.3912, places=4)

    def test_profile_edit_not_driver_clears_fields(self):
        self.login()
        # premièrement on met conducteur, puis on décoche
        profile = self.user.profile
        profile.is_driver = True
        profile.vehicle_type='moto'
        profile.seats=1
        profile.save()
        url = reverse('profile_edit')
        data = {
            'first_name': 'Test2',
            'last_name': 'User2',
            'email': 'test2@example.com',
            # is_driver absent => False
            # vehicle_type etc. ne sont pas envoyés
        }
        resp = self.client.post(url, data, follow=True)
        self.assertContains(resp, "Ton profil a bien été mis à jour.")
        profile.refresh_from_db()
        self.assertFalse(profile.is_driver)
        self.assertIsNone(profile.vehicle_type)
        self.assertIsNone(profile.seats)
        self.assertEqual(profile.brand, '')
        self.assertEqual(profile.model, '')
