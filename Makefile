all:

install_vagrant:
	yes | apt-get install virtualbox
	yes | wget https://releases.hashicorp.com/vagrant/2.0.3/vagrant_2.0.3_x86_64.deb
	yes | sudo dpkg -i vagrant_2.0.3_x86_64.deb
	@yes | vagrant plugin install vagrant-vbguest

vagrant_up:
	vagrant up