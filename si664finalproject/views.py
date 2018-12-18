from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Hospital
from .models import City

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .forms import si664finalprojectForm
from django.urls import reverse_lazy

from django_filters.views import FilterView


from .filters import si664finalprojectFilter



def index(request):
	return HttpResponse("Hello, world. You're at the Hospital Payment and Value of Care index page.")


class AboutPageView(generic.TemplateView):
	template_name = 'si664finalproject/about.html'


class HomePageView(generic.TemplateView):
	template_name = 'si664finalproject/home.html'


class HospitalListView(generic.ListView):
	model = Hospital
	context_object_name = 'hospitals'
	template_name = 'si664finalproject/hospital.html'
	paginate_by = 50

	def get_queryset(self):
		return Hospital.objects.all().select_related('state', 'county', 'city', 'zip_code').order_by('hospital_name')

class HospitalDetailView(generic.DetailView):
	model = Hospital
	context_object_name = 'hospital'
	template_name = 'si664finalproject/hospital_detail.html'

@method_decorator(login_required, name='dispatch')
class CityListView(generic.ListView):
	model = City
	context_object_name = 'cities'
	template_name = 'si664finalproject/city.html'
	paginate_by = 20

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		return City.objects.all().select_related('hospital', 'state').order_by('city')

@method_decorator(login_required, name='dispatch')
class CityDetailView(generic.DetailView):
	model = City
	context_object_name = 'city'
	template_name = 'si664finalproject/city_detail.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

@method_decorator(login_required, name='dispatch')
class HospitalCreateView(generic.View):
	model = Hospital
	form_class = si664finalprojectForm
	success_message = "Hospital created successfully"
	template_name = 'si664finalproject/hospital_new.html'
	# fields = '__all__' <-- superseded by form_class
	# success_url = reverse_lazy('heritagesites/site_list')

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def post(self, request):
		form = si664finalprojectForm(request.POST)
		if form.is_valid():
			site = form.save(commit=False)
			site.save()
			for hospital in form.cleaned_data['city']:
				Hospital.objects.create(hospital=hospital, city=city)
			return redirect(site) # shortcut to object's get_absolute_url()
			# return HttpResponseRedirect(site.get_absolute_url())
		return render(request, 'si664finalproject/hospital_new.html', {'form': form})

	def get(self, request):
		form = si664finalprojectForm()
		return render(request, 'si664finalproject/hospital_new.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class HospitalUpdateView(generic.UpdateView):
	model = Hospital
	form_class = si664finalprojectForm
	# fields = '__all__' <-- superseded by form_class
	context_object_name = 'hospital'
	# pk_url_kwarg = 'site_pk'
	success_message = "Hospital updated successfully"
	template_name = 'si664finalproject/hospital_update.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		hospital = form.save(commit=False)
		# site.updated_by = self.request.user
		# site.date_updated = timezone.now()
		hospital.save()

		old_ids = Hospital.objects\
			.values_list('hospital_id', flat=True)\
			.filter(hospital_id=hospital.hospital_id)

		# New countries list
		new_hospitals = form.cleaned_data['hospital_name']

		# TODO can these loops be refactored?

		# New ids
		new_ids = []

		# Insert new unmatched country entries
		for hospital in new_hospitals:
			new_id = hospital.hospital_id
			new_ids.append(new_id)
			if new_id in old_ids:
				continue
			else:
				Hospital.objects \
					.create(hospital = hospital, city=city)

		# Delete old unmatched country entries
		for old_id in old_ids:
			if old_id in new_ids:
				continue
			else:
				Hospital.objects \
					.filter(hospital_id=hospital.hospital_id) \
					.delete()

		return HttpResponseRedirect(hospital.get_absolute_url())

@method_decorator(login_required, name='dispatch')
class HospitalDeleteView(generic.DeleteView):
	model = Hospital
	success_message = "Hospital deleted successfully"
	success_url = reverse_lazy('hospitals')
	context_object_name = 'hospital'
	template_name = 'si664finalproject/hospital_delete.html'

	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()

		# Delete HeritageSiteJurisdiction entries
		Hospital.objects \
			.filter(hospital_id=self.object.hospital_id) \
			.delete()

		self.object.delete()

		return HttpResponseRedirect(self.get_success_url())

class HospitalFilterView(FilterView):
	filterset_class = si664finalprojectFilter
	template_name = 'si664finalproject/hospital_filter.html'
