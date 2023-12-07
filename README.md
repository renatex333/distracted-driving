# distracted-driving

Projeto por: Pedro Altobelli, Renato Laffranchi e Vinicius Moraes

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
- Demo no celular, com deploy no servidor.
- Cobrir todos os tipos de distracao do YOLO.

### Entrega via email até 08/12

- Link do repositório.
- Instruções para rodar demonstração local.
- Link da demonstração online.
- Descrição do processo de atualização.

## Rubricas

### Conceito C

- Versão web, mesmo que rodando localmente.
- Webcam ao vivo, mesmo que com FPS baixo.
- Exibição em tempo real de todas as informações.
- Implementação modular de todos os alertas.
- Envio de informações em alto nível do servidor.

### Conceito B

- Deploy de versão online com acesso público.
- Facilidade de atualização, mesmo que não seja um CD.

### Conceito A

- Acabamento profissional.
- Configuração completa dos alertas.

## Setup do ambiente

    python3 -m venv env

Para ativar o ambiente virtual basta rodar o comando:

    # Linux
    source env/bin/activate
    # Windows
    env/Scripts/activate

## Instalando dependências

    pip install --upgrade pip
    pip install -r requirements.txt

Se der problema para instalar os `requirements.txt`, instale as dependências manualmente:

    pip install flask flask-sock opencv-python ultralytics


## Rodar demo Flask

    flask --app app/distracted-driving.py run

## Planilhas 

[Planilha dos grupos](https://docs.google.com/spreadsheets/d/1881UvEfp4QGNdXIWUzFsebN4hCH7xh6pZpvL-mi7xM4/edit#gid=0)

[Planilha das rubricas](https://docs.google.com/spreadsheets/d/1-sJTng3EHL6j4yCbi8HgM0QcyZhv86lO3-wTwadBPj4/edit#gid=0)

## Referências

Sam Ansari. (2022). [How to Train YOLO Model to Detect Distracted Drivers](https://ansarisam.medium.com/how-to-train-yolo-v5-model-to-detect-distracted-drivers-ac62b2d44a27).

Yacine Rouizi. (2023). [Real-time Object Tracking with OpenCV and YOLOv8 in Python](https://thepythoncode.com/article/real-time-object-tracking-with-yolov8-opencv).

Ultralytics. (2023). [YoloV8 Docs](https://docs.ultralytics.com/).

Vercel. [Flask Hello World](https://vercel.com/templates/python/flask-hello-world).

Vercel. [Django Hello World](https://vercel.com/templates/python/django-hello-world).

Mozilla, MDN Web Docs. (2023). [Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API).

[Distracted Driving Images Dataset 01](https://universe.roboflow.com/search?q=distracted%20driving).

[Distracted Driving Images Dataset 02](https://universe.roboflow.com/sebastin-ezequiel-galeano/prueba-otro-dataset).

[Distracted Driving Images Dataset 03](https://universe.roboflow.com/cutm-iwh4a/mobile-detection-9demc).

[Distracted Driving Images Dataset 04](https://universe.roboflow.com/m013dsx1277/driver-behavior-jtsfy).

[Distracted Driving Images Dataset 05](https://huggingface.co/datasets/Nexdata/Driver_Behavior_Collection_Data).
