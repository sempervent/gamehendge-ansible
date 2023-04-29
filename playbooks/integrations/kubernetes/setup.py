"""Setup config for a kubernets playbook."""
from typing import List, Optional, Union
from pathlib import Path

from playbooks.utils import templates, inventory, playbook
from .models import PlaybookContext


def kubernetes_setup(
    template_files: List[str],
    context: PlaybookContext,
    output_dir: Optional[Union[str, Path]] = None,

):
    """Setup kubernetes in the output_dir."""
    if not output_dir:
        output_dir = '.'
    if isinstance(output_dir, str):
        output_dir = Path(output_dir)
    # Render the Jinja templates with the provided context
    rendered_templates = []
    for template_file in template_files:
        rendered_template = templates.render_template(template_file, context.dict())
        rendered_templates.append(rendered_template)

    # Generate the inventory.ini file
    inventory_content = inventory.generate_inventory(
        [device.ip_address for device in context.inventory.devices],
        context.inventory.kubernetes_controller.ip_address
    )

    # Create the Ansible playbooks and inventory file
    for idx, rendered_template in enumerate(rendered_templates):
        playbook_name = f"kubernetes_setup_{idx + 1}"
        playbook.create_playbook(output_dir, playbook_name, rendered_template, inventory_content)
