from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Member

# Create your views here.
class MemberListView(ListView):
    model = Member
    template_name = 'members/member_list.html'
    context_object_name = 'members'
    #paginate_by = 10   #Number of members per page

