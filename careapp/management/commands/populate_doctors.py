from django.core.management.base import BaseCommand
from careapp.models import Doctor


class Command(BaseCommand):
    help = 'Populates the database with sample doctors'

    def handle(self, *args, **kwargs):
        doctors_data = [
            {"first_name": "Walter", "last_name": "White", "specialty": "Chief Medical Officer"},
            {"first_name": "Sarah", "last_name": "Johnson", "specialty": "Anesthesiologist"},
            {"first_name": "William", "last_name": "Anderson", "specialty": "Cardiology"},
            {"first_name": "Amanda", "last_name": "Jepson", "specialty": "Neurosurgeon"},
            {"first_name": "Michael", "last_name": "Brown", "specialty": "Pediatrics"},
            {"first_name": "Emily", "last_name": "Davis", "specialty": "Ophthalmology"},
        ]

        for doc_data in doctors_data:
            doctor, created = Doctor.objects.get_or_create(
                first_name=doc_data['first_name'],
                last_name=doc_data['last_name'],
                defaults={'specialty': doc_data['specialty']}
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created: Dr. {doctor.first_name} {doctor.last_name} - {doctor.specialty}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Already exists: Dr. {doctor.first_name} {doctor.last_name}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(f"\nTotal doctors in database: {Doctor.objects.count()}")
        )
