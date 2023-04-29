"""Kubernetes related information models."""
from typing import List
from pydantic import BaseModel


class Device(BaseModel):
    ip_address: str


class KubernetesController(BaseModel):
    ip_address: str


class Inventory(BaseModel):
    devices: List[Device]
    kubernetes_controller: KubernetesController


class PlaybookContext(BaseModel):
    inventory: Inventory
