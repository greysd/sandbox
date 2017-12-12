default: help


help:
	@echo Please use \"cat Makefile\" for more details...


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


.PHONY: default help bootstrap vagrant server python_egg lint
