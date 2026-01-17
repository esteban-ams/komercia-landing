"""
Komercia Landing Page
FastHTML + HTMX + Alpine.js
"""
from fasthtml.common import *
import os

# Importar componentes
from components.layout import PageLayout, POSPageLayout, Navbar, Footer
from components.sections import (
    HeroSection,
    ServicesSection,
    FeaturesSection,
    PricingSection,
    TestimonialsSection,
    AboutSection,
    FAQSection,
    ContactSection,
    CTASection
)
from components.sections_pos import (
    POSHeroSection,
    SyncSection,
    ProductsGridSection,
    POSFeaturesSection,
    WhatsIncludedSection,
    IndividualProductsSection,
    POSCTASection,
    SupportSection
)

# ============================================================================
# APP SETUP
# ============================================================================

app, rt = fast_app(
    pico=False,
    static_path='static',
    hdrs=(
        Link(rel='stylesheet', href='/static/css/styles.css'),
    )
)


# ============================================================================
# ROUTES
# ============================================================================

@rt('/')
def get():
    """Página principal - Landing Page"""
    return PageLayout(
        HeroSection(),
        ServicesSection(),
        FeaturesSection(),
        AboutSection(),
        PricingSection(),
        TestimonialsSection(),
        FAQSection(),
        CTASection(),
        ContactSection(),
        title="Komercia - Sistema POS y Gestión para Minimarkets",
        description="La gestión completa de tu minimarket. Hardware POS y software de gestión diseñados para simplificar tu negocio. Prueba gratis."
    )


@rt('/pos', methods=['GET'])
def pos_page():
    """Página de Komercia POS - Hardware + Software"""
    return POSPageLayout(
        POSHeroSection(),
        SyncSection(),
        POSFeaturesSection(),
        ProductsGridSection(),
        WhatsIncludedSection(),
        IndividualProductsSection(),
        SupportSection(),
        POSCTASection(),
        title="Komercia POS - Hardware y Software para tu Minimarket",
        description="Terminal de punto de venta con software integrado. Hardware profesional con sincronización cloud automática. Desde $349.990."
    )


# ============================================================================
# API ENDPOINTS (HTMX)
# ============================================================================

@rt('/api/contact', methods=['POST'])
async def contact_form(request):
    """Procesar formulario de contacto"""
    form_data = await request.form()

    nombre = form_data.get('nombre', '')
    email = form_data.get('email', '')
    telefono = form_data.get('telefono', '')
    empresa = form_data.get('empresa', '')
    interes = form_data.get('interes', '')
    mensaje = form_data.get('mensaje', '')
    newsletter = form_data.get('newsletter', False)

    # Aquí iría la lógica de envío de email con Resend
    # Por ahora, solo retornamos un mensaje de éxito

    # TODO: Integrar Resend para envío de emails
    # import resend
    # resend.api_key = os.environ.get("RESEND_API_KEY")
    # resend.Emails.send({
    #     "from": "onboarding@resend.dev",
    #     "to": "contacto@komercia.cl",
    #     "subject": f"Nuevo contacto: {nombre}",
    #     "html": f"..."
    # })

    return Div(
        Div(
            I(cls="icon icon-check-circle success-icon"),
            H3("¡Mensaje enviado!", cls="success-title"),
            P(
                f"Gracias {nombre.split()[0] if nombre else ''}, hemos recibido tu mensaje. "
                "Nos pondremos en contacto contigo pronto.",
                cls="success-text"
            ),
            Button(
                "Enviar otro mensaje",
                variant="outline",
                size="md",
                hx_get="/api/contact-form",
                hx_swap="outerHTML",
                hx_target=".contact-form-wrapper"
            ),
            cls="form-success"
        ),
        cls="contact-form-wrapper"
    )


@rt('/api/contact-form', methods=['GET'])
def get_contact_form():
    """Retornar formulario de contacto vacío"""
    from components.sections import ContactSection
    from components.ui import Input, Textarea, Select, Checkbox, Button

    interest_options = [
        {"value": "pos", "label": "Komercia POS (Hardware + Software)"},
        {"value": "cloud", "label": "Komercia Cloud (SaaS)"},
        {"value": "both", "label": "Ambos (POS + Cloud)"},
        # {"value": "api", "label": "Komercia API (Desarrolladores)"},
        {"value": "other", "label": "Otro / Consulta general"},
    ]

    return Div(
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
    )


@rt('/api/newsletter', methods=['POST'])
async def newsletter_signup(request):
    """Procesar suscripción a newsletter"""
    form_data = await request.form()
    email = form_data.get('email', '')

    # TODO: Integrar con servicio de email marketing

    return Div(
        Div(
            I(cls="icon icon-check-circle"),
            Span("¡Suscrito! Te mantendremos informado.", cls="newsletter-success-text"),
            cls="newsletter-success"
        ),
        cls="newsletter-form"
    )


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5003))
    serve(port=port)
