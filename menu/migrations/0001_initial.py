# Generated by Django 4.2.3 on 2023-08-14 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddonCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('created_on', models.DecimalField(decimal_places=2, max_digits=10)),
                ('modified_on', models.DecimalField(decimal_places=2, max_digits=10)),
                ('visible', models.BooleanField(default=True)),
                ('brand_id', models.IntegerField()),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AddonCategoryOutletLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('outlet_id', models.IntegerField()),
                ('addon_categories_id', models.IntegerField()),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddonVariantOutletLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('outlet_id', models.IntegerField()),
                ('addon_variant_id', models.IntegerField()),
                ('visible', models.BooleanField(default=True)),
                ('sold_out', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AddonVariants',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('addon_categories_id', models.IntegerField()),
                ('food_tag', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=1000)),
                ('created_on', models.CharField(max_length=50)),
                ('modified_on', models.CharField(max_length=50)),
                ('visible', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('display_in', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('created_on', models.DecimalField(decimal_places=2, max_digits=10)),
                ('modified_on', models.DecimalField(decimal_places=2, max_digits=10)),
                ('visible', models.BooleanField(default=False)),
                ('brand_id', models.IntegerField()),
                ('mrp_items', models.BooleanField(default=False)),
                ('single_unavailable', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryOutletLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('outlet_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('visible', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ComboItemsLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('combo_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemAddonLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_id', models.IntegerField()),
                ('addon_variant_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemOutletLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('outlet_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('visible', models.BooleanField(default=True)),
                ('sold_out', models.BooleanField(default=False)),
                ('unit', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=255)),
                ('strike_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('category_id', models.IntegerField()),
                ('food_tag', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('media_url', models.CharField(max_length=255)),
                ('item_type', models.CharField(max_length=255)),
                ('created_on', models.DecimalField(decimal_places=2, max_digits=10)),
                ('modified_on', models.DecimalField(decimal_places=2, max_digits=10)),
                ('visible', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ItemVariantLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_id', models.IntegerField()),
                ('variant_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VariantCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('created_on', models.DecimalField(decimal_places=2, max_digits=10)),
                ('modified_on', models.DecimalField(decimal_places=2, max_digits=10)),
                ('visible', models.BooleanField(default=True)),
                ('brand_id', models.IntegerField()),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VariantCategoryOutletLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('outlet_id', models.IntegerField()),
                ('variant_categories_id', models.IntegerField()),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='VariantOuletLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('outlet_id', models.IntegerField()),
                ('variant_id', models.IntegerField()),
                ('visible', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sold_out', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('variant_categories_id', models.IntegerField()),
                ('created_on', models.DecimalField(decimal_places=2, max_digits=10)),
                ('modified_on', models.DecimalField(decimal_places=2, max_digits=10)),
                ('visible', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
