from django.contrib import admin
from .models import Record

admin.site.register(Record)

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

@user_passes_test(lambda u: u.is_superuser)
def invite_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Validate the email address
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'tasks/invite_user.html', {'error': 'Invalid email address.'})

        # Generate the signup link dynamically
        signup_url = request.build_absolute_uri(reverse('signup'))  # Replace 'signup' with your signup view's name
        
        # Send the email
        try:
            send_mail(
                subject='You are invited to Task Manager',
                message=f'Hello,\n\nYou have been invited to Task Manager. Click the link below to register:\n\n{signup_url}\n\nBest regards,\nTask Manager Team',
                from_email='your-email@gmail.com',
                recipient_list=[email],
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        # Redirect to admin panel after sending the email
        return redirect('/admin/')
    
    return render(request, 'tasks/invite_user.html')
