# Jovian Careers Website

A Django-based careers/job listings website for Jovian.ai — an EdTech platform. Allows visitors to browse open positions, view job details, and submit applications.

## Tech Stack

- **Language:** Python 3.11
- **Framework:** Django 5.2
- **Database:** SQLite (db.sqlite3)
- **Static Files:** WhiteNoise
- **Server:** Django dev server (dev) / Gunicorn (production)

## Project Structure

```
jovian_careers/     # Django project config (settings, urls, wsgi)
careers/            # Main app
  models.py         # JobListing, JobApplication models
  views.py          # List, detail, apply, success views
  urls.py           # careers/ URL routes
  forms.py          # JobApplicationForm
  admin.py          # Django admin registrations
  fixtures/         # sample_jobs.json - sample data
  migrations/       # Database migrations
templates/
  base.html         # Base layout with navbar/footer
  careers/          # App-specific templates
start.sh            # Startup script (migrate + runserver)
```

## Running Locally

```bash
bash start.sh
```

Runs at: http://0.0.0.0:5000

## Admin

Django admin is at `/admin/`. Create a superuser with:
```bash
python3 manage.py createsuperuser
```

## Key Features

- Job listing page with filters (department, work type, employment type)
- Job detail page with full description & requirements
- Application form with cover letter, resume link, LinkedIn/portfolio
- Application success confirmation page
- Django admin for managing jobs and applications

## Deployment

Configured for Gunicorn autoscale deployment:
```
gunicorn --bind=0.0.0.0:5000 --reuse-port jovian_careers.wsgi:application
```
