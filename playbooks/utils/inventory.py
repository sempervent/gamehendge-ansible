"""Tools for making an inventory.ini file."""

def generate_inventory(devices, controller_ip):
    inventory_content = "[kubernetes_controller]\n"
    inventory_content += f"{controller_ip}\n\n"
    inventory_content += "[devices]\n"
    for device in devices:
        inventory_content += f"{device}\n"
    return inventory_content
