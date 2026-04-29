# Lalawmpuia Ralte — Creative Portfolio (Django + HTML/CSS + SQLite)

A dark, cinematic videographer/video-editor portfolio built with **pure Django, HTML, CSS, and vanilla JavaScript**, backed by **SQLite**. Fully responsive (mobile + desktop) with rich load animations.

## Features
- Hero with overlapping image collage, serif display typography, and animated entrance
- Content index, About, Gallery (dynamic from DB), Experience, Contact
- Contact form saving to SQLite via Django
- Django admin to manage gallery items, experience, and view contact messages
- Pure HTML/CSS — **no React, no frameworks**
- Vanilla JS for scroll/load animations and parallax

## Quick Start

```bash
# 1. Create & activate virtualenv
python -m venv venv
source venv/bin/activate          # macOS/Linux
venv\Scripts\activate             # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Migrate database (creates db.sqlite3)
python manage.py migrate

# 4. Seed sample data (optional but recommended)
python manage.py seed_portfolio

# 5. Create admin user
python manage.py createsuperuser

# 6. Run dev server
python manage.py runserver
```

Visit:
- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Project Structure
```
lalawmpuia_portfolio/
├── manage.py
├── requirements.txt
├── lalawmpuia_portfolio/   # Django project (settings, urls)
├── portfolio/              # Main app (models, views, forms, admin)
│   └── management/commands/seed_portfolio.py
├── templates/              # HTML templates
│   └── portfolio/
├── static/                 # CSS, JS, images
└── media/                  # User-uploaded media
```

## Customizing
- Edit `portfolio/management/commands/seed_portfolio.py` to change seed content
- Edit `static/css/style.css` for visual tweaks
- Add gallery items / experience via Django admin

Enjoy 🎬
