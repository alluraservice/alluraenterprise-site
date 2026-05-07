import webbrowser

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.title = "Allura Enterprise"

# --- 1. CSS ANIMATIONS & RESPONSIVENESS ---
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            .hover-element {
                transition: transform 0.3s ease, box-shadow 0.3s ease !important;
                cursor: pointer;
            }
            .hover-element:hover {
                transform: scale(1.05);
                box-shadow: 0px 12px 20px rgba(0,0,0,0.3) !important;
            }
            .hover-card {
                transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                cursor: pointer;
            }
            .hover-card:hover {
                transform: scale(1.03);
                z-index: 5;
            }

            /* --- MOBILE FIXES --- */
            @media (max-width: 768px) {
                .top-bar { display: none !important; } /* Hide green top bar on mobile */
                
                .nav-bar { 
                    padding: 10px 20px !important; 
                    flex-direction: column !important;
                    height: auto !important;
                }
                
                .nav-links { 
                    margin: 15px 0 !important; 
                    text-align: center;
                    font-size: 14px;
                }

                .hero-text {
                    font-size: 32px !important; /* Smaller headline for mobile */
                    text-align: center;
                }

                .hero-container {
                    padding: 60px 20px !important;
                    text-align: center;
                }

                .footer-col {
                    margin-bottom: 40px;
                    text-align: center;
                }
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# --- 2. STYLE DEFINITIONS ---
HEADER_STYLE = {"position": "sticky", "top": "0", "zIndex": "1000", "width": "100%"}

TOP_BAR_STYLE = {
    "backgroundColor": "#008a44", 
    "color": "white",
    "fontSize": "13px",
    "padding": "10px 80px",
    "display": "flex",
    "justifyContent": "flex-end",
    "gap": "30px",
}

NAV_BAR_STYLE = {
    "backgroundColor": "white",
    "padding": "15px 80px",
    "display": "flex",
    "alignItems": "center",
    "justifyContent": "space-between",
    "boxShadow": "0px 2px 10px rgba(0,0,0,0.05)"
}

BUTTON_SHADOW = {
    "borderRadius": "30px",
    "padding": "10px 25px",
    "fontWeight": "500",
    "boxShadow": "0px 4px 8px rgba(0,0,0,0.2)",
    "border": "none",
    "color": "white"
}

FOOTER_STYLE = {
    "backgroundColor": "#6d6e71", 
    "color": "white",
    "padding": "60px 80px",
    "fontSize": "14px"
}

FOOTER_HEADING = {
    "color": "#a8e0c1", 
    "fontWeight": "400",
    "fontSize": "28px",
    "marginBottom": "25px"
}

# --- 3. HELPER FOR CARDS ---
def create_styled_card(title, img_name, tint_class):
    if tint_class == "green":
        img_filter = "grayscale(100%) sepia(70%) hue-rotate(90deg) saturate(130%) brightness(0.6)"
        overlay_bg = "rgba(0, 60, 30, 0.3)" 
    else:
        img_filter = "grayscale(100%) brightness(0.5)"
        overlay_bg = "rgba(0, 0, 0, 0.3)"

    return html.Div([
        html.Div([
            html.Img(
                src=app.get_asset_url(img_name), 
                style={
                    "width": "100%", "height": "350px", "objectFit": "cover", 
                    "filter": img_filter, "borderRadius": "20px"
                }
            ),
            html.Div([
                html.H3(title, style={
                    "color": "white", "fontWeight": "bold", "textAlign": "center",
                    "textTransform": "uppercase", "letterSpacing": "2px", "margin": "0"
                })
            ], style={
                "position": "absolute", "top": "0", "left": "0", "width": "100%", "height": "100%",
                "display": "flex", "alignItems": "center", "justifyContent": "center",
                "backgroundColor": overlay_bg, "borderRadius": "20px", "padding": "20px"
            })
        ], className="hover-card", style={
            "borderRadius": "20px", "overflow": "hidden", "position": "relative", 
            "boxShadow": "0px 10px 20px rgba(0,0,0,0.15)"
        })
    ], className="mb-5")

# --- 4. APP LAYOUT ---
app.layout = html.Div([

    # Header
    html.Div([
        html.Div([
            html.Span("📍 BGC, Taguig City, Philippines"),
            html.Span("📞 +63 917 770 1820"),
            html.Span("✉️ info@alluraenterpriseph.com"),
        ], style=TOP_BAR_STYLE),
        html.Div([
            html.Img(src=app.get_asset_url('1_logo.jpg'), style={"height": "70px"}),
            html.Div([
                dcc.Link("Home", href="/", style={"margin": "0 15px", "color": "#333", "textDecoration": "none"}),
                dcc.Link("About Us", href="/", style={"margin": "0 15px", "color": "#333", "textDecoration": "none"}),
                html.Span("Products ⌄", style={"margin": "0 15px", "cursor": "pointer"}),
                html.Span("Services ⌄", style={"margin": "0 15px", "cursor": "pointer"}),
                dcc.Link("Contact Us", href="/", style={"margin": "0 15px", "color": "#333", "textDecoration": "none"}),
            ], style={"fontWeight": "600"}),
            html.Div([
                dbc.Button("Request a Quote", className="hover-element me-3", 
                           style={**BUTTON_SHADOW, "backgroundColor": "#005a2b"}),
                dbc.Button("Service Request", className="hover-element", 
                           style={**BUTTON_SHADOW, "backgroundColor": "#444"}),
            ])
        ], style=NAV_BAR_STYLE)
    ], style=HEADER_STYLE),

    # Hero
    html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1(["Precision Equipment.", html.Br(), "Unfailing Power.", html.Br(), 
                             html.Span("Protecting Lives.", style={"color": "#008a44"})], 
                            style={"fontSize": "65px", "fontWeight": "800", "lineHeight": "1.1"}),
                    dbc.Button("Browse Catalog", className="hover-element mt-4", size="lg", 
                               style={**BUTTON_SHADOW, "backgroundColor": "#008a44"})
                ], width=7)
            ])
        ], style={"padding": "120px 0"})
    ], style={
        "backgroundImage": "linear-gradient(to right, rgba(255,255,255,1) 0%, rgba(255,255,255,0) 100%), url('/assets/2_coverphoto03.jpg')",
        "backgroundSize": "cover", "backgroundPosition": "center"
    }),

    # Products & Services
    dbc.Container([
        html.H2("Explore our Products", className="mt-5 mb-5", style={"fontWeight": "bold", "textAlign": "center"}),
        dbc.Row([
            dbc.Col(create_styled_card("Medical Equipment", "3_medicalequipment.jpeg", "green"), width=4),
            dbc.Col(create_styled_card("Hospital Supplies", "4_hospitalsupplies.jpeg", "green"), width=4),
            dbc.Col(create_styled_card("Power Protection", "5_powerprotection.jpeg", "green"), width=4),
        ]),
        html.H2("Explore our Services", className="mt-5 mb-5", style={"fontWeight": "bold", "textAlign": "center"}),
        dbc.Row([
            dbc.Col(create_styled_card("Technical Support", "6_technicalsupport.webp", "grey"), width=4),
            dbc.Col(create_styled_card("Power Services", "7_powerservices.jpg", "grey"), width=4),
            dbc.Col(create_styled_card("Electrical Services", "8_electricalservices.jpeg", "grey"), width=4),
        ])
    ], className="mb-5"),

    # LATEST NEWS SECTION
    dbc.Container([
        html.H2("Latest News", className="mb-4", style={"fontWeight": "bold"}),
        dbc.Card([
            dbc.Row([
                dbc.Col(html.Img(src=app.get_asset_url('5_powerprotection.jpeg'), 
                                 style={"width":"100%","height":"100%","objectFit":"cover", "filter":"grayscale(100%)"}), width=4),
                dbc.Col(dbc.CardBody([
                    html.P("April 18, 2026", className="text-muted"),
                    html.H4("M90Ci-6S vs Eaton BladeUPS | 400V Modular UPS Replacement", style={"fontWeight":"bold"}),
                    html.P("The Xtreme Power X90-1S is a compact, integrated 480V three-phase UPS platform designed for critical infrastructure where space, deployment simplicity, and service access are key..."),
                    dcc.Link("Read More →", href="#", style={"color":"#008a44", "textDecoration":"none", "fontWeight":"bold"})
                ]), width=8)
            ], align="center")
        ], className="hover-card", style={"borderRadius": "20px", "overflow": "hidden", "border": "none", "boxShadow": "0px 10px 30px rgba(0,0,0,0.05)"})
    ], className="my-5 pb-5"),

    # FOOTER
    html.Footer([
        dbc.Row([
            dbc.Col([
                html.H2("About Us", style=FOOTER_HEADING),
                html.P("ALLURA ENTERPRISE stands as a trusted leader in the distribution and supply of high-quality Medical Equipment, Medical Supplies, and Power Protection solutions for both medical and industrial sectors. Since its inception in 2014, Allura Enterprise has been committed to upholding the highest standards of safety, reliability, and operational excellence, ensuring seamless installation and continuous support for every client.",
                       style={"lineHeight": "1.6"})
            ], width=3),
            dbc.Col([
                html.H2("Contact Us", style=FOOTER_HEADING),
                html.P([
                    html.B("Main Office: "), "Doña Paz Village, Cruzada, Legazpi City", html.Br(), html.Br(),
                    html.B("Satellite Office: "), "Villa Angelina Phase 1, Mambog 4, Bacoor Cavite", html.Br(), html.Br(),
                    html.B("Contact: "), "+63 917 770 1820", html.Br(), html.Br(),
                    html.B("Email: "), "allura.enterprise@gmail.com"
                ])
            ], width=3),
            dbc.Col([
                html.H2("Quick Links", style=FOOTER_HEADING),
                html.Div([html.P(link) for link in ["Home", "About Us", "Products", "Services", "Contact Us"]])
            ], width=3),
            dbc.Col([
                html.H2("Allura Legal", style=FOOTER_HEADING),
                html.Div([html.P("Terms and Conditions"), html.P("Privacy Policy")])
            ], width=3),
        ])
    ], style=FOOTER_STYLE)
])

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050', autoraise=True)
    app.run()