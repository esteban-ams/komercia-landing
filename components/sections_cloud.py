"""
Komercia Cloud Page Sections
Secciones específicas para la página de Komercia Cloud (SaaS)
Enfoque: Simple, claro, para usuarios no técnicos
"""
from fasthtml.common import *
from .ui import (
    Button, Badge, Card, Section, SectionHeader, FeatureCard
)


# ============================================================================
# CLOUD HERO SECTION
# ============================================================================

def CloudHeroSection(**kwargs):
    """
    Hero para Komercia Cloud - Enfocado en accesibilidad y simplicidad
    """
    return ft_hx('section',
        Div(
            # Background con estilo cloud/moderno
            Div(
                Div(cls="cloud-hero-gradient"),
                Div(cls="cloud-hero-pattern"),
                Div(cls="cloud-hero-shapes"),
                cls="cloud-hero-bg"
            ),

            Div(
                # Contenido
                Div(
                    Badge("100% en la nube", variant="primary"),
                    H1(
                        Span("Tu negocio en", cls="cloud-hero-line"),
                        Br(),
                        Span("tus manos, ", cls="cloud-hero-line"),
                        Span("donde estés", cls="cloud-hero-highlight"),
                        cls="cloud-hero-title"
                    ),
                    P(
                        "Gestiona tu minimarket desde el celular, tablet o computador. "
                        "Revisa ventas, controla inventario y toma decisiones sin estar en el local.",
                        cls="cloud-hero-subtitle"
                    ),
                    Div(
                        Button(
                            "Probar gratis 14 días",
                            variant="primary",
                            size="lg",
                            href="/#contacto",
                            icon="icon-arrow-right",
                            icon_position="right"
                        ),
                        Button(
                            "Ver cómo funciona",
                            variant="outline",
                            size="lg",
                            href="#como-funciona"
                        ),
                        cls="cloud-hero-cta"
                    ),
                    # Trust indicators
                    Div(
                        Div(
                            I(cls="icon icon-check-circle"),
                            Span("Sin instalación"),
                            cls="trust-item"
                        ),
                        Div(
                            I(cls="icon icon-check-circle"),
                            Span("Soporte incluido"),
                            cls="trust-item"
                        ),
                        Div(
                            I(cls="icon icon-check-circle"),
                            Span("Cancela cuando quieras"),
                            cls="trust-item"
                        ),
                        cls="trust-indicators"
                    ),
                    cls="cloud-hero-content"
                ),

                # Visual - Dashboard mockup
                Div(
                    Div(
                        # Browser frame
                        Div(
                            Div(
                                Span(cls="browser-dot browser-dot-red"),
                                Span(cls="browser-dot browser-dot-yellow"),
                                Span(cls="browser-dot browser-dot-green"),
                                cls="browser-dots"
                            ),
                            Span("app.komercia.cl", cls="browser-url"),
                            cls="browser-bar"
                        ),
                        # Dashboard content
                        Div(
                            # Header del dashboard
                            Div(
                                Div(
                                    Span("Komercia", cls="dash-logo"),
                                    Span("Cloud", cls="dash-logo-accent"),
                                    cls="dash-header-logo"
                                ),
                                Div(
                                    Span("Minimarket Don Pedro", cls="dash-store-name"),
                                    cls="dash-header-right"
                                ),
                                cls="dash-header"
                            ),
                            # Stats cards
                            Div(
                                Div(
                                    Span("Ventas hoy", cls="stat-label"),
                                    Span("$847.350", cls="stat-value stat-value-green"),
                                    Span("+12% vs ayer", cls="stat-change stat-change-up"),
                                    cls="stat-card"
                                ),
                                Div(
                                    Span("Productos", cls="stat-label"),
                                    Span("1.247", cls="stat-value"),
                                    Span("15 stock bajo", cls="stat-change stat-change-warning"),
                                    cls="stat-card"
                                ),
                                Div(
                                    Span("Transacciones", cls="stat-label"),
                                    Span("89", cls="stat-value"),
                                    Span("Ticket prom: $9.520", cls="stat-change"),
                                    cls="stat-card"
                                ),
                                cls="dash-stats"
                            ),
                            # Mini chart placeholder
                            Div(
                                Div(cls="dash-chart-bars"),
                                Span("Ventas últimos 7 días", cls="dash-chart-label"),
                                cls="dash-chart"
                            ),
                            cls="dash-content"
                        ),
                        cls="browser-window"
                    ),
                    # Floating phone
                    Div(
                        Div(
                            Div(cls="phone-notch"),
                            Div(
                                Span("Alerta de stock", cls="phone-notification-title"),
                                Span("Coca-Cola 2L bajo mínimo", cls="phone-notification-text"),
                                cls="phone-notification"
                            ),
                            cls="phone-screen"
                        ),
                        cls="floating-phone"
                    ),
                    cls="cloud-hero-visual"
                ),

                cls="cloud-hero-grid container"
            ),

            cls="cloud-hero"
        ),
        id="inicio",
        **kwargs
    )


# ============================================================================
# HOW IT WORKS SECTION
# ============================================================================

def HowItWorksSection(**kwargs):
    """
    Sección simple de cómo funciona - 3 pasos
    """
    steps = [
        {
            "number": "1",
            "icon": "icon-user-plus",
            "title": "Crea tu cuenta",
            "description": "Regístrate en 2 minutos con tu email. Sin tarjeta de crédito, sin compromiso."
        },
        {
            "number": "2",
            "icon": "icon-upload",
            "title": "Carga tus productos",
            "description": "Sube tu inventario manualmente o impórtalo desde Excel. Te ayudamos si lo necesitas."
        },
        {
            "number": "3",
            "icon": "icon-trending-up",
            "title": "¡Listo para vender!",
            "description": "Empieza a registrar ventas, controlar stock y ver reportes desde cualquier lugar."
        }
    ]

    step_cards = [
        Div(
            Div(
                Span(step["number"], cls="step-number"),
                cls="step-number-wrapper"
            ),
            Div(
                Div(I(cls=f"icon {step['icon']}"), cls="step-icon"),
                H3(step["title"], cls="step-title"),
                P(step["description"], cls="step-desc"),
                cls="step-content"
            ),
            cls="step-card"
        ) for step in steps
    ]

    return Section(
        SectionHeader(
            title="Empieza en minutos, no en días",
            subtitle="Sin instalaciones complicadas. Sin técnicos. Sin esperas.",
            badge="Cómo funciona"
        ),
        Div(*step_cards, cls="steps-grid"),
        id="como-funciona",
        variant="alt",
        **kwargs
    )


# ============================================================================
# BENEFITS SECTION - What you can do
# ============================================================================

def CloudBenefitsSection(**kwargs):
    """
    Beneficios principales de Komercia Cloud
    Enfocado en lo que el usuario PUEDE HACER, no en features técnicas
    """
    benefits = [
        {
            "icon": "icon-smartphone",
            "title": "Revisa tu negocio desde el celular",
            "description": "¿Cómo van las ventas? ¿Qué productos se están acabando? Míralo en tiempo real desde donde estés.",
            "visual": "mobile"
        },
        {
            "icon": "icon-package",
            "title": "Nunca más te quedes sin stock",
            "description": "El sistema te avisa automáticamente cuando un producto está por acabarse. Adiós a las ventas perdidas.",
            "visual": "alerts"
        },
        {
            "icon": "icon-bar-chart",
            "title": "Sabe qué vende y qué no",
            "description": "Reportes simples que te muestran tus productos estrella, horarios peak y tendencias de venta.",
            "visual": "reports"
        },
        {
            "icon": "icon-users",
            "title": "Tu equipo, bajo control",
            "description": "Cada cajero con su cuenta. Sabes quién vendió qué y cuándo. Cierres de caja automáticos.",
            "visual": "team"
        },
        {
            "icon": "icon-shield",
            "title": "Tus datos siempre seguros",
            "description": "Respaldo automático en la nube. Si se daña tu computador, no pierdes nada. Todo está protegido.",
            "visual": "security"
        },
        {
            "icon": "icon-file-text",
            "title": "Boletas electrónicas sin complicarte",
            "description": "Emite boletas válidas ante el SII automáticamente. Nosotros nos encargamos de lo técnico.",
            "visual": "invoicing"
        }
    ]

    benefit_cards = [
        Div(
            Div(I(cls=f"icon {b['icon']}"), cls="benefit-icon"),
            H3(b["title"], cls="benefit-title"),
            P(b["description"], cls="benefit-desc"),
            cls="benefit-card"
        ) for b in benefits
    ]

    return Section(
        SectionHeader(
            title="Todo lo que necesitas, nada que no",
            subtitle="Herramientas pensadas para hacerte la vida más fácil, no más complicada.",
            badge="Beneficios"
        ),
        Div(*benefit_cards, cls="benefits-grid"),
        id="beneficios",
        variant="default",
        **kwargs
    )


# ============================================================================
# DASHBOARD PREVIEW SECTION
# ============================================================================

def DashboardPreviewSection(**kwargs):
    """
    Vista previa del dashboard con explicaciones simples
    """
    features = [
        {
            "icon": "icon-home",
            "title": "Panel principal",
            "desc": "Ve de un vistazo cómo va tu día"
        },
        {
            "icon": "icon-shopping-cart",
            "title": "Punto de venta",
            "desc": "Registra ventas rápido y fácil"
        },
        {
            "icon": "icon-package",
            "title": "Inventario",
            "desc": "Controla productos y stock"
        },
        {
            "icon": "icon-truck",
            "title": "Proveedores",
            "desc": "Gestiona compras y pedidos"
        },
        {
            "icon": "icon-bar-chart",
            "title": "Reportes",
            "desc": "Entiende tu negocio con datos"
        },
        {
            "icon": "icon-settings",
            "title": "Configuración",
            "desc": "Personaliza a tu medida"
        }
    ]

    feature_tabs = [
        Div(
            I(cls=f"icon {f['icon']}"),
            Div(
                Span(f["title"], cls="preview-tab-title"),
                Span(f["desc"], cls="preview-tab-desc"),
                cls="preview-tab-text"
            ),
            cls="preview-tab"
        ) for f in features
    ]

    return Section(
        Div(
            # Left - Feature list
            Div(
                Badge("Interfaz simple", variant="accent"),
                H2("Diseñado para que cualquiera lo use", cls="preview-title"),
                P(
                    "No necesitas ser experto en computación. Komercia Cloud es tan fácil "
                    "como usar WhatsApp. Botones grandes, textos claros, sin menús escondidos.",
                    cls="preview-subtitle"
                ),
                Div(*feature_tabs, cls="preview-tabs"),
                cls="preview-content"
            ),

            # Right - Screenshot
            Div(
                Div(
                    Div(cls="preview-screenshot"),
                    cls="preview-screen"
                ),
                cls="preview-visual"
            ),

            cls="preview-grid"
        ),
        id="interfaz",
        variant="alt",
        cls="dashboard-preview-section",
        **kwargs
    )


# ============================================================================
# PRICING SECTION - Cloud Plans
# ============================================================================

def CloudPricingSection(**kwargs):
    """
    Planes de precios para Komercia Cloud
    Simple y transparente
    """
    plans = [
        {
            "name": "Básico",
            "tagline": "Para empezar",
            "price": "29.990",
            "period": "/mes",
            "features": [
                "1 usuario",
                "Hasta 500 productos",
                "Ventas ilimitadas",
                "Reportes básicos",
                "Soporte por email",
                "Respaldo automático"
            ],
            "popular": False,
            "cta": "Empezar gratis"
        },
        {
            "name": "Profesional",
            "tagline": "El más popular",
            "price": "49.990",
            "period": "/mes",
            "features": [
                "3 usuarios",
                "Productos ilimitados",
                "Ventas ilimitadas",
                "Reportes avanzados",
                "Alertas de stock",
                "Control de vencimientos",
                "Soporte prioritario",
                "Boleta electrónica"
            ],
            "popular": True,
            "cta": "Empezar gratis"
        },
        {
            "name": "Empresarial",
            "tagline": "Multi-sucursal",
            "price": "89.990",
            "period": "/mes",
            "features": [
                "Usuarios ilimitados",
                "Productos ilimitados",
                "Múltiples sucursales",
                "Dashboard consolidado",
                "Reportes por sucursal",
                "API de integración",
                "Soporte telefónico",
                "Capacitación incluida"
            ],
            "popular": False,
            "cta": "Contactar ventas"
        }
    ]

    def create_plan_card(plan):
        classes = ["cloud-plan-card"]
        if plan["popular"]:
            classes.append("cloud-plan-popular")

        features_list = [
            Li(
                I(cls="icon icon-check"),
                Span(f),
                cls="plan-feature"
            ) for f in plan["features"]
        ]

        return Div(
            Span("Más elegido", cls="plan-popular-badge") if plan["popular"] else None,
            Div(
                H3(plan["name"], cls="plan-name"),
                P(plan["tagline"], cls="plan-tagline"),
                cls="plan-header"
            ),
            Div(
                Span("$", cls="plan-currency"),
                Span(plan["price"], cls="plan-price"),
                Span(plan["period"], cls="plan-period"),
                cls="plan-pricing"
            ),
            Ul(*features_list, cls="plan-features"),
            Button(
                plan["cta"],
                variant="primary" if plan["popular"] else "outline",
                full_width=True,
                href="/#contacto"
            ),
            P("14 días gratis, sin tarjeta", cls="plan-trial-text"),
            cls=" ".join(classes)
        )

    plan_cards = [create_plan_card(p) for p in plans]

    return Section(
        SectionHeader(
            title="Precios simples, sin sorpresas",
            subtitle="Todos los planes incluyen 14 días de prueba gratis. Sin tarjeta de crédito.",
            badge="Precios"
        ),
        Div(*plan_cards, cls="cloud-plans-grid"),
        # FAQ pricing
        Div(
            Div(
                H4("¿Qué pasa después de los 14 días?", cls="pricing-faq-q"),
                P("Si te gusta, eliges un plan y sigues. Si no, no te cobramos nada.", cls="pricing-faq-a"),
                cls="pricing-faq-item"
            ),
            Div(
                H4("¿Puedo cambiar de plan después?", cls="pricing-faq-q"),
                P("Sí, puedes subir o bajar de plan en cualquier momento.", cls="pricing-faq-a"),
                cls="pricing-faq-item"
            ),
            Div(
                H4("¿Hay contrato de permanencia?", cls="pricing-faq-q"),
                P("No. Cancela cuando quieras, sin multas ni preguntas.", cls="pricing-faq-a"),
                cls="pricing-faq-item"
            ),
            cls="pricing-faq"
        ),
        id="precios",
        variant="default",
        **kwargs
    )


# ============================================================================
# USE CASES / WHO IS IT FOR
# ============================================================================

def UseCasesSection(**kwargs):
    """
    Para quién es Komercia Cloud
    """
    cases = [
        {
            "icon": "icon-store",
            "title": "Minimarkets",
            "description": "Control de inventario con fechas de vencimiento, múltiples formas de pago y boleta electrónica."
        },
        {
            "icon": "icon-coffee",
            "title": "Almacenes de barrio",
            "description": "Simple y rápido para el día a día. Fiado, ventas al peso y productos sin código de barras."
        },
        {
            "icon": "icon-shopping-bag",
            "title": "Botillerías",
            "description": "Gestión de stock con alertas, control de proveedores y reportes de productos más vendidos."
        },
        {
            "icon": "icon-package",
            "title": "Distribuidoras",
            "description": "Multi-sucursal, control de bodegas y sincronización con puntos de venta."
        }
    ]

    case_cards = [
        Div(
            Div(I(cls=f"icon {c['icon']}"), cls="usecase-icon"),
            H4(c["title"], cls="usecase-title"),
            P(c["description"], cls="usecase-desc"),
            cls="usecase-card"
        ) for c in cases
    ]

    return Section(
        SectionHeader(
            title="Pensado para negocios como el tuyo",
            subtitle="Miles de comerciantes ya gestionan su negocio con Komercia Cloud.",
            badge="¿Para quién es?"
        ),
        Div(*case_cards, cls="usecases-grid"),
        id="para-quien",
        variant="alt",
        **kwargs
    )


# ============================================================================
# CLOUD CTA SECTION
# ============================================================================

def CloudCTASection(**kwargs):
    """
    Call to action final
    """
    return ft_hx('section',
        Div(
            Div(
                Div(
                    H2("Empieza hoy, gratis", cls="cloud-cta-title"),
                    P(
                        "14 días para probar todo, sin límites. Si no te convence, "
                        "no pagas nada. Así de simple.",
                        cls="cloud-cta-text"
                    ),
                    Div(
                        Button(
                            "Crear cuenta gratis",
                            variant="accent",
                            size="lg",
                            href="/#contacto",
                            icon="icon-arrow-right",
                            icon_position="right"
                        ),
                        Button(
                            "Hablar con ventas",
                            variant="outline-light",
                            size="lg",
                            href="/#contacto",
                            icon="icon-message-circle",
                            icon_position="left"
                        ),
                        cls="cloud-cta-buttons"
                    ),
                    Div(
                        I(cls="icon icon-check-circle"),
                        Span("Sin tarjeta de crédito"),
                        I(cls="icon icon-check-circle"),
                        Span("Configuración en 5 minutos"),
                        I(cls="icon icon-check-circle"),
                        Span("Soporte incluido"),
                        cls="cloud-cta-features"
                    ),
                    cls="cloud-cta-content"
                ),
                cls="cloud-cta-wrapper"
            ),
            cls="container"
        ),
        cls="cloud-cta-section",
        **kwargs
    )


# ============================================================================
# FAQ SECTION - Cloud specific
# ============================================================================

def CloudFAQSection(**kwargs):
    """
    Preguntas frecuentes específicas de Cloud
    """
    faqs = [
        {
            "question": "¿Necesito instalar algo en mi computador?",
            "answer": "No. Komercia Cloud funciona 100% en tu navegador (Chrome, Safari, Edge). Solo necesitas internet."
        },
        {
            "question": "¿Funciona en el celular?",
            "answer": "Sí. Puedes revisar ventas, inventario y reportes desde tu celular o tablet. La interfaz se adapta automáticamente."
        },
        {
            "question": "¿Qué pasa si se me corta el internet?",
            "answer": "Tu información está segura en la nube. Cuando vuelva el internet, todo sigue donde lo dejaste. También puedes usar Komercia POS que funciona offline."
        },
        {
            "question": "¿Mis datos están seguros?",
            "answer": "Sí. Usamos los mismos estándares de seguridad que los bancos. Tus datos están encriptados y respaldados automáticamente."
        },
        {
            "question": "¿Puedo migrar mis datos desde otro sistema?",
            "answer": "Sí. Te ayudamos a importar tus productos desde Excel o desde otros sistemas. El proceso es gratis y guiado."
        },
        {
            "question": "¿El soporte está incluido?",
            "answer": "Sí. Todos los planes incluyen soporte por email y chat. Los planes Profesional y Empresarial tienen soporte prioritario."
        },
        {
            "question": "¿Komercia Cloud se conecta con Komercia POS?",
            "answer": "¡Sí! Si tienes el hardware Komercia POS, se sincroniza automáticamente con Cloud. Ves todas tus ventas en un solo lugar."
        },
        {
            "question": "¿Emite boletas electrónicas?",
            "answer": "Sí. Los planes Profesional y Empresarial incluyen emisión de boletas electrónicas válidas ante el SII."
        }
    ]

    faq_items = [
        Div(
            Div(
                H4(faq["question"], cls="faq-question"),
                I(cls="icon icon-chevron-down faq-icon"),
                cls="faq-header",
                **{"@click": "open = !open"}
            ),
            Div(
                P(faq["answer"], cls="faq-answer"),
                cls="faq-content",
                x_show="open",
                x_transition=True
            ),
            cls="faq-item",
            x_data="{ open: false }",
            **{":class": "{ 'open': open }"}
        ) for faq in faqs
    ]

    return Section(
        SectionHeader(
            title="Preguntas frecuentes",
            subtitle="¿Tienes dudas? Aquí las respuestas más comunes.",
            badge="FAQ"
        ),
        Div(*faq_items, cls="faq-list cloud-faq-list"),
        id="faq",
        variant="default",
        **kwargs
    )
