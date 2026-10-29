import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="COLACTEOS S.A.S. - Naturalmente Irresistible",
    page_icon="🥛",
    layout="wide",
)

# Estilos CSS avanzados y limpios
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@700&display=swap');

        .stApp {
            background-color: #FDF9F0;
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #2C1810;
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Banner principal corporativo */
        .hero-section {
            background: linear-gradient(rgba(43, 24, 10, 0.85), rgba(92, 58, 33, 0.85)), url('https://images.unsplash.com/photo-1500595046743-cd271d694d30?q=80&w=1200&auto=format&fit=crop');
            background-size: cover;
            background-position: center;
            color: white;
            padding: 80px 50px;
            border-radius: 16px;
            margin-bottom: 40px;
            box-shadow: 0 10px 30px rgba(92, 58, 33, 0.3);
        }

        .hero-title {
            font-family: 'Playfair Display', serif;
            font-size: 44px;
            color: #FFFFFF;
            margin-bottom: 20px;
            line-height: 1.2;
        }

        .hero-desc {
            font-size: 18px;
            color: #F4E8D1;
            max-width: 650px;
            line-height: 1.6;
        }

        /* Tarjetas corporativas entrelazadas */
        .entrelazado-left {
            background-color: #E8F4F1;
            border-radius: 20px 0px 0px 20px;
            padding: 45px;
            color: #2C1810;
            height: 100%;
            box-shadow: 0 6px 20px rgba(0,0,0,0.04);
            border-left: 6px solid #00838F;
        }

        .entrelazado-right {
            background-color: #F5EBE6;
            border-radius: 0px 20px 20px 0px;
            padding: 25px;
            color: #2C1810;
            height: 100%;
            box-shadow: 0 6px 20px rgba(0,0,0,0.04);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .standard-card {
            background-color: #FFFFFF;
            border: 1px solid #E6D5B8;
            border-left: 6px solid #5C3A21;
            padding: 35px;
            border-radius: 12px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.05);
            margin-bottom: 30px;
        }

        .standard-card h3 {
            font-family: 'Playfair Display', serif;
            color: #5C3A21;
            font-size: 24px;
            margin-bottom: 15px;
        }

        /* Estilo retro / pixel-art para la brújula y la huella verde */
        .pixel-retro-card {
            background-color: #FFFDF9;
            border: 4px solid #5C3A21;
            box-shadow: 6px 6px 0px #C49A45;
            padding: 35px;
            border-radius: 4px;
            margin-bottom: 30px;
            color: #2C1810;
        }

        .pixel-retro-card h3 {
            font-family: 'Playfair Display', serif;
            color: #5C3A21;
            font-size: 24px;
            margin-bottom: 15px;
        }

        /* Tarjetas de productos modernas */
        .product-card {
            background: linear-gradient(135deg, #00838F 0%, #004D40 100%);
            border-radius: 14px;
            padding: 30px 20px;
            color: white;
            text-align: center;
            box-shadow: 0 8px 20px rgba(0, 131, 143, 0.25);
            transition: all 0.3s ease;
        }

        .product-card:hover {
            transform: translateY(-8px) scale(1.02);
        }

        .impact-metric {
            background: linear-gradient(135deg, #C49A45 0%, #8C6D48 100%);
            padding: 25px;
            border-radius: 12px;
            color: white;
            text-align: center;
            box-shadow: 0 6px 15px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# ENCABEZADO SUPERIOR CON TEXTO EN NEGRO NÍTIDO Y LOGO
st.markdown(
    """
    <div style="background: linear-gradient(135deg, #F5EBE6 0%, #EEDCC2 100%); padding: 25px 40px; display: flex; align-items: center; justify-content: space-between; border-bottom: 5px solid #C49A45; border-top: 4px solid #5C3A21; box-shadow: 0 6px 20px rgba(0,0,0,0.08); margin: -6rem -6rem 3rem -6rem;">
        <div style="display: flex; align-items: center; gap: 20px;">
""",
    unsafe_allow_html=True,
)

col_logo, col_titulo = st.columns([1, 4])
with col_logo:
  try:
    st.image("logo.png", width=150)
  except:
    st.markdown(
        """
        <div style="background-color: #5C3A21; border: 2px solid #FFD54F; padding: 15px; border-radius: 50%; width: 100px; height: 100px; display: flex; align-items: center; justify-content: center; text-align: center;">
            <span style="color: #FFD54F; font-weight: bold; font-size: 14px;">COLACTEOS</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_titulo:
  st.markdown(
      """
        <div style="text-align: right; padding-top: 10px;">
            <h1 style="color: #2C1810 !important; font-family: 'Playfair Display', serif; font-size: 34px; font-weight: 800; margin: 0; letter-spacing: 1px;">COLACTEOS S.A.S.</h1>
            <p style="color: #5C3A21 !important; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; font-weight: 700; margin-top: 5px;">Naturalmente Irresistible | Guamal, Magdalena</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

st.markdown("</div>", unsafe_allow_html=True)
st.write("")

# BANNER PRINCIPAL (INICIO)
st.markdown(
    """
    <div class="hero-section">
        <div class="hero-title">Lo que viene del campo con sabor artesanal</div>
        <div class="hero-desc">
            Producimos y comercializamos derivados lácteos de la más alta calidad, garantizando frescura, inocuidad y el compromiso absoluto con el desarrollo de nuestra comunidad en Guamal.
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# INDICADOR DE IMPACTO (+50 VENTAS)
st.markdown(
    """
    <div class="impact-metric">
        <h2 style="color: white; font-family: 'Playfair Display', serif; margin: 0; font-size: 32px;">+50 Ventas Exitosas en el Año</h2>
        <p style="margin: 5px 0 0 0; color: #FFF8EE; font-size: 16px;">Con una comunidad 100% satisfecha por el auténtico sabor artesanal.</p>
    </div>
""",
    unsafe_allow_html=True,
)

# SECCIÓN: NUESTRA ESENCIA CORPORATIVA
st.markdown("## Nuestra Esencia Corporativa")

col_q1, col_q2 = st.columns([1.3, 1], gap="small")
with col_q1:
  st.markdown(
      """
        <div class="entrelazado-left">
            <h3 style="font-family: 'Playfair Display', serif; color: #004D40; font-size: 26px; margin-bottom: 15px;">¿Quiénes Somos?</h3>
            <p style="line-height: 1.7; font-size: 16px; color: #2C1810;">Colácteos S.A.S. es una microempresa dedicada a la producción y comercialización de productos derivados de la leche, como yogures, arequipes y postres. Nuestro propósito es ofrecer alimentos frescos, nutritivos, de alta calidad y a precios accesibles mediante procesos rigurosamente estandarizados que garantizan total inocuidad, higiene y bienestar a la comunidad.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )
with col_q2:
  st.markdown(
      """
        <div class="entrelazado-right" style="flex-direction: column; text-align: center;">
    """,
      unsafe_allow_html=True,
  )
  try:
    st.image("Iglesia.png", use_container_width=True)
  except:
    st.markdown(
        """
        <div style="background-color: #E6D5B8; padding: 30px; border-radius: 12px; text-align: center; width: 100%;">
            <h4 style="color: #5C3A21; margin: 0; font-family: 'Playfair Display', serif; font-size: 20px;">Tradición y Calidad</h4>
            <p style="color: #2C1810; font-size: 14px; margin-top: 10px;">El orgullo de producir lo nuestro con amor y dedicación.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
  st.markdown("</div>", unsafe_allow_html=True)

st.write("")

col_mision, col_vision = st.columns(2)
with col_mision:
  st.markdown(
      """
        <div class="standard-card">
            <h3>Misión</h3>
            <p>Ofrecer productos lácteos frescos, nutritivos y de alta calidad, elaborados con ingredientes seleccionados y rigurosos procesos higiénicos, brindando una experiencia satisfactoria a nuestros clientes y aportando al desarrollo de nuestra comunidad.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

with col_vision:
  st.markdown(
      """
        <div class="standard-card">
            <h3>Visión</h3>
            <p>Ser una microempresa reconocida a nivel local y regional por la calidad, frescura y variedad de sus productos lácteos, destacándose por su compromiso con la satisfacción de los clientes, el cuidado del medio ambiente y el apoyo a la economía local.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )


# SECCIÓN: PORTAFOLIO DE PRODUCTOS
st.markdown("## Portafolio de Productos")
st.write(
    "Haz clic en cada producto para desplegar sus detalles artesanales y"
    " conocer más."
)
st.write("")

prod1, prod2, prod3 = st.columns(3)

with prod1:
  st.markdown(
      """
        <div class="product-card">
            <h3 style="color: white; font-family: 'Playfair Display', serif; font-size: 20px;">Yogur de Guanábana</h3>
            <p style="font-size: 14px; color: #E0F2F1;">Presentación: 1 Litro</p>
            <div style="font-size: 26px; font-weight: 800; color: #FFD54F; margin-top: 15px;">$11.500</div>
        </div>
    """,
      unsafe_allow_html=True,
  )
  with st.expander("Ver detalles del Yogur"):
    st.write(
        "Elaborado con pulpa de fruta seleccionada y leche fresca de la"
        " región. Nuestro producto estrella, validado con gran éxito por el"
        " mercado local."
    )

with prod2:
  st.markdown(
      """
        <div class="product-card">
            <h3 style="color: white; font-family: 'Playfair Display', serif; font-size: 20px;">Cheesecake de Coroso</h3>
            <p style="font-size: 14px; color: #E0F2F1;">Postre Tradicional</p>
            <div style="font-size: 26px; font-weight: 800; color: #FFD54F; margin-top: 15px;">$7.000</div>
        </div>
    """,
      unsafe_allow_html=True,
  )
  with st.expander("Ver detalles del Cheesecake"):
    st.write(
        "Un postre artesanal único con el auténtico toque y sabor tradicional"
        " de la región de coroso, logrando una textura suave e irresistible."
    )

with prod3:
  st.markdown(
      """
        <div class="product-card">
            <h3 style="color: white; font-family: 'Playfair Display', serif; font-size: 20px;">Arequipe Tradicional</h3>
            <p style="font-size: 14px; color: #E0F2F1;">Presentación: 500 Gramos</p>
            <div style="font-size: 26px; font-weight: 800; color: #FFD54F; margin-top: 15px;">$7.000</div>
        </div>
    """,
      unsafe_allow_html=True,
  )
  with st.expander("Ver detalles del Arequipe"):
    st.write(
        "Dulce, cremoso y cocinado a fuego lento con leche pura y estándares"
        " artesanales que garantizan su sabor casero inigualable."
    )

st.write("")

# RESEÑAS DE LA COMUNIDAD (CASUALES Y CON TUS NOMBRES)
st.markdown("## Lo que dice nuestra comunidad")
r1, r2, r3, r4, r5 = st.columns(5)

with r1:
  st.markdown(
      """
        <div class="standard-card" style="padding: 20px;">
            <p style="font-style: italic; font-size: 13px;">"Oigan, el yogur de guanábana quedó a otro nivel, súper recomendado."</p>
            <p style="font-weight: bold; color: #5C3A21; margin-top: 8px; font-size: 13px;">— Verónica Arango</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

with r2:
  st.markdown(
      """
        <div class="standard-card" style="padding: 20px;">
            <p style="font-style: italic; font-size: 13px;">"Muy buen producto, se nota que es 100% artesanal y fresco."</p>
            <p style="font-weight: bold; color: #5C3A21; margin-top: 8px; font-size: 13px;">— Alejandro T.A</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

with r3:
  st.markdown(
      """
        <div class="standard-card" style="padding: 20px;">
            <p style="font-style: italic; font-size: 13px;">"El arequipe es una locura, buenísimo para acompañar cualquier postre."</p>
            <p style="font-weight: bold; color: #5C3A21; margin-top: 8px; font-size: 13px;">— Sebastián L.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

with r4:
  st.markdown(
      """
        <div class="standard-card" style="padding: 20px;">
            <p style="font-style: italic; font-size: 13px;">"Excelente servicio y la entrega súper puntual aquí en Guamal."</p>
            <p style="font-weight: bold; color: #5C3A21; margin-top: 8px; font-size: 13px;">— Luis R.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

with r5:
  st.markdown(
      """
        <div class="standard-card" style="padding: 20px;">
            <p style="font-style: italic; font-size: 13px;">"Los postres de coroso son únicos, de verdad que se los recomiendo a todos."</p>
            <p style="font-weight: bold; color: #5C3A21; margin-top: 8px; font-size: 13px;">— José Guerra</p>
        </div>
    """,
      unsafe_allow_html=True,
  )


# SECCIÓN: INVESTIGACIÓN DE MERCADO Y SOSTENIBILIDAD (ESTILO PIXEL-RETRO)
st.markdown("## Investigación de Mercado y Sostenibilidad")

col_inv, col_sust = st.columns(2)

with col_inv:
  st.markdown(
      """
        <div class="pixel-retro-card">
            <h3>Nuestra Brújula hacia la Viabilidad</h3>
            <p>Mediante una investigación aplicada a nuestra comunidad, validamos las preferencias reales:</p>
            <ul>
                <li><b>Demanda asegurada:</b> El 100% de los encuestados consume lácteos y compraría nuestros productos.</li>
                <li><b>Frecuencia:</b> El 55% consume de 1 a 2 veces por semana y el 35% diariamente.</li>
                <li><b>Validación estrella:</b> El 80% aprobó la creación y compra del yogur de guanábana.</li>
            </ul>
        </div>
    """,
      unsafe_allow_html=True,
  )

with col_sust:
  st.markdown(
      """
        <div class="pixel-retro-card">
            <h3>Nuestra Huella es Verde</h3>
            <p>Creemos en un modelo microempresarial comprometido con el medio ambiente:</p>
            <ul>
                <li><b>Insumos locales:</b> Trabajamos con productores de la región, reduciendo la huella de carbono.</li>
                <li><b>Empaques conscientes:</b> Minimizamos el uso de plásticos innecesarios promoviendo la reutilización.</li>
                <li><b>Residuos responsables:</b> Optimizamos procesos artesanales para aprovechar al máximo cada recurso.</li>
            </ul>
        </div>
    """,
      unsafe_allow_html=True,
  )


# PREGUNTAS FRECUENTES (FAQ) AL FINAL DEL TODO
st.markdown("## Preguntas Frecuentes")

with st.expander("¿Cómo puedo realizar un pedido?"):
  st.write(
      "Puedes hacerlo de forma directa haciendo clic en nuestros botones de"
      " WhatsApp o visitando nuestro Instagram oficial."
  )

with st.expander("¿Hacen entregas a domicilio en Guamal?"):
  st.write(
      "Sí, coordinamos las entregas directamente a través de nuestro canal de"
      " atención por WhatsApp para garantizar frescura."
  )

with st.expander("¿Cuáles son los métodos de pago aceptados?"):
  st.write(
      "Aceptamos transferencias bancarias y pagos en efectivo al momento de"
      " recibir tu producto."
  )


# BUZÓN DE PQRS
st.markdown("## Buzón de PQRS y Atención al Cliente")
st.markdown(
    """
    <div class="standard-card">
        <p><b>Estimado usuario:</b> Su opinión es fundamental para seguir creciendo. Si tiene alguna petición, queja, reclamo o sugerencia, por favor diligencie el formulario oficial a continuación. Nuestro equipo le dará respuesta formal en un plazo máximo de 3 a 5 días hábiles.</p>
        <p style="font-size: 13px; color: #666; margin-top: 10px;">Nota: Este sistema cuenta con notificación automática de recepción informativa.</p>
    </div>
""",
    unsafe_allow_html=True,
)

st.components.v1.iframe(
    "https://forms.cloud.microsoft/r/DnBNcDy8jC", height=650, scrolling=True
)


# WIDGET FLOTANTE DE LA VAQUITA (CON EL NUEVO ENLACE DIRECTO)
st.markdown(
    """
    <style>
        .floating-cow-container {
            position: fixed;
            bottom: 25px;
            right: 25px;
            z-index: 99999;
            display: flex;
            flex-direction: column;
            align-items: flex-end;
        }
        .cow-speech-bubble {
            background-color: white;
            border: 2px solid #5C3A21;
            padding: 10px 16px;
            border-radius: 18px;
            font-size: 14px;
            font-weight: 700;
            color: #2C1810;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            margin-bottom: 8px;
        }
        .cow-menu {
            display: none;
            background: white;
            border: 2px solid #C49A45;
            border-radius: 12px;
            padding: 10px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.2);
            margin-bottom: 10px;
            width: 180px;
            text-align: center;
        }
        .floating-cow-container:hover .cow-menu {
            display: block;
        }
        .cow-btn {
            display: block;
            padding: 8px;
            margin: 5px 0;
            border-radius: 6px;
            color: white;
            text-decoration: none;
            font-weight: bold;
            font-size: 13px;
        }
    </style>

    <div class="floating-cow-container">
        <div class="cow-menu">
            <p style="margin: 0 0 5px 0; font-size: 12px; font-weight: bold; color: #5C3A21;">¡Contáctanos!</p>
            <a href="https://wa.me/573117256808?text=Hola,%20deseo%20información%20de%20Colácteos" target="_blank" class="cow-btn" style="background-color: #25D366;">💬 WhatsApp</a>
            <a href="https://www.instagram.com/colacteos_sas/" target="_blank" class="cow-btn" style="background: linear-gradient(45deg, #f09433 0%, #bc1888 100%);">📸 Instagram</a>
        </div>
        <div class="cow-speech-bubble">
            ¡Hola! ¿Te ayudo con algo?
        </div>
        <div style="background: #FFF; border-radius: 50%; padding: 5px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); cursor: pointer; border: 3px solid #5C3A21;">
            <img src="https://i.pinimg.com/736x/e2/0b/a2/e20ba2b7929df19fb60b3396b4538efd.jpg" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover;">
        </div>
    </div>
""",
    unsafe_allow_html=True,
)