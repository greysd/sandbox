default: help


help:
	@echo Please use \"cat Makefile\" for more details...

ansible_pack:
	sudo apt-get --assume-yes install ansible
	
bootstrap: python_egg
	@echo BOOTSTRAP DONE


vagrant:
	vagrant up && vagrant ssh -c 'tmux attach || tmux'


# Development helper to run a server.
server:
	PYTHONDONTWRITEBYTECODE=1 python -m apiserver.server --logging=debug

python_egg: setup.py
	sudo python setup.py develop

lint:
	@flake8 myjet

ansible_server:
	ansible-playbook -i inventory --extra-vars 'server_name=tornado1 server_port=5000' newserver.yaml --tags installation

ansible_rerun_default_server:
	sudo kill -KILL $(netstat -napt 2>&1 | grep ':5000' | tail -1 | awk ' {split($7,a,"/"); print a[1]}')
	sudo rm -rf tornado1
	ansible-playbook -i inventory --extra-vars 'server_name=tornado1 server_port=5000' newserver.yaml

ansible_add_backend:
	ansible-playbook -i inventory --extra-vars 'server_name=tornado2 server_port=5001 killed_port=5000' newserver.yaml

ansible_remove_backend:
	ansible-playbook -i inventory --extra-vars 'server_name=tornado2 server_port=5001 killed_port=5000' revert_newserver.yaml
  
.PHONY: default help bootstrap vagrant server python_egg lint

