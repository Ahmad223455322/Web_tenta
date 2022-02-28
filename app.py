from flask import Flask, render_template,redirect,request,url_for
from flask_migrate import Migrate, upgrade
from form import PersonNewForm,AccuontNewForm,PersonEditForm
from model import db,Person,Account

 
app = Flask(__name__)
app.config.from_object('config.ConfigDebug')


db.app = app
db.init_app(app)
migrate = Migrate(app,db)



@app.route("/", methods=['GET', 'POST'])
def index()->str:
     return render_template("index.html")




@app.route("/personnew",methods=["GET", "POST"]) 
def personNewPage()->str:
    form = PersonNewForm(request.form) 

    if request.method == "GET":
        return render_template('personnew.html',form=form)

    if form.validate_on_submit():
        personFromDb = Person()
        personFromDb.Förnamn = form.Förnman.data
        personFromDb.Efternamn = form.Efternamn.data 
        personFromDb.Address = form.Address.data
        personFromDb.Stad = form.Stad.data
        db.session.add(personFromDb)
        db.session.commit()
        return redirect(url_for('personNewPage'))

    return render_template('personnew.html',form=form)     




@app.route("/kontonew",methods=["GET", "POST"]) 
def kontoNewPage()->str:
    form = AccuontNewForm(request.form) 

    if request.method == "GET":
        return render_template('kontonew.html',form=form)

    if form.validate_on_submit():
        kontonFromDB = Account()
        kontonFromDB.Kontotyp = form.Kontotyp.data
        kontonFromDB.Saldo = form.Saldo.data
        kontonFromDB.PersonId= form.PersonID.data
   
        db.session.add(kontonFromDB)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('kontonew.html',form=form)    



    
@app.route("/personedit/<id>",methods=["GET", "POST"])  # EDIT   3

def personedit(id):
    form = PersonEditForm(request.form) 
    personFromDb = Person.query.filter(Person.Id == id).first()

    if request.method == "GET":
        form.Förnamn.data = personFromDb.Förnamn
        form.Efternamn.data = personFromDb.Efternamn
        form.Address.data = personFromDb.Address
        form.Stad.data = personFromDb.Stad
        return render_template('personedit.html',person=personFromDb, form=form)
    if form.validate_on_submit():
        personFromDb.Förnamn = form.Förnamn.data
        personFromDb.Efternamn = form.Efternamn.data 
        personFromDb.Address = form.Address.data
        personFromDb.Stad = form.Stad.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('personedit.html',person=personFromDb, form=form)
    
 


if __name__  == "__main__":
    with app.app_context():
        upgrade()
    app.run()


