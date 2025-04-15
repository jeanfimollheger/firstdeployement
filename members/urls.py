from django.urls import path
from .views import MemberListView#, MemberDetailView


urlpatterns = [
    path('', MemberListView.as_view(), name='member_list'),
    #path('<slug:slug>/', MemberDetailView.as_view(), name='member_detail'),  
]