# Generated by Django 4.2.6 on 2023-10-31 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AccountingLedger",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tuition_fee", models.DecimalField(decimal_places=2, max_digits=10)),
                ("week_start_date", models.DateField()),
                ("week_end_date", models.DateField()),
                ("payment_status", models.BooleanField(default=False)),
                (
                    "amount_paid",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Child",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("dob", models.DateField()),
                ("allergies", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Facility",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("address", models.TextField()),
                ("phone_number", models.CharField(max_length=20)),
                ("license_number", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("dob", models.DateField()),
                ("address", models.TextField()),
                ("phone_number", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=200)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("SYS_ADMIN", "System Administrator"),
                            ("FAC_ADMIN", "Facility Administrator"),
                            ("TEACHER", "Teacher"),
                            ("PARENT", "Parent"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hourly_salary", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_of_hire", models.DateField()),
                ("date_of_termination", models.DateField(blank=True, null=True)),
                (
                    "facility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="facility.facility",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="facility.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount_paid", models.DecimalField(decimal_places=2, max_digits=10)),
                ("payment_date", models.DateField()),
                (
                    "ledger",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="facility.accountingledger",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="facility.user"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="facility",
            name="admin",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="facility.user"
            ),
        ),
        migrations.CreateModel(
            name="Enrollment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("classroom_type", models.CharField(max_length=50)),
                ("date_of_enrollment", models.DateField()),
                ("date_of_withdrawal", models.DateField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("ENROLLED", "Enrolled"),
                            ("WITHDRAWN", "Withdrawn"),
                            ("WAITING", "Waiting"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "child",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="facility.child"
                    ),
                ),
                (
                    "facility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="facility.facility",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClassroomAssignment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("classroom_type", models.CharField(max_length=50)),
                ("capacity", models.PositiveIntegerField()),
                (
                    "child",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="facility.child"
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="facility.staff"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="child",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="facility.user",
            ),
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("time_in", models.TimeField()),
                ("time_out", models.TimeField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="facility.user"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="accountingledger",
            name="child",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="facility.child"
            ),
        ),
    ]
