from django import forms 
from .models import ccc 

class postccc_entries(forms.app): 
    model = ccc
    fields = ('ccc_hospitalname', 'ccc_patientsname', 'ccc_patients_status ',  'ccc_no_of_beds')
    
