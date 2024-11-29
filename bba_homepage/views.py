from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

SENDER = "blueboatadvisor@gmail.com"


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
                send_mail("NEW INQUIRY [BBA - Contact Us]", body, SENDER, [SENDER])
                send_mail("BBA Support", user_email, SENDER, [email])

                messages.success(request, 'Thank you! Our customer support executive will get in touch shortly.')
            except:
                logger.info("Exception when sending email")
                messages.success(request,
                                 'There seems to be some issue with form submission, please email/call us directly.')

    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})


