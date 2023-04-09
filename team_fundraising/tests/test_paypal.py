
from paypal.standard.models import ST_PP_COMPLETED
from django.conf import settings

from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from django.utils import timezone
from unittest.mock import patch

from team_fundraising.text import Donation_text, Fundraiser_text
from team_fundraising.paypal import  process_paypal


class IPNobj(object):
    def __init__(self,
            payment_status,
            receiver_email,
            custom ):
        self.payment_status = payment_status
        self.receiver_email = receiver_email
        self.custom = custom

class DonationTest(TransactionTestCase):
    reset_sequences = True
    fixtures = ["testdata.json"]

    @patch('team_fundraising.paypal.send_mail')
    def test_paypal(self, mock_sendmail):
        EMAIL = "test@test.com"
        settings.PAYPAL_ACCOUNT = EMAIL
        ipn = IPNobj(ST_PP_COMPLETED, EMAIL, 2)
        # make a donation
        data={
            "name": "julio jones",
            "amount": "100",
            "other_amount":"10",
            "email": "julio@nothing.com",
            "anonymous": False,
            "tax_name": "todo",
            "message": "test",
            "address": "111 sesame st",
            "city": "sesame",
            "province": "WA",
            "country": "USA",
            "postal_code": "33322",
            "date": timezone.now()
            }
        response = self.client.post(
                reverse('team_fundraising:donation', args='1'),
                data
            
            )
        self.assertEqual(response.status_code, 201)


        process_paypal(ipn)
        self.assertEqual(mock_sendmail.call_count, 2)


 
