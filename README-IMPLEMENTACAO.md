# Implementação EstudaPlus + Docker + K8s + ArgoCD - Passo a Passo

## 0. Pré-requisitos
Docker Desktop, kubectl, kind, argocd CLI

## 1. Copiar arquivos
Copie backend/Dockerfile -> EstudaPlus/backend/Dockerfile
Copie frontend/.../Dockerfile -> EstudaPlus/frontend/estudaplus-frontend/Dockerfile
Copie k8s/ -> EstudaPlus/k8s/
Copie argocd/ -> EstudaPlus/argocd/
Copie kind-cluster.yaml, docker-compose.yml para raiz

## 2. Ajuste settings.py do Django
Em backend/config/settings.py ou onde estiver:
- Ler DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT do os.environ
- ALLOWED_HOSTS = ['*'] para demo
- Se usar python-decouple, ele já lê env.

## 3. Build
docker build -t estudaplus-backend:v1 ./backend
docker build -t estudaplus-frontend:v1 ./frontend/estudaplus-frontend
# Para Kind, carregar imagens:
kind load docker-image estudaplus-backend:v1 --name estudaplus-demo
kind load docker-image estudaplus-frontend:v1 --name estudaplus-demo

## 4. Cluster
kind create cluster --config kind-cluster.yaml
kubectl apply -k k8s/

## 5. ArgoCD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl apply -f argocd/application.yaml
kubectl port-forward svc/argocd-server -n argocd 8080:443

## 6. Acessar
kubectl port-forward svc/frontend-service -n estudaplus 3000:3000
http://localhost:3000
Backend: kubectl port-forward svc/backend-service -n estudaplus 8000:8000

## 7. Testes que impressionam
kubectl delete pod -l app=backend -n estudaplus  # self-healing
kubectl scale deployment backend -n estudaplus --replicas=4 # escala
kubectl get hpa -n estudaplus
