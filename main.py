# pip3 freeze > requirements.txt  initializing req.txt file

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


#suing local comp
@app.route ("/")
def pie():
       
 #connect to pyscopg2 lib
   conn=psycopg2.connect("dbname=de723tjimc0c7b user=gygwqrdwerdekx host=ec2-18-210-51-239.compute-1.amazonaws.com password=3b24d6681e35a1c68211f7026e627708f43e92cb06f914303865b1636d4db1f7")   

   cur=conn.cursor() 

  

   cur.execute("""CREATE TABLE mysales(id serial PRIMARY KEY,inv_id integer,quantity numeric, date_created date)""");
   cur.execute("""CREATE TABLE inventories(id serial PRIMARY KEY,name character varying(100),type character varying(100),bp numeric (13,2), sp numeric(13,2))""");
   cur.execute("""CREATE TABLE stock(id serial PRIMARY KEY,inv_id integer,date_created date, stock numeric (13,2))""");
   conn.commit()

   cur.execute(""" insert into inventories (id, name, bp, sp, type) values (1, 'Pork - Suckling Pig', 175.52, 245.728, 'vegetables');
   insert into inventories (id, name, bp, sp, type) values (2, 'Lid - 3oz Med Rec', 182.48, 255.472, 'Drinks');
   insert into inventories (id, name, bp, sp, type) values (3, 'Wine - Guy Sage Touraine', 182.65, 255.71, 'Fruits');
   insert into inventories (id, name, bp, sp, type) values (4, 'Veal - Ground', 184.64, 258.496, 'vegetables');
   insert into inventories (id, name, bp, sp, type) values (5, 'Sprouts - Brussel', 199.54, 279.356, 'vegetables');
   insert into inventories (id, name, bp, sp, type) values (6, 'Bar Mix - Pina Colada, 355 Ml', 177.04, 247.856, 'vegetables');
   insert into inventories (id, name, bp, sp, type) values (7, 'Pastry - Apple Large', 183.33, 256.662, 'Drinks');
   insert into inventories (id, name, bp, sp, type) values (8, 'Juice - Happy Planet', 170.72, 239.008, 'Drinks');
   insert into inventories (id, name, bp, sp, type) values (9, 'Pasta - Fettuccine, Dry', 164.78, 230.692, 'vegetables');
   insert into inventories (id, name, bp, sp, type) values (10, 'Fish - Bones', 174.79, 244.706, 'vegetables');
   insert into inventories (id, name, bp, sp, type) values (11, 'Shrimp - 100 / 200 Cold Water', 188.73, 264.222, 'Drinks');
   insert into inventories (id, name, bp, sp, type) values (12, 'Gatorade - Fruit Punch', 167.63, 234.682, 'Drinks');
   insert into inventories (id, name, bp, sp, type) values (13, 'Chilli Paste, Sambal Oelek', 198.55, 277.97, 'Fruits');
   insert into inventories (id, name, bp, sp, type) values (14, 'Bread - 10 Grain Parisian', 187.25, 262.15, 'Fruits');
   insert into inventories (id, name, bp, sp, type) values (15, 'Dc Hikiage Hira Huba', 159.57, 223.398, 'Drinks');
   insert into inventories (id, name, bp, sp, type) values (16, 'Coffee Caramel Biscotti', 159.79, 223.706, 'vegetables');
   insert into inventories (id, name, bp, sp, type) values (17, 'Squid - U - 10 Thailand', 153.44, 214.816, 'vegetables');
   insert into inventories (id, name, bp, sp, type) values (18, 'Bar - Sweet And Salty Chocolate', 178.53, 249.942, 'vegetables');
   insert into inventories (id, name, bp, sp, type) values (19, 'Rabbit - Whole', 161.98, 226.772, 'vegetables');
   insert into inventories (id, name, bp, sp, type) values (20, 'Broom - Push', 169.44, 237.216, 'Fruits');
   insert into inventories (id, name, bp, sp, type) values (21, 'Fudge - Chocolate Fudge', 172.3, 241.22, 'vegetables');
   insert into inventories (id, name, bp, sp, type) values (22, 'Nantucket - Carrot Orange', 180.39, 252.546, 'Fruits');
   insert into inventories (id, name, bp, sp, type) values (23, 'Dry Ice', 179.53, 251.342, 'Fruits');
   insert into inventories (id, name, bp, sp, type) values (24, 'Mushroom - Chantrelle, Fresh', 178.64, 250.096, 'Drinks');
   insert into inventories (id, name, bp, sp, type) values (25, 'Worcestershire Sauce', 166.56, 233.184, 'Fruits');
   insert into inventories (id, name, bp, sp, type) values (26, 'Smoked Paprika', 183.13, 256.382, 'Drinks');
   insert into inventories (id, name, bp, sp, type) values (27, 'Juice - Orange, 341 Ml', 173.95, 243.53, 'Fruits');
   insert into inventories (id, name, bp, sp, type) values (28, 'Sauce - Salsa', 196.82, 275.548, 'Fruits');
   insert into inventories (id, name, bp, sp, type) values (29, 'Cheese - Mozzarella, Buffalo', 171.5, 240.1, 'Fruits');
   insert into inventories (id, name, bp, sp, type) values (30, 'Roe - Lump Fish, Black', 171.75, 240.45, 'Fruits');
   insert into inventories (id, name, bp, sp, type) values (31, 'Orange Roughy 4/6 Oz', 168.51, 235.914, 'Drinks');
   insert into inventories (id, name, bp, sp, type) values (32, 'Wine - Dubouef Macon - Villages', 165.36, 231.504, 'Drinks');
   insert into inventories (id, name, bp, sp, type) values (33, 'Sultanas', 196.42, 274.988, 'Drinks');
   insert into inventories (id, name, bp, sp, type) values (34, 'Wine - Mas Chicet Rose, Vintage', 190.87, 267.218, 'vegetables');
   insert into inventories (id, name, bp, sp, type) values (35, 'Oil - Olive Bertolli', 182.36, 255.304, 'Drinks');
   insert into inventories (id, name, bp, sp, type) values (36, 'Muffin - Mix - Mango Sour Cherry', 180.29, 252.406, 'vegetables');
   insert into inventories (id, name, bp, sp, type) values (37, 'Sobe - Liz Blizz', 195.1, 273.14, 'Drinks');
   insert into inventories (id, name, bp, sp, type) values (38, 'Vinegar - White', 162.59, 227.626, 'Fruits');
   insert into inventories (id, name, bp, sp, type) values (39, 'Cumin - Ground', 162.89, 228.046, 'Drinks');
   insert into inventories (id, name, bp, sp, type) values (40, 'Cranberries - Fresh', 188.44, 263.816, 'vegetables');
   """);
   conn.commit()

   cur.execute(""" insert into stock (id, inv_id, stock, date_created) values (1, 1, 411, '05/03/2015');
   insert into stock (id, inv_id, stock, date_created) values (2, 15, 133, '02/11/2012');
   insert into stock (id, inv_id, stock, date_created) values (3, 12, 293, '07/19/2010');
   insert into stock (id, inv_id, stock, date_created) values (4, 24, 318, '09/22/2017');
   insert into stock (id, inv_id, stock, date_created) values (5, 2, 52, '12/03/2018');
   insert into stock (id, inv_id, stock, date_created) values (6, 1, 596, '05/07/2015');
   insert into stock (id, inv_id, stock, date_created) values (7, 33, 953, '04/13/2010');
   insert into stock (id, inv_id, stock, date_created) values (8, 39, 973, '11/17/2019');
   insert into stock (id, inv_id, stock, date_created) values (9, 35, 385, '06/18/2017');
   insert into stock (id, inv_id, stock, date_created) values (10, 28, 852, '09/04/2013');
   insert into stock (id, inv_id, stock, date_created) values (11, 35, 829, '04/06/2009');
   insert into stock (id, inv_id, stock, date_created) values (12, 34, 368, '12/28/2015');
   insert into stock (id, inv_id, stock, date_created) values (13, 13, 744, '10/06/2011');
   insert into stock (id, inv_id, stock, date_created) values (14, 28, 535, '04/08/2013');
   insert into stock (id, inv_id, stock, date_created) values (15, 6, 200, '11/12/2015');
   insert into stock (id, inv_id, stock, date_created) values (16, 38, 920, '01/27/2011');
   insert into stock (id, inv_id, stock, date_created) values (17, 5, 231, '03/15/2018');
   insert into stock (id, inv_id, stock, date_created) values (18, 1, 361, '12/27/2012');
   insert into stock (id, inv_id, stock, date_created) values (19, 33, 589, '10/02/2019');
   insert into stock (id, inv_id, stock, date_created) values (20, 18, 412, '08/23/2019');
   insert into stock (id, inv_id, stock, date_created) values (21, 21, 109, '12/31/2011');
   insert into stock (id, inv_id, stock, date_created) values (22, 9, 933, '10/10/2014');
   insert into stock (id, inv_id, stock, date_created) values (23, 15, 448, '05/09/2010');
   insert into stock (id, inv_id, stock, date_created) values (24, 33, 445, '11/17/2014');
   insert into stock (id, inv_id, stock, date_created) values (25, 6, 395, '02/17/2016');
   insert into stock (id, inv_id, stock, date_created) values (26, 22, 486, '12/31/2010');
   insert into stock (id, inv_id, stock, date_created) values (27, 40, 783, '04/24/2014');
   insert into stock (id, inv_id, stock, date_created) values (28, 18, 445, '04/04/2010');
   insert into stock (id, inv_id, stock, date_created) values (29, 11, 192, '08/07/2015');
   insert into stock (id, inv_id, stock, date_created) values (30, 11, 498, '07/10/2018');
   insert into stock (id, inv_id, stock, date_created) values (31, 1, 435, '07/09/2015');
   insert into stock (id, inv_id, stock, date_created) values (32, 20, 172, '03/12/2011');
   insert into stock (id, inv_id, stock, date_created) values (33, 9, 922, '08/28/2017');
   insert into stock (id, inv_id, stock, date_created) values (34, 1, 533, '08/20/2019');
   insert into stock (id, inv_id, stock, date_created) values (35, 35, 972, '06/07/2018');
   insert into stock (id, inv_id, stock, date_created) values (36, 28, 520, '05/10/2016');
   insert into stock (id, inv_id, stock, date_created) values (37, 19, 228, '09/21/2019');
   insert into stock (id, inv_id, stock, date_created) values (38, 8, 885, '07/14/2018');
   insert into stock (id, inv_id, stock, date_created) values (39, 5, 548, '06/03/2012');
   insert into stock (id, inv_id, stock, date_created) values (40, 38, 970, '09/26/2010');
   """);
   conn.commit()
   cur.execute()

   cur.execute("""SELECT EXTRACT (MONTH FROM mysales.date_created) as months,SUM(mysales.quantity) as total_sales FROM public.mysales GROUP BY months ORDER BY months""");
   records=cur.fetchall()
   conn.commit()
   cur.close()
   conn.close()
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

   #pie chart
   pie_chart = pygal.Pie()
   pie_chart.title = 'Browser usage in February 2012 (in %)'
   pie_chart.add('IE', 20)
   pie_chart.add('Firefox', 40)
   pie_chart.add('cHROME', 40)
   pie_chart = pie_chart.render_data_uri()


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




#using heroku
@app.route ("/online")
def online():
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


 