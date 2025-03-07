
📌 Trivia Fetch API

🚀 Descripción
Trivia Fetch API es una herramienta de línea de comandos que permite obtener datos curiosos sobre cualquier número, conectándose a la API de NumbersAPI. Además, traduce automáticamente la información al español para una mejor experiencia.

🛠️ Características

✔️ Entrada del usuario: Permite ingresar cualquier número.

✔️ Conexión con API: Obtiene información en tiempo real.

✔️ Procesamiento de JSON: Extrae y organiza los datos.

✔️ Salida en español: Traduce la trivia automáticamente.

✔️ Interfaz simple: Uso intuitivo desde la terminal.

📂 Estructura del proyecto

trivia_fetch_API/

│── trivia.py        # Función para obtener y traducir la trivia

│── main.py          # Interfaz de usuario en línea de comandos

│── test.py          # Pruebas automáticas con pytest

│── README.md        # Documentación del proyecto

▶️ Uso

1️⃣ Ejecuta main.py:
python3 main.py

2️⃣ Ingresa un número cuando se te solicite.

3️⃣ Recibe un dato curioso sobre ese número en español.

🧪 Pruebas
Para validar el correcto funcionamiento, ejecuta:
python3 -m pytest test.py

📌 Requisitos

Python 3

requests y deep-translator (instalar con pip install -r requirements.txt)

📢 ¡Disfruta explorando curiosidades numéricas con Trivia Fetch API! 🚀