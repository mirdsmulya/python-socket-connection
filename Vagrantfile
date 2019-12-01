# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
echo "cd /vagrant" >> /home/vagrant/.bashrc
echo "ln -sf /vagrant/.vim /home/vagrant/.vim" >> /home/vagrant/.bashrc
echo "ln -sf /vagrant/.vimrc /home/vagrant/.vimrc" >> /home/vagrant/.bashrc
SCRIPT



Vagrant.configure(2) do |config|
  config.vm.define "Server" do |s1|
      s1.vm.box = "ubuntu/xenial64"
      s1.vm.network :private_network, ip: "10.0.0.10", virtualbox__intnet: "network3"
      s1.vm.hostname = "Server"
      s1.vm.provision "shell", inline: $script
      s1.vm.provider :virtualbox do |v|
        v.customize ["modifyvm", :id, "--memory", 512]
      end
  end

  config.vm.define "Client" do |s2|
      s2.vm.box = "ubuntu/xenial64"
      s2.vm.network :private_network, ip: "10.0.0.20", virtualbox__intnet: "network3"
      s2.vm.hostname = "Client"
      s2.vm.provision "shell", inline: $script
      s2.vm.provider :virtualbox do |v|
        v.customize ["modifyvm", :id, "--memory", 512]
      end
  end


  config.vm.box_check_update = false
  config.vbguest.auto_update = false
end
