"""Build playbooks."""
import os


def create_playbook(playbook_name, template_content, inventory_content):
    output_dir = os.path.join(os.getcwd(), 'playbooks')
    os.makedirs(output_dir, exist_ok=True)

    playbook_file = os.path.join(output_dir, f"{playbook_name}.yml")
    with open(playbook_file, 'w') as f:
        f.write(template_content)

    inventory_file = os.path.join(output_dir, "inventory.ini")
    with open(inventory_file, 'w') as f:
        f.write(inventory_content)

    return output_dir
