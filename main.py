from fasthtml.common import *

app, rt = fast_app(
    pico=False,
    static_path='static',
    hdrs=(
        Link(rel='stylesheet', href='/static/css/styles.css'),
    )
)

@rt('/')
def get():
    return Html(
        Head(
            Title("Komercia - Sistema ERP para Retail"),
            Meta(charset='utf-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1'),
        ),
        Body(
            H1("Komercia"),
            P("Landing page en construcción..."),
        )
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5003))
    serve(port=port)
