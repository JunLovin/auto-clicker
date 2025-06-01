# 🖱️ Auto Clicker

Un sencillo auto-clicker en Python que simula clics automáticos del mouse usando la librería `pynput`.

## ⚠️ Aviso

Este script está hecho para practicar y aprender Python. No me hago responsable del uso que le puedan dar.

## 🚀 ¿Cómo funciona?

- Presiona la tecla **+** para activar el auto-clicker.
- Presiona la tecla **!** para desactivar el auto-clicker.
- El clicker realiza un clic izquierdo cada **3 segundos** mientras está activo.

## 🛠️ Instalación

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias necesarias:
   ```sh
   pip install pynput
   ```
3. Ejecuta el script:
   ```sh
   python main.py
   ```

## ⚙️ Personalización

Puedes modificar los siguientes valores en `main.py`:

- **Tecla de activación**
   ```python
    ACTIVATE_KEY = KeyCode(char="+")
   ```

Por la tecla que prefieras (por ejemplo, `"a"`, para la tecla A)

- **Tecla de desactivación**
   ```python
    DEACTIVATE_KEY = KeyCode(char="!")
   ```

Por la tecla que prefieras

- **Intervalo entre clics**
   ```python
    time.sleep(3)
   ```

Por el intervalo deseado (por ejemplo, `time.sleep(1)` para un clic cada segundo)

## 📃 Notas

- El script funciona en segundo plano y detecta las teclas globalmente.
- Para detener el script, simplemente cierra la terminal o presiona `Ctrl + C`

## 📜 Licencia

Este programa está bajo la licencia **MIT**, cualquier duda revisar el archivo [LICENSE](LICENSE)