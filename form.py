from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators,DateTimeField
from wtforms.fields import IntegerField, SelectField, BooleanField



class PersonNewForm(FlaskForm):
    Förnman = StringField("Förnman",[validators.Length(min=3, max=80, message="Skriv in mellan 2 och 80 tecken")])
    Efternamn = StringField("Efternamn",[validators.Length(min=5, max=30)])
    Address = StringField("Address",[validators.Length(min=1,max=200)])
    Stad = StringField("Stad",[validators.Length(min=3, max=80, message="Skriv in mellan 2 och 80 tecken")])    






class AccuontNewForm(FlaskForm):
    Kontotyp = StringField("Kontotyp",[validators.Length(min=1, max=10, message="Skriv in mellan 2 och 10 tecken")])
    Saldo = IntegerField("Saldo",[validators.NumberRange(1,15000)])
    PersonID = IntegerField("ID",[validators.NumberRange(1,100)])
   




class PersonEditForm(FlaskForm):
    Förnamn = StringField("Förnman",[validators.Length(min=3, max=80, message="Skriv in mellan 2 och 80 tecken")])
    Efternamn = StringField("Efternamn",[validators.Length(min=5, max=30)])
    Address = StringField("Address",[validators.Length(min=1,max=200)])
    Stad = StringField("Stad",[validators.Length(min=3, max=80, message="Skriv in mellan 2 och 80 tecken")])    
