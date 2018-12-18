from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.HomePageView.as_view(), name='home'),
	path('about/', views.AboutPageView.as_view(), name='about'),
	path('cities/', views.CityListView.as_view(), name='cities'),
	path('cities/<int:pk>/', views.CityDetailView.as_view(), name='city_detail'),
	path('hospitals/', views.HospitalListView.as_view(), name='hospitals'),
	path('filters/', views.HospitalFilterView.as_view(), name='filters'),
	path('hospitals/<int:pk>/', views.HospitalDetailView.as_view(), name='hospital_detail'),
	path('hospitals/new/', views.HospitalCreateView.as_view(), name='hospital_new'),
	path('hospitals/<int:pk>/delete/', views.HospitalDeleteView.as_view(), name='hospital_delete'),
	path('hospitals/<int:pk>/update/', views.HospitalUpdateView.as_view(), name='hospital_update'),

]
