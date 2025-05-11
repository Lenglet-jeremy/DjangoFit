from django.test import TestCase
from django.utils import timezone
from .models import Customer, Plan, Subscription

class CustomerTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="Alice", email="alice@test.com", phone="0600000000")
        self.plan = Plan.objects.create(name="Mensuel", price=30, duration_days=30)
        self.subscription = Subscription.objects.create(
            customer=self.customer,
            plan=self.plan,
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timezone.timedelta(days=30)
        )

    def test_subscription_is_active(self):
        self.assertTrue(self.subscription.is_active())

