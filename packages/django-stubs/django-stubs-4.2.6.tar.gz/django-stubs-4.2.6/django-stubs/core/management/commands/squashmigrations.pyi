from django.core.management.base import BaseCommand
from django.db.migrations.loader import MigrationLoader
from django.db.migrations.migration import Migration

class Command(BaseCommand):
    verbosity: int
    interactive: bool
    def find_migration(self, loader: MigrationLoader, app_label: str, name: str) -> Migration: ...
