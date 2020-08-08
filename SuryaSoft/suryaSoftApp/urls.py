from django.conf.urls import url
from . import views

urlpatterns=[
    url('^index/',views.index),
    url('^displayExpence/',views.displayExpence),
    url('^remove/',views.remove),
    # url('^addDescription/',views.addDescription),
    url('^edit/',views.edit)
]