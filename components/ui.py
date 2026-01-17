"""
Komercia UI Components
Componentes reutilizables de interfaz de usuario
"""
from fasthtml.common import *


# ============================================================================
# BUTTONS
# ============================================================================

def Button(
    text: str,
    variant: str = "primary",  # primary, secondary, outline, ghost
    size: str = "md",  # sm, md, lg
    icon: str = None,
    icon_position: str = "left",  # left, right
    full_width: bool = False,
    href: str = None,
    **kwargs
):
    """
    Componente de botón reutilizable
    """
    classes = ["btn", f"btn-{variant}", f"btn-{size}"]
    if full_width:
        classes.append("btn-full")

    content = []
    if icon and icon_position == "left":
        content.append(I(cls=f"icon {icon}"))
    content.append(Span(text))
    if icon and icon_position == "right":
        content.append(I(cls=f"icon {icon}"))

    class_str = " ".join(classes)

    if href:
        return A(*content, href=href, cls=class_str, **kwargs)
    return Button_(*content, cls=class_str, **kwargs)


def Button_(*args, **kwargs):
    """HTML Button element"""
    return ft_hx('button', *args, **kwargs)


def IconButton(icon: str, variant: str = "ghost", label: str = "", **kwargs):
    """Botón solo con icono"""
    return Button_(
        I(cls=f"icon {icon}"),
        cls=f"btn-icon btn-{variant}",
        aria_label=label,
        **kwargs
    )


# ============================================================================
# CARDS
# ============================================================================

def Card(*content, variant: str = "default", hover: bool = True, **kwargs):
    """
    Componente de card reutilizable
    """
    classes = ["card", f"card-{variant}"]
    if hover:
        classes.append("card-hover")

    return Div(*content, cls=" ".join(classes), **kwargs)


def ServiceCard(
    icon: str,
    title: str,
    description: str,
    features: list = None,
    cta_text: str = "Conocer más",
    cta_href: str = "#",
    badge: str = None,
    **kwargs
):
    """Card para mostrar un servicio"""
    content = []

    # Badge opcional
    if badge:
        content.append(Span(badge, cls="card-badge"))

    # Icono
    content.append(
        Div(
            Div(cls=f"service-icon-bg"),
            I(cls=f"icon {icon}"),
            cls="service-icon-wrapper"
        )
    )

    # Título y descripción
    content.append(H3(title, cls="card-title"))
    content.append(P(description, cls="card-description"))

    # Features
    if features:
        feature_items = [Li(I(cls="icon icon-check"), Span(f)) for f in features]
        content.append(Ul(*feature_items, cls="card-features"))

    # CTA
    content.append(
        A(
            Span(cta_text),
            I(cls="icon icon-arrow-right"),
            href=cta_href,
            cls="card-cta"
        )
    )

    return Card(*content, variant="service", **kwargs)


def PricingCard(
    name: str,
    price: str,
    period: str = "/mes",
    description: str = "",
    features: list = None,
    cta_text: str = "Comenzar",
    cta_href: str = "#contacto",
    popular: bool = False,
    **kwargs
):
    """Card para mostrar un plan de precios"""
    classes = ["card", "card-pricing"]
    if popular:
        classes.append("card-pricing-popular")

    content = []

    # Badge de popular
    if popular:
        content.append(Span("Más popular", cls="pricing-badge"))

    # Header
    content.append(
        Div(
            H3(name, cls="pricing-name"),
            P(description, cls="pricing-description"),
            cls="pricing-header"
        )
    )

    # Precio
    content.append(
        Div(
            Span("$", cls="pricing-currency"),
            Span(price, cls="pricing-amount"),
            Span(period, cls="pricing-period"),
            cls="pricing-price"
        )
    )

    # Features
    if features:
        feature_items = []
        for f in features:
            if isinstance(f, dict):
                included = f.get("included", True)
                text = f.get("text", "")
                icon_cls = "icon-check" if included else "icon-x"
                item_cls = "included" if included else "not-included"
                feature_items.append(Li(I(cls=f"icon {icon_cls}"), Span(text), cls=item_cls))
            else:
                feature_items.append(Li(I(cls="icon icon-check"), Span(f), cls="included"))
        content.append(Ul(*feature_items, cls="pricing-features"))

    # CTA
    btn_variant = "primary" if popular else "outline"
    content.append(
        Button(cta_text, variant=btn_variant, full_width=True, href=cta_href)
    )

    return Div(*content, cls=" ".join(classes), **kwargs)


def FeatureCard(icon: str, title: str, description: str, **kwargs):
    """Card compacta para features"""
    return Div(
        Div(I(cls=f"icon {icon}"), cls="feature-icon"),
        H4(title, cls="feature-title"),
        P(description, cls="feature-description"),
        cls="feature-card",
        **kwargs
    )


def TestimonialCard(
    quote: str,
    author: str,
    role: str,
    company: str = "",
    avatar: str = None,
    **kwargs
):
    """Card para testimonios"""
    avatar_content = Div(author[0].upper(), cls="testimonial-avatar-placeholder")
    if avatar:
        avatar_content = Img(src=avatar, alt=author, cls="testimonial-avatar")

    company_text = f" - {company}" if company else ""

    return Div(
        Div(
            I(cls="icon icon-quote"),
            cls="testimonial-quote-icon"
        ),
        P(quote, cls="testimonial-quote"),
        Div(
            avatar_content,
            Div(
                Span(author, cls="testimonial-author"),
                Span(f"{role}{company_text}", cls="testimonial-role"),
                cls="testimonial-info"
            ),
            cls="testimonial-footer"
        ),
        cls="testimonial-card",
        **kwargs
    )


# ============================================================================
# FORM ELEMENTS
# ============================================================================

def Input(
    name: str,
    type: str = "text",
    label: str = None,
    placeholder: str = "",
    required: bool = False,
    helper: str = None,
    error: str = None,
    **kwargs
):
    """Input con label y estados"""
    content = []

    input_id = kwargs.pop("id", f"input-{name}")

    if label:
        label_content = [label]
        if required:
            label_content.append(Span(" *", cls="text-accent"))
        content.append(Label(*label_content, for_=input_id, cls="input-label"))

    input_classes = ["input"]
    if error:
        input_classes.append("input-error")

    content.append(
        ft_hx('input',
            type=type,
            name=name,
            id=input_id,
            placeholder=placeholder,
            required=required if required else None,
            cls=" ".join(input_classes),
            **kwargs
        )
    )

    if helper and not error:
        content.append(Span(helper, cls="input-helper"))
    if error:
        content.append(Span(error, cls="input-error-text"))

    return Div(*content, cls="input-group")


def Textarea(
    name: str,
    label: str = None,
    placeholder: str = "",
    required: bool = False,
    rows: int = 4,
    **kwargs
):
    """Textarea con label"""
    content = []

    textarea_id = kwargs.pop("id", f"textarea-{name}")

    if label:
        label_content = [label]
        if required:
            label_content.append(Span(" *", cls="text-accent"))
        content.append(Label(*label_content, for_=textarea_id, cls="input-label"))

    content.append(
        ft_hx('textarea',
            name=name,
            id=textarea_id,
            placeholder=placeholder,
            required=required if required else None,
            rows=rows,
            cls="input textarea",
            **kwargs
        )
    )

    return Div(*content, cls="input-group")


def Select(
    name: str,
    options: list,
    label: str = None,
    placeholder: str = "Selecciona una opción",
    required: bool = False,
    **kwargs
):
    """Select dropdown"""
    content = []

    select_id = kwargs.pop("id", f"select-{name}")

    if label:
        label_content = [label]
        if required:
            label_content.append(Span(" *", cls="text-accent"))
        content.append(Label(*label_content, for_=select_id, cls="input-label"))

    option_elements = [Option(placeholder, value="", disabled=True, selected=True)]
    for opt in options:
        if isinstance(opt, dict):
            option_elements.append(Option(opt["label"], value=opt["value"]))
        else:
            option_elements.append(Option(opt, value=opt))

    content.append(
        ft_hx('select',
            *option_elements,
            name=name,
            id=select_id,
            required=required if required else None,
            cls="input select",
            **kwargs
        )
    )

    return Div(*content, cls="input-group")


def Checkbox(name: str, label: str, checked: bool = False, **kwargs):
    """Checkbox con label"""
    checkbox_id = kwargs.pop("id", f"checkbox-{name}")

    return Div(
        ft_hx('input',
            type="checkbox",
            name=name,
            id=checkbox_id,
            checked=checked if checked else None,
            cls="checkbox",
            **kwargs
        ),
        Label(label, for_=checkbox_id, cls="checkbox-label"),
        cls="checkbox-group"
    )


# ============================================================================
# BADGES & TAGS
# ============================================================================

def Badge(text: str, variant: str = "default", **kwargs):
    """Badge/tag component"""
    return Span(text, cls=f"badge badge-{variant}", **kwargs)


def Tag(text: str, removable: bool = False, **kwargs):
    """Tag component"""
    content = [Span(text)]
    if removable:
        content.append(Button_(I(cls="icon icon-x"), cls="tag-remove"))
    return Span(*content, cls="tag", **kwargs)


# ============================================================================
# ACCORDION
# ============================================================================

def Accordion(*items, **kwargs):
    """Container para accordion items"""
    return Div(*items, cls="accordion", x_data="{ activeItem: null }", **kwargs)


def AccordionItem(title: str, content: str, index: int = 0, **kwargs):
    """Item individual del accordion"""
    return Div(
        Button_(
            Span(title, cls="accordion-title"),
            I(cls="icon icon-chevron-down accordion-icon"),
            cls="accordion-trigger",
            x_on_click=f"activeItem = activeItem === {index} ? null : {index}",
            aria_expanded=f"activeItem === {index}",
            x_bind_aria_expanded=f"activeItem === {index}"
        ),
        Div(
            Div(P(content), cls="accordion-content-inner"),
            cls="accordion-content",
            x_show=f"activeItem === {index}",
            x_collapse=True
        ),
        cls="accordion-item",
        **kwargs
    )


# ============================================================================
# SECTION COMPONENTS
# ============================================================================

def Section(*content, id: str = None, variant: str = "default", **kwargs):
    """Wrapper de sección con estilos"""
    classes = ["section", f"section-{variant}"]
    extra_cls = kwargs.pop("cls", "")
    if extra_cls:
        classes.append(extra_cls)

    return ft_hx('section',
        Div(*content, cls="container"),
        id=id,
        cls=" ".join(classes),
        **kwargs
    )


def SectionHeader(
    title: str,
    subtitle: str = None,
    badge: str = None,
    centered: bool = True,
    **kwargs
):
    """Header de sección con título y subtítulo"""
    content = []

    if badge:
        content.append(Badge(badge, variant="primary"))

    content.append(H2(title, cls="section-title"))

    if subtitle:
        content.append(P(subtitle, cls="section-subtitle"))

    classes = ["section-header"]
    if centered:
        classes.append("text-center")

    return Div(*content, cls=" ".join(classes), **kwargs)


# ============================================================================
# UTILITY COMPONENTS
# ============================================================================

def Divider(variant: str = "default", **kwargs):
    """Línea divisoria"""
    return Hr(cls=f"divider divider-{variant}", **kwargs)


def Spacer(size: str = "md", **kwargs):
    """Espacio vertical"""
    return Div(cls=f"spacer spacer-{size}", **kwargs)


def Icon(name: str, size: str = "md", **kwargs):
    """Icono wrapper"""
    return I(cls=f"icon icon-{name} icon-{size}", **kwargs)


def Logo(variant: str = "default", **kwargs):
    """Logo de Komercia"""
    return Div(
        Span("Komercia", cls="logo-text"),
        cls=f"logo logo-{variant}",
        **kwargs
    )


def LoadingSpinner(size: str = "md", **kwargs):
    """Spinner de carga"""
    return Div(
        Div(cls="spinner-circle"),
        cls=f"spinner spinner-{size}",
        **kwargs
    )
