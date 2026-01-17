"""
Komercia Landing Page Sections
Todas las secciones de la landing page
"""
from fasthtml.common import *
from .ui import (
    Button, Badge, Card, ServiceCard, PricingCard, FeatureCard,
    TestimonialCard, Section, SectionHeader, Input, Textarea, Select,
    Accordion, AccordionItem, Checkbox
)


# ============================================================================
# HERO SECTION
# ============================================================================

def HeroSection(**kwargs):
    """
    Sección hero principal con propuesta de valor
    """
    return ft_hx('section',
        Div(
            # Background decorativo
            Div(
                Div(cls="hero-gradient-orb hero-orb-1"),
                Div(cls="hero-gradient-orb hero-orb-2"),
                Div(cls="hero-pattern"),
                cls="hero-bg"
            ),

            Div(
                # Content
                Div(
                    # Badge
                    Badge("Nuevo: Komercia Cloud ya disponible", variant="accent"),

                    # Headline
                    H1(
                        Span("La gestión completa", cls="hero-title-line"),
                        Br(),
                        Span("de tu ", cls="hero-title-line"),
                        Span("minimarket", cls="hero-title-highlight"),
                        cls="hero-title"
                    ),

                    # Subheadline
                    P(
                        "Hardware para control y software para gestión. Todo lo que necesitas para administrar tu negocio desde cualquier lugar, de manera sencilla.",
                        cls="hero-subtitle"
                    ),

                    # CTAs
                    Div(
                        Button(
                            "Solicitar demo",
                            variant="primary",
                            size="lg",
                            href="#contacto",
                            icon="icon-arrow-right",
                            icon_position="right"
                        ),
                        Button(
                            "Ver precios",
                            variant="outline",
                            size="lg",
                            href="#precios"
                        ),
                        cls="hero-cta"
                    ),

                    # Trust badges
                    Div(
                        Div(
                            I(cls="icon icon-check-circle"),
                            Span("Sin contratos"),
                            cls="trust-badge"
                        ),
                        Div(
                            I(cls="icon icon-check-circle"),
                            Span("Soporte incluido"),
                            cls="trust-badge"
                        ),
                        Div(
                            I(cls="icon icon-check-circle"),
                            Span("Instalación gratis"),
                            cls="trust-badge"
                        ),
                        cls="trust-badges"
                    ),

                    cls="hero-content"
                ),

                # Visual
                Div(
                    Div(
                        # POS Device mockup
                        Div(
                            Div(
                                Div(cls="pos-screen-header"),
                                Div(
                                    Div("Total", cls="pos-label"),
                                    Div("$47.890", cls="pos-total"),
                                    Div(
                                        Span("Leche Entera 1L", cls="pos-item-name"),
                                        Span("$1.290", cls="pos-item-price"),
                                        cls="pos-item"
                                    ),
                                    Div(
                                        Span("Pan Molde", cls="pos-item-name"),
                                        Span("$2.100", cls="pos-item-price"),
                                        cls="pos-item"
                                    ),
                                    Div(
                                        Span("Bebida 2L", cls="pos-item-name"),
                                        Span("$1.890", cls="pos-item-price"),
                                        cls="pos-item"
                                    ),
                                    cls="pos-screen-content"
                                ),
                                cls="pos-screen"
                            ),
                            Div(cls="pos-base"),
                            cls="pos-device"
                        ),

                        # Floating cards
                        Div(
                            I(cls="icon icon-trending-up"),
                            Div(
                                Span("Ventas hoy", cls="float-card-label"),
                                Span("$342.500", cls="float-card-value"),
                                cls="float-card-content"
                            ),
                            cls="float-card float-card-sales"
                        ),
                        Div(
                            I(cls="icon icon-package"),
                            Div(
                                Span("Stock bajo", cls="float-card-label"),
                                Span("3 productos", cls="float-card-value float-card-warning"),
                                cls="float-card-content"
                            ),
                            cls="float-card float-card-stock"
                        ),
                        Div(
                            I(cls="icon icon-check-circle"),
                            Span("Boleta emitida", cls="float-card-label"),
                            cls="float-card float-card-receipt"
                        ),

                        cls="hero-visual-wrapper"
                    ),
                    cls="hero-visual"
                ),

                cls="hero-grid container"
            ),

            cls="hero"
        ),
        id="inicio",
        **kwargs
    )


# ============================================================================
# SERVICES SECTION
# ============================================================================

def ServicesSection(**kwargs):
    """
    Sección de servicios (los 3 modelos de negocio)
    """
    services = [
        {
            "icon": "icon-monitor",
            "title": "Komercia POS",
            "description": "Hardware y software integrado para tu punto de venta. Equipo completo listo para usar.",
            "features": [
                "Equipo POS táctil incluido",
                "Impresora de boletas",
                "Lector de código de barras",
                "Software de ventas instalado",
                "Capacitación incluida"
            ],
            "badge": "Hardware + Software",
            "cta_text": "Ver equipos",
            "cta_href": "#contacto"
        },
        {
            "icon": "icon-cloud",
            "title": "Komercia Cloud",
            "description": "Plataforma SaaS para gestionar tu negocio desde cualquier dispositivo, en cualquier momento.",
            "features": [
                "Dashboard en tiempo real",
                "Gestión de inventario",
                "Reportes y analytics",
                "Multi-sucursal",
                "Acceso móvil"
            ],
            "badge": "SaaS",
            "cta_text": "Ver planes",
            "cta_href": "#precios"
        },
        {
            "icon": "icon-code",
            "title": "Komercia API",
            "description": "Integra facturación electrónica y más funcionalidades en tu propio sistema.",
            "features": [
                "API REST moderna",
                "Facturación electrónica",
                "Documentación completa",
                "Soporte técnico",
                "Sandbox de pruebas"
            ],
            "badge": "Próximamente",
            "cta_text": "Más información",
            "cta_href": "#contacto"
        }
    ]

    service_cards = [
        ServiceCard(**service) for service in services
    ]

    return Section(
        SectionHeader(
            title="Todo lo que tu negocio necesita",
            subtitle="Desde el hardware hasta el software, tenemos la solución completa para tu minimarket.",
            badge="Servicios"
        ),
        Div(*service_cards, cls="services-grid"),
        id="servicios",
        variant="default",
        **kwargs
    )


# ============================================================================
# FEATURES SECTION
# ============================================================================

def FeaturesSection(**kwargs):
    """
    Sección de características principales
    """
    features = [
        {
            "icon": "icon-smartphone",
            "title": "Acceso remoto",
            "description": "Monitorea tu negocio desde tu celular en cualquier momento y lugar."
        },
        {
            "icon": "icon-bar-chart",
            "title": "Reportes en tiempo real",
            "description": "Conoce tus ventas, productos más vendidos y tendencias al instante."
        },
        {
            "icon": "icon-package",
            "title": "Control de inventario",
            "description": "Alertas de stock bajo y gestión automática de tu inventario."
        },
        {
            "icon": "icon-file-text",
            "title": "Boletas electrónicas",
            "description": "Emisión automática de boletas cumpliendo con normativa SII."
        },
        {
            "icon": "icon-users",
            "title": "Multi-usuario",
            "description": "Diferentes niveles de acceso para dueños, administradores y cajeros."
        },
        {
            "icon": "icon-headphones",
            "title": "Soporte dedicado",
            "description": "Equipo de soporte en español disponible cuando lo necesites."
        }
    ]

    feature_cards = [
        FeatureCard(**feature) for feature in features
    ]

    return Section(
        SectionHeader(
            title="Diseñado para minimarkets",
            subtitle="Funcionalidades pensadas específicamente para las necesidades de tu negocio.",
            badge="Características"
        ),
        Div(*feature_cards, cls="features-grid"),
        id="caracteristicas",
        variant="alt",
        **kwargs
    )


# ============================================================================
# PRICING SECTION
# ============================================================================

def PricingSection(**kwargs):
    """
    Sección de precios para Komercia Cloud
    """
    plans = [
        {
            "name": "Básico",
            "price": "29.990",
            "description": "Ideal para empezar a digitalizar tu negocio",
            "features": [
                {"text": "1 punto de venta", "included": True},
                {"text": "Gestión de inventario", "included": True},
                {"text": "Boletas electrónicas", "included": True},
                {"text": "Reportes básicos", "included": True},
                {"text": "Soporte por email", "included": True},
                {"text": "Multi-sucursal", "included": False},
                {"text": "API access", "included": False},
            ],
            "popular": False
        },
        {
            "name": "Profesional",
            "price": "49.990",
            "description": "La opción más completa para tu minimarket",
            "features": [
                {"text": "Hasta 3 puntos de venta", "included": True},
                {"text": "Gestión de inventario avanzada", "included": True},
                {"text": "Boletas y facturas electrónicas", "included": True},
                {"text": "Reportes avanzados", "included": True},
                {"text": "Soporte prioritario", "included": True},
                {"text": "Multi-sucursal", "included": True},
                {"text": "API access", "included": False},
            ],
            "popular": True
        },
        {
            "name": "Enterprise",
            "price": "99.990",
            "description": "Para cadenas y operaciones grandes",
            "features": [
                {"text": "Puntos de venta ilimitados", "included": True},
                {"text": "Gestión completa de inventario", "included": True},
                {"text": "Documentos tributarios completos", "included": True},
                {"text": "Analytics avanzados", "included": True},
                {"text": "Soporte 24/7", "included": True},
                {"text": "Multi-sucursal ilimitado", "included": True},
                {"text": "API access completo", "included": True},
            ],
            "popular": False
        }
    ]

    pricing_cards = [
        PricingCard(**plan) for plan in plans
    ]

    return Section(
        SectionHeader(
            title="Planes simples y transparentes",
            subtitle="Sin sorpresas ni costos ocultos. Elige el plan que mejor se adapte a tu negocio.",
            badge="Precios"
        ),
        Div(*pricing_cards, cls="pricing-grid"),
        Div(
            P("¿Necesitas un plan personalizado? ", cls="pricing-custom-text"),
            A("Contáctanos", href="#contacto", cls="pricing-custom-link"),
            cls="pricing-custom"
        ),
        id="precios",
        variant="default",
        **kwargs
    )


# ============================================================================
# TESTIMONIALS SECTION
# ============================================================================

def TestimonialsSection(**kwargs):
    """
    Sección de testimonios
    """
    testimonials = [
        {
            "quote": "Antes no sabía cuánto vendía hasta contar la caja al final del día. Ahora puedo ver todo desde mi celular, incluso cuando no estoy en el local.",
            "author": "María González",
            "role": "Dueña de Minimarket",
            "company": "Minimarket La Esquina"
        },
        {
            "quote": "El sistema es muy fácil de usar. Mi hijo me ayudó a instalarlo y en dos días ya estaba funcionando solo. El soporte siempre responde rápido.",
            "author": "Jorge Muñoz",
            "role": "Propietario",
            "company": "Almacén Don Jorge"
        },
        {
            "quote": "Tengo 3 locales y por fin puedo ver las ventas de todos desde un solo lugar. Los reportes me ayudan a tomar mejores decisiones de compra.",
            "author": "Carmen Silva",
            "role": "Gerente General",
            "company": "Supermercado Silva"
        }
    ]

    testimonial_cards = [
        TestimonialCard(**testimonial) for testimonial in testimonials
    ]

    return Section(
        SectionHeader(
            title="Lo que dicen nuestros clientes",
            subtitle="Cientos de minimarkets ya confían en Komercia para gestionar su negocio.",
            badge="Testimonios"
        ),
        Div(*testimonial_cards, cls="testimonials-grid"),
        id="testimonios",
        variant="alt",
        **kwargs
    )


# ============================================================================
# ABOUT SECTION
# ============================================================================

def AboutSection(**kwargs):
    """
    Sección sobre nosotros
    """
    stats = [
        {"number": "500+", "label": "Clientes activos"},
        {"number": "15M+", "label": "Transacciones procesadas"},
        {"number": "99.9%", "label": "Uptime garantizado"},
        {"number": "24/7", "label": "Soporte disponible"},
    ]

    stat_items = [
        Div(
            Span(stat["number"], cls="stat-number"),
            Span(stat["label"], cls="stat-label"),
            cls="stat-item"
        ) for stat in stats
    ]

    return Section(
        Div(
            # Content
            Div(
                Badge("Nosotros", variant="primary"),
                H2("Construido para comerciantes, por comerciantes", cls="about-title"),
                P(
                    "Nacimos de la necesidad real de dueños de minimarket que buscaban una solución simple, accesible y que realmente funcionara para su día a día.",
                    cls="about-text"
                ),
                P(
                    "Nuestro equipo combina experiencia en retail y tecnología para crear herramientas que simplifican la gestión de tu negocio, sin complicaciones innecesarias.",
                    cls="about-text"
                ),
                Div(
                    Button("Conoce más", variant="primary", href="#contacto"),
                    cls="about-cta"
                ),
                cls="about-content"
            ),

            # Stats
            Div(*stat_items, cls="about-stats"),

            cls="about-grid"
        ),
        id="nosotros",
        variant="default",
        **kwargs
    )


# ============================================================================
# FAQ SECTION
# ============================================================================

def FAQSection(**kwargs):
    """
    Sección de preguntas frecuentes
    """
    faqs = [
        {
            "question": "¿Qué incluye el equipo POS?",
            "answer": "El equipo POS incluye una terminal táctil con nuestro software instalado, impresora de boletas térmica, lector de código de barras y todo el cableado necesario. También incluimos capacitación inicial y soporte técnico."
        },
        {
            "question": "¿Necesito internet para usar el sistema?",
            "answer": "Para las funcionalidades básicas de venta, el sistema funciona sin internet. Sin embargo, para sincronizar datos en la nube, emitir boletas electrónicas y acceder remotamente, necesitas conexión a internet."
        },
        {
            "question": "¿Puedo cambiar de plan después?",
            "answer": "Sí, puedes cambiar tu plan en cualquier momento. Si subes de plan, el cambio es inmediato. Si bajas, se aplicará al inicio del siguiente ciclo de facturación."
        },
        {
            "question": "¿El sistema cumple con las normativas del SII?",
            "answer": "Sí, Komercia está certificado por el SII para la emisión de boletas y facturas electrónicas. Cumplimos con todas las normativas tributarias vigentes en Chile."
        },
        {
            "question": "¿Cómo es el proceso de instalación?",
            "answer": "Nuestro equipo coordina contigo la instalación. Un técnico va a tu local, instala el equipo, configura el sistema con tus productos y te capacita en el uso. Todo en un solo día."
        },
        {
            "question": "¿Qué pasa si tengo problemas técnicos?",
            "answer": "Contamos con soporte técnico por teléfono, chat y email. Para planes Profesional y Enterprise, el soporte es prioritario. También ofrecemos visitas técnicas cuando es necesario."
        }
    ]

    accordion_items = [
        AccordionItem(
            title=faq["question"],
            content=faq["answer"],
            index=i
        ) for i, faq in enumerate(faqs)
    ]

    return Section(
        SectionHeader(
            title="Preguntas frecuentes",
            subtitle="Resolvemos tus dudas más comunes sobre Komercia.",
            badge="FAQ"
        ),
        Accordion(*accordion_items),
        Div(
            P("¿No encontraste lo que buscabas? ", cls="faq-more-text"),
            A("Escríbenos", href="#contacto", cls="faq-more-link"),
            cls="faq-more"
        ),
        id="faq",
        variant="alt",
        **kwargs
    )


# ============================================================================
# CONTACT SECTION
# ============================================================================

def ContactSection(**kwargs):
    """
    Sección de contacto con formulario
    """
    # Opciones para el select de interés
    interest_options = [
        {"value": "pos", "label": "Komercia POS (Hardware + Software)"},
        {"value": "cloud", "label": "Komercia Cloud (SaaS)"},
        {"value": "both", "label": "Ambos (POS + Cloud)"},
        # {"value": "api", "label": "Komercia API (Desarrolladores)"},
        {"value": "other", "label": "Otro / Consulta general"},
    ]

    return Section(
        Div(
            # Info de contacto
            Div(
                Badge("Contacto", variant="primary"),
                H2("Hablemos de tu negocio", cls="contact-title"),
                P(
                    "Cuéntanos sobre tu minimarket y te ayudaremos a encontrar la solución perfecta.",
                    cls="contact-text"
                ),

                Div(
                    Div(
                        I(cls="icon icon-mail"),
                        Div(
                            Span("Email", cls="contact-item-label"),
                            A("contacto@komercia.cl", href="mailto:contacto@komercia.cl", cls="contact-item-value"),
                            cls="contact-item-text"
                        ),
                        cls="contact-item"
                    ),
                    Div(
                        I(cls="icon icon-phone"),
                        Div(
                            Span("Teléfono", cls="contact-item-label"),
                            A("+56 9 1234 5678", href="tel:+56912345678", cls="contact-item-value"),
                            cls="contact-item-text"
                        ),
                        cls="contact-item"
                    ),
                    Div(
                        I(cls="icon icon-map-pin"),
                        Div(
                            Span("Oficina", cls="contact-item-label"),
                            Span("Santiago, Chile", cls="contact-item-value"),
                            cls="contact-item-text"
                        ),
                        cls="contact-item"
                    ),
                    Div(
                        I(cls="icon icon-clock"),
                        Div(
                            Span("Horario", cls="contact-item-label"),
                            Span("Lun - Vie, 9:00 - 18:00", cls="contact-item-value"),
                            cls="contact-item-text"
                        ),
                        cls="contact-item"
                    ),
                    cls="contact-items"
                ),

                cls="contact-info"
            ),

            # Formulario
            Div(
                Form(
                    Div(
                        Input(
                            name="nombre",
                            label="Nombre completo",
                            placeholder="Tu nombre",
                            required=True
                        ),
                        Input(
                            name="email",
                            type="email",
                            label="Email",
                            placeholder="tu@email.com",
                            required=True
                        ),
                        cls="form-row"
                    ),
                    Div(
                        Input(
                            name="telefono",
                            type="tel",
                            label="Teléfono",
                            placeholder="+56 9 1234 5678"
                        ),
                        Input(
                            name="empresa",
                            label="Nombre del negocio",
                            placeholder="Minimarket/Almacén"
                        ),
                        cls="form-row"
                    ),
                    Select(
                        name="interes",
                        label="¿Qué te interesa?",
                        options=interest_options,
                        required=True
                    ),
                    Textarea(
                        name="mensaje",
                        label="Mensaje",
                        placeholder="Cuéntanos sobre tu negocio y cómo podemos ayudarte...",
                        rows=4
                    ),
                    Checkbox(
                        name="newsletter",
                        label="Quiero recibir novedades y consejos para mi negocio"
                    ),
                    Button(
                        "Enviar mensaje",
                        variant="primary",
                        size="lg",
                        full_width=True,
                        icon="icon-send",
                        icon_position="right"
                    ),

                    cls="contact-form",
                    id="contact-form",
                    hx_post="/api/contact",
                    hx_swap="outerHTML",
                    hx_indicator=".form-loading"
                ),
                Div(cls="form-loading"),
                cls="contact-form-wrapper"
            ),

            cls="contact-grid"
        ),
        id="contacto",
        variant="default",
        cls="contact-section",
        **kwargs
    )


# ============================================================================
# CTA SECTION
# ============================================================================

def CTASection(**kwargs):
    """
    Sección de llamada a la acción final
    """
    return ft_hx('section',
        Div(
            Div(
                H2("¿Listo para modernizar tu minimarket?", cls="cta-title"),
                P(
                    "Únete a cientos de comerciantes que ya gestionan su negocio de forma más eficiente con Komercia.",
                    cls="cta-text"
                ),
                Div(
                    Button(
                        "Comenzar ahora",
                        variant="accent",
                        size="lg",
                        href="#contacto",
                        icon="icon-arrow-right",
                        icon_position="right"
                    ),
                    Button(
                        "Ver demo",
                        variant="outline-light",
                        size="lg",
                        href="#contacto"
                    ),
                    cls="cta-buttons"
                ),
                cls="cta-content"
            ),
            cls="container"
        ),
        cls="cta-section",
        **kwargs
    )
