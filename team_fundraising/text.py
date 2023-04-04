
class Donation_text:

    # Shown as a message across the top of the page on return from a donation
    # used in views.py:new_donation()
    thank_you = (
        "Thank you for your donation. "
        "You may need to refresh this page to see the donation."
    )

    confirmation_email_subject = (
        'Thank you for donating! '
    )

    # Start of the email sent confirming the paypal payment has gone through
    # used in paypal.py:process_paypal()
    confirmation_email_opening = (
        'Thank you for your generous donation of '
    )

    # Closing of the email sent confirming the paypal payment has gone through
    # used in paypal.py:process_paypal() - text only
    confirmation_email_closing_text = (
        "\nYour PayPal receipt should arrive in a separate email.\n"
    )

    # Closing of the email sent confirming the paypal payment has gone through
    # used in paypal.py:process_paypal() - with html link
    confirmation_email_closing_html = (
        "Your PayPal receipt should arrive in a separate email.\n"
    )

    notification_email_subject = (
        "You got a donation!"
    )

    notification_email_opening = (
        "Great news! You've just received a donation of "
    )

    notification_email_closing = (
        "\n\nAwesome work! They would probably appreciate "
        "a quick thank you email.\n\n"
    )


class Fundraiser_text:

    # Subject of the email sent on signup
    signup_email_subject = (
        "Welcome to fundraising!"
    )

    # Start of the email sent when someone signs up
    # used in views.py:signup()
    signup_email_opening = (
        "Thanks for signing up to fundraise with us!\n"
        "Your fundraising page can be found at:\n"
    )

    # Closing of the email sent when someone signs up
    # used in views.py:signup()
    signup_email_closing = (
        '\n\nYou can change your information by using the "Login" link at the '
        'top of that page.'
        '\n\nThe easiest way to start fundraising is to post the above link '
        'on social media or write a short email to your friends telling them '
        'about your ride.'
        '\nDon\'t forget to include the link to your page!\n'
    )

    # Message show at the top of the fundraiser page after signing up
    # used in views.py:signup()
    signup_return_message = (
        "Thank you for signing up."
    )

    signup_wrong_password_existing_user = (
        "The username already exists, but the password entered is incorrect. "
        "If you were already a fundraiser for a previous campaign, please "
        "enter your previous password or use "
        "<a href='/team_fundraising/accounts/password_reset/'>"
        "Forgot your password</a>. If this is your first campaign, "
        "please choose a different username."
    )
