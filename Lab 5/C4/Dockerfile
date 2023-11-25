#cargar imagen 
FROM ubuntu:20.10

#modificar temporalmente el archivo sources.list
RUN sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu/http:\/\/old-releases.ubuntu.com\/ubuntu/' /etc/apt/sources.list
RUN sed -i '/^deb.*security.ubuntu.com/s/^/#/' /etc/apt/sources.list

#actualizar las dependencias e instalar el cliente openssh
RUN apt-get update && apt-get install -y net-tools openssh-client 

# instalar el servidor openssh
RUN apt install -y sudo openssh-server && mkdir /run/sshd

# instalar wireshark y tshark
RUN apt install -y tshark
RUN apt install -y wireshark

#crear usuario test con contraseña test
RUN useradd -m -s /bin/bash test && echo 'test:test' | chpasswd && adduser test sudo

#configurar el servidor SSH para permitir acceso al usuario test
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 22

#iniciar el servidor SSH
CMD ["/usr/sbin/sshd", "-D"]

