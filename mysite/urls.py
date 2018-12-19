from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

# Use static() to add url mapping to serve static files during development (only)
urlpatterns = [
	path('', lambda r: HttpResponseRedirect('si664finalproject/')),
	path('admin/', admin.site.urls),
	path('auth/', include('social_django.urls', namespace='social')),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},
		 name='logout'),
	path('si664finalproject/', include('si664finalproject.urls')),
	path('si664finalproject/api/rest-auth/', include('rest_auth.urls')),
	path('api-auth/', include('rest_framework.urls')),
	path('si664finalproject/api/', include('api.urls')),
	path('si664finalproject/api/rest-auth/registration/', include('rest_auth.registration.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
