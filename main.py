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

   cur.execute("DROP TABLE mysales;")
   

   # cur.execute("""CREATE TABLE mysales(id serial PRIMARY KEY,inv_id integer,quantity numeric, date_created date)""");
   # cur.execute(""" insert into mysales (id, inv_id, quantity, date_created) values (1, 24, 495.03, '8/17/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (2, 26, 739.07, '2/27/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (3, 24, 952.85, '4/25/2016');
   # insert into mysales(id, inv_id, quantity, date_created) values (4, 27, 47.12, '11/3/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (5, 14, 468.0, '11/17/2016');
   # insert into mysales (id, inv_id, quantity, date_created) values (6, 16, 625.93, '10/20/2012');
   # insert into mysales(id, inv_id, quantity, date_created) values (7, 4, 152.95, '10/21/2016');
   # insert into mysales (id, inv_id, quantity, date_created) values (8, 11, 356.26, '2/23/2016');
   # insert into mysales (id, inv_id, quantity, date_created) values (9, 16, 749.47, '5/24/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (10, 35, 724.6, '11/30/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (11, 16, 447.89, '11/26/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (12, 16, 700.93, '1/8/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (13, 12, 626.68, '7/19/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (14, 7, 93.88, '10/14/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (15, 34, 305.85, '12/8/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (16, 27, 301.71, '1/17/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (17, 22, 351.2, '8/21/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (18, 31, 165.71, '1/20/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (19, 31, 268.02, '8/30/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (20, 9, 334.03, '10/8/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (21, 40, 106.54, '10/31/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (22, 40, 976.62, '1/22/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (23, 15, 931.09, '3/5/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (24, 15, 798.54, '10/12/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (25, 12, 848.3, '2/25/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (26, 39, 41.02, '5/29/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (27, 12, 971.67, '6/14/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (28, 31, 54.54, '6/5/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (29, 31, 793.17, '8/7/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (30, 36, 138.37, '5/26/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (31, 21, 5.91, '5/24/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (32, 2, 725.82, '3/22/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (33, 33, 425.6, '1/11/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (34, 14, 167.52, '2/17/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (35, 5, 432.28, '8/6/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (36, 18, 95.12, '5/21/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (37, 16, 934.3, '6/6/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (38, 35, 340.88, '8/2/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (39, 11, 968.9, '5/10/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (40, 9, 574.62, '8/26/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (41, 18, 662.07, '8/20/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (42, 26, 151.48, '3/16/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (43, 36, 931.34, '3/2/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (44, 29, 357.73, '3/15/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (45, 18, 198.87, '4/22/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (46, 27, 457.46, '7/27/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (47, 2, 367.62, '1/9/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (48, 19, 223.37, '2/3/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (49, 4, 345.9, '3/8/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (50, 40, 624.35, '4/5/2016');
   # insert into mysales (id, inv_id, quantity, date_created) values (51, 3, 227.96, '7/30/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (52, 37, 262.6, '7/12/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (53, 14, 285.77, '5/30/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (54, 27, 329.7, '7/6/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (55, 19, 936.9, '8/13/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (56, 5, 880.64, '2/14/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (57, 37, 301.62, '6/16/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (58, 30, 919.48, '6/23/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (59, 4, 297.3, '1/2/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (60, 2, 351.09, '3/20/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (61, 19, 560.55, '8/24/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (62, 33, 254.83, '1/23/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (63, 3, 429.7, '5/21/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (64, 26, 85.02, '6/24/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (65, 22, 914.33, '3/24/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (66, 39, 161.52, '12/30/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (67, 10, 849.08, '9/3/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (68, 7, 491.52, '8/7/2016');
   # insert into mysales (id, inv_id, quantity, date_created) values (69, 20, 917.41, '5/16/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (70, 7, 214.74, '11/26/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (71, 31, 180.73, '4/27/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (72, 29, 64.88, '12/26/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (73, 31, 181.5, '10/25/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (74, 16, 912.27, '11/26/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (75, 16, 944.42, '11/23/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (76, 9, 263.72, '10/23/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (77, 16, 682.06, '7/31/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (78, 13, 698.93, '9/16/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (79, 4, 873.49, '4/6/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (80, 26, 109.1, '11/19/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (81, 38, 129.85, '1/5/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (82, 1, 471.64, '2/15/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (83, 21, 429.28, '2/14/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (84, 25, 871.35, '8/12/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (85, 35, 626.0, '1/31/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (86, 11, 162.21, '10/14/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (87, 21, 303.95, '4/28/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (88, 13, 263.64, '3/16/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (89, 26, 332.14, '6/5/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (90, 29, 374.17, '6/4/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (91, 28, 874.64, '4/28/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (92, 5, 666.82, '10/9/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (93, 13, 743.88, '10/13/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (94, 28, 794.15, '12/24/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (95, 12, 974.88, '2/6/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (96, 34, 860.69, '10/23/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (97, 27, 928.9, '5/20/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (98, 23, 809.75, '2/24/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (99, 5, 37.63, '6/10/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (100, 33, 571.27, '1/26/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (101, 8, 593.14, '7/20/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (102, 30, 368.69, '7/19/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (103, 35, 68.65, '10/1/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (104, 16, 534.56, '9/17/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (105, 21, 122.32, '3/10/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (106, 20, 994.96, '3/29/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (107, 18, 958.26, '6/23/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (108, 40, 8.02, '6/25/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (109, 1, 401.06, '1/26/2016');
   # insert into mysales (id, inv_id, quantity, date_created) values (110, 10, 286.15, '6/27/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (111, 24, 925.11, '2/28/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (112, 40, 310.31, '6/18/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (113, 26, 213.61, '12/8/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (114, 27, 438.37, '7/18/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (115, 20, 31.01, '11/18/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (116, 20, 188.62, '10/12/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (117, 37, 203.53, '10/27/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (118, 34, 433.56, '5/18/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (119, 15, 694.45, '7/25/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (120, 3, 533.75, '6/1/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (121, 34, 120.2, '4/17/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (122, 33, 14.26, '2/23/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (123, 5, 617.05, '3/11/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (124, 39, 526.99, '10/6/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (125, 3, 828.66, '5/6/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (126, 24, 325.67, '10/2/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (127, 17, 193.81, '4/7/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (128, 23, 771.24, '8/29/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (129, 38, 551.48, '6/7/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (130, 19, 223.71, '2/3/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (131, 28, 137.88, '8/5/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (132, 32, 35.93, '7/18/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (133, 33, 500.06, '9/16/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (134, 3, 262.12, '8/14/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (135, 10, 549.38, '4/24/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (136, 32, 393.78, '6/22/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (137, 6, 565.84, '1/20/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (138, 34, 864.67, '12/5/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (139, 17, 846.11, '5/8/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (140, 38, 733.42, '10/13/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (141, 37, 511.59, '8/16/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (142, 12, 616.78, '7/19/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (143, 17, 357.62, '2/21/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (144, 9, 28.6, '3/3/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (145, 11, 328.13, '6/9/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (146, 25, 167.29, '1/29/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (147, 27, 32.12, '12/4/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (148, 26, 559.3, '1/28/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (149, 12, 274.69, '5/14/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (150, 16, 804.14, '7/1/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (151, 12, 643.12, '12/30/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (152, 40, 94.22, '6/18/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (153, 29, 363.19, '8/14/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (154, 8, 372.65, '5/15/2016');
   # insert into mysales (id, inv_id, quantity, date_created) values (155, 27, 209.39, '4/30/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (156, 37, 320.59, '12/19/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (157, 30, 174.72, '4/19/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (158, 4, 948.28, '7/16/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (159, 1, 123.79, '2/3/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (160, 34, 172.61, '11/23/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (161, 20, 496.53, '8/24/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (162, 40, 652.54, '10/9/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (163, 24, 140.81, '7/30/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (164, 36, 154.72, '7/19/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (165, 28, 223.54, '2/12/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (166, 37, 589.27, '7/22/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (167, 25, 695.88, '9/19/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (168, 8, 453.42, '11/10/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (169, 17, 512.27, '9/2/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (170, 27, 538.59, '7/12/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (171, 1, 803.75, '7/27/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (172, 34, 583.33, '12/18/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (173, 18, 994.61, '5/26/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (174, 22, 923.23, '12/4/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (175, 19, 402.08, '11/19/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (176, 11, 973.82, '7/1/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (177, 18, 961.1, '2/11/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (178, 4, 403.15, '8/24/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (179, 6, 502.41, '1/9/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (180, 35, 943.83, '8/29/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (181, 27, 660.68, '5/14/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (182, 31, 288.86, '4/24/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (183, 12, 661.01, '8/13/2012');
   # insert into mysales (id, inv_id, quantity, date_created) values (184, 26, 790.43, '7/27/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (185, 39, 989.77, '4/1/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (186, 9, 913.37, '11/10/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (187, 4, 205.28, '4/3/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (188, 29, 108.19, '4/25/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (189, 32, 57.43, '1/20/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (190, 30, 170.66, '5/25/2017');
   # insert into mysales (id, inv_id, quantity, date_created) values (191, 23, 111.58, '5/4/2014');
   # insert into mysales (id, inv_id, quantity, date_created) values (192, 37, 352.1, '7/11/2015');
   # insert into mysales (id, inv_id, quantity, date_created) values (193, 12, 933.48, '8/25/2013');
   # insert into mysales (id, inv_id, quantity, date_created) values (194, 30, 145.7, '1/17/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (195, 3, 978.26, '5/18/2009');
   # insert into mysales (id, inv_id, quantity, date_created) values (196, 32, 593.02, '1/16/2018');
   # insert into mysales (id, inv_id, quantity, date_created) values (197, 24, 240.07, '2/26/2010');
   # insert into mysales (id, inv_id, quantity, date_created) values (198, 36, 246.98, '3/2/2019');
   # insert into mysales (id, inv_id, quantity, date_created) values (199, 25, 8.77, '3/25/2011');
   # insert into mysales (id, inv_id, quantity, date_created) values (200, 27, 555.11, '4/21/2009');
   # """)
   # conn.commit()

  
   

   # cur.execute("""SELECT EXTRACT (MONTH FROM mysales.date_created) as months,SUM(mysales.quantity) as total_mysales FROM public.mysales GROUP BY months ORDER BY months""");
   # records=cur.fetchall()
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
   line_chart.title="mysales over the year 2019"
   x=[]
   y=[]
   for i in records: 
      x.append(i[0])
      y.append(i[1])


   line_chart.x_labels=map(str, x)
   line_chart.add("mysales",y)

         
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
   return "Welcome to Contact page"

@app.route ("/services")
def services():
   return "Welcome to Services page"


if __name__ == '__main__':
    app.debug= True
    app.run()


 