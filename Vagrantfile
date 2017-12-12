Vagrant.require_version ">= 1.8.1"


Vagrant.configure("2") do |config|
    config.vm.box = "mokote/ubuntu1604"
    config.vm.hostname = "sandbox.vm"

    config.vm.network :forwarded_port, guest:5000, host:5000

    config.vm.synced_folder ".", "/vagrant"
    config.vm.provider :virtualbox do |vbox|
        vbox.name = 'sandbox'
        vbox.customize ["modifyvm", :id, "--memory", "2048"]
        vbox.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        vbox.customize ["modifyvm", :id, "--cableconnected1", "on"]
    end

	config.vm.provision :ansible do |ansible|
		ansible.verbose = "vv"
		ansible.limit = "all"
        ansible.host_key_checking = false
        ansible.playbook = "ansible/vagrant.yml"
    end
end
