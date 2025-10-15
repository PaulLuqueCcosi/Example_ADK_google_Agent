# Agentes Google ADK - Proyecto de Demostración

Este repositorio contiene ejemplos de agentes desarrollados con el **Google Agent Development Kit (ADK)**, un framework para crear agentes de IA conversacionales con herramientas personalizadas.

## Inicio Rápido

### Configuración paso a paso (después de descargar el repositorio)

#### 1. Navegar al directorio del proyecto
```bash
cd agentes-google-adk
```

#### 2. Crear entorno virtual

**En Windows:**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

#### 4. Configurar API Key de Google

**Paso 4.1: Obtener la API Key**
- Ve a [Google AI Studio](https://aistudio.google.com/app/api-keys)
- Inicia sesión y crea una nueva API Key
- Copia la API Key generada

**Paso 4.2: Configurar archivo .env**

**En Windows:**
```cmd
copy .env.example .env
notepad .env
```

**En macOS/Linux:**
```bash
cp .env.example .env
nano .env
```

**Paso 4.3: Editar el archivo .env**
Reemplaza `tu_api_key_aqui` con tu API Key real:
```env
GOOGLE_API_KEY=AIzaSy...tu_api_key_real_aqui
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

#### 5. Verificar instalación
```bash
adk --version
```

#### 6. Ejecutar la interfaz web
```bash
adk web
```

¡Listo! Ahora puedes interactuar con los agentes desde tu navegador.

## ¿Qué es Google ADK?

Google ADK (Agent Development Kit) es un framework flexible y modular para desarrollar e implementar agentes de IA. Aunque está optimizado para Gemini y el ecosistema de Google, ADK es agnóstico al modelo, agnóstico al despliegue, y está construido para ser compatible con otros frameworks.

**Características principales:**
- Interactuar de forma conversacional con usuarios
- Utilizar herramientas y funciones personalizadas
- Integrarse con servicios de Google Cloud
- Ejecutarse tanto localmente como en la nube
- Desarrollo modular y escalable

## Estructura del Proyecto

```
├── local_agent/          # Agente con contexto geográfico (Puno, Perú)
│   └── .env             # Variables de entorno (API key)
├── local_agent_2/        # Agente con contexto geográfico (Arequipa, Perú)
│   └── .env             # Variables de entorno (API key)
├── multi_tool_agent/     # Agente con múltiples herramientas (clima y hora)
│   └── .env             # Variables de entorno (API key)
├── .env.example          # Plantilla para configurar variables de entorno
├── requirements.txt      # Dependencias del proyecto
└── README.md            # Este archivo
```

## Agentes Incluidos

### 1. Local Agent (Puno)
- **Ubicación**: `local_agent/`
- **Funcionalidad**: Agente consciente del contexto geográfico ubicado en Puno, Perú
- **Herramientas**: 
  - `get_user_location()`: Obtiene la ubicación del usuario (Puno)
- **Modelo**: Gemini 2.0 Flash

### 2. Local Agent 2 (Arequipa)
- **Ubicación**: `local_agent_2/`
- **Funcionalidad**: Agente consciente del contexto geográfico ubicado en Arequipa, Perú
- **Herramientas**: 
  - `get_user_location()`: Obtiene la ubicación del usuario (Arequipa)
- **Modelo**: Gemini 2.0 Flash

### 3. Multi Tool Agent
- **Ubicación**: `multi_tool_agent/`
- **Funcionalidad**: Agente con múltiples herramientas para consultas de clima y hora
- **Herramientas**: 
  - `get_weather(city)`: Obtiene el clima de una ciudad (actualmente solo Nueva York)
  - `get_current_time(city)`: Obtiene la hora actual de una ciudad
- **Modelo**: Gemini 2.0 Flash

## Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- Cuenta de Google Cloud con acceso a Vertex AI
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-proyecto>
   ```

2. **Crear entorno virtual (recomendado)**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # En Windows
   # source .venv/bin/activate  # En Linux/Mac
   ```

3. **Instalar Google ADK y dependencias**
   
   **Opción 1: Instalación directa de ADK (recomendada)**
   ```bash
   pip install google-adk
   ```
   
   **Opción 2: Usar requirements.txt (incluye todas las dependencias del proyecto)**
   ```bash
   pip install -r requirements.txt
   ```
   
   > **Nota**: El archivo `requirements.txt` ya incluye `google-adk==1.16.0` y todas las dependencias necesarias para este proyecto.

4. **Verificar la instalación**
   ```bash
   adk --version
   ```

5. **Configurar la API Key de Google**
   
   **⚠️ IMPORTANTE**: Necesitas una API key de Google para usar los agentes.
   
   a) **Obtener la API Key:**
   - Ve a [Google AI Studio](https://aistudio.google.com/app/api-keys)
   - Inicia sesión con tu cuenta de Google
   - Haz clic en "Create API Key"
   - Copia la API key generada
   
   b) **Configurar el archivo .env:**
   ```bash
   # Copia el archivo de ejemplo
   cp .env.example .env
   
   # Edita el archivo .env y reemplaza 'tu_api_key_aqui' con tu API key real
   ```
   
   c) **Estructura del archivo .env:**
   ```env
   GOOGLE_API_KEY=tu_api_key_real_aqui
   GOOGLE_GENAI_USE_VERTEXAI=FALSE
   ```
   
   > **Nota de Seguridad**: Nunca compartas tu API key públicamente. El archivo `.env` está incluido en `.gitignore` para evitar subirlo accidentalmente al repositorio.

## Uso

### Ejecutar con Interfaz Web

Para probar e interactuar con los agentes, utiliza la interfaz web proporcionada por ADK:

```bash
adk web
```

Este comando iniciará una interfaz web donde podrás:
- Seleccionar diferentes agentes
- Interactuar con ellos mediante chat
- Probar las herramientas disponibles
- Ver los logs y respuestas en tiempo real

### Ejecutar Agentes Individuales

También puedes ejecutar cada agente por separado navegando a su carpeta correspondiente.

## Documentación Adicional

Para más información sobre el desarrollo con Google ADK:

- **Documentación Oficial**: [Google ADK Documentation](https://google.github.io/adk-docs/)
- **Guía de Inicio con Python**: [Get Started with Python](https://google.github.io/adk-docs/get-started/python/)
- **Documentación de Agentes**: [Agents Documentation](https://google.github.io/adk-docs/agents/)
- **Instalación y Configuración**: [Installation Guide](https://google.github.io/adk-docs/)

## Características de los Agentes

### Agentes de Contexto Geográfico
Los agentes `local_agent` y `local_agent_2` demuestran cómo crear agentes conscientes de la ubicación que pueden:
- Obtener información geográfica del usuario
- Responder de manera contextualmente apropiada según la ubicación
- Proporcionar información relevante sobre cultura local, clima, zona horaria, etc.

### Agente Multi-herramienta
El `multi_tool_agent` muestra cómo integrar múltiples herramientas en un solo agente para:
- Consultar información meteorológica
- Obtener la hora actual en diferentes ciudades
- Manejar errores cuando la información no está disponible

## Desarrollo y Personalización

Para crear tus propios agentes:

1. Crea una nueva carpeta para tu agente
2. Define las herramientas (funciones) que necesitas
3. Configura el agente con `Agent()` especificando:
   - Nombre y descripción
   - Modelo a utilizar
   - Instrucciones de comportamiento
   - Lista de herramientas disponibles
