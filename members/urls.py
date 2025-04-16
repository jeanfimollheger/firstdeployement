from django.urls import path
from .views import MemberListView, MemberSignUpView#, MemberDetailView


urlpatterns = [
    path('member_list', MemberListView.as_view(), name='member_list'),
    path('signup/', MemberSignUpView.as_view(), name='signup'),
    #path('<slug:slug>/', MemberDetailView.as_view(), name='member_detail'),  
]