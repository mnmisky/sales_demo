# line_chart.title = 'Browser usage evolution (in %)'
               #  line_chart.x_labels = map(str, range(2002, 2013))
               # line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
               # line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
               # line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
               # line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])

from flask import Flask,render_template
import pygal
import psycopg2



app = Flask(__name__)
@app.route ("/person/<name>/<int:age>")
def hello_world(name,age):
    return (name + " is " + age + " years old") .upper()

@app.route ("/numbers/<int:one>/<int:two>")
def numbers (one,two):   
   result = one+two
   return f'{result}'
   # '{}'.format(result)

@app.route ("/pie")
def pie():
   conn=psycopg2.connect("dbname=sales_demo user=postgres host=localhost password=Miskitoo.1998")   

   cur=conn.cursor() 
   cur.execute(""" SELECT EXTRACT (MONTH FROM sales.date_created) as months,
      SUM(sales.quantity) as total_sales

      FROM public.sales
      GROUP BY 
      months
      ORDER BY 
      months""")
   records=cur.fetchall()

   print(records)


   pie_chart = pygal.Pie()
   pie_chart.title = 'Browser usage in February 2012 (in %)'
   pie_chart.add('IE', 20)
   pie_chart.add('Firefox', 40)
   pie_chart.add('cHROME', 40)
   pie_chart = pie_chart.render_data_uri()

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

   #    ]
      
               
   line_chart = pygal.Line()
   line_chart.title="Sales over the year 2019"
   x=[]
   y=[]
   for i in records: 
      x.append(i[0])
      y.append(i[1])


   line_chart.x_labels=map(str, x)
   line_chart.add("sales",y)

         
   line_chart=line_chart.render_data_uri()


   return render_template  ('index.htm',pie_chart=pie_chart,line_chart=line_chart )



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
      line_chart.title="Sales over the year 2019"
      x=[]
      y=[]
      for i in data_line: 
          x.append(i[0])
          y.append(i[1])


      line_chart.x_labels=map(str, x)
      line_chart.add("sales",y)

            
      line_chart=line_chart.render_data_uri()
            
      return render_template ('index.htm', line_chart=line_chart)





@app.route ("/about")
def about():
   return "Welcome to About page"

@app.route ("/contact")
def contact():
   return "Welcome to Contact page"

@app.route ("/services")
def services():
   return "Welcome to Services page"


if __name__ == '__main__':
    app.debug= True
    app.run()


 