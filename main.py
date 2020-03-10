# pip3 freeze > requirements.txt  initializing req.txt file

# line_chart.title = 'Browser usage evolution (in %)'
               #  line_chart.x_labels = map(str, range(2002, 2013))
               # line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
               # line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
               # line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
               # line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])

from flask import Flask,render_template,request,redirect,flash,url_for
from flask_sqlalchemy import SQLAlchemy
import pygal
import psycopg2
import datetime
from configs.config import Development,Production
app = Flask(__name__)
app.config.from_object(Production)

db = SQLAlchemy(app)

from models.inventory import Inventories
from models.stock import Stock
from models.sale import Sales

conn=psycopg2.connect("dbname=de723tjimc0c7b user=gygwqrdwerdekx host=ec2-18-210-51-239.compute-1.amazonaws.com password=3b24d6681e35a1c68211f7026e627708f43e92cb06f914303865b1636d4db1f7")  
# conn=psycopg2.connect("dbname=sales_demo user=postgres host=localhost password=Miskitoo.1998") 

@app.before_first_request
def create_tables():
       db.create_all()



# @app.before_first_request
# def create_tables():
# db.create_all()




@app.route("/")
def home():
    return render_template  ('home.html' )   


#suing local comp
@app.route ("/charts")
def pie():
       
 #connect to pyscopg2 lib
   # conn=psycopg2.connect("dbname=sales_demo user=postgres host=localhost password=Miskitoo.1998")   
   # conn=psycopg2.connect("dbname=de723tjimc0c7b user=gygwqrdwerdekx host=ec2-18-210-51-239.compute-1.amazonaws.com password=3b24d6681e35a1c68211f7026e627708f43e92cb06f914303865b1636d4db1f7")   
   #opening connection
   cur=conn.cursor() 


   



   #making changes persisitent
   conn.commit()

  
   
   #QUERY THAT CALCULATES TOTAL SALES PER MONTH
   # cur.execute("""SELECT EXTRACT (MONTH FROM mysales.date_created) as months,SUM(mysales.quantity) as total_mysales FROM public.mysales GROUP BY months ORDER BY months""");
   # records=cur.fetchall()
   # conn.commit()
   # cur.close()
   # conn.close()
   # try:
   # except Exception as e:
   #    print(e)


 
   # print(records)


   
   # data_line=[('January',20),
   #                ('Jan',20),
   #                ('Feb',40),
   #                ('Mar',31),
   #                ('Apr',82),
   #                ('May',69),
   #                ('Jun',44),
   #                ('Jul',45),
   #                ('Aug',78),
   #                ('Sep',32),
   #                ('Oct',54),
   #                ('Nov',22),
   #                ('Dec',20)

   #    
      
               
   # line_chart = pygal.Line()
   # line_chart.title="mysales over the year 2019"
   # x=[]
   # y=[]
   # for i in records: 
   #    x.append(i[0])
   #    y.append(i[1])


   # line_chart.x_labels=map(str, x)
   # line_chart.add("mysales",y)

         
   # line_chart=line_chart.render_data_uri()

   #pie chart
   pie_chart = pygal.Pie()
   pie_chart.title = 'Browser usage in February 2012 (in %)'
   pie_chart.add('IE', 20)
   pie_chart.add('Firefox', 40)
   pie_chart.add('cHROME', 40)
   pie_chart = pie_chart.render_data_uri()


   return render_template  ('index.htm',pie_chart=pie_chart )
   # line_chart=line_chart


@app.route("/inventories", methods=['POST','GET'])
def inventories():
         
    
      # conn=psycopg2.connect("dbname=sales_demo user=postgres host=localhost password=Miskitoo.1998")      

      r= Inventories.query.all()
      cur=conn.cursor()
      #  adding http verbs so that it can execute if the verb is called
      cur.execute("""SELECT inv_id, sum(quantity) as "stock"
         FROM ((SELECT st.inv_id, sum(stock) as "quantity"
         FROM public.new_stock as st
         GROUP BY inv_id) union all
            (SELECT sa.inv_id, - sum(quantity) as "quantity"
         FROM public.new_sales as sa
         GROUP BY inv_id) 
            ) stsa
         GROUP BY inv_id
         ORDER BY inv_id;""")
      conn.commit()

      remStock = cur.fetchall()
      #    for each in remStock:
      #    print(each[1])


      if request.method=='POST':
         name= request.form['name']        
         type= request.form['type']        
         bp= request.form['buying_price']        
         sp= request.form['selling_price'] 
   
         record=Inventories(name=name, type=type, bp=bp, sp=sp)  
         db.session.add(record)
         db.session.commit()

         return redirect(url_for('inventories'))

            #  crud method. using http verbs eg get,post,delete,put 
         
      return render_template('inventories.html',records=r,remStock = remStock)
        


@app.route("/addsale/<inv_id>", methods=['POST','GET'])
def addsale():
      #  adding http verbs so that it can execute if the verb is called
       if request.method=='POST':
         quantity= request.form['quantity']        
         sale = Sales(inv_id=inv_id, quantity=total)
         db.session.add(sale)
         db.session.commit()
       return redirect(url_for('inventories'))

              
   
       return render_template('inventories.html')



@app.route("/addstock/<inv_id>", methods=['POST','GET'])
def addstock(inv_id):
   
       if request.method=='POST':
        stock= request.form['stock']        
         
        stock = Stock(inv_id=inv_id, stock=stock)
        db.session.add(stock)
        db.session.commit()      
       return redirect(url_for('inventories'))

       return render_template('inventories.html')



#editing an inventory entry
@app.route("/editinventory/<int:id>", methods=['POST','GET'])
def addstock(id):
   
       if request.method=='POST':
         name= request.form['name']        
         type= request.form['type']        
         bp= request.form['buying_price']        
         sp= request.form['selling_price'] 

         #getting records so it shows up to the form for you to edit
         record=Inventories.query.filter by(id=id).first()
         #now replacing back values whether or not you chnaged them
         record.name=name
         record.type=type
         record.bp=bp
         record.sp=sp
         
         db.session.add(record)
         db.session.commit()
       flash("Succesfully updated")
       flash("Oops.Seems like that record doesn't exist")
       return redirect(url_for('inventories'))

       return render_template('inventories.html')






@app.route("/line")
def line():
       
      data_line=[('January',20),
                  ('Jan',20),
                  ('Feb',40),
                  ('Mar',31),
                  ('Apr',82),
                  ('May',69),
                  ('Jun',44),
                  ('Jul',45),
                  ('Aug',78),
                  ('Sep',32),
                  ('Oct',54),
                  ('Nov',22),
                  ('Dec',20)

      ]
      
               
      line_chart = pygal.Line()
      line_chart.title="mysales over the year 2019"
      x=[]
      y=[]
      for i in data_line: 
          x.append(i[0])
          y.append(i[1])


      line_chart.x_labels=map(str, x)
      line_chart.add("mysales",y)

            
      line_chart=line_chart.render_data_uri()
            
      return render_template ('index.htm', line_chart=line_chart)









#using heroku
@app.route ("/online")
def online():
   return "Welcome to About page"
   

@app.route ("/contact")
def contact():
   return render_template('contact.html')


@app.route ("/creative")
def creative():
   return render_template('creative.html')



@app.route ("/services")
def services():
   return "Welcome to Services page"

# miscellenous 
@app.route ("/person/<name>/<int:age>")
def hello_world(name,age):
    return (name + " is " + age + " years old") .upper()

@app.route ("/numbers/<int:x>/<int:y>")
def numbers (x,y):   
   return str(int(x)+int(y))
   # '{}'.format(result)

if __name__ == '__main__':
   app.run()


 