


from django import urls

from . import views
urlpatterns = [
    urls.path('all',views.getAll),
    urls.path('class',views.getByClass),
    urls.path('add',views.addStudent)
]
