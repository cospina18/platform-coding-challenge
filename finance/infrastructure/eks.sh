#!/bin/bash

echo =====================================
echo Crear cluster de Kubernetes
echo =====================================
eksctl create cluster -f $SYSTEM_DEFAULTWORKINGDIRECTORY/infrastructure/eks.yaml 

sleep 50

echo ============================================================================
echo Ejecutar aws eks list-clusters
echo ============================================================================
aws eks list-clusters

echo ============================================================================
echo Ejecutar update kubeconfig
echo ============================================================================
aws eks update-kubeconfig --name eks-p-poc

echo =====================================
echo Validar nodos
echo =====================================
kubectl get nodes 

echo =====================================
echo Validar pod
echo =====================================
kubectl get po --all-namespaces

