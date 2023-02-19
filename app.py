
# from flask import Flask, render_template, request, redirect, session
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mcw_user:yGOOLdxwUfgC8qROQEUIozOg6SemRuVI@dpg-cfo8b0g2i3mo4brtdgv0-a.oregon-postgres.render.com/mcw"
# # postgres://mcw_user:yGOOLdxwUfgC8qROQEUIozOg6SemRuVI@dpg-cfo8b0g2i3mo4brtdgv0-a.oregon-postgres.render.com/mcw

# db = SQLAlchemy(app)
# app.secret_key = 'you'



# class User(db.Model):
    
#     id = db.Column(db.Integer, primary_key=True)
#     Shopname = db.Column(db.String(20), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     customers = db.relationship('Customers', backref='user', lazy=True)
#     addworker = db.relationship('Addworker', backref='user', lazy=True)
    

#     def __repr__(self):
#         return f"User('{self.Shopname}', '{self.email}')"

# class Customers(db.Model):
    
#     SNo = db.Column(db.Integer, primary_key=True)
#     Name = db.Column(db.String(200), nullable=True)
#     Phone = db.Column(db.Integer, nullable=True)
#     date = db.Column(db.DateTime, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) 

#     def __repr__(self) -> str:
#         return f"{self.SNo} - {self.Name}"
    
# with app.app_context():
#     db.create_all()


    
# class Addworker(db.Model):
    
#     SNo = db.Column(db.Integer, primary_key=True)
#     Name1 = db.Column(db.String(200), nullable=True)
#     Phone1 = db.Column(db.Integer, nullable=True)
#     date = db.Column(db.DateTime, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) 

#     def __repr__(self) -> str:
#         return f"{self.SNo} - {self.Name1}"

# with app.app_context():
#     db.create_all()



# @app.route('/Managersignup', methods=['GET', 'POST'])
# def Managersignup():
#     if request.method == 'POST':
#         Shopname = request.form['Shopname']
#         email = request.form['Email']
#         password1 = request.form['password1']
#         password2 = request.form['password2']
#         if not email or not password1 or not password2 or not Shopname:
#             return redirect('/Managersignup')
#         if password1 != password2:
#             return redirect('/Managersignup')
#         try:
#             users = User(Shopname=Shopname, email=email, password=password1)
#             db.session.add(users)
#             db.session.commit()
#             # session['user_id'] = users.id
#             return redirect('/Managerlogin')
#         except:
#             # handle the error by redirecting the user back to the signup page with an error message
#             return render_template('Managersignup.html', error_message='Error: Email already exists or Invalid credentials')
#     return render_template('Managersignup.html')



# @app.route('/Managerlogin', methods=['GET', 'POST'])
# def Managerlogin():
#     if request.method == 'POST':
        
#         Shopname = request.form['Shopname']
#         password = request.form['password']
#         if not Shopname or not password:
#             return redirect('/Managerlogin')

#         user = User.query.filter_by(Shopname=Shopname).first()
#         if user and user.password == password:
#             session['logged_in'] = True
#             return redirect('/Manager')
#         else:
#             return redirect('/Managerlogin')

#     return render_template('Managerlogin.html')


# @app.route('/')
# def MCW():
#     return render_template("MCW.html")





# @app.route('/Manager', methods=['GET', 'POST', 'DELETE'])
# def Manager():
#     if request.method == "POST":
#         if 'logged_in' not in session:
#             return redirect('/Managerlogin')
       
#         Name = request.form["Name"]
#         Phone = request.form["Phone"]
#         if not Name or not Phone:
#             return redirect('/Manager')
        
#         customers = Customers(Name=Name, Phone=Phone)
        
#         try:
#             db.session.add(customers)
#             db.session.commit()
            
#         except:
#             db.session.rollback()
#     allcustomers = Customers.query.all()

#     return render_template("Manager.html", allcustomers=allcustomers)


# @app.route('/delete/<int:SNo>')
# def delete(SNo):
#     allcustomerss = Customers.query.filter_by(SNo=SNo).first()
#     db.session.delete(allcustomerss)
#     db.session.commit()
#     return redirect("/Manager")


# @app.route('/customers/delete', methods=['DELETE'])
# def delete_customers():
#     Customers.query.delete()
#     db.session.commit()
#     return redirect('/Manager')


# @app.route('/update/<int:SNo>', methods=["GET", "POST"])
# def update(SNo):
#     if request.method == "POST":
#         Name = request.form["Name"]
#         Phone = request.form["Phone"]
#         customers = Customers.query.filter_by(SNo=SNo).first()
#         customers.Name = Name
#         customers.Phone = Phone
        
#         try:
#             db.session.add(customers)
#             db.session.commit()
            
#         except:
#             db.session.rollback()
        
#         return redirect('/Manager')
#     customers = Customers.query.filter_by(SNo=SNo).first()
#     return render_template("update.html", customers=customers)





# @app.route('/Addworker', methods=['GET', 'POST', 'DELETE'])
# def Addworkers():
#     if request.method == "POST":
#         Name1 = request.form["Name1"]
#         Phone1 = request.form["Phone1"]
#         if not Name1 or not Phone1:
#             return redirect('/Addworker')
#         workers = Addworker(Name1=Name1, Phone1=Phone1, user_id = 1)
      
#         try:
#              db.session.add(workers)
#              db.session.commit()
            
#         except:
#             db.session.rollback()

#     allworkers = Addworker.query.all()

#     return render_template("Addworker.html", allworkers = allworkers)

# @app.route('/Wdelete/<int:SNo>')
# def Wdelete(SNo):
#     allworkerss = Addworker.query.filter_by(SNo=SNo).first()
#     db.session.delete(allworkerss)
#     db.session.commit()
#     return redirect("/Addworker")


# @app.route('/workers/Wdelete', methods=['DELETE'])
# def delete_workers():
#     Addworker.query.delete()
#     db.session.commit()
#     return redirect('/Addworker')


# @app.route('/Wupdate/<int:SNo>', methods=["GET", "POST"])
# def Wupdate(SNo):
#     if request.method == "POST":
#         Name1 = request.form["Name1"]
#         Phone1 = request.form["Phone1"]
#         workers = Addworker.query.filter_by(SNo=SNo).first()
#         workers.Name1 = Name1
#         workers.Phone1 = Phone1
#         try:
#             db.session.add(workers)
#             db.session.commit()
            
#         except:
#             db.session.rollback()
        
#         return redirect('/Addworker')
#     workers = Addworker.query.filter_by(SNo=SNo).first()
#     return render_template("Wupdate.html", workers=workers)

# @app.route('/Workerlogin', methods=['GET', 'POST'])
# def Workerlogin():
#    if request.method == 'POST':
#         Shopname = request.form['Shopname']
#         Name1 = request.form['Name1']
#         if not Shopname or not Name1:
#             return redirect('/Workerlogin')
#         users = User.query.filter_by(Shopname=Shopname).first()
#         userss = Addworker.query.filter_by(Name1=Name1).first()
#         if users and userss:
#             return redirect('/Worker')
#         else:
#             return redirect('/Workerlogin')
#    return render_template("Workerlogin.html")


# @app.route('/Customer')
# def Customer():
#     allcustomers = Customers.query.all()
#     return render_template("Customer.html", allcustomers=allcustomers)

# @app.route('/Customerlogin', methods=['GET', 'POST'])
# def Customerlogin():
    
#     if request.method == 'POST':
#         Shopname = request.form['Shopname']
#         Name = request.form['Name']
#         if not Name or not Shopname:
#             return redirect('/Customerlogin')
#         custom = Customers.query.filter_by(Name=Name).first()
#         users = User.query.filter_by(Shopname=Shopname).first()
#         if users and custom:
           
#             return redirect('/Customer')
#         else:
#             return redirect('/Customerlogin')
#     return render_template("Customerlogin.html")

# @app.route('/Worker')
# def Worker():
#     allcustomers = Customers.query.all()
#     return render_template("Worker.html", allcustomers=allcustomers)

# @app.route('/Cdelete/<int:SNo>')
# def Cdelete(SNo):
#     allcustomerss = Customers.query.filter_by(SNo=SNo).first()
#     db.session.delete(allcustomerss)
#     db.session.commit()
#     return redirect("/Worker")
   
# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     return redirect('/Managerlogin')

# if __name__ == "__main__":
#     app.run(debug=True, port=8000)









from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mcw_user:yGOOLdxwUfgC8qROQEUIozOg6SemRuVI@dpg-cfo8b0g2i3mo4brtdgv0-a.oregon-postgres.render.com/mcw"
# postgres://mcw_user:yGOOLdxwUfgC8qROQEUIozOg6SemRuVI@dpg-cfo8b0g2i3mo4brtdgv0-a.oregon-postgres.render.com/mcw

db = SQLAlchemy(app)

app.secret_key = 'you'



class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    Shopname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    customers = db.relationship('Customers', backref='user', lazy=True)
    addworker = db.relationship('Addworker', backref='user', lazy=True)
    

    def __repr__(self):
        return f"User('{self.Shopname}', '{self.email}')"

class Customers(db.Model):
    
    SNo = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200), nullable=True)
    Phone = db.Column(db.BigInteger, nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) 

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.Name}"
    
with app.app_context():
    db.create_all()


    
class Addworker(db.Model):
    
    SNo = db.Column(db.Integer, primary_key=True)
    Name1 = db.Column(db.String(200), nullable=True)
    Phone1 = db.Column(db.BigInteger, nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) 

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.Name1}"

with app.app_context():
    db.create_all()



@app.route('/Managersignup', methods=['GET', 'POST'])
def Managersignup():
    if request.method == 'POST':
        Shopname = request.form['Shopname']
        email = request.form['Email']
        password1 = request.form['password1']
        password2 = request.form['password2']
        if not email or not password1 or not password2 or not Shopname:
            return redirect('/Managersignup')
        if password1 != password2:
            return redirect('/Managersignup')
        try:
            users = User(Shopname=Shopname, email=email, password=password1)
            db.session.add(users)
            db.session.commit()
            # session['user_id'] = users.id
            return redirect('/Managerlogin')
        except:
            # handle the error by redirecting the user back to the signup page with an error message
            return render_template('Managersignup.html', error_message='Error: Email already exists or Invalid credentials')
    return render_template('Managersignup.html')



@app.route('/Managerlogin', methods=['GET', 'POST'])
def Managerlogin():
    if request.method == 'POST':
        
        Shopname = request.form['Shopname']
        password = request.form['password']
        if not Shopname or not password:
            return redirect('/Managerlogin')

        user = User.query.filter_by(Shopname=Shopname).first()
        if user and user.password == password:
            session['logged_in'] = True
            return redirect('/Manager')
        else:
            return redirect('/Managerlogin')

    return render_template('Managerlogin.html')


@app.route('/')
def MCW():
    return render_template("MCW.html")





@app.route('/Manager', methods=['GET', 'POST', 'DELETE'])
def Manager():
    if request.method == "POST":
        if 'logged_in' not in session:
            return redirect('/Managerlogin')
       
        Name = request.form["Name"]
        Phone = request.form["Phone"]
        if not Name or not Phone:
            return redirect('/Manager')
        
        customers = Customers(Name=Name, Phone=Phone)
        
        try:
            db.session.add(customers)
            db.session.commit()
            
        except Exception as e:
            db.session.rollback()
            print(f"An error occured:{e}")

    allcustomers = Customers.query.all()

    return render_template("Manager.html", allcustomers=allcustomers)


@app.route('/delete/<int:SNo>')
def delete(SNo):
    allcustomerss = Customers.query.filter_by(SNo=SNo).first()
    db.session.delete(allcustomerss)
    db.session.commit()
    return redirect("/Manager")


@app.route('/customers/delete', methods=['DELETE'])
def delete_customers():
    Customers.query.delete()
    db.session.commit()
    return redirect('/Manager')


@app.route('/update/<int:SNo>', methods=["GET", "POST"])
def update(SNo):
    if request.method == "POST":
        Name = request.form["Name"]
        Phone = request.form["Phone"]
        customers = Customers.query.filter_by(SNo=SNo).first()
        customers.Name = Name
        customers.Phone = Phone
        
        try:
            db.session.add(customers)
            db.session.commit()
            
        except:
            db.session.rollback()
        
        return redirect('/Manager')
    customers = Customers.query.filter_by(SNo=SNo).first()
    return render_template("update.html", customers=customers)





@app.route('/Addworker', methods=['GET', 'POST', 'DELETE'])
def Addworkers():
    if request.method == "POST":
        Name1 = request.form["Name1"]
        Phone1 = request.form["Phone1"]
        if not Name1 or not Phone1:
            return redirect('/Addworker')
        workers = Addworker(Name1=Name1, Phone1=Phone1, user_id = 1)
      
        try:
             db.session.add(workers)
             db.session.commit()
            
        except Exception as e:
            db.session.rollback()
            print(f"An error occured:{e}")

    allworkers = Addworker.query.all()

    return render_template("Addworker.html", allworkers = allworkers)

@app.route('/Wdelete/<int:SNo>')
def Wdelete(SNo):
    allworkerss = Addworker.query.filter_by(SNo=SNo).first()
    db.session.delete(allworkerss)
    db.session.commit()
    return redirect("/Addworker")


@app.route('/workers/Wdelete', methods=['DELETE'])
def delete_workers():
    Addworker.query.delete()
    db.session.commit()
    return redirect('/Addworker')


@app.route('/Wupdate/<int:SNo>', methods=["GET", "POST"])
def Wupdate(SNo):
    if request.method == "POST":
        Name1 = request.form["Name1"]
        Phone1 = request.form["Phone1"]
        workers = Addworker.query.filter_by(SNo=SNo).first()
        workers.Name1 = Name1
        workers.Phone1 = Phone1
        try:
            db.session.add(workers)
            db.session.commit()
            
        except:
            db.session.rollback()
        
        return redirect('/Addworker')
    workers = Addworker.query.filter_by(SNo=SNo).first()
    return render_template("Wupdate.html", workers=workers)

@app.route('/Workerlogin', methods=['GET', 'POST'])
def Workerlogin():
   if request.method == 'POST':
        Shopname = request.form['Shopname']
        Name1 = request.form['Name1']
        if not Shopname or not Name1:
            return redirect('/Workerlogin')
        users = User.query.filter_by(Shopname=Shopname).first()
        userss = Addworker.query.filter_by(Name1=Name1).first()
        if users and userss:
            return redirect('/Worker')
        else:
            return redirect('/Workerlogin')
   return render_template("Workerlogin.html")


@app.route('/Customer')
def Customer():
    allcustomers = Customers.query.all()
    return render_template("Customer.html", allcustomers=allcustomers)

@app.route('/Customerlogin', methods=['GET', 'POST'])
def Customerlogin():
    
    if request.method == 'POST':
        Shopname = request.form['Shopname']
        Name = request.form['Name']
        if not Name or not Shopname:
            return redirect('/Customerlogin')
        custom = Customers.query.filter_by(Name=Name).first()
        users = User.query.filter_by(Shopname=Shopname).first()
        if users and custom:
           
            return redirect('/Customer')
        else:
            return redirect('/Customerlogin')
    return render_template("Customerlogin.html")

@app.route('/Worker')
def Worker():
    allcustomers = Customers.query.all()
    return render_template("Worker.html", allcustomers=allcustomers)

@app.route('/Cdelete/<int:SNo>')
def Cdelete(SNo):
    allcustomerss = Customers.query.filter_by(SNo=SNo).first()
    db.session.delete(allcustomerss)
    db.session.commit()
    return redirect("/Worker")
   
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/Managerlogin')

if __name__ == "__main__":
    app.run(debug=True, port=8000)
