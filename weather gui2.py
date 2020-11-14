import requests ,json #line:1
import datetime #line:2
from tkinter.tix import *

from tkinter import *#line:3
from tkinter.ttk import*
import tkinter as tk #line:4
import tkinter .font as tkFont #line:5
from PIL import Image ,ImageTk #line:6
import tkinter .messagebox #line:7
from urllib .request import urlopen #line:9
import base64 #line:10

root =tix.Tk ()#line:13
root .title ("Weather")#line:14
root .geometry ("")#line:15
root .resizable (False ,False )#line:17
def startup ():#line:20
    try :#line:21
        OO00O0000O00OO0OO ="006d6dbf520677a12b92a3815f743041"#line:24
        OO0OOO00O0O0O000O ="http://api.openweathermap.org/data/2.5/weather?"#line:28
        O0O00O0O0000OO000 =OO0OOO00O0O0O000O +"appid="+OO00O0000O00OO0OO +"&q="+city_name .get ()#line:35
        O0OOO0O0O00OO0000 =requests .get (O0O00O0O0000OO000 )#line:39
        OO0O0OO0O0O0OOOO0 =O0OOO0O0O00OO0000 .json ()#line:44
        OOO0O00OOO00OO0O0 =OO0O0OO0O0O0OOOO0 ["main"]#line:55
        OO000OOOO0000O000 =round (OOO0O00OOO00OO0O0 ["temp"])#line:59
        ct .set (OO000OOOO0000O000 -273 )#line:60
        O0O00O0O0OOO0O0O0 =OOO0O00OOO00OO0O0 ["pressure"]#line:61
        cp .set (O0O00O0O0OOO0O0O0 )#line:63
        O0OO0O00OO0O0000O =OOO0O00OOO00OO0O0 ["humidity"]#line:65
        ch .set (O0OO0O00OO0O0000O )#line:66
        O0O0O00O0O0OOOOO0 =round (OOO0O00OOO00OO0O0 ["temp_max"])#line:68
        cm .set (O0O0O00O0O0OOOOO0 -273 )#line:69
        OO0OOOO00O0O00O00 =round (OOO0O00OOO00OO0O0 ["temp_min"])#line:71
        cmi .set (OO0OOOO00O0O00O00 -273 )#line:72
        OO0O000OO0000OOO0 =round (OOO0O00OOO00OO0O0 ["feels_like"])#line:74
        cc .set (OO0O000OO0000OOO0 -273 )#line:75
        O0OO000O00O0O00O0 =OO0O0OO0O0O0OOOO0 ["visibility"]#line:77
        aa .set (O0OO000O00O0O00O0 )#line:78
        O00OO0000OO00O0OO =OO0O0OO0O0O0OOOO0 ["wind"]#line:80
        O000O0000O00O0O00 =O00OO0000OO00O0OO ["speed"]#line:82
        cs .set (O000O0000O00O0O00 )#line:83
        O0OOOO0OO000O0OO0 =O00OO0000OO00O0OO ["deg"]#line:85
        cd .set (O0OOOO0OO000O0OO0 )#line:86
        O00OO0OOO0OOO00OO =OO0O0OO0O0O0OOOO0 ["coord"]#line:87
        O0O00OOO0OO00000O =O00OO0OOO0OOO00OO ["lon"]#line:88
        O0OO00OOO0O00OO0O =O00OO0OOO0OOO00OO ["lat"]#line:89
        OO000O0OO0000OO00 =OO0O0OO0O0O0OOOO0 ["dt"]#line:91
        OO0OOOOO0000O0000 =datetime .datetime .fromtimestamp (OO000O0OO0000OO00 )#line:92
        jj .set (OO0OOOOO0000O0000 )#line:93
        O00O0OOOOOO00OO0O =OO0O0OO0O0O0OOOO0 ["weather"]#line:96
        O00OO000OOO000OO0 =O00O0OOOOOO00OO0O [0 ]["description"]#line:97
        zz .set (O00OO000OOO000OO0 )#line:98
        O0O00O00000000OO0 =OO0O0OO0O0O0OOOO0 ["weather"][0 ]["icon"]#line:99
        O00000O00OOO0OOOO ="http://openweathermap.org/img/w/"+O0O00O00000000OO0 +".png"#line:100
        OOO00000O00OO00O0 =urlopen (O00000O00OOO0OOOO ).read ()#line:101
        OOOOO00OOO0O00O00 =base64 .encodestring (OOO00000O00OO00O0 )#line:102
        OOOO0O0O000O00000 =PhotoImage (data =OOOOO00OOO0O00O00 )#line:103
        OOOO0O0O000O00000 =OOOO0O0O000O00000 .zoom (2 ,2 )#line:104
        O0OO000OO0O00O0OO =Label (root ,image =OOOO0O0O000O00000 )#line:105
        O0OO000OO0O00O0OO .image =OOOO0O0O000O00000 #line:106
        O0OO000OO0O00O0OO .grid (row =9 ,column =0 ,columnspan =4 )#line:108
        O0O0O0O00O00OO000 =OO0O0OO0O0O0OOOO0 ["clouds"]#line:115
        OO0O000OO00OOOO00 =O0O0O0O00O00OO000 ["all"]#line:116
        dd .set (OO0O000OO00OOOO00 )#line:117
        OO0OOO0O0O00O0O00 =OO0O0OO0O0O0OOOO0 ["sys"]#line:119
        O000OO0OO0O00O0OO =OO0OOO0O0O00O0O00 ["country"]#line:120
        ee .set (O000OO0OO0O00O0OO )#line:121
        OOOO0OOO0OO0OOO0O =OO0OOO0O0O00O0O00 ["sunrise"]#line:122
        OO0O0O0000O0O0O00 =OO0OOO0O0O00O0O00 ["sunset"]#line:123
        O0000OO00O0OO00OO =datetime .datetime .fromtimestamp (OOOO0OOO0OO0OOO0O )#line:125
        dti .set (O0000OO00O0OO00OO )#line:126
        O0000OO0O0O00O000 =datetime .datetime .fromtimestamp (OO0O0O0000O0O0O00 )#line:127
        dth .set (O0000OO0O0O00O000 )#line:128
        OOO000OOOOOO00OO0 =OO0O0OO0O0O0OOOO0 ["name"]#line:129
        ll .set (OOO000OOOOOO00OO0 )#line:130
        O0OOOOOOOO00000O0 ="https://api.waqi.info/feed/"+city_name .get ()+"/?token=0574c99883d41944c6ddd40f22de31ffbf39e7b2"#line:132
        O000OOOO0000O0OO0 =requests .get (O0OOOOOOOO00000O0 )#line:133
        O0OO0OOOOO00OOOOO =O000OOOO0000O0OO0 .json ()#line:134
        O0OOOO0OO0OO00OO0 =O0OO0OOOOO00OOOOO ["data"]#line:136
        OO00O00O00OO00OO0 =O0OOOO0OO0OO00OO0 [str ("aqi")]#line:137
        aq .set (OO00O00O00OO00OO0 )#line:138

        fontStyle =tkFont .Font (family ="Lucida Grande",size =27 )#line:172
        fontStyle1 =tkFont .Font (family ="Helvetica",size =13 )#line:173
        fontStyle2 =tkFont .Font (family ="Roboto",size =15 )#line:174
        Label (root ,text ="",textvariable =ct ,font =fontStyle ).grid (row =1 ,column =0 ,columnspan =1 ,rowspan =1 )#line:178
        Label (root ,text ="Max Temperature (C): ",font =fontStyle1 ).grid (row =3 ,column =0 )#line:180
        Label (root ,text ="",textvariable =cm ,font =fontStyle1 ).grid (row =3 ,column =1 )#line:182
        Label (root ,text ="Min Temperature (C): ",font =fontStyle1 ).grid (row =4 ,column =0 )#line:184
        Label (root ,text ="",textvariable =cmi ,font =fontStyle1 ).grid (row =4 ,column =1 )#line:186
        Label (root ,text ="Temperature Feels like (C): ",font =fontStyle1 ).grid (row =5 ,column =0 )#line:188
        Label (root ,text ="",textvariable =cc ,font =fontStyle1 ).grid (row =5 ,column =1 )#line:190
        Label (root ,text ="Visibility (in m): ",font =fontStyle1 ).grid (row =6 ,column =0 )#line:192
        Label (root ,text ="",textvariable =aa ,font =fontStyle1 ).grid (row =6 ,column =1 )#line:194
        Label (root ,text ="Wind Speed (in km): ",font =fontStyle1 ).grid (row =7 ,column =0 )#line:196
        Label (root ,text ="",textvariable =cs ,font =fontStyle1 ).grid (row =7 ,column =1 )#line:198
        Label (root ,text ="Wind Degree: ",font =fontStyle1 ).grid (row =3 ,column =2 )#line:200
        Label (root ,text ="",textvariable =cd ,font =fontStyle1 ).grid (row =3 ,column =3 )#line:202
        Label (root ,text ="Pressure (in hPa): ",font =fontStyle1 ).grid (row =4 ,column =2 )#line:204
        Label (root ,text ="",textvariable =cp ,font =fontStyle1 ).grid (row =4 ,column =3 )#line:206
        Label (root ,text ="Humidity (%): ",font =fontStyle1 ).grid (row =5 ,column =2 )#line:208
        Label (root ,text ="",textvariable =ch ,font =fontStyle1 ).grid (row =5 ,column =3 )#line:210
        Label (root ,text ="Weather Description: ",font =fontStyle1 ).grid (row =6 ,column =2 )#line:212
        Label (root ,textvariable =zz ,font =fontStyle1 ).grid (row =6 ,column =3 )#line:214
        Label (root ,text ="Sunrise Time:",font =fontStyle1 ).grid (row =7 ,column =2 )#line:216
        Label (root ,textvariable =dti ,font =fontStyle1 ).grid (row =7 ,column =3 )#line:218
        Label (root ,text ="Sunset Time:",font =fontStyle1 ).grid (row =8 ,column =2 )#line:220
        Label (root ,textvariable =dth ,font =fontStyle1 ).grid (row =8 ,column =3 )#line:222
        label1 =Label (root ,textvariable =jj ,font =fontStyle2 ).grid (row =0 ,column =2 ,columnspan =2 )#line:224
        Label (root ,textvariable =ll ,font =fontStyle2 ).grid (row =1 ,column =2 )#line:227
        Label (root ,textvariable =ee ,font =fontStyle2 ).grid (row =1 ,column =3 )#line:228
        label2=Label (root ,text ="AQI(Hover over me!):",font =fontStyle1 );label2.grid (row =8 ,column =0 )#line:229
        balloon = Balloon(root,bg="white", title="Help")

        balloon.bind_widget(label2,balloonmsg= "AQI Range:\n0-50 : Excellent\n51-100 : Moderate\n101-150 : Unhealthy for sensitive groups\n151-200 : Unhealthy\n201-300 : Very Unhealthy\n301+ : HAZARDOUS")

        Label (root ,textvariable =aq ,font =fontStyle1 ).grid (row =8 ,column =1 )#line:230
    except KeyError :#line:141
        tkinter .messagebox .showerror ("Sys Message","City Not Found")#line:142
    except TypeError :#line:144
        tkinter .messagebox .showerror ("Sys Message","The AQI given for the following country is incorrect, beccause there aren't any nearby air quality stations in this location")#line:145
ct =StringVar ()#line:153
cp =StringVar ()#line:154
ch =StringVar ()#line:155
cm =StringVar ()#line:156
cmi =StringVar ()#line:157
cc =StringVar ()#line:158
aa =StringVar ()#line:159
cs =StringVar ()#line:160
cd =StringVar ()#line:161
zz =StringVar ()#line:162
dd =StringVar ()#line:163
dti =StringVar ()#line:164
dth =StringVar ()#line:165
jj =StringVar ()#line:166
ll =StringVar ()#line:167
ee =StringVar ()#line:168
aq =StringVar ()#line:169
b=Button(root,text="Check",command=startup)
b.grid(row=0,column=1)

city_name =Entry (root ,width =25 )#line:233
city_name .grid (row =0 ,column =0 )#line:234
root .mainloop ()#line:237

