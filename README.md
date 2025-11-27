# Mini-X 🐦

Prototipo de red social inspirada en X (ex-Twitter), desarrollada con Django que permite a los usuarios a crear post, interactuar mediante likes y comentarios, y gestionar perfiles.

## 🎯 Problema Resuelto

**Mini-X** se contruye con la finalidad de implementar páginas web como blogs o redes sociales, y como herramienta de productividad empresarial integrandose a plataformas de comunicación entre equipos de trabajo. Además sienta las bases para la creación de una red social más compleja que incluya imágenes, interfaces modernas y otras funcionalidades.El proyecto implementa:

- **Comunicación**: Permite a los usuarios expresar ideas o entregar información
- **Interacción social**: Facilita la conexión entre usuarios a través de un sistema de likes y comentarios
- **Gestión de contenido**: Proporciona herramientas para crear, editar y eliminar publicaciones de manera intuitiva
- **Personalización de perfiles**: Permite a los usuarios crear y customizar sus perfiles con información personal
- **Experiencia de usuario moderna**: Interfaz responsiva y limpia que funciona en dispositivos móviles y desktop

## 🚀 Tecnologías Utilizadas

### Backend
- **Django 5.2.8**: Framework web principal para el desarrollo de la aplicación
- **Python**: Lenguaje de programación base
- **MySQL**: Sistema de gestión de base de datos relacional

### Frontend
- **HTML5**: Estructura de las páginas web
- **CSS3 & Bootstrap 5.3.8**: Diseño responsivo y componentes de interfaz
- **JavaScript**: Interactividad del lado del cliente
- **Font Awesome**: Iconografía moderna

### Herramientas de Desarrollo
- **Django Crispy Forms**: Renderizado avanzado de formularios
- **Crispy Bootstrap5**: Integración de formularios con Bootstrap
- **MySQL Client**: Conector de base de datos

## 🏗️ Enfoque de Desarrollo

### Arquitectura MVC (Model-View-Controller)
El proyecto sigue el patrón arquitectónico **MTV (Model-Template-View)** de Django:

- **Models**: Definición de la estructura de datos (Posts, Comentarios, Perfiles)
- **Views**: Lógica de negocio y procesamiento de requests
- **Templates**: Presentación e interfaz de usuario

### Aplicaciones Modulares
```
mini-x/
├── posts/          # Gestión de publicaciones y comentarios
├── usuarios/       # Autenticación y perfiles de usuario
└── minix_project/ # Configuración principal del proyecto
```

### Características Implementadas

#### Gestión de Usuarios
- Sistema de registro y autenticación
- Perfiles personalizables con biografía
- Redirects inteligentes para completar perfiles

#### Sistema de Posts
- Creación, edición y eliminación de publicaciones
- Límite de 250 caracteres por post
- Timestamps automáticos (creación y actualización)
- Sistema de likes con contadores

#### Sistema de Comentarios
- Comentarios anidados en publicaciones
- Asociación con usuarios y posts

#### Interfaz de Usuario
- Diseño responsivo con Bootstrap 5
- Navegación intuitiva
- Formularios con validación crispy
- Iconografía con Font Awesome

## 📦 Dependencias

### Dependencias Principales
```txt
Django==5.2.8
mysqlclient==2.2.7
django-crispy-forms==2.5
crispy-bootstrap5==2025.6
```

### Dependencias del Sistema
```txt
asgiref==3.11.0
sqlparse==0.5.3
tzdata==2025.2
```

### Requisitos del Sistema
- **Python**: 3.8 o superior
- **MySQL**: 5.7 o superior
- **Pip**: Gestor de paquetes de Python

## 🛠️ Instrucciones de Uso

### 1. Prerrequisitos

Asegúrate de tener instalado:
- Python 3.8+
- MySQL Server
- Git

### 2. Clonación del Repositorio

```bash
git clone https://github.com/jflevig/mini-x.git
cd mini-x
```

### 3. Configuración del Entorno Virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows)
venv\Scripts\activate

# Activar entorno virtual (macOS/Linux)
source venv/bin/activate
```

### 4. Instalación de Dependencias

```bash
pip install -r requirements.txt
```

### 5. Configuración de la Base de Datos

#### 5.1 Crear Base de Datos MySQL
```sql
CREATE SCHEMA `mini-x_db` DEFAULT CHARACTER SET utf8 ;
```

#### 5.2 Configurar Credenciales
Edita `minix_project/settings.py` si es necesario:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mini-x_db',
        'USER': 'root',          # Tu usuario MySQL
        'PASSWORD': '',          # Tu contraseña MySQL
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### 6. Migraciones de Base de Datos

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate
```

### 7. Crear Superusuario (Opcional)

```bash
python manage.py createsuperuser
```

### 8. Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

### 9. Acceso a la Aplicación

#### Usuarios Finales
- **Registro**: `/registro/`
- **Login**: `/login/`
- **Home**: `/` (feed principal)

#### Panel de Administración
- **URL**: `/admin/`
- **Acceso**: Con las credenciales del superusuario

## 📱 Funcionalidades Principales

### Para Usuarios No Autenticados
- ✅ Registro de nueva cuenta
- ✅ Inicio de sesión
- ✅ Visualización del feed público

### Para Usuarios Autenticados
- ✅ Crear nuevos posts (máx. 250 caracteres)
- ✅ Dar/quitar likes a publicaciones
- ✅ Comentar en posts
- ✅ Editar posts propios
- ✅ Eliminar posts propios
- ✅ Gestionar perfil personal
- ✅ Ver perfiles de otros usuarios

### Para Administradores (Panel de Administración)
- ✅ Gestión completa de usuarios
- ✅ Moderación de contenido 
- ✅ Estadísticas de la plataforma

## Configuración de Producción (Render)
Para un entorno de producción, considera:

1. **Variables de Entorno**: 
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['.on.render.com']
   ```

2. **Configuración de la Base de Datos**:
    ```python
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600
        )
    }
   ```

## 👨‍💻 Autor

**jflevig** - [GitHub](https://github.com/jflevig)