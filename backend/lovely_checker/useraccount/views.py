from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView, UpdateAPIView, \
    GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView

from useraccount.forms import LoginForm
from useraccount.models import BecomeOwnerQuestionnaire, UserProfile
from useraccount.serializers import AddNewQuestionnaireSerializer, \
    UserProfileSerializer


class AddNewQuestionnaire(CreateAPIView):
    queryset = BecomeOwnerQuestionnaire
    serializer_class = AddNewQuestionnaireSerializer


class UserProfileView(RetrieveAPIView):
    queryset = UserProfile
    serializer_class = UserProfileSerializer


class CurrentUserView(ListAPIView):
    serializer_class = UserProfileSerializer
    def get_queryset(self):
        print(self.request.user)
        if 'user_id' in self.request.session:
            print(self.request.session['user_id'])
            return UserProfile.objects.filter(user__id=self.request.session['user_id'])
        else:
            return []


class LoginView(APIView):
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
