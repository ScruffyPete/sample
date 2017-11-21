from collections import defaultdict

from datetime import datetime, date, timedelta
from django.core.management.base import BaseCommand
from django.db.models.aggregates import Count
from django.db.models.expressions import Case, Subquery, OuterRef
from django.db.models.fields import IntegerField
from openpyxl.styles import Alignment
from openpyxl.writer.excel import save_workbook

from clients.models import Client
from offers.models import Offer
from utils import exporter


class Command(BaseCommand):

    def handle(self, *args, **options):
        today = date.today()

        lower = datetime.combine(today - timedelta(days=7), datetime.min.time())
        upper = datetime.combine(today, datetime.max.time())

        offer_queryset = Offer.objects.filter(
            client_id=OuterRef('pk'), create_date__range=(lower, upper)
        ).order_by().values('client').annotate(Count('pk')).values('pk__count')

        clients = Client.objects.annotate(
            advisers_count=Count('advisers'),
            last_week_offer_count=Subquery(offer_queryset, output_field=IntegerField()),
        )

        headers = [
            'Klient',
            'L. doradców',
            'L. ofert z ostatniego tygodnia',
        ]

        styles = defaultdict(dict)
        for header in headers:
            styles[header]['alignment'] = Alignment(wrap_text=True, vertical='center')

        rows = []
        for client in clients:
            rows.append([
                client.name,
                client.advisers_count,
                client.last_week_offer_count,
            ])

        workbook = exporter.export_to_excel(rows, headers=headers, styles=styles)
        save_workbook(workbook, 'clients/adviser_report.xlsx')
