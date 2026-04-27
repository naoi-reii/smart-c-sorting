# SmartC Calamansi Dashboard

## Project Overview
This project is a web application providing a dashboard and settings interface for a system named "SmartC Calamansi", which appears to be a real-time tracking, diagnostics, and sorting interface. It is built to display processing metrics, yield distributions, weight trends, and activity logs.

## Technology Stack
- **Backend Framework:** Django 6.0.4 (Python 3)
- **Database:** SQLite (`db.sqlite3`)
- **Frontend Styling:** Tailwind CSS (via CDN for rapid development/prototyping).
- **Frontend Interactivity:** HTMX (included via CDN).
- **Charting:** ApexCharts (included via CDN).
- **Typography/Fonts:** DM Sans (Google Fonts).

## Project Structure
- **`app/`**: The primary Django application containing models, views, urls, and static assets.
  - **`templates/app/`**: Contains the HTML templates (`base.html`, `dashboard.html`, `logs.html`, `login.html`, `settings.html`).
  - **`static/app/`**: Contains static assets like images and SVGs.
- **`project/`**: The core Django project configuration folder (settings, main urls, wsgi/asgi).
- **`design-guide.md`**: A critical file outlining the design system, typography, colors, layout components, and UI patterns for the application.

## Development Conventions & Instructions

### 1. UI and Styling
- **Strictly adhere to the `design-guide.md`**. It acts as the single source of truth for UI modifications.
- **Tailwind CSS Utility Classes:** Use Tailwind for styling.
- **Dark/Light Mode:** The application fully supports both themes. Always include corresponding `dark:` prefixes for colors and backgrounds (e.g., `bg-white dark:bg-dark-card`, `text-gray-900 dark:text-white`). Theme configurations are handled globally in `base.html` within a `<script>` tag customizing Tailwind.
- **Component Consistency:** Reuse existing card structures, button styles (e.g., uppercase tracking-widest for actions), and font-size utilities (`text-ui-tiny`, `text-ui-base`, `text-ui-header`, etc.) defined in the Tailwind config script.

### 2. Django Conventions
- **Routing:** App-specific routes are managed in `app/urls.py` and included in the main `project/urls.py`.
- **Views:** Views should be mapped carefully, and restricted pages should utilize the `@login_required` decorator.
- **Templates:** Use Django template inheritance. Pages should extend `app/base.html` and populate the `{% block content %}`.

### 3. Building and Running
The project is a standard Django application managed via `manage.py`.
- **Run the development server:** `python manage.py runserver`
- **Make migrations:** `python manage.py makemigrations`
- **Migrate the database:** `python manage.py migrate`
- **Create a superuser:** `python manage.py createsuperuser`

*Note: As this project appears to be in its early or frontend-focused phases, `app/models.py` may be sparse or empty. Ensure any future data handling aligns with standard Django ORM practices.*