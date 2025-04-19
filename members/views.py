from django.views.generic import ListView, FormView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Member
from .forms import MemberSignUpForm, MemberLoginForm

# Create your views here.
class MemberListView(ListView):
    model = Member
    template_name = 'members/member_list.html'
    context_object_name = 'members'
    #paginate_by = 10   #Number of members per page


class MemberSignUpView(FormView):
    template_name = 'members/signup.html'
    form_class = MemberSignUpForm
    success_url = reverse_lazy('home')  # Redirect to home page after successful signup
    redirect_authenticated_user = True  # Redirect authenticated users to home page

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    

class MemberLoginView(LoginView):
    template_name = 'members/login.html'
    authentication_form = MemberLoginForm
    success_url = reverse_lazy('home')  # Redirect to home page after successful login
    redirect_authenticated_user = True  # Redirect authenticated users to home page

class MemberLogoutView(LogoutView):
    template_name = 'members/logout.html'
    next_page = reverse_lazy('home')  # Redirect to home page after successful logout