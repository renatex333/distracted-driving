# distracted-driving

## Setup do ambiente

```
python -m venv env
```

### Linux

```
source env/bin/activate
```

### Windows

```
env/Scripts/activate
```

### Instalando dependências

```
pip install --upgrade pip
pip install -r requirements.txt
```
### Rodar demo

```
python src/detect.py --weights src/best.onnx --source 0 --project results/
```

**Aperte Q para sair!**

## Benchmarks

Ver quais aplicativos e bibliotecas existem com o mesmo proposito ou proposito parecido.

## Compromissos para 07/11

- Encontrar e rodar um demo com algum modelo existente.
- Fechar quais são os tipos de distração que serão observadas.


## Planilha dos grupos

[Clique Aqui](https://docs.google.com/spreadsheets/d/1881UvEfp4QGNdXIWUzFsebN4hCH7xh6pZpvL-mi7xM4/edit#gid=0)


## Referências

Sam Ansari. (2022). [How to Train YOLO Model to Detect Distracted Drivers](https://ansarisam.medium.com/how-to-train-yolo-v5-model-to-detect-distracted-drivers-ac62b2d44a27).

[Distracted Driving Images Dataset 01](https://universe.roboflow.com/search?q=distracted%20driving).

[Distracted Driving Images Dataset 02](https://universe.roboflow.com/sebastin-ezequiel-galeano/prueba-otro-dataset).

[Distracted Driving Images Dataset 03](https://universe.roboflow.com/cutm-iwh4a/mobile-detection-9demc).

[Distracted Driving Images Dataset 04](https://universe.roboflow.com/m013dsx1277/driver-behavior-jtsfy).

[Distracted Driving Images Dataset 05](https://huggingface.co/datasets/Nexdata/Driver_Behavior_Collection_Data).
