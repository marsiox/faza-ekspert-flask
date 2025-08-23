# Faza-Ekspert - Flask Website

A modern Flask web application recreating the Faza-Ekspert electrical services website using Tailwind CSS.

## Features

- **Modern Design**: Clean, responsive design using Tailwind CSS
- **Multi-page Structure**: Complete website with all main pages
- **Mobile Responsive**: Fully responsive design for all devices
- **SEO Friendly**: Proper meta tags and semantic HTML structure
- **Contact Forms**: Interactive contact and quote request forms
- **Professional Layout**: Modern electric services company website

## Pages Included

- **Homepage** (`/`) - Main landing page with hero section, services overview, testimonials
- **Services** (`/uslugi-elektryczne`) - Detailed services page
- **About Us** (`/o-nas`) - Company history and mission
- **Contact** (`/kontakt`) - Contact information and form
- **Quote** (`/wycena`) - Online quote calculator
- **Emergency Services** (`/pogotowie-elektryczne-trojmiasto`) - 24/7 emergency electrical services
- **Electrical Measurements** (`/pomiary-elektryczne`) - Professional electrical measurements

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Icons**: Font Awesome
- **Responsive Design**: Mobile-first approach

## Installation

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:

   ```bash
   python run.py
   ```

3. Open your browser and visit `http://localhost:5000`

## Project Structure

```
faza/
├── app/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── services.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   ├── quote.html
│   │   ├── emergency.html
│   │   └── measurements.html
│   ├── __init__.py
│   └── routes.py
├── requirements.txt
├── run.py
└── README.md
```

## Original Website

This Flask application is a recreation of the original website: https://faza-ekspert.pl/

The original was built with Django and Bootstrap. This version uses Flask and Tailwind CSS for a more modern approach.

## Company Information

**Faza-Ekspert sp. z o.o.**

- Address: ul. Racławicka 9/5, 80-280 Gdańsk
- Phone: 664 883 028
- Email: elektryk@faza-ekspert.pl
- NIP: 796-302-88-52

### Services Offered:

- Electrical installations
- Electrical measurements (periodic and acceptance)
- Emergency electrical services (24/7)
- IT services and network cabling
- Smart Home systems
- Server rack installation

### Service Areas:

- Gdańsk and surroundings
- Gdynia and surroundings
- Sopot and surroundings
- Other locations in Pomeranian Voivodeship

## Development

To extend or modify the application:

1. **Add new routes** in `app/routes.py`
2. **Create templates** in `app/templates/`
3. **Add static assets** in `app/static/`
4. **Modify styling** using Tailwind CSS classes
5. **Add JavaScript** for enhanced interactivity

## Deployment

For production deployment:

1. Set environment variables
2. Configure production WSGI server (e.g., Gunicorn)
3. Set up reverse proxy (e.g., Nginx)
4. Configure SSL certificates
5. Set up database if needed for forms

## License

This project recreates the design and content of the original Faza-Ekspert website for demonstration purposes.
