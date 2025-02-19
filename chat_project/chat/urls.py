from django.urls import path
from .views import chat_view, ts_view  # Import ts_view directly

urlpatterns = [
    path('', chat_view, name='chat'),
    path('ts/', ts_view, name='chat_ts'),  # No need for views.ts_view
]