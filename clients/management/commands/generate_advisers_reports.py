from collections import defaultdict

from django.core.management.base import BaseCommand
from django.db.models.aggregates import Count
from openpyxl.styles import Alignment
from openpyxl.writer.excel import save_workbook

from clients.models import Adviser
from utils import exporter


class Command(BaseCommand):

    def handle(self, *args, **options):
        advisers = Adviser.objects.annotate(
            client_count=Count('client')
        )

        headers = [
            'Doradca',
            'L. klientów'
        ]

        styles = defaultdict(dict)
        for header in headers:
            styles[header]['alignment'] = Alignment(wrap_text=True, vertical='center')

        rows = []
        for adviser in advisers:
            rows.append([
                adviser.name,
                adviser.client_count
            ])

        workbook = exporter.export_to_excel(rows, headers=headers, styles=styles)
        save_workbook(workbook, 'clients/adviser_report.xlsx')
