# Hamburguesas IT - Sistema de Gestión de Ventas

Bienvenido a **Hamburguesas IT**, un programa sencillo pero efectivo para gestionar las ventas y operaciones básicas de un restaurante de hamburguesas. Este script permite:

- Registrar nuevos pedidos de los clientes.
- Calcular el total de cada pedido.
- Gestionar pagos y calcular el vuelto.
- Confirmar o cancelar pedidos con mensajes personalizados.
- Registrar los ingresos y salidas de turno de los encargados.
- Almacenar los registros de ventas y actividades en archivos de texto.

## Características

- **Interfaz interactiva**: El programa guía al usuario mediante entradas y validaciones para asegurar que solo se ingresen datos válidos.
- **Registro de ventas**: Los detalles de cada pedido se guardan en `ventas.txt` para su posterior revisión.
- **Registro de actividades**: Se almacena la hora y fecha de ingreso y salida del encargado en `registro.txt`.
- **Control de caja**: Calcula automáticamente la caja total al finalizar el turno.

## Requisitos

- **Python 3.x**: Asegúrate de tener instalado Python 3.x en tu sistema.
- **Conocimientos básicos**: Es recomendable tener familiaridad con cómo ejecutar scripts en la terminal o línea de comandos.

## Uso

1. **Clona este repositorio** en tu máquina local:

   ```bash
   git clone https://github.com/franragona/hamburguesas-it.git
2. **Ejecuta el script** en la terminal:

   ```bash
   python hamburguesas_it.py
   ```

3. **Interacciones en el programa**:
   - Ingresa tu nombre como encargado y comienza tu turno.
   - Registra nuevos pedidos, selecciona opciones, y gestiona los pagos.
   - Cambia de turno o apaga el sistema cuando sea necesario.
   - Los mensajes te guiarán en cada paso, asegurando una experiencia de usuario divertida (¡y a veces un poco sarcástica!).

## Funciones Principales

- `solo_letras(mensaje)`: Valida que el usuario ingrese solo letras.
- `solo_numeros(mensaje)`: Valida que el usuario ingrese solo números.
- `pedido()`: Gestiona un nuevo pedido, calcula el total y almacena los datos en `ventas.txt`.
- `ingreso()`: Registra el inicio de turno del encargado.
- `salida()`: Registra el fin de turno y el total de la caja.

## Archivos Generados

- **ventas.txt**: Guarda los registros de cada venta realizada.
- **registro.txt**: Almacena las entradas y salidas de turno, así como el total de la caja.

## Nota Importante

Este programa está diseñado con un toque de humor. Los mensajes de error y algunas confirmaciones son sarcásticas y pueden no ser adecuados para todos los entornos. Puedes modificar los mensajes en el código si prefieres un tono más formal.
