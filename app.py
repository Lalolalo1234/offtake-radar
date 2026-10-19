import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="EU–Argentina Offtake Radar", layout="wide")

# --- SISTEMA DE AUTENTICACIÓN SIMPLE ---
def check_password():
    """Retorna True si el usuario ingresó la contraseña correcta."""
    def password_entered():
        if st.session_state["password"] == "prototipo":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("### 🔒 EU–Argentina Offtake Radar")
        st.markdown("Espacio de trabajo interno · Acceso restringido")
        st.text_input("Contraseña de acceso", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.markdown("### 🔒 EU–Argentina Offtake Radar")
        st.text_input("Contraseña de acceso", type="password", on_change=password_entered, key="password")
        st.error("😕 Contraseña incorrecta. Inténtalo de nuevo.")
        return False
    else:
        return True

if not check_password():
    st.stop()

# --- APLICACIÓN PRINCIPAL ---
st.title("🌍 EU–Argentina Offtake Radar - CRM")
st.markdown("Bienvenido al espacio de trabajo interno. Uso exclusivo regulado.")

menu = st.sidebar.selectbox("Secciones", ["Proyectos", "Contratos Offtake", "Empresas", "Pipeline / Seguimiento"])

if menu == "Proyectos":
    st.header("📋 Base de Datos de Proyectos")
    df_proyectos = pd.DataFrame(columns=[
        "ID_Proyecto", "Nombre_Proyecto", "Empresa_Operadora", "País", 
        "Commodity", "Estado", "Capacidad_Anual", "Inicio_Estimado"
    ])
    st.data_editor(df_proyectos, num_rows="dynamic", use_container_width=True)

elif menu == "Contratos Offtake":
    st.header("🤝 Acuerdos de Comercialización (Offtakes)")
    df_offtakes = pd.DataFrame(columns=[
        "ID_Contrato", "ID_Proyecto", "Comprador", "%_Comprometido", 
        "Volumen_Anual", "Fecha_Inicio", "Fecha_Vencimiento", "Estado"
    ])
    st.data_editor(df_offtakes, num_rows="dynamic", use_container_width=True)

elif menu == "Empresas":
    st.header("🏢 Directorio de Empresas y Contrapartes")
    df_empresas = pd.DataFrame(columns=[
        "ID_Empresa", "Nombre", "Tipo_Entidad", "País_Sede", 
        "Sitio_Web", "Compromisos_Sostenibilidad"
    ])
    st.data_editor(df_empresas, num_rows="dynamic", use_container_width=True)

elif menu == "Pipeline / Seguimiento":
    st.header("📈 Seguimiento Comercial e Interacciones")
    df_pipeline = pd.DataFrame(columns=[
        "ID_Interaccion", "Proyecto_Empresa", "Fecha", 
        "Tipo_Interaccion", "Responsable", "Siguientes_Pasos", "Probabilidad"
    ])
    st.data_editor(df_pipeline, num_rows="dynamic", use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.text("Uso interno. La actividad queda registrada.")