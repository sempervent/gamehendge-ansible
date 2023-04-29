"""Kubernetes CLI implementation."""
import os
import click

from playbooks.integrations.kubernetes import models, setup


def kubernetes_setup(setup_type):
    if setup_type == "setup":
        devices = click.prompt("Enter the network addresses for the devices (comma-separated)")
        devices = [models.Device(ip_address=device.strip()) for device in devices.split(',')]
        controller_ip = click.prompt("Enter the Kubernetes controller IP address")

        # Add more prompts for other necessary information

        inventory = models.Inventory(
            devices=devices,
            kubernetes_controller=models.KubernetesController(ip_address=controller_ip)
        )
        context = models.PlaybookContext(inventory=inventory)

        template_files = ["kubernetes_template.j2"]  # Add more templates if needed
        output_dir = os.path.join(os.getcwd(), 'playbooks')
        setup.kubernetes_setup(output_dir, template_files, context)

        click.echo(f"Ansible playbooks generated successfully in '{output_dir}'.")
    else:
        click.echo("Invalid setup type. Please provide a valid setup type.")
