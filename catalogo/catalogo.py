# ─────────────────────────────────────────────────────────────────────
#  catalogo.py  —  ESTE ES EL TUYO
# ─────────────────────────────────────────────────────────────────────
#
#  Arma tu catálogo (index.html) a partir de la planilla productos.csv.
#  Lo armó el panel de la clase, con una marca en cada función:
#     ✏️  la tuya: la resolviste en la clase y vino tal cual
#     📎  la de la clase: no estaba Resuelta en tu navegador, o viene hecha
#
#  En la terminal, parado en esta carpeta:   python catalogo.py
#  Después abrí index.html con doble clic.
# ─────────────────────────────────────────────────────────────────────

import csv
from urllib.parse import quote

TITULO = "Bambú costuras"

# Tu WhatsApp: 54 + 9 + la característica sin el 0 + el número sin el 15.
NUMERO = "5492215228896"

# La dirección de tu catálogo en el editor, la que te dieron con tu código.
# Con ella, lo que cambies en el editor aparece solo en tu página publicada.
# Vacía, la página muestra solo lo que tiene productos.csv.
CATALOGO = ""


# ✏️ La tuya, del ejercicio "Los productos, desde la planilla".
def leer_productos(ruta):
  productos = []
  # cada fila de la planilla, como diccionario, a la lista
  with open(ruta, encoding="utf-8") as archivo:
    for fila in csv.DictReader(archivo):
        productos.append(fila)
  return productos


# ✏️ La tuya, del ejercicio "El precio, siempre igual".
def precio(texto):
  # "12500"  ->  "$12.500"
  return "$" + f"{int(texto):,}".replace(",", ".")


# ✏️ La tuya, del ejercicio "El botón de WhatsApp".
def link_whatsapp(numero, nombre):
    # el link de wa.me, con el mensaje ya escrito
    texto = quote(f"Hola, quiero consultar por: {nombre}")
    return f"https://wa.me/{numero}?text={texto}"


# ✏️ La tuya, del ejercicio "La foto, o el emoji".
def foto(producto):
  # con foto: <img class="producto__foto" src="fotos/..." alt="...">
  # sin foto: el emoji, como hasta ahora
    
    if producto.get("foto", "")!= "":
        return f'<img class="producto__foto" src="fotos/{producto["foto"]}" alt="{producto["nombre"]}">'
    return f'<div class="producto__foto">{producto["emoji"]}</div>'


# 📎 De la clase: viene hecha.
# Las columnas que ya tienen su lugar en la tarjeta. Todas las demás son datos de más.
BASICAS = ["nombre", "precio", "emoji", "foto", "descripcion"]

def extras(producto):
    otros = {}
    for clave, valor in producto.items():
        if clave not in BASICAS and valor:
            otros[clave] = valor
    return otros


# ✏️ La tuya, del ejercicio "Detalles a tu medida".
def detalles(**datos):
    html = ""
    if datos: 
        html += '<ul class="detalles">'
        for clave, valor in datos.items():
            html += f"<li><strong>{clave.capitalize().replace("_", " ")}:</strong> {valor}</li>"
        html += "</ul>"
    return html


# 📎 De la clase: muestra los datos de más.
def tarjeta(producto, numero):
    return f"""
<article class="producto">
    {foto(producto)}
    <h2>{producto['nombre']}</h2>
    <p class="descripcion">{producto['descripcion']}</p>
    {detalles(**extras(producto))}
    <p class="precio">{precio(producto['precio'])}</p>
    <a class="consultar" href="{link_whatsapp(numero, producto['nombre'])}" target="_blank">Consultar por WhatsApp</a>
</article>
"""


# 📎 De la clase: suma el editor.
def pagina(titulo, productos, numero):
    tarjetas = ""
    for producto in productos:
        tarjetas += tarjeta(producto, numero)
    return f"""<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{titulo}</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header class="encabezado"><h1>{titulo}</h1></header>
    <main class="catalogo">{tarjetas}</main>
    <footer class="contacto">
        <h2>¡Contactá conmigo!</h2>
        <a class="consultar" href="https://wa.me/{numero}" target="_blank">Escribime por WhatsApp</a>
        <p>Tu consulta no es molestia</p>
    </footer>
    <script src="catalogo.js" data-catalogo="{CATALOGO}" data-numero="{numero}"></script>
</body>
</html>
"""


# ✏️ La tuya, del ejercicio "Guardar la página".
def generar(ruta_csv, ruta_html, titulo, numero):
    # 1. leer los productos de la planilla
    productos = leer_productos(ruta_csv)
    # 2. armar la página
    html= pagina(titulo,productos,numero)
    # 3. escribirla en ruta_html
    with open(ruta_html, "w", encoding ="utf-8") as f:
        f.write(html)


generar("productos.csv", "index.html", TITULO, NUMERO)
print("Listo: se generó index.html. Abrilo con doble clic para verlo.")
