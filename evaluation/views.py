from django.contrib.auth.models import User
from evaluation.models import Evaluation,QuestionEvaluation,UserEvaluation

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class TestInitial(TemplateView):
    template_name = "evaluation/test_initial.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = QuestionEvaluation.objects.all()
        list_questions = []
        for question in questions:
            alternatives = question.alternatives.split(";")
            list_questions.append({'title':question.title,
                                    'description':question.description,
                                    'alternatives':alternatives})
        context['questions'] = list_questions
        return context

class RegistrationSchool(TemplateView):
    template_name = "evaluation/registration.html"

class SendEvaluationAPI(APIView):
    def get(self,request,format=None):
        user_default = User.objects.filter(id=self.request['id_user'])
        pulses = []
        if user_default.exists():
            user_default = user_default.last()
            user_evaluation = UserEvaluation.objects.filter(user=user_default)
            for pulse in user_evaluation:
                pulses.append({'date':pulse.date,
                                'pulse':pulse.pulse})
        dict_response = {'status':True,
                        'pulses':pulses}
        return Response(dict_response)
    
    def post(self,request):
        """ Create new pulse in a user """
        pulse = request.data['pulse']
        user_default = User.objects.filter(id=1)
        if user_default.exists():
            user_default = user_default.last()
            data_pulse = (UserEvaluation.objects
                            .create(user_pulse=user_default,
                                    pulse=pulse))
            user_default.last_update = data_pulse.date
            user_default.last_pulse = pulse
            user_default.save()
            return Response({'status':True})
        return Response({'status':True})