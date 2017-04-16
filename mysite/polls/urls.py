
from django.conf.urls import url

from . import views

# The url() function is passed four arguments, two required: regex and view, 
# and two optional: kwargs, and name.
urlpatterns = [
		url(r'^$', views.index, name='index'),  # map index view to a urlconf
		]

