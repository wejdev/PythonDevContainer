FROM nvidia/cuda:11.8.0-devel-ubuntu22.04 AS dev_container_auto_added_stage_label

ENV DEBIAN_FRONTEND=noninteractive
ENV CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

# Use bash login shell for all following RUN commands
SHELL ["/bin/bash", "--login", "-c"]

# Install system dependencies
RUN apt-get update \
    && apt-get install -y \
        wget \
        git \
        curl \
        bash \
        bzip2 \
        ca-certificates \
        libglib2.0-0 \
        libxext6 \
        libsm6 \
        libxrender1 \
        libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -b -p $CONDA_DIR \
    && rm /tmp/miniconda.sh \
    && $CONDA_DIR/bin/conda clean --all --yes \
    && ln -s $CONDA_DIR/etc/profile.d/conda.sh /etc/profile.d/conda.sh

# Initialize Conda and set up environment
RUN conda init bash \
    && conda create -n yolodev python=3.10 -y \
    && echo "conda activate yolodev" >> /root/.bashrc

# Install Python libraries
RUN bash -l -c "source /opt/conda/etc/profile.d/conda.sh && \
    conda activate yolodev && \
    conda install -y \
        pytorch==2.5.0 \
        torchvision==0.20.0 \
        torchaudio==2.5.0 \
        pytorch-cuda=11.8 \
        -c pytorch -c nvidia && \
    pip install --upgrade pip && \
    pip install \
        ultralytics \
        pytest \
        ruff \
        black \
        mypy && \
    conda install -y \
        opencv \
        jupyter \
        -c conda-forge"

# Jupyter defaults
EXPOSE 8888
