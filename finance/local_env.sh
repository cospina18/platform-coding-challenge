
# Iniciar Minikube con la red de puente
minikube start --driver=docker --network=minikube-network --memory=8192mb --cpus=4
kubectl config set-context --current --namespace=web-app
docker build -t ms_info -f finance/web/ms_info/src/deployment/docker/dockerfile .  --label test_ms_info
docker build -t ms_suggestion -f finance/web/ms_suggestion/src/deployment/docker/dockerfile . --label test_ms_suggestions
kubectl config set-context --current --namespace=web-app
cd finance/web/ms_info/src/deployment/k8s
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
cd finance/web/ms_suggestion/src/deployment/k8s
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get service

