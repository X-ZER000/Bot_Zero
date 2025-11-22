Nombre del Proyecto
ZeroBot – v1.0.0

Bot inicial desarrollado para Discord. Esta es la primera versión funcional del proyecto, creada como base para futuras expansiones más avanzadas. Incluye comandos básicos, sistema de retos y el primer diseño del sistema Boss.

Características (v1.0.0)
-Sistema de retos semanales
Comando ¡retosemanal para publicar un reto aleatorio.
Retos organizados por categorías: Python, JavaScript, Web, C/C++, IA, Algoritmos y Retos Rápidos.
Se publican en el canal #retos-semanales.

-Sistema Boss (versión básica)
Canal fijo (temporal): #boss
Los usuarios pueden entregar su reto directamente escribiendo un mensaje en el canal.
El bot detecta la entrega y responde automáticamente con un embed simple.
La lógica interna está lista para expansión en la versión 2.

-Prefijo personalizado
Todos los comandos usan el prefijo:
¡

-Tecnologías utilizadas
Python 3.x
Librería: discord.py
Estructura simple dentro de un único archivo principal (main.py o principal.py)

-Cómo ejecutar este bot
Instala las dependencias:
pip install discord
Coloca tu token en:
bot.run("TU_TOKEN_AQUI")

Ejecuta el bot:
python principal.py

-Requisitos
Tener activados en Discord Developer Portal:
Message Content Intent
Server Members Intent
Presence Intent

-El bot debe tener permisos:
Leer mensajes
Escribir mensajes
Enviar embeds
o ser activado como: Administrador (recomendación: unicamente utilizarlo cuando el bot es para uso personal)
Gestionar canales (opcional para v1)

-Notas
Esta es una versión base pensada para crecer.

***La v2.0.0 incluirá:***
-Guardado de entregas
-Sistema de niveles
-Sistema XP
-Perfiles
-Retroalimentación inteligente
-Embeds avanzados
-Arquitectura modular
-Canales extra
-entre otras mejoras
