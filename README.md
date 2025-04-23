# Paso a paso para ejecutar correctamente el proyecto
## 1. Sin Docker
Si no se desea utilizar docker entonces se debe instalar los requerimientos en un entorno virtual sea con conda o con venv. 
Se hará el ejemplo con conda, para ello, se requiere una versión de Python y para este caso se utilizó la versión de Python 3.11.9 
```
conda create -n DriftDetection Python=3.11.9
```
Posteriormente se accede a la ruta donde se encuentra los requerimientos y se procede con la instalación

```
pip install -r requirements.txt
```
Luego se ingresa a un IDE de Python como Visual Studio Code, se configura para ejecutar el código en el entorno creado y listo!

## 2. Con Docker
Para este caso es importante realizar una correcta instalación de Docker para que se pueda utilizar desde el cmd los comandos de Docker. 
 Luego de instalarlo correctamente, en el terminal del VS Code se ejecuta lo siguiente:

```
docker-compose up --build
```

Si ejecutó correctamente se debería visualizar los resultados en http://localhost:8081/
.Luego podemos acceder dentro del localhost al html creado por la librería evidently http://localhost:8081/data_drift_report.html como se ve en la imagen.

![Imagen_drift](https://github.com/user-attachments/assets/79f501ba-e313-4bfc-82f6-11a915338c5b)
