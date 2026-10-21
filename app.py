import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="EU–Argentina Offtake Radar", layout="wide")

# Lista oficial definitiva con los 8 proyectos de cobre de Argentina
def obtener_datos_oficiales():
    return pd.DataFrame([
        {
            "ID_Proyecto": "PROJ-001",
            "Nombre_Proyecto": "Josemaría (Vicuña)",
            "Empresa_Contraparte": "Vicuña JV (BHP / Lundin Mining)",
            "Sector": "Minería",
            "Commodity": "Cobre / Oro / Plata",
            "Estado": "Construction & Production",
            "Volumen_tn_anio": 0.0,
            "Responsable": "Equipo Comercial",
            "Notas": "RIGI aprobado; avanzando en infraestructura y permisos.",
            "Proxima_Accion": "Revisar acuerdos de off-take"
        },
        {
            "ID_Proyecto": "PROJ-002",
            "Nombre_Proyecto": "Filo del Sol (Vicuña)",
            "Empresa_Contraparte": "Vicuña JV (BHP / Lundin Mining)",
            "Sector": "Minería",
            "Commodity": "Cobre / Oro / Plata",
            "Estado": "Factibilized",
            "Volumen_tn_anio": 0.0,
            "Responsable": "Equipo Comercial",
            "Notas": "PFS avanzado / integración con distrito Vicuña.",
            "Proxima_Accion": "Monitorear avances de ingeniería"
        },
        {
            "ID_Proyecto": "PROJ-003",
            "Nombre_Proyecto": "El Pachón",
            "Empresa_Contraparte": "Glencore Plc",
            "Sector": "Minería",
            "Commodity": "Cobre / Molibdeno / Plata",
            "Estado": "Factibilized",
            "Volumen_tn_anio": 280000.0,
            "Responsable": "Equipo Comercial",
            "Notas": "CAPEX > US$ 5.0B; abiertos a estructurar acuerdos comerciales.",
            "Proxima_Accion": "Contacto inicial con contraparte"
        },
        {
            "ID_Proyecto": "PROJ-004",
            "Nombre_Proyecto": "MARA (Agua Rica)",
            "Empresa_Contraparte": "Glencore Plc",
            "Sector": "Minería",
            "Commodity": "Cobre / Oro / Plata / Molibdeno",
            "Estado": "Factibilized",
            "Volumen_tn_anio": 168500.0,
            "Responsable": "Equipo Comercial",
            "Notas": "Sinergia operativa con infraestructura existente de Alumbrera.",
            "Proxima_Accion": "Evaluar sinergias logísticas"
        },
        {
            "ID_Proyecto": "PROJ-005",
            "Nombre_Proyecto": "Taca Taca",
            "Empresa_Contraparte": "First Quantum Minerals (FQM)",
            "Sector": "Minería",
            "Commodity": "Cobre / Oro / Molibdeno",
            "Estado": "Factibilized",
            "Volumen_tn_anio": 0.0,
            "Responsable": "Equipo Comercial",
            "Notas": "DFS completado en Salta. Gran escala de recursos.",
            "Proxima_Accion": "Revisión de off-take de concentrados"
        },
        {
            "ID_Proyecto": "PROJ-006",
            "Nombre_Proyecto": "Los Azules",
            "Empresa_Contraparte": "McEwen Copper",
            "Sector": "Minería",
            "Commodity": "Cobre / Oro / Plata",
            "Estado": "Factibilized",
            "Volumen_tn_anio": 0.0,
            "Responsable": "Equipo Comercial",
            "Notas": "PFS avanzado en San Juan; atado a infraestructura eléctrica.",
            "Proxima_Accion": "Seguimiento de financiamiento"
        },
        {
            "ID_Proyecto": "PROJ-007",
            "Nombre_Proyecto": "San Jorge / Cobre Mendocino",
            "Empresa_Contraparte": "Zonda Metals / Solway",
            "Sector": "Minería",
            "Commodity": "Cobre / Oro",
            "Estado": "Greenfield",
            "Volumen_tn_anio": 0.0,
            "Responsable": "Equipo Comercial",
            "Notas": "En revisión de permisos y actualización de PFS en Mendoza.",
            "Proxima_Accion": "Actualizar estatus regulatorio"
        },
        {
            "ID_Proyecto": "PROJ-008",
            "Nombre_Proyecto": "Altar",
            "Empresa_Contraparte": "Aldebaran Resources",
            "Sector": "Minería",
            "Commodity": "Cobre / Oro",
            "Estado": "Greenfield",
            "Volumen_tn_anio": 0.0,
            "Responsable": "Equipo Comercial",
            "Notas": "Exploración avanzada en la Cordillera de San Juan.",
            "Proxima_Accion": "Monitorear resultados de perforación"
        }
    ])

# Inicializar estado en memoria de la sesión
if "df_proyectos" not in st.session_state:
    st.session_state.df_proyectos = obtener_datos_oficiales()

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

if menu == "Gestión de Proyectos (CRM)":
    st.header("📋 Base de Datos y CRM de Proyectos Mineros")
    st.markdown("Edita la tabla directamente o agrega nuevos proyectos utilizando los campos personalizados.")

    # Botón para restablecer datos si es necesario
    if st.sidebar.button("🔄 Recargar Base de Datos"):
        st.session_state.df_proyectos = obtener_datos_oficiales()
        st.rerun()

    # Formulario para agregar un proyecto nuevo
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
                    nuevo_id = f"PROJ-{len(st.session_state.df_proyectos) + 1:03d}"
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
                    st.session_state.df_proyectos = pd.concat([st.session_state.df_proyectos, nueva_fila], ignore_index=True)
                    st.success(f"¡Proyecto '{nuevo_nombre}' agregado con éxito!")
                    st.rerun()
                else:
                    st.warning("Por lo menos ingresa el Nombre del Proyecto.")

    # Editor de datos interactivo
    st.subheader("Modificar / Actualizar Proyectos Registrados")
    edited_df = st.data_editor(st.session_state.df_proyectos, num_rows="dynamic", use_container_width=True, key="editor_proyectos")
    
    # Actualizamos el estado con lo editado en la tabla
    st.session_state.df_proyectos = edited_df

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

