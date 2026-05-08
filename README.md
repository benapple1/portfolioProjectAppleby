# AI Portfolio Website

A professional Django portfolio website for a final AI class project. The site presents AI course projects in an interview-ready format with business problems, tools, key features, personal contribution, challenges, and lessons learned.

## Features

- Home, About, Projects, Project Detail, Skills, Resume, Contact pages
- Django authentication with login/logout
- Protected Resume page using `LoginRequiredMixin`
- `Project` model with the required portfolio fields
- Bootstrap styling with reusable `base.html`
- Seed data for six required class projects
- Ready for GitHub and Render deployment

## Projects Included

- n8n Agent Workflow Project
- LangChain Agent Project
- Google AI Studio Media Project
- Machine Learning Project using scikit-learn
- Campus SkillSwap Django Project

## Local Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_projects
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Render Deployment

1. Push the project to GitHub.
2. Create a new Render Web Service from the repository.
3. Use this build command:

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate && python manage.py seed_projects
```

4. Use this start command:

```bash
gunicorn portfolio_project.wsgi:application
```

5. Add environment variables:

```bash
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=your-render-service.onrender.com,.onrender.com
```

## Customization Checklist

- Replace placeholder contact details in `templates/portfolio/contact.html`
- Update GitHub and demo links in `portfolio/management/commands/seed_projects.py`
- Add project screenshots through the Django admin if desired
- Expand `templates/portfolio/resume.html` with your final resume content
