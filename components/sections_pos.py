"""
Komercia POS Page Sections
Secciones específicas para la página de Komercia POS
"""
from fasthtml.common import *
from .ui import (
    Button, Badge, Card, Section, SectionHeader, FeatureCard
)


# ============================================================================
# POS HERO SECTION
# ============================================================================

def POSHeroSection(**kwargs):
    """
    Hero específico para la página de Komercia POS
    Con visual del equipo POS y propuesta de valor
    """
    return ft_hx('section',
        Div(
            # Background con patrón único
            Div(
                Div(cls="pos-hero-gradient"),
                Div(cls="pos-hero-grid-pattern"),
                Div(cls="pos-hero-glow"),
                cls="pos-hero-bg"
            ),

            Div(
                # Contenido
                Div(
                    Badge("Hardware + Software", variant="accent"),
                    H1(
                        Span("El punto de venta", cls="pos-hero-line"),
                        Br(),
                        Span("completo para tu ", cls="pos-hero-line"),
                        Span("minimarket", cls="pos-hero-highlight"),
                        cls="pos-hero-title"
                    ),
                    P(
                        "Equipo POS profesional con software integrado, listo para usar desde el primer día. "
                        "Conectado a la nube para que nunca pierdas el control de tu negocio.",
                        cls="pos-hero-subtitle"
                    ),
                    Div(
                        Button(
                            "Ver paquetes",
                            variant="primary",
                            size="lg",
                            href="#paquetes",
                            icon="icon-arrow-right",
                            icon_position="right"
                        ),
                        Button(
                            "Solicitar demo",
                            variant="outline",
                            size="lg",
                            href="/#contacto"
                        ),
                        cls="pos-hero-cta"
                    ),
                    # Highlights
                    Div(
                        Div(
                            Span("12", cls="highlight-number"),
                            Span("meses garantía", cls="highlight-label"),
                            cls="hero-highlight-item"
                        ),
                        Div(
                            Span("24h", cls="highlight-number"),
                            Span("instalación", cls="highlight-label"),
                            cls="hero-highlight-item"
                        ),
                        Div(
                            Span("100%", cls="highlight-number"),
                            Span("capacitación", cls="highlight-label"),
                            cls="hero-highlight-item"
                        ),
                        cls="hero-highlights"
                    ),
                    cls="pos-hero-content"
                ),

                # Visual del POS
                Div(
                    Div(
                        # Terminal POS principal
                        Div(
                            Div(
                                Div(
                                    Div(cls="terminal-camera"),
                                    Div(cls="terminal-status-light"),
                                    cls="terminal-top-bar"
                                ),
                                Div(
                                    # Header del software
                                    Div(
                                        Div(
                                            Span("Komercia", cls="sw-logo"),
                                            Span("POS", cls="sw-logo-accent"),
                                            cls="sw-header-logo"
                                        ),
                                        Div(
                                            Span("Online", cls="sync-status"),
                                            Div(cls="sync-indicator"),
                                            cls="sw-sync-badge"
                                        ),
                                        cls="sw-header"
                                    ),
                                    # Contenido de venta
                                    Div(
                                        Div(
                                            Span("Venta #1247", cls="sale-id"),
                                            Span("14:32", cls="sale-time"),
                                            cls="sale-header"
                                        ),
                                        Div(
                                            Div(
                                                Span("Coca-Cola 2L", cls="item-name"),
                                                Span("x2", cls="item-qty"),
                                                Span("$3.980", cls="item-total"),
                                                cls="sale-item"
                                            ),
                                            Div(
                                                Span("Pan Molde Ideal", cls="item-name"),
                                                Span("x1", cls="item-qty"),
                                                Span("$2.190", cls="item-total"),
                                                cls="sale-item"
                                            ),
                                            Div(
                                                Span("Leche Colun 1L", cls="item-name"),
                                                Span("x3", cls="item-qty"),
                                                Span("$4.170", cls="item-total"),
                                                cls="sale-item"
                                            ),
                                            cls="sale-items"
                                        ),
                                        Div(
                                            Span("Total", cls="total-label"),
                                            Span("$10.340", cls="total-amount"),
                                            cls="sale-total"
                                        ),
                                        cls="sw-sale-content"
                                    ),
                                    # Botones de acción
                                    Div(
                                        Div("Efectivo", cls="action-btn"),
                                        Div("Tarjeta", cls="action-btn action-btn-primary"),
                                        cls="sw-actions"
                                    ),
                                    cls="sw-screen"
                                ),
                                cls="terminal-screen"
                            ),
                            Div(cls="terminal-base"),
                            cls="pos-terminal"
                        ),

                        # Periféricos
                        Div(
                            Div(cls="printer-body"),
                            Div(
                                Div(cls="receipt-line"),
                                Div(cls="receipt-line receipt-line-short"),
                                Div(cls="receipt-line"),
                                Div(cls="receipt-line receipt-line-medium"),
                                cls="printer-receipt"
                            ),
                            cls="pos-printer"
                        ),
                        Div(
                            Div(cls="scanner-head"),
                            Div(cls="scanner-beam"),
                            cls="pos-scanner"
                        ),

                        cls="pos-hardware-group"
                    ),
                    cls="pos-hero-visual"
                ),

                cls="pos-hero-grid container"
            ),

            cls="pos-hero"
        ),
        id="inicio",
        **kwargs
    )


# ============================================================================
# SYNC SECTION - La sección destacada de sincronía
# ============================================================================

def SyncSection(**kwargs):
    """
    Sección visualmente impactante que muestra la sincronía
    entre Komercia POS y Komercia Cloud
    """
    return ft_hx('section',
        Div(
            # Background animado
            Div(
                Div(cls="sync-bg-gradient"),
                Div(cls="sync-particles"),
                Div(cls="sync-connection-lines"),
                cls="sync-bg"
            ),

            Div(
                # Header
                Div(
                    Badge("Sincronización en tiempo real", variant="accent"),
                    H2(
                        Span("Tu POS y la nube,", cls="sync-title-line"),
                        Br(),
                        Span("siempre ", cls="sync-title-line"),
                        Span("conectados", cls="sync-title-highlight"),
                        cls="sync-title"
                    ),
                    P(
                        "Cada venta, cada producto, cada movimiento se sincroniza automáticamente. "
                        "Consulta tu negocio desde cualquier lugar, en cualquier momento.",
                        cls="sync-subtitle"
                    ),
                    cls="sync-header"
                ),

                # Visualización de sincronía
                Div(
                    # POS Side
                    Div(
                        Div(
                            Div(
                                I(cls="icon icon-monitor"),
                                cls="sync-device-icon"
                            ),
                            H3("Komercia POS", cls="sync-device-title"),
                            P("En tu local", cls="sync-device-location"),
                            cls="sync-device-header"
                        ),
                        Div(
                            Div(
                                I(cls="icon icon-shopping-cart"),
                                Div(
                                    Span("Nueva venta", cls="sync-action-title"),
                                    Span("$45.890", cls="sync-action-value"),
                                    cls="sync-action-text"
                                ),
                                cls="sync-action-item sync-action-sale"
                            ),
                            Div(
                                I(cls="icon icon-package"),
                                Div(
                                    Span("Stock actualizado", cls="sync-action-title"),
                                    Span("-3 unidades", cls="sync-action-value"),
                                    cls="sync-action-text"
                                ),
                                cls="sync-action-item sync-action-stock"
                            ),
                            Div(
                                I(cls="icon icon-file-text"),
                                Div(
                                    Span("Boleta emitida", cls="sync-action-title"),
                                    Span("#B-004521", cls="sync-action-value"),
                                    cls="sync-action-text"
                                ),
                                cls="sync-action-item sync-action-receipt"
                            ),
                            cls="sync-actions-list"
                        ),
                        cls="sync-device sync-device-pos"
                    ),

                    # Connection animation
                    Div(
                        Div(
                            Div(cls="sync-pulse-ring"),
                            Div(cls="sync-pulse-ring sync-pulse-ring-2"),
                            Div(cls="sync-pulse-ring sync-pulse-ring-3"),
                            Div(
                                I(cls="icon icon-refresh-cw"),
                                cls="sync-pulse-icon"
                            ),
                            cls="sync-pulse"
                        ),
                        Div(
                            Div(cls="data-packet data-packet-1"),
                            Div(cls="data-packet data-packet-2"),
                            Div(cls="data-packet data-packet-3"),
                            cls="sync-data-flow sync-data-flow-right"
                        ),
                        Div(
                            Div(cls="data-packet data-packet-4"),
                            Div(cls="data-packet data-packet-5"),
                            cls="sync-data-flow sync-data-flow-left"
                        ),
                        Span("Sincronizando...", cls="sync-status-text"),
                        cls="sync-connection"
                    ),

                    # Cloud Side
                    Div(
                        Div(
                            Div(
                                I(cls="icon icon-cloud"),
                                cls="sync-device-icon sync-device-icon-cloud"
                            ),
                            H3("Komercia Cloud", cls="sync-device-title"),
                            P("Donde estés", cls="sync-device-location"),
                            cls="sync-device-header"
                        ),
                        Div(
                            Div(
                                I(cls="icon icon-smartphone"),
                                Div(
                                    Span("Notificación", cls="sync-action-title"),
                                    Span("Venta registrada", cls="sync-action-value"),
                                    cls="sync-action-text"
                                ),
                                cls="sync-action-item sync-action-notification"
                            ),
                            Div(
                                I(cls="icon icon-bar-chart"),
                                Div(
                                    Span("Dashboard", cls="sync-action-title"),
                                    Span("Actualizado", cls="sync-action-value"),
                                    cls="sync-action-text"
                                ),
                                cls="sync-action-item sync-action-dashboard"
                            ),
                            Div(
                                I(cls="icon icon-database"),
                                Div(
                                    Span("Respaldo", cls="sync-action-title"),
                                    Span("Automático", cls="sync-action-value"),
                                    cls="sync-action-text"
                                ),
                                cls="sync-action-item sync-action-backup"
                            ),
                            cls="sync-actions-list"
                        ),
                        cls="sync-device sync-device-cloud"
                    ),

                    cls="sync-visualization"
                ),

                # Beneficios de la sincronía
                Div(
                    Div(
                        Div(
                            I(cls="icon icon-zap"),
                            cls="sync-benefit-icon"
                        ),
                        H4("Instantáneo", cls="sync-benefit-title"),
                        P("Datos sincronizados, siempre", cls="sync-benefit-text"),
                        cls="sync-benefit"
                    ),
                    Div(
                        Div(
                            I(cls="icon icon-shield"),
                            cls="sync-benefit-icon"
                        ),
                        H4("Seguro", cls="sync-benefit-title"),
                        P("Encriptación de los datos de tu empresa", cls="sync-benefit-text"),
                        cls="sync-benefit"
                    ),
                    Div(
                        Div(
                            I(cls="icon icon-wifi-off"),
                            cls="sync-benefit-icon"
                        ),
                        H4("Sin internet", cls="sync-benefit-title"),
                        P("Funciona offline y sincroniza después", cls="sync-benefit-text"),
                        cls="sync-benefit"
                    ),
                    Div(
                        Div(
                            I(cls="icon icon-clock"),
                            cls="sync-benefit-icon"
                        ),
                        H4("24/7", cls="sync-benefit-title"),
                        P("Monitoreo continuo de tu negocio", cls="sync-benefit-text"),
                        cls="sync-benefit"
                    ),
                    cls="sync-benefits"
                ),

                cls="container"
            ),

            cls="sync-section"
        ),
        id="sincronizacion",
        **kwargs
    )


# ============================================================================
# PRODUCTS GRID SECTION - Paquetes POS
# ============================================================================

def ProductsGridSection(**kwargs):
    """
    Parrilla de productos/paquetes POS
    """
    packages = [
        {
            "name": "POS Starter",
            "tagline": "Ideal para comenzar",
            "price": "349.990",
            "image_type": "starter",
            "features": [
                "Terminal táctil 15.6\"",
                "Impresora térmica 80mm",
                "Cajón de dinero",
                "Software Komercia POS",
                "1 mes Komercia Cloud",
                "Instalación incluida",
            ],
            "specs": {
                "pantalla": "15.6\" táctil",
                "procesador": "Intel Celeron",
                "memoria": "4GB RAM",
                "almacenamiento": "64GB SSD"
            },
            "popular": False,
            "cta": "Consultar"
        },
        {
            "name": "POS Pro",
            "tagline": "El más vendido",
            "price": "549.990",
            "image_type": "pro",
            "features": [
                "Terminal táctil 15.6\" HD",
                "Impresora térmica 80mm",
                "Lector código de barras",
                "Cajón de dinero reforzado",
                "Software Komercia POS",
                "3 meses Komercia Cloud",
                "Instalación + Capacitación",
            ],
            "specs": {
                "pantalla": "15.6\" Full HD",
                "procesador": "Intel Core i3",
                "memoria": "8GB RAM",
                "almacenamiento": "128GB SSD"
            },
            "popular": True,
            "cta": "Consultar"
        },
        {
            "name": "POS Enterprise",
            "tagline": "Máximo rendimiento",
            "price": "849.990",
            "image_type": "enterprise",
            "features": [
                "Terminal táctil 17\" Full HD",
                "Impresora térmica de alta velocidad",
                "Lector código de barras inalámbrico",
                "Cajón de dinero premium",
                "Balanza digital integrada",
                "Software Komercia POS Pro",
                "6 meses Komercia Cloud",
                "Instalación VIP + Capacitación",
            ],
            "specs": {
                "pantalla": "17\" Full HD IPS",
                "procesador": "Intel Core i5",
                "memoria": "16GB RAM",
                "almacenamiento": "256GB SSD"
            },
            "popular": False,
            "cta": "Consultar"
        }
    ]

    def create_package_card(pkg):
        classes = ["product-card"]
        if pkg["popular"]:
            classes.append("product-card-popular")

        # Features list
        features_list = [
            Li(
                I(cls="icon icon-check"),
                Span(f),
                cls="product-feature"
            ) for f in pkg["features"]
        ]

        # Specs
        specs_items = [
            Div(
                Span(key.capitalize(), cls="spec-label"),
                Span(value, cls="spec-value"),
                cls="spec-item"
            ) for key, value in pkg["specs"].items()
        ]

        return Div(
            # Popular badge
            Span("Más vendido", cls="product-popular-badge") if pkg["popular"] else None,

            # Visual del producto
            Div(
                Div(cls=f"product-visual-{pkg['image_type']}"),
                cls="product-visual"
            ),

            # Info
            Div(
                Div(
                    H3(pkg["name"], cls="product-name"),
                    P(pkg["tagline"], cls="product-tagline"),
                    cls="product-header"
                ),

                # Precio
                Div(
                    Span("$", cls="product-currency"),
                    Span(pkg["price"], cls="product-price"),
                    Span(" CLP", cls="product-price-suffix"),
                    cls="product-pricing"
                ),

                # Features
                Ul(*features_list, cls="product-features"),

                # Specs
                Div(
                    Button_(
                        Span("Ver especificaciones"),
                        I(cls="icon icon-chevron-down"),
                        cls="specs-toggle",
                        x_on_click="specsOpen = !specsOpen"
                    ),
                    Div(
                        *specs_items,
                        cls="specs-content",
                        x_show="specsOpen",
                        x_collapse=True
                    ),
                    cls="product-specs",
                    x_data="{ specsOpen: false }"
                ),

                # CTA
                Button(pkg["cta"], variant="primary" if pkg["popular"] else "outline", full_width=True, href="/#contacto"),

                cls="product-info"
            ),

            cls=" ".join(classes)
        )

    package_cards = [create_package_card(pkg) for pkg in packages]

    return Section(
        SectionHeader(
            title="Paquetes POS listos para usar",
            subtitle="Elige el paquete que mejor se adapte a tu negocio. Todos incluyen instalación y capacitación.",
            badge="Paquetes"
        ),
        Div(*package_cards, cls="products-grid"),
        id="paquetes",
        variant="alt",
        cls="products-section",
        **kwargs
    )


# ============================================================================
# INDIVIDUAL PRODUCTS SECTION
# ============================================================================

def IndividualProductsSection(**kwargs):
    """
    Sección de productos individuales y armar paquete personalizado
    """
    individual_products = [
        {"name": "Terminal táctil 15.6\"", "price": "189.990"},
        {"name": "Terminal táctil 17\"", "price": "249.990"},
        {"name": "Impresora térmica 80mm", "price": "79.990"},
        {"name": "Lector código de barras USB", "price": "29.990"},
        {"name": "Lector código de barras inalámbrico", "price": "49.990"},
        {"name": "Cajón de dinero estándar", "price": "39.990"},
        {"name": "Cajón de dinero reforzado", "price": "59.990"},
        {"name": "Balanza digital", "price": "89.990"},
    ]

    product_pills = [
        Span(
            Span(p["name"], cls="pill-name"),
            Span(f"${p['price']}", cls="pill-price"),
            cls="product-pill"
        ) for p in individual_products
    ]

    return Section(
        # Contenido de productos individuales
        Div(
            Div(
                Div(
                    I(cls="icon icon-layers"),
                    cls="individual-icon"
                ),
                Div(
                    H3("También vendemos productos individuales", cls="individual-title"),
                    P(
                        "¿Ya tienes parte del equipo? Complementa tu setup con los componentes que necesitas. "
                        "Todos nuestros productos son compatibles entre sí.",
                        cls="individual-desc"
                    ),
                    cls="individual-text"
                ),
                cls="individual-header"
            ),

            # Pills de productos
            Div(*product_pills, cls="individual-products"),

            cls="individual-content"
        ),

        # CTA para armar paquete personalizado
        Div(
            Div(
                Div(
                    Div(cls="custom-pkg-decoration custom-pkg-decoration-1"),
                    Div(cls="custom-pkg-decoration custom-pkg-decoration-2"),
                    Div(cls="custom-pkg-decoration custom-pkg-decoration-3"),
                    cls="custom-pkg-decorations"
                ),
                Div(
                    I(cls="icon icon-edit-3"),
                    cls="custom-pkg-icon"
                ),
                H3("Arma tu propio paquete", cls="custom-pkg-title"),
                P(
                    "Cuéntanos qué necesitas y te preparamos una cotización a tu medida. "
                    "Sin compromiso.",
                    cls="custom-pkg-desc"
                ),
                Button(
                    "Cotizar paquete personalizado",
                    variant="accent",
                    size="lg",
                    href="/#contacto",
                    icon="icon-arrow-right",
                    icon_position="right"
                ),
                cls="custom-pkg-card"
            ),
            cls="custom-pkg-wrapper"
        ),
        id="productos-individuales",
        variant="default",
        cls="individual-section-wrapper",
        **kwargs
    )


# Helper para Button_
def Button_(*args, **kwargs):
    return ft_hx('button', *args, **kwargs)


# ============================================================================
# POS FEATURES SECTION
# ============================================================================

def POSFeaturesSection(**kwargs):
    """
    Características del sistema POS
    """
    features = [
        {
            "icon": "icon-zap",
            "title": "Ultra rápido",
            "description": "Procesa ventas en segundos. Interfaz optimizada para agilidad máxima."
        },
        {
            "icon": "icon-wifi-off",
            "title": "Funciona offline",
            "description": "Sin internet, sigue vendiendo. Se sincroniza automáticamente cuando vuelve la conexión."
        },
        {
            "icon": "icon-file-text",
            "title": "Boleta electrónica",
            "description": "Emisión automática de boletas y facturas. Cumple con normativa SII."
        },
        {
            "icon": "icon-package",
            "title": "Control de stock",
            "description": "Inventario actualizado en tiempo real. Alertas de stock bajo."
        },
        {
            "icon": "icon-users",
            "title": "Multi-cajero",
            "description": "Cada cajero con su sesión. Control de turnos y cierres de caja."
        },
        {
            "icon": "icon-credit-card",
            "title": "Múltiples pagos",
            "description": "Efectivo, tarjetas, transferencias. Pagos mixtos y vuelto automático."
        }
    ]

    feature_cards = [
        Div(
            Div(I(cls=f"icon {f['icon']}"), cls="pos-feature-icon"),
            H4(f["title"], cls="pos-feature-title"),
            P(f["description"], cls="pos-feature-desc"),
            cls="pos-feature-card"
        ) for f in features
    ]

    return Section(
        SectionHeader(
            title="Software pensado para vender",
            subtitle="Cada función diseñada para hacer tu trabajo más fácil y rápido.",
            badge="Características"
        ),
        Div(*feature_cards, cls="pos-features-grid"),
        id="caracteristicas",
        variant="default",
        **kwargs
    )


# ============================================================================
# WHAT'S INCLUDED SECTION
# ============================================================================

def WhatsIncludedSection(**kwargs):
    """
    Qué incluye cada paquete POS
    """
    included_items = [
        {
            "icon": "icon-monitor",
            "title": "Terminal POS",
            "description": "Pantalla táctil de alta resolución con procesador potente"
        },
        {
            "icon": "icon-printer",
            "title": "Impresora",
            "description": "Impresora térmica de alta velocidad para boletas"
        },
        {
            "icon": "icon-scan",
            "title": "Lector de barras",
            "description": "Escanea productos rápidamente (en paquetes Pro y Enterprise)"
        },
        {
            "icon": "icon-box",
            "title": "Cajón de dinero",
            "description": "Cajón metálico con apertura automática"
        },
        {
            "icon": "icon-download",
            "title": "Software",
            "description": "Komercia POS instalado y configurado con tus productos"
        },
        {
            "icon": "icon-cloud",
            "title": "Cloud incluido",
            "description": "Acceso a Komercia Cloud para gestión remota"
        },
        {
            "icon": "icon-tool",
            "title": "Instalación",
            "description": "Técnico en tu local para instalar y configurar todo"
        },
        {
            "icon": "icon-book-open",
            "title": "Capacitación",
            "description": "Entrenamiento para ti y tu equipo en el uso del sistema"
        }
    ]

    items = [
        Div(
            Div(I(cls=f"icon {item['icon']}"), cls="included-icon"),
            Div(
                H4(item["title"], cls="included-title"),
                P(item["description"], cls="included-desc"),
                cls="included-text"
            ),
            cls="included-item"
        ) for item in included_items
    ]

    return Section(
        SectionHeader(
            title="Todo lo que necesitas incluido",
            subtitle="No te preocupes por nada. Nosotros nos encargamos de todo.",
            badge="Incluido"
        ),
        Div(*items, cls="included-grid"),
        id="incluido",
        variant="alt",
        **kwargs
    )


# ============================================================================
# POS CTA SECTION
# ============================================================================

def POSCTASection(**kwargs):
    """
    Call to action específico para POS
    """
    return ft_hx('section',
        Div(
            Div(
                Div(
                    H2("¿Listo para modernizar tu punto de venta?", cls="pos-cta-title"),
                    P(
                        "Contáctanos y te ayudamos a elegir el paquete perfecto para tu negocio. "
                        "Instalación en 24 horas.",
                        cls="pos-cta-text"
                    ),
                    Div(
                        Button(
                            "Solicitar cotización",
                            variant="accent",
                            size="lg",
                            href="/#contacto",
                            icon="icon-arrow-right",
                            icon_position="right"
                        ),
                        Button(
                            "Llamar ahora",
                            variant="outline-light",
                            size="lg",
                            href="tel:+56912345678",
                            icon="icon-phone",
                            icon_position="left"
                        ),
                        cls="pos-cta-buttons"
                    ),
                    cls="pos-cta-content"
                ),
                # Visual decorativo
                Div(
                    Div(cls="pos-cta-visual-element pos-cta-visual-1"),
                    Div(cls="pos-cta-visual-element pos-cta-visual-2"),
                    Div(cls="pos-cta-visual-element pos-cta-visual-3"),
                    cls="pos-cta-visual"
                ),
                cls="pos-cta-wrapper"
            ),
            cls="container"
        ),
        cls="pos-cta-section",
        **kwargs
    )


# ============================================================================
# SUPPORT SECTION
# ============================================================================

def SupportSection(**kwargs):
    """
    Sección de soporte y garantía
    """
    return Section(
        Div(
            # Left content
            Div(
                Badge("Soporte", variant="primary"),
                H2("Siempre contigo", cls="support-title"),
                P(
                    "No te dejamos solo. Nuestro equipo está disponible para ayudarte "
                    "en cada paso del camino.",
                    cls="support-text"
                ),
                Div(
                    Div(
                        Div(
                            I(cls="icon icon-headphones"),
                            cls="support-item-icon"
                        ),
                        Div(
                            H4("Soporte técnico", cls="support-item-title"),
                            P("Atención por teléfono, WhatsApp y email", cls="support-item-desc"),
                            cls="support-item-text"
                        ),
                        cls="support-item"
                    ),
                    Div(
                        Div(
                            I(cls="icon icon-shield"),
                            cls="support-item-icon"
                        ),
                        Div(
                            H4("Garantía extendida", cls="support-item-title"),
                            P("12 meses de garantía en todo el hardware", cls="support-item-desc"),
                            cls="support-item-text"
                        ),
                        cls="support-item"
                    ),
                    Div(
                        Div(
                            I(cls="icon icon-tool"),
                            cls="support-item-icon"
                        ),
                        Div(
                            H4("Visitas técnicas", cls="support-item-title"),
                            P("Servicio en terreno cuando lo necesites", cls="support-item-desc"),
                            cls="support-item-text"
                        ),
                        cls="support-item"
                    ),
                    Div(
                        Div(
                            I(cls="icon icon-refresh-cw"),
                            cls="support-item-icon"
                        ),
                        Div(
                            H4("Actualizaciones", cls="support-item-title"),
                            P("Software siempre actualizado sin costo adicional", cls="support-item-desc"),
                            cls="support-item-text"
                        ),
                        cls="support-item"
                    ),
                    cls="support-items"
                ),
                cls="support-content"
            ),

            # Right - Image placeholder
            Div(
                Div(
                    Div(
                        I(cls="icon icon-message-circle"),
                        cls="support-visual-icon"
                    ),
                    Div(
                        Span("Equipo de soporte", cls="support-visual-title"),
                        # Span("Respuesta promedio: 5 min", cls="support-visual-subtitle"),
                        cls="support-visual-text"
                    ),
                    cls="support-visual-card"
                ),
                cls="support-visual"
            ),

            cls="support-grid"
        ),
        id="soporte",
        variant="default",
        **kwargs
    )
