# distracted-driving [EN-US]

Project by: Pedro Altobelli Teixeira Pinto, Renato Laffranchi Falcão, and Vinicius Matheus Morales

## Project Overview

An application to identify when the driver is distracted and provide real-time warnings to help them stay focused on driving.

### Types of Distractions to be Monitored

- Eyes closed: high-intensity alarm
- Head down / Indicative of falling asleep at the wheel: low-intensity alarm 
- Using a cellphone: intermittent sound warning
- Talking on the phone: intermittent sound warning
- Trying to reach something in the back seat: single sound warning, increasing if the attempt continues
- Adjusting the radio: single sound warning
- Yawning: a distinct sound warning from the others, to be associated with a rest break. A text indication can also be provided
- Eating: visual alert, screen flashing

### Final Objective

- Web application, but close to real-time.
- Progressive warning system.
- Mobile demo, with server deployment.
- Cover all types of distraction listed above.

## Environment Setup (local development and testing)

    python3 -m venv env

To activate the virtual environment, run the command:

    # Linux
    source env/bin/activate
    # Windows
    env/Scripts/activate

To deactivate the virtual environment, run the command:

    deactivate

## Installing Dependencies

    pip install --upgrade pip
    pip install -r requirements.txt

If there are problems installing `requirements.txt`, install the dependencies manually:

    pip install flask flask-sock opencv-python ultralytics


## Run Demo

    flask --app app/distracted-driving.py run

## References

Sam Ansari. (2022). [How to Train YOLO Model to Detect Distracted Drivers](https://ansarisam.medium.com/how-to-train-yolo-v5-model-to-detect-distracted-drivers-ac62b2d44a27).

Yacine Rouizi. (2023). [Real-time Object Tracking with OpenCV and YOLOv8 in Python](https://thepythoncode.com/article/real-time-object-tracking-with-yolov8-opencv).

Ultralytics. (2023). [YoloV8 Docs](https://docs.ultralytics.com/).

Vercel. [Flask Hello World](https://vercel.com/templates/python/flask-hello-world).

Vercel. [Django Hello World](https://vercel.com/templates/python/django-hello-world).

Mozilla, MDN Web Docs. (2023). [Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API).

Ipylot project, Roboflow Universe. (2022). [Distracted Driving Dataset](https://universe.roboflow.com/ipylot-project/distracted-driving-v2wk5).

# distracted-driving [PT-BR]

Projeto por: Pedro Altobelli Teixeira Pinto, Renato Laffranchi Falcão, e Vinicius Matheus Morales

## Objetivo do Projeto

Aplicativo para identificar quando o motorista está distraído e fornecer avisos em tempo real que o ajude a se manter focado na direção.

### Tipos de distrações que serão observadas

- Olhos fechados: alarme de alta intensidade
- Cabeça caída / Indicativo de que dormiu na direção: alarme de baixa intensidade 
- Mexer no celular: aviso sonoro intermitente
- Falar no celular: aviso sonoro intermitente
- Tentar alcançar algo no banco de trás: aviso sonoro único, mas aumenta se continuar tentando alcançar
- Mexer no rádio: aviso sonoro único
- Bocejo: aviso sonoro distinto dos outros, para ser associado com uma pausa para descanso. Uma indicação em texto também pode ser fornecida
- Se alimentar: alerta visual, piscar tela

### Objetivo final

- Aplicativo web, mas em algo próximo de tempo real.
- Sistema de avisos progressivo.
- Demo no celular, com deploy em servidor.
- Cobrir todos os tipos de distração listados acima.

## Setup do ambiente (desenvolvimento e teste local)

    python3 -m venv env

Para ativar o ambiente virtual basta rodar o comando:

    # Linux
    source env/bin/activate
    # Windows
    env/Scripts/activate

Para desativar o ambiente virtual basta rodar o comando:

    deactivate

## Instalando dependências

    pip install --upgrade pip
    pip install -r requirements.txt

Se algum erro de instalação for encontrado ao instalar os `requirements.txt`, as dependências podem ser instaladas manualmente manualmente:

    pip install flask flask-sock opencv-python ultralytics


## Rodar demo

    flask --app app/distracted-driving.py run

## Referências

Sam Ansari. (2022). [How to Train YOLO Model to Detect Distracted Drivers](https://ansarisam.medium.com/how-to-train-yolo-v5-model-to-detect-distracted-drivers-ac62b2d44a27).

Yacine Rouizi. (2023). [Real-time Object Tracking with OpenCV and YOLOv8 in Python](https://thepythoncode.com/article/real-time-object-tracking-with-yolov8-opencv).

Ultralytics. (2023). [YoloV8 Docs](https://docs.ultralytics.com/).

Vercel. [Flask Hello World](https://vercel.com/templates/python/flask-hello-world).

Vercel. [Django Hello World](https://vercel.com/templates/python/django-hello-world).

Mozilla, MDN Web Docs. (2023). [Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API).

Ipylot project, Roboflow Universe. (2022). [Distracted Driving Dataset](https://universe.roboflow.com/ipylot-project/distracted-driving-v2wk5).
