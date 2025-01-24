# platform-coding-challenge arquitectura de la implementacion
# Arquitectura
La solucion se compone de dos microservicios desplegados en EKS. 
![alt text](image.png)


# Ambiente 
El proyecto tiene 2 micros que reciben nombre, cuidad, y edad.
ms_info responde con informacion de las sucursales bancolombia cercanas a dicha cuidad y una sugerencia de inversion. 
https://ms-info.demo-riders.link/ms_info?nombre=Juan&edad=70&cuidad=Medellin

ms_suggestion dummy de mensaje sugerido para invertir. 
https://ms-info.demo-riders.link/ms_suggestion?nombre=Juan&edad=70&cuidad=Medellin

# Configuraciones locales linux o WSL
1. en la carpeta configuration ejecutar el archivo install_minikube sino lo tiene instalado.
2. situado en la carpeta finance ejecutar local_env.sh



