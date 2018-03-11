Sandbox
=======

Установка и настройка
---------------------

Традиционно, установка и настройка происходят с помощью [Vagrant](https://www.vagrantup.com/downloads.html), [VirtualBox](https://www.virtualbox.org/wiki/Downloads), [Ansible](http://docs.ansible.com/ansible/intro_installation.html), виртуальных машин и магии.

1. Клонируем репозиторий:

    `git clone ssh://git@github.com:MySkyTech/sandbox.git sandbox`

2. Запускаем виртуалку:

    `make vagrant`

	
---- далее не делаем

3. На этом шаге вы уже внутри виртуалки, переходим в директорию `/vagrant` и завершаем настройку:

    `make bootstrap`

	

4. Запускаем девелоперский сервер:

    `make server`

5. Enjoy.

=====================
Apiserver перенес в папку tornado
Все изменения делаются в ней и распространяются копированием в соседние папки (например tornado1, tornado2 и тд)
Так как хост-машина имеет ОС Windows, то ansible устанавливается непосредственно в виртуальную машину
Соотвественно плейбук ansible запускается внутри нее
в плейбуке устанавливается haproxy вместе с конфигом на один дефолтный бакенд и фронтенд на порт 15000.
соответственно заходить надо в
 
http://localhost:15000

Бакенд запускается из папки которая скопировалась  из папки tornado на дефолтном порту 5000
Вся установка и запуск бакенда осуществлется командой make c таргетом ansible_server

3. Устанавливаем ansible

make ansible_pack



4. 

cd /vagrant/tornado/ansible

ansible-playbook -i inventory vagrant.yaml

5. 

cd /vagrant/tornado
make bootstrap


6. 
cd /vagrant
make ansible_server

или вручную

ansible-playbook -i inventory --extra-vars 'server_name=tornado1 server_port=5000' newserver.yaml --tags installation




Когда код подправлен и дождались пока закончится загрузка файла 
запускаем

make ansible_rerun_default_server

или вручную 

убиваем сервер
kill -KILL $(netstat -napt 2>&1 | grep ' 5000' | tail -1 | awk ' {split($7,a,"/"); print a[1]}')

удаляем папку первого сервера

rm -rf tornado1

убиваем процесс


и запускаем его заново

ansible-playbook -i inventory --extra-vars 'server_name=tornado2 server_port=5000' newserver.yaml