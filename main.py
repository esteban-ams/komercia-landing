"""
Komercia Landing Page
FastHTML + HTMX + Alpine.js
"""
from fasthtml.common import *
from starlette.responses import FileResponse, Response
from pathlib import Path
import os
from dotenv import load_dotenv
import resend

# Cargar variables de entorno
load_dotenv()

# Configurar Resend
resend.api_key = os.getenv("RESEND_API_KEY")

# Importar componentes
from components.layout import PageLayout, POSPageLayout, CloudPageLayout, Navbar, Footer
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
from components.sections_cloud import (
    CloudHeroSection,
    HowItWorksSection,
    CloudBenefitsSection,
    DashboardPreviewSection,
    CloudPricingSection,
    UseCasesSection,
    CloudCTASection,
    CloudFAQSection
)

# ============================================================================
# APP SETUP
# ============================================================================

# Path for static files
STATIC_PATH = Path(__file__).resolve().parent / 'static'

app, rt = fast_app(
    pico=False,
    secret_key=os.getenv("SECRET_KEY", "komercia-landing-default-key-change-in-prod"),
    hdrs=(
        Link(rel='stylesheet', href='/static/css/styles.css'),
    )
)


# Explicit route for static files (required for gunicorn/uvicorn)
@rt('/static/{path:path}')
async def static_files(path: str):
    file_path = STATIC_PATH / path
    if file_path.exists() and file_path.is_file():
        return FileResponse(file_path)
    return Response('Not found', status_code=404)


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


@rt('/cloud', methods=['GET'])
def cloud_page():
    """Página de Komercia Cloud - SaaS"""
    return CloudPageLayout(
        CloudHeroSection(),
        HowItWorksSection(),
        CloudBenefitsSection(),
        UseCasesSection(),
        DashboardPreviewSection(),
        CloudPricingSection(),
        CloudFAQSection(),
        CloudCTASection(),
        title="Komercia Cloud - Gestiona tu Minimarket desde Cualquier Lugar",
        description="Software en la nube para minimarkets. Controla ventas, inventario y reportes desde tu celular. 14 días gratis."
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

    # Mapeo de valores de interés
    interes_labels = {
        "pos": "Komercia POS (Hardware + Software)",
        "cloud": "Komercia Cloud (SaaS)",
        "both": "Ambos (POS + Cloud)",
        "other": "Otro / Consulta general"
    }
    interes_text = interes_labels.get(interes, interes)

    # Enviar email con Resend
    try:
        resend.Emails.send({
            "from": os.getenv("RESEND_FROM_EMAIL", "onboarding@resend.dev"),
            "to": os.getenv("CONTACT_EMAIL"),
            "subject": f"Nuevo contacto de Komercia: {nombre}",
            "html": f"""
            <h2>Nuevo mensaje de contacto</h2>
            <table style="border-collapse: collapse; width: 100%; max-width: 600px;">
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Nombre:</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #eee;">{nombre}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Email:</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #eee;"><a href="mailto:{email}">{email}</a></td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Teléfono:</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #eee;">{telefono or 'No proporcionado'}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Empresa:</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #eee;">{empresa or 'No proporcionada'}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Interés:</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #eee;">{interes_text}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Newsletter:</strong></td>
                    <td style="padding: 10px; border-bottom: 1px solid #eee;">{'Sí' if newsletter else 'No'}</td>
                </tr>
            </table>
            <h3 style="margin-top: 20px;">Mensaje:</h3>
            <p style="background: #f5f5f5; padding: 15px; border-radius: 8px;">{mensaje or 'Sin mensaje adicional'}</p>
            <hr style="margin-top: 30px; border: none; border-top: 1px solid #eee;">
            <p style="color: #888; font-size: 12px;">Este mensaje fue enviado desde el formulario de contacto de Komercia.</p>
            """
        })
    except Exception as e:
        # Log del error (en producción usarías un logger apropiado)
        print(f"Error enviando email: {e}")
        return Div(
            Div(
                I(cls="icon icon-alert-circle error-icon"),
                H3("Error al enviar", cls="error-title"),
                P(
                    "Hubo un problema al enviar tu mensaje. Por favor intenta de nuevo o contáctanos directamente.",
                    cls="error-text"
                ),
                cls="form-error"
            ),
            cls="contact-form-wrapper"
        )

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

    # Enviar notificación de nueva suscripción
    try:
        resend.Emails.send({
            "from": os.getenv("RESEND_FROM_EMAIL", "onboarding@resend.dev"),
            "to": os.getenv("CONTACT_EMAIL"),
            "subject": f"Nueva suscripción al newsletter: {email}",
            "html": f"""
            <h2>Nueva suscripción al newsletter</h2>
            <p>El siguiente email se ha suscrito al newsletter de Komercia:</p>
            <p style="font-size: 18px; background: #f5f5f5; padding: 15px; border-radius: 8px;">
                <a href="mailto:{email}">{email}</a>
            </p>
            <hr style="margin-top: 30px; border: none; border-top: 1px solid #eee;">
            <p style="color: #888; font-size: 12px;">Suscripción desde el footer de Komercia.</p>
            """
        })
    except Exception as e:
        print(f"Error enviando notificación de newsletter: {e}")

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
