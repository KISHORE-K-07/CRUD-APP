from flask import Flask,render_template,request,redirect,url_for
from models import db,User
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+pymysql://root:Kisop%40123@localhost/details_db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/',methods={'GET','POST'})
def details():
    if request.method=='POST':
        new_detail=User(name=request.form['user_name'],age=request.form['age'])
        db.session.add(new_detail)
        db.session.commit()
    return render_template('details_add.html')

@app.route('/detail_list')
def detail_list():
    users=User.query.all()
    return render_template('details_list.html',u=users)

@app.route('/details_edit1/<int:id>',methods=['GET','POST'])
def details_edit(id):
    data=User.query.get(id)
    if request.method=='POST':
        data.name=request.form['user_name']
        data.age=request.form['age']
        db.session.commit()

        return redirect(url_for('detail_list'))

    return render_template('details_edit1.html',d=data)  



@app.route('/details_delete/<int:id>')
def details_delete(id):
    data=User.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('detail_list'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)