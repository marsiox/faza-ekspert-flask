from flask import render_template, make_response
from app.routes import main

@main.route('/robots.txt')
def robots_txt():
    """Generate robots.txt file"""
    content = """User-agent: *
Allow: /

# Sitemaps
Sitemap: {{ request.url_root }}sitemap.xml

# Crawl-delay (optional)
Crawl-delay: 1

# Disallow admin areas (if any)
# Disallow: /admin/
"""
    response = make_response(content)
    response.headers['Content-Type'] = 'text/plain'
    return response

@main.route('/sitemap.xml')
def sitemap():
    """Generate sitemap.xml"""
    pages = [
        {'url': '/', 'changefreq': 'weekly', 'priority': '1.0'},
        {'url': '/uslugi-elektryczne', 'changefreq': 'monthly', 'priority': '0.9'},
        {'url': '/o-nas', 'changefreq': 'monthly', 'priority': '0.8'},
        {'url': '/kontakt', 'changefreq': 'monthly', 'priority': '0.9'},
        {'url': '/wycena', 'changefreq': 'monthly', 'priority': '0.8'},
        {'url': '/pogotowie-elektryczne-trojmiasto', 'changefreq': 'monthly', 'priority': '0.9'},
        {'url': '/pomiary-elektryczne', 'changefreq': 'monthly', 'priority': '0.9'},
    ]

    sitemap_xml = render_template('sitemap.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers['Content-Type'] = 'application/xml'
    return response
