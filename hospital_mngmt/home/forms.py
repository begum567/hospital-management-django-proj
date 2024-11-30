from django import forms 
from .models import Booking


class DateInput(forms.DateInput):
    input_type='date'
    
    
       
class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = '__all__'
        widgets ={
            'booking_date':DateInput(),
        }
        labels={
            'p_name' :"Patient's Name ",
            'p_phone' :"Patient's Phone",
            'p_email': "Patient's email",
            'doc_name':"Doctors' name",
            'booking_date' :"Booking Date",
        }