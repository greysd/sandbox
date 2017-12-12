Sandbox
=======

Установка и настройка
---------------------

Традиционно, установка и настройка происходят с помощью [Vagrant](https://www.vagrantup.com/downloads.html), [VirtualBox](https://www.virtualbox.org/wiki/Downloads), [Ansible](http://docs.ansible.com/ansible/intro_installation.html), виртуальных машин и магии.

1. Клонируем репозиторий:

    `git clone ssh://git@github.com:MySkyTech/sandbox.git sandbox`

2. Запускаем виртуалку:

    `make vagrant`

3. На этом шаге вы уже внутри виртуалки, переходим в директорию `/vagrant` и завершаем настройку:

    `make bootstrap`

4. Запускаем девелоперский сервер:

    `make server`

5. Enjoy.
