from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
import smtplib
import os


SENDER = "blueboatadvisor@gmail.com"
PASSCODE = os.getenv("GMAIL_PASSCODE")


def send_email(to_addrs, msg, subject):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(SENDER, PASSCODE)
    message = 'Subject: {}\n\n{}'.format(subject, msg)
    server.sendmail(SENDER, to_addrs, message)


def render_homepage(request):
    return render(request, 'homepage.html')


def render_about_us(request):
    return render(request, 'about_us.html')


def render_services(request):
    return render(request, 'services.html')


def render_under_construction(request):
    return render(request, 'under_construction.html')


def render_contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.data['name']
            phone = form.data['phone']
            subject = form.data['subject']
            email = form.data['email']
            body = '\n\n'.join([
                "NAME\n" + name,
                "PHONE\n" + phone,
                "EMAIL\n" + email,
                "SUB\n" + subject,
                "MESSAGE\n " + form.data['message'],
                ])

            user_email = f"Hi {name},\n\nThank you for reaching out, we have received your message. Our support executive will get in touch shortly.\n\nRegards,\nBlueBoat Advisors"

            try:
                send_email(SENDER, body, "NEW INQUIRY [BBA - Contact Us]")
                send_email(email, user_email, 'BBA Support')
                messages.success(request, 'Thank you! Our customer support executive will get in touch shortly.')
            except:
                print("Exception when sending email")
                messages.success(request,
                                 'There seems to be some issue with form submission, please email us directly.')

    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})


