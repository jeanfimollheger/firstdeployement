from django.urls import path
from .views import MemberListView, MemberSignUpView, MemberLoginView, MemberLogoutView#, MemberDetailView


urlpatterns = [
    path('member_list', MemberListView.as_view(), name='member_list'),
    path('signup/', MemberSignUpView.as_view(), name='signup'),
    path('login/', MemberLoginView.as_view(), name='login'),
    path('logout/', MemberLogoutView.as_view(), name='logout'),
    #path('<slug:slug>/', MemberDetailView.as_view(), name='member_detail'),  
]