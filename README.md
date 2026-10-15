# Evaluación práctica: pruebas con GitHub Actions

## Objetivo

Configurar un flujo de integración continua para un programa Python desde GitHub. El workflow se ejecutará en la nube de GitHub cuando el repositorio remoto reciba un `push` enviado desde el repositorio local del alumno.

## Proyecto

Este repositorio contiene un conversor de temperaturas entre Celsius y Fahrenheit. El programa valida que la escala sea admitida y que la temperatura no esté por debajo del cero absoluto.

Archivos iniciales:

- `conversor.py`: programa y función de conversión.
- `tests/test_conversor.py`: pruebas automatizadas con `pytest`.
- `requirements-dev.txt`: dependencia necesaria para ejecutar las pruebas.

## Consigna

Crea y configura un workflow de GitHub Actions llamado `tests.yml`, desde la pestaña **Actions** del repositorio en GitHub. El workflow debe guardarse en `.github/workflows/tests.yml` y ejecutarse únicamente cuando:

1. El repositorio remoto recibe un `push`.

El workflow debe:

1. Ejecutarse en un runner hospedado por GitHub con Ubuntu. La ejecución debe ocurrir en la nube, no en la computadora del alumno.
2. Obtener el código del repositorio remoto.
3. Configurar Python 3.12.
4. Instalar las dependencias de `requirements-dev.txt`.
5. Ejecutar todas las pruebas con `pytest`.
6. Indicar claramente si las pruebas finalizaron correctamente o con errores.

## Requerimientos

- Tener una cuenta de GitHub y acceso a este repositorio.
- Tener Git instalado para trabajar en un repositorio local y enviar cambios al repositorio remoto de GitHub.
- Tener Python 3.10 o superior y `pip` para ejecutar el proyecto en la computadora.
- Conocer la estructura básica de un archivo YAML.
- Crear el workflow desde GitHub y guardarlo en `.github/workflows/` con extensión `.yml` o `.yaml`.
- Configurar el evento `push`; no se requiere que el workflow se ejecute al abrir un pull request.
- No incluir contraseñas, tokens ni credenciales en el código o en el archivo YAML.

## Secuencia de trabajo

1. Crea el repositorio remoto en GitHub y carga los archivos iniciales del proyecto.
2. En el repositorio, abre la pestaña **Actions** y crea el workflow `tests.yml`. Comprueba que quede guardado en `.github/workflows/tests.yml` y que su evento sea `push`.
3. Clona el repositorio remoto en tu computadora.
4. Realiza un cambio sencillo en el código o en el README local, por ejemplo, agrega un ejemplo de uso.
5. Confirma el cambio con un commit y envíalo al repositorio remoto con `git push`.
6. Abre la pestaña **Actions** en GitHub y observa la ejecución iniciada por ese `push`. El trabajo debe ejecutarse en un runner hospedado por GitHub.

## Probar el proyecto localmente

Desde la carpeta principal del repositorio, crea un entorno virtual:

```bash
python -m venv .venv
```

Actívalo:

```bash
# macOS o Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Instala las dependencias y ejecuta las pruebas:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -v
```

Prueba el conversor desde la terminal:

```bash
python conversor.py 25 C F
python conversor.py 77 F C
```

## Comprobación del resultado

Verifica que el `push` de tu cambio local genere una ejecución exitosa en **Actions**. Luego provoca temporalmente un fallo en una prueba o en el código, realiza otro commit y envíalo con `git push`. Comprueba que esa ejecución aparezca como fallida. Finalmente, restaura el proyecto, vuelve a enviar los cambios y verifica que el workflow finalice correctamente.

## Entrega

- El workflow guardado en `.github/workflows/tests.yml`.
- El enlace al repositorio utilizado.
- Una captura o enlace a la ejecución exitosa iniciada por el `push` desde el repositorio local.
- Una breve explicación de cómo el `push` local llegó al repositorio remoto y qué pasos ejecutó el workflow.
- Evidencia de una ejecución fallida cuando las pruebas no pasan y otra ejecución exitosa posterior.

## Criterios de evaluación

| Criterio | Puntaje |
|---|---:|
| Workflow ubicado en la ruta correcta y con sintaxis válida | 2 |
| Eventos `push` y `pull_request` configurados | 2 |
| Runner Ubuntu y Python 3.12 configurados | 2 |
| Dependencias instaladas desde `requirements-dev.txt` | 2 |
| Pruebas ejecutadas y evidencia de ejecuciones exitosa y fallida | 2 |
| **Total** | **10** |

## Uso del conversor

```text
python conversor.py <valor> <escala_origen> <escala_destino>
```

Las escalas admitidas son `C` y `F` (también se acepta minúscula). Ejemplo: `python conversor.py 100 C F`.
