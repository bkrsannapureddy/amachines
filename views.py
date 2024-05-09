# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Import this decorator if CSRF protection is enabled
from .models import User

@csrf_exempt  # Use this decorator if CSRF protection is enabled and you want to exempt this view
def signup(request):
    if request.method == 'POST':
        data = request.json()  # Extract JSON data from the request body
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        # You should add validation and password hashing here
        user = User.objects.create(name=name, email=email, password=password)
        return JsonResponse({'message': 'User created successfully'})
    return JsonResponse({'error': 'Invalid request method'})
