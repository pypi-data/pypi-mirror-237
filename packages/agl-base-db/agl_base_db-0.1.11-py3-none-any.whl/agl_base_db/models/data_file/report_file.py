from django.db import models
from agl_report_reader.extraction import extract_report_meta
from agl_report_reader.settings import DEFAULT_SETTINGS
from agl_report_reader.anonymization import anonymize_report
from django.forms import FileField
import pdfplumber
import warnings
from ..persons import Patient, Examiner
from ..center import Center

from agl_base_db.models.examination import examination_type

class ReportFile(models.Model):
    pdf = models.FileField(upload_to="raw_report_pdfs")
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    report_meta = FileField(upload_to="report_meta", blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    text_anonymized = models.TextField(blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    examiner = models.ForeignKey(Examiner, on_delete=models.CASCADE, blank=True, null=True)
    examination_date = models.DateField(blank=True, null=True)
    examination_time = models.TimeField(blank=True, null=True)

    def get_or_create_patient(self, report_meta):
        patient_first_name = report_meta['patient_first_name']
        patient_last_name = report_meta['patient_last_name']
        patient_dob = report_meta['patient_dob']

        patient, created = Patient.objects.get_or_create(
            first_name=patient_first_name,
            last_name=patient_last_name,
            dob=patient_dob
        )

        return patient, created
    
    def get_or_create_examiner(self, report_meta):
        examiner_first_name = report_meta['examiner_first_name']
        examiner_last_name = report_meta['examiner_last_name']
        examiner_center = self.center

        examiner, created = Examiner.objects.get_or_create(
            first_name=examiner_first_name,
            last_name=examiner_last_name,
            center=examiner_center
        )

        return examiner, created
        


