"""
Komercia Layout Components
Navbar, Footer y estructura de página
"""
from fasthtml.common import *
from .ui import Button, Button_, Logo, Input, Checkbox


# ============================================================================
# NAVBAR
# ============================================================================

def Navbar(**kwargs):
    """
    Barra de navegación principal
    Con soporte móvil mediante Alpine.js
    """
    nav_links = [
        {"text": "POS", "href": "/pos"},
        {"text": "Servicios", "href": "#servicios"},
        {"text": "Precios", "href": "#precios"},
        {"text": "Nosotros", "href": "#nosotros"},
        {"text": "FAQ", "href": "#faq"},
    ]

    # Links de navegación
    nav_items = [
        A(link["text"], href=link["href"], cls="nav-link")
        for link in nav_links
    ]

    return Nav(
        Div(
            # Logo
            A(Logo(), href="/", cls="nav-logo-link"),

            # Nav links (desktop)
            Div(*nav_items, cls="nav-links"),

            # CTA buttons (desktop)
            Div(
                A("Iniciar sesión", href="#", cls="nav-login"),
                Button("Contactar", variant="primary", size="sm", href="#contacto"),
                cls="nav-cta"
            ),

            # Mobile menu button
            Button_(
                Span(cls="hamburger-line"),
                Span(cls="hamburger-line"),
                Span(cls="hamburger-line"),
                cls="nav-hamburger",
                x_on_click="mobileMenuOpen = !mobileMenuOpen",
                aria_label="Menú"
            ),

            cls="nav-container container"
        ),

        # Mobile menu
        Div(
            Div(
                *[A(link["text"], href=link["href"], cls="mobile-nav-link", x_on_click="mobileMenuOpen = false") for link in nav_links],
                Hr(cls="mobile-nav-divider"),
                A("Iniciar sesión", href="#", cls="mobile-nav-link"),
                Button("Contactar", variant="primary", full_width=True, href="#contacto"),
                cls="mobile-nav-content"
            ),
            cls="mobile-nav",
            x_show="mobileMenuOpen",
            x_transition_enter="mobile-nav-enter",
            x_transition_leave="mobile-nav-leave",
            x_on_click_away="mobileMenuOpen = false"
        ),

        cls="navbar",
        x_data="{ mobileMenuOpen: false }",
        x_bind_class="{ 'nav-scrolled': scrolled }",
        **kwargs
    )


# ============================================================================
# FOOTER
# ============================================================================

def Footer(**kwargs):
    """
    Footer con navegación, newsletter y redes sociales
    """
    # Links del footer
    footer_sections = [
        {
            "title": "Productos",
            "links": [
                {"text": "Komercia POS", "href": "/pos"},
                {"text": "Komercia Cloud", "href": "#servicios"},
                # {"text": "Komercia API", "href": "#servicios"},
                {"text": "Hardware", "href": "/pos#paquetes"},
            ]
        },
        {
            "title": "Empresa",
            "links": [
                {"text": "Nosotros", "href": "#nosotros"},
                {"text": "Precios", "href": "#precios"},
                {"text": "Blog", "href": "#"},
                {"text": "Trabaja con nosotros", "href": "#"},
            ]
        },
        {
            "title": "Soporte",
            "links": [
                {"text": "Centro de ayuda", "href": "#"},
                {"text": "Contacto", "href": "#contacto"},
                {"text": "FAQ", "href": "#faq"},
                {"text": "Estado del sistema", "href": "#"},
            ]
        },
        {
            "title": "Legal",
            "links": [
                {"text": "Términos de uso", "href": "#"},
                {"text": "Privacidad", "href": "#"},
                {"text": "Cookies", "href": "#"},
            ]
        },
    ]

    # Construir secciones de links
    link_sections = []
    for section in footer_sections:
        links = [A(link["text"], href=link["href"], cls="footer-link") for link in section["links"]]
        link_sections.append(
            Div(
                H4(section["title"], cls="footer-section-title"),
                Div(*links, cls="footer-links"),
                cls="footer-section"
            )
        )

    return ft_hx('footer',
        Div(
            # Top section
            Div(
                # Brand column
                Div(
                    Logo(variant="light"),
                    P(
                        "La gestión completa de tu minimarket. Hardware y software diseñados para simplificar tu negocio.",
                        cls="footer-brand-text"
                    ),
                    # Redes sociales
                    Div(
                        A(I(cls="icon icon-facebook"), href="#", cls="social-link", aria_label="Facebook"),
                        A(I(cls="icon icon-instagram"), href="#", cls="social-link", aria_label="Instagram"),
                        A(I(cls="icon icon-linkedin"), href="#", cls="social-link", aria_label="LinkedIn"),
                        A(I(cls="icon icon-youtube"), href="#", cls="social-link", aria_label="YouTube"),
                        cls="social-links"
                    ),
                    cls="footer-brand"
                ),

                # Link sections
                Div(*link_sections, cls="footer-nav"),

                cls="footer-top"
            ),

            # Newsletter section
            Div(
                Div(
                    H4("Mantente actualizado", cls="newsletter-title"),
                    P("Recibe consejos para gestionar mejor tu negocio.", cls="newsletter-text"),
                    cls="newsletter-info"
                ),
                Form(
                    Div(
                        ft_hx('input',
                            type="email",
                            name="email",
                            placeholder="tu@email.com",
                            required=True,
                            cls="newsletter-input"
                        ),
                        Button("Suscribirse", variant="accent", size="md"),
                        cls="newsletter-form-inner"
                    ),
                    cls="newsletter-form",
                    hx_post="/api/newsletter",
                    hx_swap="outerHTML"
                ),
                cls="footer-newsletter"
            ),

            # Bottom section
            Div(
                P(f"© 2025 Komercia. Todos los derechos reservados.", cls="footer-copyright"),
                Div(
                    Span("Hecho con ", cls="footer-made"),
                    Span("♥", cls="footer-heart"),
                    Span(" en Chile", cls="footer-made"),
                    cls="footer-made-with"
                ),
                cls="footer-bottom"
            ),

            cls="container"
        ),
        cls="footer",
        **kwargs
    )


# ============================================================================
# PAGE LAYOUT
# ============================================================================

def PageLayout(*content, title: str = "Komercia", description: str = None, **kwargs):
    """
    Layout base de página con head, navbar y footer
    """
    meta_description = description or "Komercia - La gestión completa de tu minimarket. POS, Software y Hardware para tu negocio."

    return Html(
        Head(
            # Meta básicos
            Title(title),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Meta(name="description", content=meta_description),

            # SEO
            Meta(name="robots", content="index, follow"),
            Meta(name="author", content="Komercia"),
            Meta(name="keywords", content="minimarket, POS, ERP, software, gestión, inventario, ventas, Chile"),

            # Open Graph
            Meta(property="og:title", content=title),
            Meta(property="og:description", content=meta_description),
            Meta(property="og:type", content="website"),
            Meta(property="og:locale", content="es_CL"),

            # Fonts - Plus Jakarta Sans y DM Sans
            Link(rel="preconnect", href="https://fonts.googleapis.com"),
            Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
            Link(
                rel="stylesheet",
                href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=DM+Sans:wght@400;500;600&display=swap"
            ),

            # Styles
            Link(rel="stylesheet", href="/static/css/styles.css"),

            # Alpine.js
            Script(src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js", defer=True),

            # Favicon (placeholder)
            Link(rel="icon", href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏪</text></svg>"),
        ),
        Body(
            # Scroll tracking
            Div(
                Navbar(),
                Main(*content, cls="main-content"),
                Footer(),
                cls="page-wrapper",
                x_data="{ scrolled: false }",
                x_init="window.addEventListener('scroll', () => { scrolled = window.scrollY > 50 })"
            ),
            # Chat widget placeholder
            Div(
                Button_(
                    I(cls="icon icon-message-circle"),
                    cls="chat-widget-btn",
                    aria_label="Abrir chat"
                ),
                cls="chat-widget"
            )
        ),
        lang="es"
    )


# ============================================================================
# HEADER ALTERNATIVO (para páginas internas)
# ============================================================================

def POSPageLayout(*content, title: str = "Komercia POS", description: str = None, **kwargs):
    """
    Layout para la página de Komercia POS con estilos específicos
    """
    meta_description = description or "Komercia POS - Hardware y software diseñados para tu minimarket. Terminal de punto de venta con sincronización cloud."

    return Html(
        Head(
            # Meta básicos
            Title(title),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Meta(name="description", content=meta_description),

            # SEO
            Meta(name="robots", content="index, follow"),
            Meta(name="author", content="Komercia"),
            Meta(name="keywords", content="POS, terminal punto de venta, minimarket, hardware, software, inventario, Chile"),

            # Open Graph
            Meta(property="og:title", content=title),
            Meta(property="og:description", content=meta_description),
            Meta(property="og:type", content="website"),
            Meta(property="og:locale", content="es_CL"),

            # Fonts - Plus Jakarta Sans y DM Sans
            Link(rel="preconnect", href="https://fonts.googleapis.com"),
            Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
            Link(
                rel="stylesheet",
                href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=DM+Sans:wght@400;500;600&display=swap"
            ),

            # Styles - Base + POS específicos
            Link(rel="stylesheet", href="/static/css/styles.css"),
            Link(rel="stylesheet", href="/static/css/pos-styles.css"),

            # Alpine.js
            Script(src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js", defer=True),

            # Favicon
            Link(rel="icon", href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏪</text></svg>"),
        ),
        Body(
            # Scroll tracking
            Div(
                POSNavbar(),
                Main(*content, cls="main-content"),
                Footer(),
                cls="page-wrapper",
                x_data="{ scrolled: false }",
                x_init="window.addEventListener('scroll', () => { scrolled = window.scrollY > 50 })"
            ),
            # Chat widget placeholder
            Div(
                Button_(
                    I(cls="icon icon-message-circle"),
                    cls="chat-widget-btn",
                    aria_label="Abrir chat"
                ),
                cls="chat-widget"
            )
        ),
        lang="es"
    )


def POSNavbar(**kwargs):
    """
    Barra de navegación para la página POS
    """
    nav_links = [
        {"text": "Características", "href": "#caracteristicas"},
        {"text": "Paquetes", "href": "#paquetes"},
        {"text": "Sincronización", "href": "#sync"},
        {"text": "Soporte", "href": "#soporte"},
    ]

    # Links de navegación
    nav_items = [
        A(link["text"], href=link["href"], cls="nav-link")
        for link in nav_links
    ]

    return Nav(
        Div(
            # Logo
            A(Logo(), href="/", cls="nav-logo-link"),

            # Nav links (desktop)
            Div(*nav_items, cls="nav-links"),

            # CTA buttons (desktop)
            Div(
                A("Ver Cloud", href="/cloud", cls="nav-login"),
                Button("Cotizar", variant="primary", size="sm", href="#paquetes"),
                cls="nav-cta"
            ),

            # Mobile menu button
            Button_(
                Span(cls="hamburger-line"),
                Span(cls="hamburger-line"),
                Span(cls="hamburger-line"),
                cls="nav-hamburger",
                x_on_click="mobileMenuOpen = !mobileMenuOpen",
                aria_label="Menú"
            ),

            cls="nav-container container"
        ),

        # Mobile menu
        Div(
            Div(
                *[A(link["text"], href=link["href"], cls="mobile-nav-link", x_on_click="mobileMenuOpen = false") for link in nav_links],
                Hr(cls="mobile-nav-divider"),
                A("Ver Cloud", href="/cloud", cls="mobile-nav-link"),
                Button("Cotizar", variant="primary", full_width=True, href="#paquetes"),
                cls="mobile-nav-content"
            ),
            cls="mobile-nav",
            x_show="mobileMenuOpen",
            x_transition_enter="mobile-nav-enter",
            x_transition_leave="mobile-nav-leave",
            x_on_click_away="mobileMenuOpen = false"
        ),

        cls="navbar",
        x_data="{ mobileMenuOpen: false }",
        x_bind_class="{ 'nav-scrolled': scrolled }",
        **kwargs
    )


# ============================================================================
# HEADER ALTERNATIVO (para páginas internas)
# ============================================================================

def PageHeader(title: str, subtitle: str = None, breadcrumbs: list = None, **kwargs):
    """Header para páginas internas"""
    content = []

    if breadcrumbs:
        crumb_items = []
        for i, crumb in enumerate(breadcrumbs):
            if i > 0:
                crumb_items.append(Span("/", cls="breadcrumb-separator"))
            if crumb.get("href"):
                crumb_items.append(A(crumb["text"], href=crumb["href"], cls="breadcrumb-link"))
            else:
                crumb_items.append(Span(crumb["text"], cls="breadcrumb-current"))
        content.append(Nav(*crumb_items, cls="breadcrumbs", aria_label="Breadcrumb"))

    content.append(H1(title, cls="page-header-title"))

    if subtitle:
        content.append(P(subtitle, cls="page-header-subtitle"))

    return Div(
        Div(*content, cls="container"),
        cls="page-header",
        **kwargs
    )
