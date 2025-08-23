from flask import Blueprint, render_template, make_response, request
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/usługi-elektryczne')
def services():
    return render_template('services.html')

@main.route('/o-nas')
def about():
    return render_template('about.html')

@main.route('/kontakt')
def contact():
    return render_template('contact.html')

@main.route('/pogotowie-elektryczne-trójmiasto')
def emergency():
    return render_template('emergency.html')

@main.route('/pomiary-elektryczne')
def measurements():
    return render_template('measurements.html')

# SEO Routes
@main.route('/robots.txt')
def robots_txt():
    """Generate robots.txt file"""
    content = f"""User-agent: *
Allow: /

# Sitemaps
Sitemap: {request.url_root}sitemap.xml

# Crawl-delay
Crawl-delay: 1
"""
    response = make_response(content)
    response.headers['Content-Type'] = 'text/plain'
    return response

@main.route('/sitemap.xml')
def sitemap():
    """Generate sitemap.xml"""
    pages = [
        {'url': '/', 'changefreq': 'weekly', 'priority': '1.0'},
        {'url': '/usługi-elektryczne', 'changefreq': 'monthly', 'priority': '0.9'},
        {'url': '/o-nas', 'changefreq': 'monthly', 'priority': '0.8'},
        {'url': '/kontakt', 'changefreq': 'monthly', 'priority': '0.9'},
        {'url': '/pogotowie-elektryczne-trójmiasto', 'changefreq': 'monthly', 'priority': '0.9'},
        {'url': '/pomiary-elektryczne', 'changefreq': 'monthly', 'priority': '0.9'},
    ]

    current_date = datetime.now().strftime('%Y-%m-%d')

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">"""

    for page in pages:
        sitemap_xml += f"""
    <url>
        <loc>{request.url_root.rstrip('/')}{page['url']}</loc>
        <changefreq>{page['changefreq']}</changefreq>
        <priority>{page['priority']}</priority>
        <lastmod>{current_date}</lastmod>
    </url>"""

    sitemap_xml += """
</urlset>"""

    response = make_response(sitemap_xml)
    response.headers['Content-Type'] = 'application/xml'
    return response
