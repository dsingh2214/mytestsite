from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
import requests
import os

API_KEY = os.environ.get('ELASTICEMAIL_API_KEY')


class ApiClient:
    apiUri = 'https://api.elasticemail.com/v2'
    apiKey = API_KEY

    def Request(method, url, data):
        data['apikey'] = ApiClient.apiKey
        if method == 'POST':
            result = requests.post(ApiClient.apiUri + url, data=data)
        elif method == 'PUT':
            result = requests.put(ApiClient.apiUri + url, data=data)
        elif method == 'GET':
            attach = ''
            for key in data:
                attach = attach + key + '=' + data[key] + '&'
            url = url + '?' + attach[:-1]
            result = requests.get(ApiClient.apiUri + url)

        jsonMy = result.json()

        if jsonMy['success'] is False:
            return jsonMy['error']

        return jsonMy['data']


def send_email(subject, from_id, fromName, to, bodyHtml, bodyText, isTransactional):
    return ApiClient.Request('POST', '/email/send', {
        'subject': subject,
        'from': from_id,
        'fromName': fromName,
        'to': to,
        'bodyHtml': bodyHtml,
        'bodyText': bodyText,
        'isTransactional': isTransactional})


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
            email = form.data['subject']
            body = '<br><br>'.join([subject, form.data['message'], name, phone, email])

            try:
                send_email("NEW INQUIRY [BBA]", "devang.ds.singh@gmail.com", "BBA",
                     "devang.ds.singh@gmail.com", f"<h1>{body}</h1>", "", True)
                messages.success(request, 'Thank you! Our customer support executive will get in touch shortly.')
            except:
                print("Exception when sending email")
                messages.success(request,
                                 'There seems to be some issue with form submission, please email us directly.')

    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})


