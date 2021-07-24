from django.urls import path
from task.views import Encrypdataview
from task.views import Decrypdataview


urlpatterns = [
    path('endata/', Encrypdataview),
    path('dedata/', Decrypdataview),

]
