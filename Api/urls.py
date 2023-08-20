from django.urls import path
from .views import register, login,logout_view
from .views import GlossaryRetrieveUpdateDeleteView, GlossaryListCreateView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('glossaries/', GlossaryListCreateView.as_view(), name='glossary-list-create'),
    path('glossary/<int:pk>/', GlossaryRetrieveUpdateDeleteView.as_view(), name='glossary-retrieve'),
]
