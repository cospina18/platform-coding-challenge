#!/bin/bash

# Actualizar paquetes
echo "Actualizando paquetes..."
sudo apt update && sudo apt upgrade -y

# Instalar paquetes necesarios
echo "Instalando paquetes necesarios..."
sudo apt install -y curl wget apt-transport-https ca-certificates software-properties-common conntrack

# Instalar Docker
echo "Instalando Docker..."
if ! command -v docker &> /dev/null; then
    sudo apt install -y docker.io
    sudo systemctl enable docker
    sudo systemctl start docker
    sudo usermod -aG docker $USER
else
    echo "Docker ya está instalado."
fi

# Descargar e instalar kubectl
echo "Instalando kubectl..."
if ! command -v kubectl &> /dev/null; then
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    chmod +x kubectl
    sudo mv kubectl /usr/local/bin/
else
    echo "kubectl ya está instalado."
fi

# Descargar e instalar Minikube
echo "Instalando Minikube..."
if ! command -v minikube &> /dev/null; then
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    sudo install minikube-linux-amd64 /usr/local/bin/minikube
    rm minikube-linux-amd64
else
    echo "Minikube ya está instalado."
fi

# Configurar Docker como controlador predeterminado de Minikube
echo "Configurando Minikube con Docker como controlador..."
minikube config set driver docker

# Verificar la instalación
echo "Verificando la instalación..."
minikube version
kubectl version --client
docker --version
newgrp docker

# Crear una red de puente en Docker
docker network create --driver bridge minikube-network
# Iniciar Minikube con la red de puente
minikube start --driver=docker --network=minikube-network --memory=8192mb --cpus=4

# Habilitar Istio en Minikube
minikube addons enable istio-provisioner
minikube addons enable istio
kubectl label namespace web-app istio-injection=enabled


# Verificar la configuración de Minikube e Istio
minikube ip
kubectl get pods -n istio-system
kubectl get pods -o wide

# Crear el namesapace
kubectl create namespace web-app



