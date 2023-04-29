# gamehendge-ansible
Ansible playbooks for setting up gamehendge.

## example raspberry pi cluster setup
Flash the Raspberry Pi OS: Unfortunately, Ansible cannot directly install the OS on the Raspberry Pi. You'll need to manually flash the Raspberry Pi OS onto the SD cards. You can use tools like "Raspberry Pi Imager" or "Balena Etcher" to flash the OS onto the SD cards.

Enable SSH: Before inserting the SD cards into your Raspberry Pi devices, you'll need to enable SSH. To do this, create an empty file named "ssh" (without any extension) and place it in the boot partition of the SD card.

Configure network: Configure the network settings for each Raspberry Pi, either by connecting them to a network via Ethernet or by setting up the Wi-Fi credentials. For Wi-Fi, create a "wpa_supplicant.conf" file in the boot partition and add the Wi-Fi configuration details.

Boot the Raspberry Pis: Insert the SD cards into the Raspberry Pi devices and power them on. They should now be accessible via SSH.

Install Ansible: Install Ansible on your control machine (the machine from which you'll run the playbooks). You can follow the official documentation for installation instructions: https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

Configure Ansible inventory: Create an Ansible inventory file that includes the IP addresses or hostnames of your Raspberry Pi devices. Example:

```
[rpi_cluster]
rpi1 ansible_host=192.168.1.100
rpi2 ansible_host=192.168.1.101
```

Write the Ansible playbook: Create a playbook to configure hostnames, mounts, and install necessary packages for Kubernetes. Example:
yaml
```yaml`
---
- name: Configure Raspberry Pi devices
  hosts: rpi_cluster
  become: yes
  tasks:
    - name: Set hostname
      ansible.builtin.hostname:
        name: "{{ inventory_hostname }}"
    
    - name: Configure mounts
      ansible.builtin.mount:
        path: "/path/to/mount"
        src: "/dev/device_name"
        fstype: "ext4"
        state: "mounted"
    
    - name: Install Docker
      ansible.builtin.package:
        name: "docker"
        state: "present"
    
    - name: Install Kubernetes packages
      ansible.builtin.package:
        name:
          - "kubelet"
          - "kubeadm"
          - "kubectl"
        state: "present"
```
Join the Kubernetes cluster: After configuring the Raspberry Pi devices, you'll need to use the kubeadm tool to join the devices to your Kubernetes master controller. You can add a task in the playbook to execute the kubeadm join command or run it manually on each Raspberry Pi.
