from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from django.utils import timezone
from unittest.mock import patch
from django.contrib import messages
from django.contrib.messages import get_messages
from team_fundraising.text import Donation_text, Fundraiser_text



class HomePageViewTests(TransactionTestCase):
    """ Test homepage information based on TestModels data """
    reset_sequences = True
    fixtures = ["testdata.json"]

    def test_homepage_loads(self):
        # Just test the top of the homepage loads with the campaign name
        response = self.client.get(reverse('team_fundraising:index', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['campaign'].name, 'Fundraising Campaign')

class HomePageViewTests2(TransactionTestCase):
    reset_sequences = True
    fixtures = ["testdata.json"]
    def test_homepage_totals(self):
        # Check the homepage displays total donations and raised
        response = self.client.get(reverse('team_fundraising:index', args='1'))
        self.assertEqual(response.context['total_raised'], 50.00)
        self.assertEqual(response.context['campaign'].goal, 10000.00)

class HomePageViewTests3(TransactionTestCase):
    reset_sequences = True
    fixtures = ["testdata.json"]
    def test_homepage_fundraiser(self):
        # Check the first fundraiser has the right information
        response = self.client.get(reverse('team_fundraising:index', args='1'))
        self.assertEqual(
            response.context['fundraisers'][0].name, 'First Fundraiser'
        )
        self.assertEqual(
            response.context['fundraisers'][0].total_raised, 50.00
        )
        self.assertEqual(
            response.context['fundraisers'][0].goal, 200.00
        )

class HomePageViewTests4(TransactionTestCase):
    fixtures = ["testdata.json"]
    def test_empty_homepage_fundraiser(self):
        # Check a fundraiser without donations still shows up
        response = self.client.get(reverse('team_fundraising:index', args='2'))
        self.assertEqual(
            response.context['fundraisers'][1].name, 'Empty Fundraiser'
        )
        self.assertEqual(
            response.context['fundraisers'][1].total_raised, 00.00
        )
        self.assertEqual(
            response.context['fundraisers'][1].goal, 100.00
        )

class HomePageViewTests4(TransactionTestCase):
    fixtures = ["testdata.json"]
    def test_recent_donations(self):
        response = self.client.get(reverse('team_fundraising:index', args='1'))
        self.assertEqual(
            response.context['recent_donations'][0].amount, 50.00
        )


class DonationTest(TestCase):
    fixtures = ["testdata.json"]
    def test_new_donation(self):
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

class SignUpViewTests(TestCase):
    fixtures = ["testdata.json"]

    @patch('team_fundraising.views.send_mail')
    def test_signup_new_user_invalid(self, mock_send_mail):
        data = {
                "email": "test@test.com",
                "username": "testuser1",
                "password1": "somePASSw12@",
                "password2": "somePASSw12@",
                "campaign": 1,
                'name': "",
                'goal': 100, 
                'message': "test message",
                'signup_email_closing': "test close",
                'signup_email_subject': "test subject",
                'signup_email_opening': "test opening"
                }
        response = self.client.post(reverse('team_fundraising:signup', args='1'), data)
        messages = get_messages(response.wsgi_request)
        self.assertEqual(messages._loaded_data[0].message,
            "Something went wrong. Please try again."
                )
        self.assertEqual(response.status_code, 400)


   
    @patch('team_fundraising.views.send_mail')
    def test_signup_new_user_existing_campaign_new_fundraiser(self, mock_send_mail):
        data = {
                "email": "test@test.com",
                "username": "testuser1",
                "password1": "somePASSw12@",
                "password2": "somePASSw12@",
                "campaign": 1,
                'name': "test",
                'goal': 100, 
                'message': "test message",
                'signup_email_closing': "test close",
                'signup_email_subject': "test subject",
                'signup_email_opening': "test opening"
                }
        response = self.client.post(reverse('team_fundraising:signup', args='1'), data)
        messages = get_messages(response.wsgi_request)
        self.assertEqual(messages._queued_messages[0].message,
            Fundraiser_text.signup_return_message
                )
        self.assertEqual(response.status_code, 302)
        # test signed in user and existing fundraiser
        data = {
                "email": "test@test.com",
                "username": "testuser1",
                "campaign": 1,
                'name': "test2",
                'goal': 100, 
                'message': "test message",
                'signup_email_closing': "test close",
                'signup_email_subject': "test subject",
                'signup_email_opening': "test opening"
                }
        response = self.client.post(reverse('team_fundraising:signup', args='1'), data)
        messages = get_messages(response.wsgi_request)
        self.assertEqual(response.url,
                '/team_fundraising/accounts/update_fundraiser/'
                )
        self.assertEqual(response.status_code, 302)

        #signout
        response = self.client.get(reverse('team_fundraising:logout',)+'?next='+reverse('team_fundraising:index', args='1'))
        # sign in with wrong password
        data = {
                "email": "test@test.com",
                "username": "testuser1",
                "password1": "wrong",
                "password2": "wrong",
                "campaign": 1,
                'name': "test",
                'goal': 100, 
                'message': "test message",
                'signup_email_closing': "test close",
                'signup_email_subject': "test subject",
                'signup_email_opening': "test opening"
                }
        response = self.client.post(reverse('team_fundraising:signup', args='1'), data)
        messages = get_messages(response.wsgi_request)
        self.assertEqual(messages._loaded_messages[1].message,
            Fundraiser_text.signup_wrong_password_existing_user,
                )
        self.assertEqual(response.status_code, 400)
 

class FundraiserViewTests(TestCase):
    """ Check the information on the fundraiser page """
    fixtures = ["testdata.json"]

    def test_homepage_loads(self):
        # Just test the top of the homepage loads with the campaign name
        response = self.client.get(reverse('team_fundraising:index', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['campaign'].name, 'Fundraising Campaign')

    def test_homepage_totals(self):
        # Check the homepage displays total donations and raised
        response = self.client.get(reverse('team_fundraising:index', args='1'))
        self.assertEqual(response.context['total_raised'], 83.00)
        self.assertEqual(response.context['campaign'].goal, 1000.00)

    def test_homepage_fundraiser(self):
        # Check the first fundraiser has the right information
        response = self.client.get(reverse('team_fundraising:index', args='1'))
        self.assertEqual(
            response.context['fundraisers'][0].name, 'First Fundraiser'
        )
        self.assertEqual(
            response.context['fundraisers'][0].total_raised, 83.00
        )
        self.assertEqual(
            response.context['fundraisers'][0].goal, 200.00
        )

    def test_empty_homepage_fundraiser(self):
        # Check a fundraiser without donations still shows up
        response = self.client.get(reverse('team_fundraising:index', args='2'))
        self.assertEqual(
            response.context['fundraisers'][1].name, 'Empty Fundraiser'
        )
        self.assertEqual(
            response.context['fundraisers'][1].total_raised, 00.00
        )
        self.assertEqual(
            response.context['fundraisers'][1].goal, 100.00
        )

    def test_recent_donations(self):
        response = self.client.get(reverse('team_fundraising:index', args='1'))
        self.assertEqual(
            response.context['recent_donations'][0].amount, 50.00
        )


class DonationTest(TestCase):
    fixtures = ["testdata.json"]
    def test_new_donation(self):
        data = {
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

class FundraiserViewTests(TestCase):
    """ Check the information on the fundraiser page """
    fixtures = ["testdata.json"]

    def test_fundraiser(self):
        """ Check the information on the first fundraiser """
        response = self.client.get(
            reverse('team_fundraising:fundraiser', args='1')
        )
        self.assertEqual(
            response.context['fundraiser'].name, 'First Fundraiser'
        )
        self.assertEqual(
            response.context['fundraiser'].goal, 200.00
        )
        self.assertEqual(
            response.context['fundraiser'].total_raised, 83.00
        )
        self.assertEqual(
            response.context['fundraiser'].percent_raised, 83/200*100
        )

    def test_empty_fundraiser(self):
        """ Check the information on a fundraiser without donations """
        response = self.client.get(
            reverse('team_fundraising:fundraiser', args='2')
        )
        self.assertEqual(
            response.context['fundraiser'].name, 'Empty Fundraiser'
        )
        self.assertEqual(
            response.context['fundraiser'].goal, 100.00
        )
        self.assertEqual(
            response.context['fundraiser'].total_raised, 0.00
        )
        self.assertEqual(
            response.context['fundraiser'].percent_raised, 0.00
        )

    def test_fundraiser(self):
        """ Check the information on the first fundraiser """
        response = self.client.get(
            reverse('team_fundraising:fundraiser', args='1')
        )
        self.assertEqual(
            response.context['fundraiser'].name, 'First Fundraiser'
        )
        self.assertEqual(
            response.context['fundraiser'].goal, 200.00
        )
        self.assertEqual(
            response.context['fundraiser'].total_raised, 50.00
        )
        self.assertEqual(
            response.context['fundraiser'].percent_raised, 50/200*100
        )

    def test_empty_fundraiser(self):
        """ Check the information on a fundraiser without donations """
        response = self.client.get(
            reverse('team_fundraising:fundraiser', args='2')
        )
        self.assertEqual(
            response.context['fundraiser'].name, 'Empty Fundraiser'
        )
        self.assertEqual(
            response.context['fundraiser'].goal, 100.00
        )
        self.assertEqual(
            response.context['fundraiser'].total_raised, 0.00
        )
        self.assertEqual(
            response.context['fundraiser'].percent_raised, 0.00
        )
