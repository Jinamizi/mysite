from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('piano/', include('piano.urls')),
	path('actilist/', include('actilist.urls')),
	path('comments/', include('comments.urls')),
	path('examples/', include('examples.urls')),
	path('cities/', include('cities.urls')),
	path('swahili/', include('swahili.urls')),
	#path('news/', include('news.urls')),
	path('polls/', include('polls.urls')),
	path('post/', include('polls.urls')),
	path('myapp1/', include('myapp1.urls')),
    path('myblog/', include('myblog.urls')),
    path('bandcollections/', include('bandcollections.urls')),
    path('form/', include('form_eg.urls')),
    path('sentimentizer/', include('sentimentizer.urls')),
    #path('generic0/', include('generic0.urls')),
    path('admin/', admin.site.urls),
]
