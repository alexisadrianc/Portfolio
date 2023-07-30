# Gestión para Academia de Conductores
¡Bienvenido al repositorio del sistema de gestión para una academia de conductores! Este proyecto tiene como objetivo proporcionar una solución completa para administrar y gestionar los procesos de formación de conductores en una academia.

## Descripción del Proyecto
El propósito de este sistema es facilitar la administración de una academia de conductores, simplificando las tareas relacionadas con el registro de estudiantes, seguimiento de su progreso, programación de clases, evaluaciones y más. Algunas características clave del sistema incluyen:

- **Registro de Estudiantes:** Permite registrar a nuevos estudiantes proporcionando su información personal y de contacto.

- **Gestión de Clases:** Facilita la programación y organización de clases para los diferentes niveles de formación.

- **Seguimiento del Progreso:** Realiza un seguimiento del progreso de cada estudiante, registrando sus calificaciones y avances en la formación.

- **Exámenes y Evaluaciones:** Administra y califica exámenes y evaluaciones prácticas y teóricas.

- **Gestión de Instructores:** Permite gestionar la información de los instructores y asignarlos a diferentes clases.

## Guía de Instalación
Para configurar el sistema en su entorno local, siga estos pasos:

1. Clonar el Repositorio: Utilice el siguiente comando para clonar el repositorio en su máquina local:

    >git clone -b web_academy --single-branch https://github.com/alexisadrianc/Portafolio.git
2. Requisitos: Asegúrese de tener instalado Python en su sistema. Se recomienda utilizar Python 3.x.

3. Entorno Virtual (opcional): Es recomendable crear un entorno virtual para este proyecto. Puede utilizar virtualenv para ello:

    >python -m venv venv
    >source venv/bin/activate  # En Windows use "venv\Scripts\activate"
4. Instalar Dependencias: Acceda al directorio del proyecto y ejecute el siguiente comando para instalar las dependencias necesarias:

    >pip install -r requirements.txt
5. Configuración: Revise el archivo de configuración config.py y ajuste los valores según sus necesidades (por ejemplo, configuración de la base de datos).

6. Base de Datos: Configure la base de datos según las opciones elegidas en el paso anterior. Puede utilizar SQLite o cualquier otro motor de base de datos compatible con Python.

7. Ejecutar la Aplicación: Una vez que todo esté configurado, inicie el servidor de desarrollo con el siguiente comando:

    >python app.py
8. Acceso a la Aplicación: Acceda a la aplicación a través de su navegador web en la siguiente dirección: **http://localhost:8000**.

## Licencia
Este proyecto se distribuye bajo la Licencia MIT. Para más detalles, consulte el archivo LICENSE.

Espero que este sistema de gestión para una academia de conductores sea de gran utilidad para simplificar sus procesos y mejorar la experiencia de formación de los estudiantes. Si tiene alguna pregunta o necesita ayuda, no dude en abrir un "issue" o contactar conmigo por medio de email alexis.adrianc@gmail.com.

¡Gracias por utilizar nuestro sistema y contribuir al proyecto!
