import streamlit as st
import pandas as pd
import os

# Configuración de la página
st.set_page_config(page_title="EU–Argentina Offtake Radar", layout="wide")

# Archivo local para persistencia de datos del CRM
CSV_FILE = "proyectos_crm.csv"

def cargar_datos():
    if os.path.exists(CSV_FILE):
        try:
            return pd.read_csv(CSV_FILE)
        except Exception:
            pass
    # DataFrame inicial por defecto si no existe el archivo
    return pd.DataFrame(columns=[
        "ID_Proyecto", "Nombre_Proyecto", "Empresa_Contraparte", "Sector",
        "Commodity", "Estado", "Volumen_tn_anio", "Responsable", "Notas", "Proxima_Accion"
    ])

def guardar_datos(df):
    df.to_csv(CSV_FILE, index=False)

# --- SISTEMA DE AUTENTICACIÓN SIMPLE ---
def check_password():
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
st.title("🌍 EU–Argentina Offtake Radar - CRM Minero")
st.markdown("Espacio de trabajo interno para el seguimiento de proyectos de off-take minero.")

menu = st.sidebar.selectbox("Secciones", ["Gestión de Proyectos (CRM)", "Contratos Offtake", "Directorio de Empresas", "Pipeline / Seguimiento"])

df_proyectos = cargar_datos()

if menu == "Gestión de Proyectos (CRM)":
    st.header("📋 Base de Datos y CRM de Proyectos Mineros")
    st.markdown("Edita la tabla directamente o agrega nuevos proyectos utilizando los campos personalizados.")

    # Formulario rápido para agregar un proyecto nuevo de forma limpia
    with st.expander("➕ Agregar Nuevo Proyecto Minero"):
        with st.form("form_nuevo_proyecto"):
            col1, col2 = st.columns(2)
            with col1:
                nuevo_nombre = st.text_input("Nombre del Proyecto")
                nueva_contraparte = st.text_input("Empresa / Contraparte")
                nuevo_commodity = st.text_input("Commodity (ej. Litio, Cobre)")
                nuevo_estado = st.selectbox("Estado del Proyecto", ["Greenfield", "Brownfield", "Factibilized", "Construction & Production"])
            with col2:
                nuevo_volumen = st.number_input("Volumen (tn/año)", min_value=0.0, format="%.2f")
                nuevo_responsable = st.text_input("Responsable a cargo")
                nueva_proxima = st.text_input("Próxima Acción / Hito")
            
            nuevo_notas = st.text_area("Notas / Bitácora de Seguimiento")
            
            submit_btn = st.form_submit_button("Guardar Proyecto")
            if submit_btn:
                if nuevo_nombre:
                    nuevo_id = f"PROJ-{len(df_proyectos) + 1:03d}"
                    nueva_fila = pd.DataFrame([{
                        "ID_Proyecto": nuevo_id,
                        "Nombre_Proyecto": nuevo_nombre,
                        "Empresa_Contraparte": nueva_contraparte,
                        "Sector": "Minería",
                        "Commodity": nuevo_commodity,
                        "Estado": nuevo_estado,
                        "Volumen_tn_anio": nuevo_volumen,
                        "Responsable": nuevo_responsable,
                        "Notas": nuevo_notas,
                        "Proxima_Accion": nueva_proxima
                    }])
                    df_proyectos = pd.concat([df_proyectos, nueva_fila], ignore_index=True)
                    guardar_datos(df_proyectos)
                    st.success(f"¡Proyecto '{nuevo_nombre}' agregado con éxito!")
                    st.rerun()
                else:
                    st.warning("Por lo menos ingresa el Nombre del Proyecto.")

    # Editor de datos interactivo conectado al archivo CSV
    st.subheader("Modificar / Actualizar Proyectos Registrados")
    edited_df = st.data_editor(df_proyectos, num_rows="dynamic", use_container_width=True, key="editor_proyectos")
    
    if st.button("💾 Guardar Cambios en la Base de Datos"):
        guardar_datos(edited_df)
        st.success("¡Base de datos actualizada y guardada correctamente!")

elif menu == "Contratos Offtake":
    st.header("🤝 Acuerdos de Comercialización (Offtakes)")
    df_offtakes = pd.DataFrame(columns=[
        "ID_Contrato", "ID_Proyecto", "Comprador (UE)", "%_Comprometido", 
        "Volumen_Anual_tn", "Fecha_Inicio", "Fecha_Vencimiento", "Estado"
    ])
    st.data_editor(df_offtakes, num_rows="dynamic", use_container_width=True)

elif menu == "Empresas":
    st.header("🏢 Directorio de Empresas y Contrapartes UE–Argentina")
    df_empresas = pd.DataFrame(columns=[
        "ID_Empresa", "Nombre", "Tipo_Entidad", "País_Sede", 
        "Sitio_Web", "Compromisos_ESG"
    ])
    st.data_editor(df_empresas, num_rows="dynamic", use_container_width=True)

elif menu == "Pipeline / Seguimiento":
    st.header("📈 Seguimiento Comercial e Interacciones")
    df_pipeline = pd.DataFrame(columns=[
        "ID_Interaccion", "Proyecto", "Fecha", 
        "Tipo_Interaccion", "Responsable", "Siguientes_Pasos", "Probabilidad"
    ])
    st.data_editor(df_pipeline, num_rows="dynamic", use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.text("Uso interno. La actividad queda registrada.")