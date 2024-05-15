import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Import this decorator if CSRF protection is enabled
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import User,Exam,QuestionBank, Subject, Question


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



@login_required
def dashboard(request):
  user = request.user
  exams = Exam.objects.filter(user=user).values('id', 'date', 'name', 'questions_attempted')
  return JsonResponse(list(exams), safe=False)

@csrf_exempt
@login_required
def create_question_bank(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    name = data.get('name')
    subject_id = data.get('subject')
    subject = Subject.objects.get(id=subject_id)
    question_bank = QuestionBank.objects.create(name=name, subject=subject)
    return JsonResponse({'status': 'success', 'question_bank_id': question_bank.id})
  return JsonResponse({'status': 'failed'}, status=400)

@csrf_exempt
@login_required
def create_question(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    question_bank_id = data.get('question_bank_id')
    question_bank = QuestionBank.objects.get(id=question_bank_id)
    questions = data.get('questions')

    for q in questions:
      Question.objects.create(
        topic=q['topic'],
        subject=question_bank.subject,
        level=q['level'],
        type=q['type'],
        mode=q['mode'],
        question_bank=question_bank
      )
    return JsonResponse({'status': 'success'})
  return JsonResponse({'status': 'failed'}, status=400)

class SubjectListView(ListView):
  model = Subject
  template_name = 'subjects_list.html'  # You can use any template name; it's not used for API views
  context_object_name = 'subjects'

  def render_to_response(self, context, **response_kwargs):
    subjects = list(context['subjects'].values())
    return JsonResponse(subjects, safe=False)