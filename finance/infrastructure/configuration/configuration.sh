#!/bin/bash

echo ============================================================================
echo Ejecutar aws eks list-clusters
echo ============================================================================
aws eks list-clusters

echo ============================================================================
echo Ejecutar update kubeconfig
echo ============================================================================
aws eks update-kubeconfig --name eks-p-poc

#######################################################################################
#######################################################################################
#########                   Instalar ISTIO, ALB IC                    #################
#######################################################################################
#######################################################################################

echo ====================================================
echo Instalar istio integrado con ALB Ingress Controller
echo ====================================================

echo ====================================================
echo Instalar Istio con istioctl
echo ====================================================

istioctl install --set values.gateways.istio-ingressgateway.type=LoadBalancer -y

kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/addons/jaeger.yaml

kubectl apply -f  https://raw.githubusercontent.com/istio/istio/release-1.7/samples/addons/kiali.yaml

echo ====================================================
echo Habilitar mTLS para el mesh entero Todos los servicios que se comuniquen entre si y tengan habilitado el istio-injection por defecto hablan mTLS
echo ====================================================
kubectl apply -n istio-system -f - <<EOF
apiVersion: "security.istio.io/v1beta1"
kind: "PeerAuthentication"
metadata:
  name: "default"
spec:
  mtls:
    mode: STRICT
EOF

echo ====================================================
echo Crear autenticacion OIDC para el cluster
echo ====================================================
eksctl utils associate-iam-oidc-provider  --region us-east-1  --cluster  eks-p-poc --approve

echo ====================================================
echo Crear RBAC role para ALB
echo ====================================================
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.6/docs/examples/rbac-role.yaml

echo ====================================================
echo Crear Service Account para ALB
echo ====================================================
eksctl create iamserviceaccount --region us-east-1 --name alb-ingress-controller --namespace kube-system --cluster  eks-p-poc --attach-policy-arn arn:aws:iam::271590248982:policy/ALBIngressControllerIAMPolicy --override-existing-serviceaccounts

echo ====================================================
echo Crear ALB Ingress Controller
echo ====================================================
kubectl apply -f  $SYSTEM_DEFAULTWORKINGDIRECTORY/infrastructure/configuration/alb-ingress-controller.yaml

echo =====================================================================
echo Crear Ingress Service que crea los ALB para el cluster  EKS
echo =====================================================================

arncertificateext=$(aws acm list-certificates --query "CertificateSummaryList[?contains(DomainName,'eks-p-poc.ext.infobranches.com')].CertificateArn" --output text)

# kubectl apply -n istio-system -f $SYSTEM_DEFAULTWORKINGDIRECTORY/infrastructure/configuration/ingress.yaml

echo ====================================================
echo Instalar cluster autoscaler
echo ====================================================

#######################################################################################
#######################################################################################
##############     GENERAR ROLES PARA LOS SERVICE CONNECTION         ##################
#######################################################################################
#######################################################################################

 kubectl apply -f $SYSTEM_DEFAULTWORKINGDIRECTORY/infrastructure/configuration/role.yaml

 kubectl get secrets

#######################################################################################
#######################################################################################
##############     FLUENTD        ##################
#######################################################################################
#######################################################################################

kubectl apply -f $SYSTEM_DEFAULTWORKINGDIRECTORY/infrastructure/configuration/amazon-cloudwatch.yaml
kubectl create configmap cluster-info --from-literal=cluster.name=eks-p-poc --from-literal=logs.region=us-east-1 -n amazon-cloudwatch
kubectl apply -f $SYSTEM_DEFAULTWORKINGDIRECTORY/infrastructure/configuration/fluentd.yaml