# Detección de manos (proyecto)

Pequeña aplicación que usa la cámara para detectar dedos/manos y reproducir sonidos cuando determinados dedos se pliegan. Implementación principal en `final_count.py`.

Requisitos
- Python 3.8+
- Cámara conectada y permisos de cámara

Instalación

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Ejecución

```bash
python final_count.py
```

Notas
- Si la cámara no es `0`, ajuste `cv2.VideoCapture(0)` en `final_count.py`.
- En Windows puede que `pygame.mixer` requiera códecs o configuraciones de audio específicos.
- Los archivos `.wav` necesarios están en la raíz (ej. `#fa.WAV`, `la.WAV`, `re.WAV`, etc.). Los nombres deben coincidir exactamente con los referenciados en `final_count.py`.

Contribuir
- Para PRs que cambien dependencias, actualiza `requirements.txt` (no renombres `requeriments.txt` sin justificar).

