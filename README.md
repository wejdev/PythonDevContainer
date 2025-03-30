# PythonDevContainer

Python setup with Jupyter, Pytorch (CUDA), OpenCV, YOLO, Conda

This folder will contain a ready-made dev container setup with:

- Conda
- Python 3.x
- PyTorch (with CUDA support for RTX 4060)
- OpenCV
- YOLO (via ultralytics)
- Jupyter Lab

Folder structure:

my-ml-project/
├── .devcontainer/
│   ├── Dockerfile
│   └── devcontainer.json
├── notebooks/
│   └── test.ipynb
├── src/
│   └── main.py
└── data/               ← this is a local folder to be mounted (optional)
