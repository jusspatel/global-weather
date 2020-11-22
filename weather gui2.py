import requests ,json #line:1
import datetime #line:2
from tkinter import *#line:3
from tkinter .ttk import *#line:4
import tkinter .font as tkFont #line:6
import tkinter .messagebox #line:8
from urllib .request import urlopen #line:9
import base64 #line:10
root =Tk ()#line:12
root .title ("Weather")#line:13
root .geometry ("")#line:14
root .resizable (False ,False )#line:15
p1 = PhotoImage(file = "weather-rain-season-cloud-rainy-1-28907.png") 
  
# Setting icon of master window 
root.iconphoto(False, p1) 
def startup ():#line:16
    try :#line:17
        OO000O000O0O000O0 ="006d6dbf520677a12b92a3815f743041"#line:18
        O000O00000O00OOOO ="http://api.openweathermap.org/data/2.5/weather?"#line:19
        OOO0OO0OOO000000O =O000O00000O00OOOO +"appid="+OO000O000O0O000O0 +"&q="+city_name .get ()#line:20
        O0O0O00O0O0O00000 =requests .get (OOO0OO0OOO000000O )#line:21
        OO0000000O000O0O0 =O0O0O00O0O0O00000 .json ()#line:22
        O0O00000000O00O0O =OO0000000O000O0O0 ["main"]#line:23
        O00000OO000OO0OO0 =round (O0O00000000O00O0O ["temp"])#line:24
        ct .set (O00000OO000OO0OO0 -273 )#line:25
        OO0O0000OOOOO0000 =O0O00000000O00O0O ["pressure"]#line:26
        cp .set (OO0O0000OOOOO0000 )#line:27
        O000OOOO0O00000O0 =O0O00000000O00O0O ["humidity"]#line:28
        ch .set (O000OOOO0O00000O0 )#line:29
        O0OOO0OO00O00O00O =round (O0O00000000O00O0O ["temp_max"])#line:30
        cm .set (O0OOO0OO00O00O00O -273 )#line:31
        O00O0O0O000O0O00O =round (O0O00000000O00O0O ["temp_min"])#line:32
        cmi .set (O00O0O0O000O0O00O -273 )#line:33
        OOOOO0O0OOOOO00OO =round (O0O00000000O00O0O ["feels_like"])#line:34
        cc .set (OOOOO0O0OOOOO00OO -273 )#line:35
        O00000000OOO0O0OO =OO0000000O000O0O0 ["visibility"]#line:36
        aa .set (O00000000OOO0O0OO )#line:37
        O0000OOOO00OOO0O0 =OO0000000O000O0O0 ["wind"]#line:38
        OO0O000O0O0OOOOO0 =O0000OOOO00OOO0O0 ["speed"]#line:39
        cs .set (OO0O000O0O0OOOOO0 )#line:40
        OOOOO0000OO000OOO =O0000OOOO00OOO0O0 ["deg"]#line:41
        cd .set (OOOOO0000OO000OOO )#line:42
        O0O000O0OO0000OOO =OO0000000O000O0O0 ["coord"]#line:43
        OOO0000OO0O00O0O0 =O0O000O0OO0000OOO ["lon"]#line:44
        OOOO0OO0OOO0O00O0 =O0O000O0OO0000OOO ["lat"]#line:45
        OO0O0O00000O0O00O =OO0000000O000O0O0 ["dt"]#line:46
        OO0OOO000O0OOO000 =datetime .datetime .fromtimestamp (OO0O0O00000O0O00O )#line:47
        jj .set (OO0OOO000O0OOO000 )#line:48
        OOO0OO0000OOOO00O =OO0000000O000O0O0 ["weather"]#line:49
        O0OO0O0O00O00OO0O =OOO0OO0000OOOO00O [0 ]["description"]#line:50
        zz .set (O0OO0O0O00O00OO0O )#line:51
        OOOO0OO00O0O0OOO0 =OO0000000O000O0O0 ["weather"][0 ]["icon"]#line:52
        OO0OO0O00OOO0OOOO ="http://openweathermap.org/img/w/"+OOOO0OO00O0O0OOO0 +".png"#line:53
        OOO0O0OOOO0OOO00O =OO0000000O000O0O0 ["clouds"]#line:54
        OOO00000O00O0OOO0 =OOO0O0OOOO0OOO00O ["all"]#line:55
        dd .set (OOO00000O00O0OOO0 )#line:56
        O00OO00O0OO0OO00O =OO0000000O000O0O0 ["sys"]#line:57
        OOOOO0O0OOO0OOOOO =O00OO00O0OO0OO00O ["country"]#line:58
        ee .set (OOOOO0O0OOO0OOOOO )#line:59
        OO0O00OOO00OO0000 =O00OO00O0OO0OO00O ["sunrise"]#line:60
        OO0OO00O00OOO0O00 =O00OO00O0OO0OO00O ["sunset"]#line:61
        OOOO00O00O0O000OO =datetime .datetime .fromtimestamp (OO0O00OOO00OO0000 )#line:62
        dti .set (OOOO00O00O0O000OO )#line:63
        O0O00O000OOOOO000 =datetime .datetime .fromtimestamp (OO0OO00O00OOO0O00 )#line:64
        dth .set (O0O00O000OOOOO000 )#line:65
        O00OO00OOO0O0OOO0 =OO0000000O000O0O0 ["name"]#line:66
        ll .set (O00OO00OOO0O0OOO0 )#line:67
        O00O0000O0O0OOO0O =tkFont .Font (family ="Lucida Grande",size =27 )#line:70
        O0OOO00OO0000O000 =tkFont .Font (family ="Helvetica",size =13 )#line:71
        OO00O000O00O00000 =tkFont .Font (family ="Roboto",size =15 )#line:72
        Label (root ,text ="",textvariable =ct ,font =O00O0000O0O0OOO0O ).grid (row =1 ,column =0 ,columnspan =1 ,rowspan =1 )#line:73
        Label (root ,text ="Max Temperature (C): ",font =O0OOO00OO0000O000 ).grid (row =3 ,column =0 )#line:74
        Label (root ,text ="",textvariable =cm ,font =O0OOO00OO0000O000 ).grid (row =3 ,column =1 )#line:75
        Label (root ,text ="Min Temperature (C): ",font =O0OOO00OO0000O000 ).grid (row =4 ,column =0 )#line:76
        Label (root ,text ="",textvariable =cmi ,font =O0OOO00OO0000O000 ).grid (row =4 ,column =1 )#line:77
        Label (root ,text ="Temperature Feels like (C): ",font =O0OOO00OO0000O000 ).grid (row =5 ,column =0 )#line:78
        Label (root ,text ="",textvariable =cc ,font =O0OOO00OO0000O000 ).grid (row =5 ,column =1 )#line:79
        Label (root ,text ="Visibility (in m): ",font =O0OOO00OO0000O000 ).grid (row =6 ,column =0 )#line:80
        Label (root ,text ="",textvariable =aa ,font =O0OOO00OO0000O000 ).grid (row =6 ,column =1 )#line:81
        Label (root ,text ="Wind Speed (in km): ",font =O0OOO00OO0000O000 ).grid (row =7 ,column =0 )#line:82
        Label (root ,text ="",textvariable =cs ,font =O0OOO00OO0000O000 ).grid (row =7 ,column =1 )#line:83
        Label (root ,text ="Wind Degree: ",font =O0OOO00OO0000O000 ).grid (row =3 ,column =2 )#line:84
        Label (root ,text ="",textvariable =cd ,font =O0OOO00OO0000O000 ).grid (row =3 ,column =3 )#line:85
        Label (root ,text ="Pressure (in hPa): ",font =O0OOO00OO0000O000 ).grid (row =4 ,column =2 )#line:86
        Label (root ,text ="",textvariable =cp ,font =O0OOO00OO0000O000 ).grid (row =4 ,column =3 )#line:87
        Label (root ,text ="Humidity (%): ",font =O0OOO00OO0000O000 ).grid (row =5 ,column =2 )#line:88
        Label (root ,text ="",textvariable =ch ,font =O0OOO00OO0000O000 ).grid (row =5 ,column =3 )#line:89
        Label (root ,text ="Weather Description: ",font =O0OOO00OO0000O000 ).grid (row =6 ,column =2 )#line:90
        Label (root ,textvariable =zz ,font =O0OOO00OO0000O000 ).grid (row =6 ,column =3 )#line:91
        Label (root ,text ="Sunrise Time:",font =O0OOO00OO0000O000 ).grid (row =7 ,column =2 )#line:92
        Label (root ,textvariable =dti ,font =O0OOO00OO0000O000 ).grid (row =7 ,column =3 )#line:93
        Label (root ,text ="Sunset Time:",font =O0OOO00OO0000O000 ).grid (row =8 ,column =2 )#line:94
        Label (root ,textvariable =dth ,font =O0OOO00OO0000O000 ).grid (row =8 ,column =3 )#line:95
        O0O00OOOO0OOOOOO0 =Label (root ,textvariable =jj ,font =OO00O000O00O00000 ).grid (row =0 ,column =2 ,columnspan =2 )#line:96
        Label (root ,textvariable =ll ,font =OO00O000O00O00000 ).grid (row =1 ,column =2 )#line:97
        Label (root ,textvariable =ee ,font =OO00O000O00O00000 ).grid (row =1 ,column =3 )#line:99
        O0O0O000OO000OOOO =Label (root ,text ="AQI:",font =O0OOO00OO0000O000 );O0O0O000OO000OOOO .grid (row =8 ,column =0 )#line:100
        O00O0O00O00OO000O =urlopen (OO0OO0O00OOO0OOOO ).read ()#line:104
        OOOO0OOO000OO0OOO =base64 .encodestring (O00O0O00O00OO000O )#line:105
        OOOO00O00OOO00OO0 =PhotoImage (data =OOOO0OOO000OO0OOO )#line:106
        OOOO00O00OOO00OO0 =OOOO00O00OOO00OO0 .zoom (2 ,2 )#line:107
        O00O0OO000O0O0OOO =Label (root ,image =OOOO00O00OOO00OO0 )#line:108
        O00O0OO000O0O0OOO .image =OOOO00O00OOO00OO0 #line:109
        O00O0OO000O0O0OOO .grid (row =9 ,column =0 ,columnspan =4 )#line:110
        OOO00O00OO000OOO0 ="https://api.waqi.info/feed/"+city_name .get ()+"/?token=0574c99883d41944c6ddd40f22de31ffbf39e7b2"#line:111
        OO00O00OO0000O000 =requests .get (OOO00O00OO000OOO0 )#line:112
        OOO0OO0O0O0OO0O00 =OO00O00OO0000O000 .json ()#line:113
        O0OO000O0O0O00000 =OOO0OO0O0O0OO0O00 ["data"]#line:114
        OOOOO0O0OOOO0000O =O0OO000O0O0O00000 [str ("aqi")]#line:115
        aq .set (OOOOO0O0OOOO0000O )#line:116
        Label (root ,textvariable =aq ,font =O0OOO00OO0000O000 ).grid (row =8 ,column =1 )#line:117
    except KeyError :#line:119
        tkinter .messagebox .showerror ("Sys Message","City Not Found")#line:120
    except TypeError :#line:121
        tkinter .messagebox .showerror ("Sys Message","The AQI given for the following country is incorrect, beccause there aren't any nearby air quality stations in this location")#line:122
ct =StringVar ()#line:123
cp =StringVar ()#line:124
ch =StringVar ()#line:125
cm =StringVar ()#line:126
cmi =StringVar ()#line:127
cc =StringVar ()#line:128
aa =StringVar ()#line:129
cs =StringVar ()#line:130
cd =StringVar ()#line:131
zz =StringVar ()#line:132
dd =StringVar ()#line:133
dti =StringVar ()#line:134
dth =StringVar ()#line:135
jj =StringVar ()#line:136
ll =StringVar ()#line:137
ee =StringVar ()#line:138
aq =StringVar ()#line:139
b =Button (root ,text ="Check",command =startup )#line:140
b .grid (row =0 ,column =1 )#line:141
city_name =Entry (root ,width =25 )#line:143
city_name .grid (row =0 ,column =0 )#line:144
root .mainloop ()#line:145
