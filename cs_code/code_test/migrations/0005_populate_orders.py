# Generated by Django 3.2.9 on 2021-11-22 02:48

from __future__ import unicode_literals

from django.db import migrations
import csv
from datetime import datetime
import os

def load_order_data(apps, schema_editor):
    Order = apps.get_model("code_test", "Order")

    migration_path = os.path.dirname(os.path.realpath(__file__))
    data_path = '{}/../data/'.format(migration_path)
    with open('{}orders.csv'.format(data_path)) as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)

        for row in reader:
            order, created = Order.objects.get_or_create(
                id=row[0],
                product_id=row[1],
                inventory_id=row[2],
                street_address=row[3],
                apartment=row[4],
                city=row[5],
                state=row[6],
                country_code=row[7],
                zip=row[8],
                phone_number=row[9],
                email=row[10],
                name=row[11],
                order_status=row[12],
                payment_ref=row[13],
                transaction_id=row[14],
                payment_amt_cents=row[15],
                ship_charged_cents=row[16] if row[16] != "NULL" else None,
                ship_cost_cents=row[17] if row[17] != "NULL" else None,
                subtotal_cents=row[18],
                total_cents=row[19],
                shipper_name=row[20],
                payment_date=row[21],
                shipped_date=row[22],
                tracking_number=row[23],
                tax_total_cents=row[24],
                created_at=row[25],
                updated_at=row[26],
            )


class Migration(migrations.Migration):

    dependencies = [
        ('code_test', '0004_populate_inventory'),
    ]

    operations = [
        migrations.RunPython(load_order_data),
    ]
