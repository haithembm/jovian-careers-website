from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import JobListing, JobApplication
from .forms import JobApplicationForm


def job_list(request):
    department = request.GET.get('department', '')
    location_type = request.GET.get('location_type', '')
    employment_type = request.GET.get('employment_type', '')

    jobs = JobListing.objects.filter(is_active=True)

    if department:
        jobs = jobs.filter(department__icontains=department)
    if location_type:
        jobs = jobs.filter(location_type=location_type)
    if employment_type:
        jobs = jobs.filter(employment_type=employment_type)

    departments = JobListing.objects.filter(is_active=True).values_list('department', flat=True).distinct()

    context = {
        'jobs': jobs,
        'departments': departments,
        'selected_department': department,
        'selected_location_type': location_type,
        'selected_employment_type': employment_type,
        'location_type_choices': JobListing.LOCATION_TYPE_CHOICES,
        'employment_type_choices': JobListing.EMPLOYMENT_TYPE_CHOICES,
    }
    return render(request, 'careers/job_list.html', context)


def job_detail(request, pk):
    job = get_object_or_404(JobListing, pk=pk, is_active=True)
    context = {'job': job}
    return render(request, 'careers/job_detail.html', context)


def job_apply(request, pk):
    job = get_object_or_404(JobListing, pk=pk, is_active=True)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('careers:apply_success', pk=application.pk)
    else:
        form = JobApplicationForm()

    context = {'job': job, 'form': form}
    return render(request, 'careers/job_apply.html', context)


def apply_success(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    context = {'application': application}
    return render(request, 'careers/apply_success.html', context)
