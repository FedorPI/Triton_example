# Triton_example

```
docker compose up -d
uvicorn api:app --reload --port 5000
```
После запуска документция к апи доступна тут - http://127.0.0.1:5000/docs

trtexec --onnx=model.onnx --saveEngine=model.plan --minShapes=input:1x3x224x224 --optShapes=input:8x3x224x224 --maxShapes=input:16x3x224x224 --fp16 --useSpinWait