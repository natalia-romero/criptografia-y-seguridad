#cargar imagen 
FROM ubuntu:18.10

#modificar temporalmente el archivo sources.list
RUN sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu/http:\/\/old-releases.ubuntu.com\/ubuntu/' /etc/apt/sources.list
RUN sed -i '/^deb.*security.ubuntu.com/s/^/#/' /etc/apt/sources.list

#actualizar las dependencias e instalar el cliente openssh
RUN apt-get update &&  apt-get install -y net-tools openssh-client

#exponer puerto 22 para permitir conexiones SSH
EXPOSE 22

#comando para iniciar un servidor SSH
CMD ["/usr/sbin/sshd", "-D"]