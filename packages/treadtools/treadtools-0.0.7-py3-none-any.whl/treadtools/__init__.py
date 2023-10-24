#!/usr/bin/env python
import warnings #line:7
import traceback #line:8
import ast #line:9
import re #line:10
import xlrd #line:11
import xlwt #line:12
import openpyxl #line:13
import pandas as pd #line:14
import numpy as np #line:15
import math #line:16
import tkinter as Tk #line:17
from tkinter import ttk #line:18
from tkinter import *#line:19
import tkinter .font as tkFont #line:20
from tkinter import filedialog ,dialog ,PhotoImage #line:21
from tkinter .messagebox import showinfo #line:22
from tkinter .scrolledtext import ScrolledText #line:23
import collections #line:24
from collections import Counter #line:25
import datetime #line:26
from datetime import datetime ,timedelta #line:27
from tkinter import END #line:28
import xlsxwriter #line:29
import os #line:30
import time #line:31
import threading #line:32
import pip #line:33
import matplotlib as plt #line:34
import requests #line:35
import random #line:36
from matplotlib .backends .backend_tkagg import FigureCanvasTkAgg #line:38
from matplotlib .figure import Figure #line:39
from matplotlib .backends .backend_tkagg import NavigationToolbar2Tk #line:40
from matplotlib .ticker import PercentFormatter #line:41
from tkinter import ttk ,Menu ,Frame ,Canvas ,StringVar ,LEFT ,RIGHT ,TOP ,BOTTOM ,BOTH ,Y ,X ,YES ,NO ,DISABLED ,END ,Button ,LabelFrame ,GROOVE ,Toplevel ,Label ,Entry ,Scrollbar ,Text ,filedialog ,dialog ,PhotoImage #line:42
global TT_ori #line:45
global TT_biaozhun #line:46
global TT_modex #line:47
global TT_ori_backup #line:48
global version_now #line:49
global usergroup #line:50
global setting_cfg #line:51
global csdir #line:52
TT_biaozhun ={}#line:53
TT_ori =""#line:54
TT_modex =0 #line:55
TT_ori_backup =""#line:56
version_now ="0.0.7"#line:57
usergroup ="用户组=0"#line:58
setting_cfg =""#line:59
csdir =str (os .path .abspath (__file__ )).replace (str (__file__ ),"")#line:61
csdir =csdir +csdir .split ("treadtools")[0 ][-1 ]#line:63
def extract_zip_file (O0O0000000O00O000 ,OOO00O0OO0OO0OOOO ):#line:72
    import zipfile #line:74
    if OOO00O0OO0OO0OOOO =="":#line:75
        return 0 #line:76
    with zipfile .ZipFile (O0O0000000O00O000 ,'r')as OO00000OO0O0O0O0O :#line:77
        for O000OOOO000000OOO in OO00000OO0O0O0O0O .infolist ():#line:78
            O000OOOO000000OOO .filename =O000OOOO000000OOO .filename .encode ('cp437').decode ('gbk')#line:80
            OO00000OO0O0O0O0O .extract (O000OOOO000000OOO ,OOO00O0OO0OO0OOOO )#line:81
def get_directory_path (OO0OO00O0OOO00O00 ):#line:87
    global csdir #line:89
    if not (os .path .isfile (os .path .join (OO0OO00O0OOO00O00 ,'规则文件.xls'))):#line:91
        extract_zip_file (csdir +"def.py",OO0OO00O0OOO00O00 )#line:96
    if OO0OO00O0OOO00O00 =="":#line:98
        quit ()#line:99
    return OO0OO00O0OOO00O00 #line:100
def convert_and_compare_dates (OOOO00OOO0OOOO0O0 ):#line:104
    import datetime #line:105
    OO0OOOO0OOOOOOO0O =datetime .datetime .now ()#line:106
    try :#line:108
       O0O00000OOOO0O0O0 =datetime .datetime .strptime (str (int (int (OOOO00OOO0OOOO0O0 )/4 )),"%Y%m%d")#line:109
    except :#line:110
        print ("fail")#line:111
        return "已过期"#line:112
    if O0O00000OOOO0O0O0 >OO0OOOO0OOOOOOO0O :#line:114
        return "未过期"#line:116
    else :#line:117
        return "已过期"#line:118
def read_setting_cfg ():#line:120
    global csdir #line:121
    if os .path .exists (csdir +'setting.cfg'):#line:123
        text .insert (END ,"已完成初始化\n")#line:124
        with open (csdir +'setting.cfg','r')as O0O00O0OOO00OO0OO :#line:125
            O0OOOOOO0000O0O00 =eval (O0O00O0OOO00OO0OO .read ())#line:126
    else :#line:127
        O000OOO00O00OO00O =csdir +'setting.cfg'#line:129
        with open (O000OOO00O00OO00O ,'w')as O0O00O0OOO00OO0OO :#line:130
            O0O00O0OOO00OO0OO .write ('{"settingdir": 0, "sidori": 0, "sidfinal": "11111180000808"}')#line:131
        text .insert (END ,"未初始化，正在初始化...\n")#line:132
        O0OOOOOO0000O0O00 =read_setting_cfg ()#line:133
    return O0OOOOOO0000O0O00 #line:134
def open_setting_cfg ():#line:137
    global csdir #line:138
    with open (csdir +"setting.cfg","r")as O00O0O0000OO000OO :#line:140
        O000O000000O00OO0 =eval (O00O0O0000OO000OO .read ())#line:142
    return O000O000000O00OO0 #line:143
def update_setting_cfg (O00OO00OOO00OO000 ,OOO0OO0000OO0000O ):#line:145
    global csdir #line:146
    with open (csdir +"setting.cfg","r")as OOOO00OOO0000O00O :#line:148
        O00O00O0OO0O0O0O0 =eval (OOOO00OOO0000O00O .read ())#line:150
    if O00O00O0OO0O0O0O0 [O00OO00OOO00OO000 ]==0 or O00O00O0OO0O0O0O0 [O00OO00OOO00OO000 ]=="11111180000808":#line:152
        O00O00O0OO0O0O0O0 [O00OO00OOO00OO000 ]=OOO0OO0000OO0000O #line:153
        with open (csdir +"setting.cfg","w")as OOOO00OOO0000O00O :#line:155
            OOOO00OOO0000O00O .write (str (O00O00O0OO0O0O0O0 ))#line:156
def generate_random_file ():#line:159
    OO00000O0O0OO0O0O =random .randint (200000 ,299999 )#line:161
    update_setting_cfg ("sidori",OO00000O0O0OO0O0O )#line:163
def display_random_number ():#line:165
    global csdir #line:166
    OO0O0OO0O0OO00OO0 =Toplevel ()#line:167
    OO0O0OO0O0OO00OO0 .title ("ID")#line:168
    OO00O00OO0O0OOOOO =OO0O0OO0O0OO00OO0 .winfo_screenwidth ()#line:170
    O000OO0O0OO000000 =OO0O0OO0O0OO00OO0 .winfo_screenheight ()#line:171
    O0O00O00O0OOO0O0O =80 #line:173
    O0OO0O0O0OO00O000 =70 #line:174
    O0O00OOO0O0OOO000 =(OO00O00OO0O0OOOOO -O0O00O00O0OOO0O0O )/2 #line:176
    OOO0000O0O0O0OO0O =(O000OO0O0OO000000 -O0OO0O0O0OO00O000 )/2 #line:177
    OO0O0OO0O0OO00OO0 .geometry ("%dx%d+%d+%d"%(O0O00O00O0OOO0O0O ,O0OO0O0O0OO00O000 ,O0O00OOO0O0OOO000 ,OOO0000O0O0O0OO0O ))#line:178
    with open (csdir +"setting.cfg","r")as OOO0OO000O0000O0O :#line:181
        OOO00O0000OOO0O0O =eval (OOO0OO000O0000O0O .read ())#line:183
    O00OO0O0OO0O0O0OO =int (OOO00O0000OOO0O0O ["sidori"])#line:184
    O000O0O0O0O0OOO00 =O00OO0O0OO0O0O0OO *2 +183576 #line:185
    print (O000O0O0O0O0OOO00 )#line:187
    OO0O00O000O000OOO =ttk .Label (OO0O0OO0O0OO00OO0 ,text =f"机器码: {O00OO0O0OO0O0O0OO}")#line:189
    OOO00O0000OO000OO =ttk .Entry (OO0O0OO0O0OO00OO0 )#line:190
    OO0O00O000O000OOO .pack ()#line:193
    OOO00O0000OO000OO .pack ()#line:194
    ttk .Button (OO0O0OO0O0OO00OO0 ,text ="验证",command =lambda :check_input (OOO00O0000OO000OO .get (),O000O0O0O0O0OOO00 )).pack ()#line:198
def check_input (O000OO0OO000O00O0 ,O0O000O0O0O0OOOO0 ):#line:200
    try :#line:204
        OOO00O0O000OO0000 =int (str (O000OO0OO000O00O0 )[0 :6 ])#line:205
        O0OO0OO0O00O0OOO0 =convert_and_compare_dates (str (O000OO0OO000O00O0 )[6 :14 ])#line:206
    except :#line:207
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:208
        return 0 #line:209
    if OOO00O0O000OO0000 ==O0O000O0O0O0OOOO0 and O0OO0OO0O00O0OOO0 =="未过期":#line:211
        update_setting_cfg ("sidfinal",O000OO0OO000O00O0 )#line:212
        showinfo (title ="提示",message ="注册成功,请重新启动程序。")#line:213
        quit ()#line:214
    else :#line:215
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:216
def update_software (O00000O0O0000O0O0 ):#line:220
    global version_now #line:222
    text .insert (END ,"当前版本为："+version_now +",正在检查更新...(您可以同时执行分析任务)")#line:223
    try :#line:224
        OO0O00O0O00O0O000 =requests .get (f"https://pypi.org/pypi/{O00000O0O0000O0O0}/json",timeout =2 ).json ()["info"]["version"]#line:225
    except :#line:226
        return "...更新失败。"#line:227
    if OO0O00O0O00O0O000 >version_now :#line:228
        text .insert (END ,"\n最新版本为："+OO0O00O0O00O0O000 +",正在尝试自动更新....")#line:229
        pip .main (['install',O00000O0O0000O0O0 ,'--upgrade'])#line:231
        text .insert (END ,"\n您可以开展工作。")#line:232
        return "...更新成功。"#line:233
def Tread_TOOLS_fileopen (OOO0000O000O00OO0 ):#line:237
    ""#line:238
    global TT_ori #line:239
    global TT_ori_backup #line:240
    global TT_biaozhun #line:241
    warnings .filterwarnings ('ignore')#line:242
    if OOO0000O000O00OO0 ==0 :#line:244
        O0O0OO0000OO0000O =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:245
        OOO0OOOOO00OO0O0O =[pd .read_excel (OO0OOOOO0O0OOOOOO ,header =0 ,sheet_name =0 )for OO0OOOOO0O0OOOOOO in O0O0OO0000OO0000O ]#line:246
        OOOOOO000O00OOO00 =pd .concat (OOO0OOOOO00OO0O0O ,ignore_index =True ).drop_duplicates ()#line:247
        try :#line:248
            OOOOOO000O00OOO00 =OOOOOO000O00OOO00 .loc [:,~TT_ori .columns .str .contains ("^Unnamed")]#line:249
        except :#line:250
            pass #line:251
        TT_ori_backup =OOOOOO000O00OOO00 .copy ()#line:252
        TT_ori =Tread_TOOLS_CLEAN (OOOOOO000O00OOO00 ).copy ()#line:253
        text .insert (END ,"\n原始数据导入成功，行数："+str (len (TT_ori )))#line:255
        text .insert (END ,"\n数据校验：\n")#line:256
        text .insert (END ,TT_ori )#line:257
        text .see (END )#line:258
    if OOO0000O000O00OO0 ==1 :#line:260
        OOOOOOOO0OOO00O0O =filedialog .askopenfilename (filetypes =[("XLS",".xls")])#line:261
        TT_biaozhun ["关键字表"]=pd .read_excel (OOOOOOOO0OOO00O0O ,sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:262
        TT_biaozhun ["产品批号"]=pd .read_excel (OOOOOOOO0OOO00O0O ,sheet_name ="产品批号",header =0 ,index_col =0 ,).reset_index ()#line:263
        TT_biaozhun ["事件发生月份"]=pd .read_excel (OOOOOOOO0OOO00O0O ,sheet_name ="事件发生月份",header =0 ,index_col =0 ,).reset_index ()#line:264
        TT_biaozhun ["事件发生季度"]=pd .read_excel (OOOOOOOO0OOO00O0O ,sheet_name ="事件发生季度",header =0 ,index_col =0 ,).reset_index ()#line:265
        TT_biaozhun ["规格"]=pd .read_excel (OOOOOOOO0OOO00O0O ,sheet_name ="规格",header =0 ,index_col =0 ,).reset_index ()#line:266
        TT_biaozhun ["型号"]=pd .read_excel (OOOOOOOO0OOO00O0O ,sheet_name ="型号",header =0 ,index_col =0 ,).reset_index ()#line:267
        TT_biaozhun ["设置"]=pd .read_excel (OOOOOOOO0OOO00O0O ,sheet_name ="设置",header =0 ,index_col =0 ,).reset_index ()#line:268
        Tread_TOOLS_check (TT_ori ,TT_biaozhun ["关键字表"],0 )#line:269
        text .insert (END ,"\n标准导入成功，行数："+str (len (TT_biaozhun )))#line:270
        text .see (END )#line:271
def Tread_TOOLS_check (O00OOOO0O000OO00O ,O00000O0OO0O0O000 ,OOOO0O0OOOO0OO00O ):#line:273
        ""#line:274
        global TT_ori #line:275
        OO0OO00OO0O000OOO =Tread_TOOLS_Countall (O00OOOO0O000OO00O ).df_psur (O00000O0OO0O0O000 )#line:276
        if OOOO0O0OOOO0OO00O ==0 :#line:278
            Tread_TOOLS_tree_Level_2 (OO0OO00OO0O000OOO ,0 ,TT_ori .copy ())#line:280
        OO0OO00OO0O000OOO ["核验"]=0 #line:283
        OO0OO00OO0O000OOO .loc [(OO0OO00OO0O000OOO ["关键字标记"].str .contains ("-其他关键字-",na =False )),"核验"]=OO0OO00OO0O000OOO .loc [(OO0OO00OO0O000OOO ["关键字标记"].str .contains ("-其他关键字-",na =False )),"总数量"]#line:284
        if OO0OO00OO0O000OOO ["核验"].sum ()>0 :#line:285
            showinfo (title ="温馨提示",message ="存在未定义类型的报告"+str (OO0OO00OO0O000OOO ["核验"].sum ())+"条，趋势分析可能会存在遗漏，建议修正该错误再进行下一步。")#line:286
def Tread_TOOLS_tree_Level_2 (O0OOO000OO0O00O0O ,O0O000O0O0OOO00OO ,OO0000O0OOO0O0O0O ,*OOO00O0OOO0OO0O00 ):#line:288
    ""#line:289
    global TT_ori_backup #line:291
    OOO0000O00O00O0OO =O0OOO000OO0O00O0O .columns .values .tolist ()#line:293
    O0O000O0O0OOO00OO =0 #line:294
    O00O0O0000OO0O000 =O0OOO000OO0O00O0O .loc [:]#line:295
    OO000OOOOO0O0OOOO =0 #line:299
    try :#line:300
        OO0000O0OO000O0O0 =OOO00O0OOO0OO0O00 [0 ]#line:301
        OO000OOOOO0O0OOOO =1 #line:302
    except :#line:303
        pass #line:304
    O0OOOOOOO00O00O0O =Toplevel ()#line:307
    O0OOOOOOO00O00O0O .title ("报表查看器")#line:308
    OOOOOO000O00O00O0 =O0OOOOOOO00O00O0O .winfo_screenwidth ()#line:309
    O0O00O0O000O00OOO =O0OOOOOOO00O00O0O .winfo_screenheight ()#line:311
    O000OOOOOO0OOO00O =1300 #line:313
    O0OO00OOO000000O0 =600 #line:314
    OOO00O000OO0000O0 =(OOOOOO000O00O00O0 -O000OOOOOO0OOO00O )/2 #line:316
    O00OOOOO0OOO00O0O =(O0O00O0O000O00OOO -O0OO00OOO000000O0 )/2 #line:317
    O0OOOOOOO00O00O0O .geometry ("%dx%d+%d+%d"%(O000OOOOOO0OOO00O ,O0OO00OOO000000O0 ,OOO00O000OO0000O0 ,O00OOOOO0OOO00O0O ))#line:318
    O000OOO000O00OOOO =ttk .Frame (O0OOOOOOO00O00O0O ,width =1300 ,height =20 )#line:319
    O000OOO000O00OOOO .pack (side =BOTTOM )#line:320
    OO0O0O0000O000OOO =ttk .Frame (O0OOOOOOO00O00O0O ,width =1300 ,height =20 )#line:322
    OO0O0O0000O000OOO .pack (side =TOP )#line:323
    if 1 >0 :#line:327
        O0O000OOO0OOO0OO0 =Button (O000OOO000O00OOOO ,text ="控制图(所有)",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (O00O0O0000OO0O000 [:-1 ],OO0000O0OO000O0O0 ,[O0O0000O000O000OO for O0O0000O000O000OO in O00O0O0000OO0O000 .columns if (O0O0000O000O000OO not in [OO0000O0OO000O0O0 ])],"关键字趋势图",100 ),)#line:337
        if OO000OOOOO0O0OOOO ==1 :#line:338
            O0O000OOO0OOO0OO0 .pack (side =LEFT )#line:339
        O0O000OOO0OOO0OO0 =Button (O000OOO000O00OOOO ,text ="控制图(总数量)",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (O00O0O0000OO0O000 [:-1 ],OO0000O0OO000O0O0 ,[O0OO0O0000O0OO0O0 for O0OO0O0000O0OO0O0 in O00O0O0000OO0O000 .columns if (O0OO0O0000O0OO0O0 in ["该元素总数量"])],"关键字趋势图",100 ),)#line:349
        if OO000OOOOO0O0OOOO ==1 :#line:350
            O0O000OOO0OOO0OO0 .pack (side =LEFT )#line:351
        O0O0OO00OOOOO00O0 =Button (O000OOO000O00OOOO ,text ="导出",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_save_dict (O00O0O0000OO0O000 ),)#line:361
        O0O0OO00OOOOO00O0 .pack (side =LEFT )#line:362
        O0O0OO00OOOOO00O0 =Button (O000OOO000O00OOOO ,text ="发生率测算",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_fashenglv (O00O0O0000OO0O000 ,OO0000O0OO000O0O0 ),)#line:372
        if "关键字标记"not in O00O0O0000OO0O000 .columns and "报告编码"not in O00O0O0000OO0O000 .columns :#line:373
            if "对象"not in O00O0O0000OO0O000 .columns :#line:374
                O0O0OO00OOOOO00O0 .pack (side =LEFT )#line:375
        O0O0OO00OOOOO00O0 =Button (O000OOO000O00OOOO ,text ="直方图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_histbar (O00O0O0000OO0O000 .copy ()),)#line:385
        if "对象"in O00O0O0000OO0O000 .columns :#line:386
            O0O0OO00OOOOO00O0 .pack (side =LEFT )#line:387
        OOO0000OO00000O0O =Button (O000OOO000O00OOOO ,text ="行数:"+str (len (O00O0O0000OO0O000 )),bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",)#line:397
        OOO0000OO00000O0O .pack (side =LEFT )#line:398
    O00O0000000O0OO0O =O00O0O0000OO0O000 .values .tolist ()#line:401
    O000O0O000OO0OOOO =O00O0O0000OO0O000 .columns .values .tolist ()#line:402
    O0O0OOOO0OOOOOO0O =ttk .Treeview (OO0O0O0000O000OOO ,columns =O000O0O000OO0OOOO ,show ="headings",height =45 )#line:403
    for O000O000000OO0O0O in O000O0O000OO0OOOO :#line:405
        O0O0OOOO0OOOOOO0O .heading (O000O000000OO0O0O ,text =O000O000000OO0O0O )#line:406
    for O00OOO0OO0O000000 in O00O0000000O0OO0O :#line:407
        O0O0OOOO0OOOOOO0O .insert ("","end",values =O00OOO0OO0O000000 )#line:408
    for OO0O0OO00O00000OO in O000O0O000OO0OOOO :#line:409
        O0O0OOOO0OOOOOO0O .column (OO0O0OO00O00000OO ,minwidth =0 ,width =120 ,stretch =NO )#line:410
    OOO000OO0O0OOO0O0 =Scrollbar (OO0O0O0000O000OOO ,orient ="vertical")#line:412
    OOO000OO0O0OOO0O0 .pack (side =RIGHT ,fill =Y )#line:413
    OOO000OO0O0OOO0O0 .config (command =O0O0OOOO0OOOOOO0O .yview )#line:414
    O0O0OOOO0OOOOOO0O .config (yscrollcommand =OOO000OO0O0OOO0O0 .set )#line:415
    O00OOO0OO0O000O00 =Scrollbar (OO0O0O0000O000OOO ,orient ="horizontal")#line:417
    O00OOO0OO0O000O00 .pack (side =BOTTOM ,fill =X )#line:418
    O00OOO0OO0O000O00 .config (command =O0O0OOOO0OOOOOO0O .xview )#line:419
    O0O0OOOO0OOOOOO0O .config (yscrollcommand =OOO000OO0O0OOO0O0 .set )#line:420
    def OO00000OO00O00OO0 (O0O00OO0OO00OOOOO ,OOOOO0O00OOO0O0O0 ,OO00O0OOO00O0O0OO ):#line:422
        for O00O0O0000O000000 in O0O0OOOO0OOOOOO0O .selection ():#line:425
            O0OO00OO0O0O00O0O =O0O0OOOO0OOOOOO0O .item (O00O0O0000O000000 ,"values")#line:426
            OOO0000OO0OOOO0O0 =dict (zip (OOOOO0O00OOO0O0O0 ,O0OO00OO0O0O00O0O ))#line:427
        if "该分类下各项计数"in OOOOO0O00OOO0O0O0 :#line:429
            OOOOOO0O000OOO0O0 =OO0000O0OOO0O0O0O .copy ()#line:430
            OOOOOO0O000OOO0O0 ["关键字查找列"]=""#line:431
            for O0O0OOOO0OO0O00O0 in TOOLS_get_list (OOO0000OO0OOOO0O0 ["查找位置"]):#line:432
                OOOOOO0O000OOO0O0 ["关键字查找列"]=OOOOOO0O000OOO0O0 ["关键字查找列"]+OOOOOO0O000OOO0O0 [O0O0OOOO0OO0O00O0 ].astype ("str")#line:433
            OOOO00OO0O00O00OO =OOOOOO0O000OOO0O0 .loc [OOOOOO0O000OOO0O0 ["关键字查找列"].str .contains (OOO0000OO0OOOO0O0 ["关键字标记"],na =False )].copy ()#line:434
            OOOO00OO0O00O00OO =OOOO00OO0O00O00OO .loc [~OOOO00OO0O00O00OO ["关键字查找列"].str .contains (OOO0000OO0OOOO0O0 ["排除值"],na =False )].copy ()#line:435
            Tread_TOOLS_tree_Level_2 (OOOO00OO0O00O00OO ,0 ,OOOO00OO0O00O00OO )#line:441
            return 0 #line:442
        if "报告编码"in OOOOO0O00OOO0O0O0 :#line:444
            OOOO0OOO00O000OOO =Toplevel ()#line:445
            O000OO000OO0O0O00 =OOOO0OOO00O000OOO .winfo_screenwidth ()#line:446
            OOO00OO000OO0O0O0 =OOOO0OOO00O000OOO .winfo_screenheight ()#line:448
            OO00OO0OOO00O000O =800 #line:450
            OOO0OOO0O00OO00OO =600 #line:451
            O0O0OOOO0OO0O00O0 =(O000OO000OO0O0O00 -OO00OO0OOO00O000O )/2 #line:453
            OOO0O00000O00OOOO =(OOO00OO000OO0O0O0 -OOO0OOO0O00OO00OO )/2 #line:454
            OOOO0OOO00O000OOO .geometry ("%dx%d+%d+%d"%(OO00OO0OOO00O000O ,OOO0OOO0O00OO00OO ,O0O0OOOO0OO0O00O0 ,OOO0O00000O00OOOO ))#line:455
            OOOOOO0OOOO0OOO0O =ScrolledText (OOOO0OOO00O000OOO ,height =1100 ,width =1100 ,bg ="#FFFFFF")#line:459
            OOOOOO0OOOO0OOO0O .pack (padx =10 ,pady =10 )#line:460
            def OO00O00O00O0O0O0O (event =None ):#line:461
                OOOOOO0OOOO0OOO0O .event_generate ('<<Copy>>')#line:462
            def OOO0OO0OOOOOO00OO (O00OO0OO0O000OOO0 ,OOOOOO0O0O0O00OO0 ):#line:463
                O000OOO0O0000000O =open (OOOOOO0O0O0O00OO0 ,"w",encoding ='utf-8')#line:464
                O000OOO0O0000000O .write (O00OO0OO0O000OOO0 )#line:465
                O000OOO0O0000000O .flush ()#line:467
                showinfo (title ="提示信息",message ="保存成功。")#line:468
            O0O0O0OO0O0O0000O =Menu (OOOOOO0OOOO0OOO0O ,tearoff =False ,)#line:470
            O0O0O0OO0O0O0000O .add_command (label ="复制",command =OO00O00O00O0O0O0O )#line:471
            O0O0O0OO0O0O0000O .add_command (label ="导出",command =lambda :thread_it (OOO0OO0OOOOOO00OO ,OOOOOO0OOOO0OOO0O .get (1.0 ,'end'),filedialog .asksaveasfilename (title =u"保存文件",initialfile =OOO0000OO0OOOO0O0 ["报告编码"],defaultextension ="txt",filetypes =[("txt","*.txt")])))#line:472
            def OOO000OOOOOOO0OOO (OOOOO00000OO00O0O ):#line:474
                O0O0O0OO0O0O0000O .post (OOOOO00000OO00O0O .x_root ,OOOOO00000OO00O0O .y_root )#line:475
            OOOOOO0OOOO0OOO0O .bind ("<Button-3>",OOO000OOOOOOO0OOO )#line:476
            OOOO0OOO00O000OOO .title (OOO0000OO0OOOO0O0 ["报告编码"])#line:478
            for O00O0O0OOO0OOOOO0 in range (len (OOOOO0O00OOO0O0O0 )):#line:479
                OOOOOO0OOOO0OOO0O .insert (END ,OOOOO0O00OOO0O0O0 [O00O0O0OOO0OOOOO0 ])#line:481
                OOOOOO0OOOO0OOO0O .insert (END ,"：")#line:482
                OOOOOO0OOOO0OOO0O .insert (END ,OOO0000OO0OOOO0O0 [OOOOO0O00OOO0O0O0 [O00O0O0OOO0OOOOO0 ]])#line:483
                OOOOOO0OOOO0OOO0O .insert (END ,"\n")#line:484
            OOOOOO0OOOO0OOO0O .config (state =DISABLED )#line:485
            return 0 #line:486
        OOO0O00000O00OOOO =O0OO00OO0O0O00O0O [1 :-1 ]#line:489
        O0O0OOOO0OO0O00O0 =OO00O0OOO00O0O0OO .columns .tolist ()#line:491
        O0O0OOOO0OO0O00O0 =O0O0OOOO0OO0O00O0 [1 :-1 ]#line:492
        O000000O0OOO0O00O ={'关键词':O0O0OOOO0OO0O00O0 ,'数量':OOO0O00000O00OOOO }#line:494
        O000000O0OOO0O00O =pd .DataFrame .from_dict (O000000O0OOO0O00O )#line:495
        O000000O0OOO0O00O ["数量"]=O000000O0OOO0O00O ["数量"].astype (float )#line:496
        Tread_TOOLS_draw (O000000O0OOO0O00O ,"帕累托图",'关键词','数量',"帕累托图")#line:497
        return 0 #line:498
    O0O0OOOO0OOOOOO0O .bind ("<Double-1>",lambda OO00OOO0OO00000O0 :OO00000OO00O00OO0 (OO00OOO0OO00000O0 ,O000O0O000OO0OOOO ,O00O0O0000OO0O000 ),)#line:506
    O0O0OOOO0OOOOOO0O .pack ()#line:507
class Tread_TOOLS_Countall ():#line:509
    ""#line:510
    def __init__ (O000OOO00OOO00O0O ,O0O00O00OOOO0OO0O ):#line:511
        ""#line:512
        O000OOO00OOO00O0O .df =O0O00O00OOOO0OO0O #line:513
    def df_psur (OOOO000OOO0O0O000 ,O00OOOO00OO0O000O ,*OOOOO0O00000O00O0 ):#line:515
        ""#line:516
        global TT_biaozhun #line:517
        O00OOO00000O0OOO0 =OOOO000OOO0O0O000 .df .copy ()#line:518
        O0000OO0O0OO00OO0 =len (O00OOO00000O0OOO0 .drop_duplicates ("报告编码"))#line:520
        OO0OO0OOOO0000O00 =O00OOOO00OO0O000O .copy ()#line:523
        O00O0O00000O0OO0O =TT_biaozhun ["设置"]#line:526
        if O00O0O00000O0OO0O .loc [1 ,"值"]:#line:527
            O0O0000O000O0OO0O =O00O0O00000O0OO0O .loc [1 ,"值"]#line:528
        else :#line:529
            O0O0000O000O0OO0O ="透视列"#line:530
            O00OOO00000O0OOO0 [O0O0000O000O0OO0O ]="未正确设置"#line:531
        O00OO0O0O0O0OO0OO =""#line:533
        OO0000OOOO00000OO ="-其他关键字-"#line:534
        for O00OOOO00OO000OOO ,O000OOOOO00000OOO in OO0OO0OOOO0000O00 .iterrows ():#line:535
            OO0000OOOO00000OO =OO0000OOOO00000OO +"|"+str (O000OOOOO00000OOO ["值"])#line:536
            O00OOOO000O00O00O =O000OOOOO00000OOO #line:537
        O00OOOO000O00O00O [3 ]=OO0000OOOO00000OO #line:538
        O00OOOO000O00O00O [2 ]="-其他关键字-|"#line:539
        OO0OO0OOOO0000O00 .loc [len (OO0OO0OOOO0000O00 )]=O00OOOO000O00O00O #line:540
        OO0OO0OOOO0000O00 =OO0OO0OOOO0000O00 .reset_index (drop =True )#line:541
        O00OOO00000O0OOO0 ["关键字查找列"]=""#line:545
        for OOO000O00O00000O0 in TOOLS_get_list (OO0OO0OOOO0000O00 .loc [0 ,"查找位置"]):#line:546
            O00OOO00000O0OOO0 ["关键字查找列"]=O00OOO00000O0OOO0 ["关键字查找列"]+O00OOO00000O0OOO0 [OOO000O00O00000O0 ].astype ("str")#line:547
        OOOOO00OO0O0OO0O0 =[]#line:550
        for O00OOOO00OO000OOO ,O000OOOOO00000OOO in OO0OO0OOOO0000O00 .iterrows ():#line:551
            OOO00O0O00O00000O =O000OOOOO00000OOO ["值"]#line:552
            O000O00000OOO0OO0 =O00OOO00000O0OOO0 .loc [O00OOO00000O0OOO0 ["关键字查找列"].str .contains (OOO00O0O00O00000O ,na =False )].copy ()#line:553
            if str (O000OOOOO00000OOO ["排除值"])!="nan":#line:554
                O000O00000OOO0OO0 =O000O00000OOO0OO0 .loc [~O000O00000OOO0OO0 ["关键字查找列"].str .contains (str (O000OOOOO00000OOO ["排除值"]),na =False )].copy ()#line:555
            O000O00000OOO0OO0 ["关键字标记"]=str (OOO00O0O00O00000O )#line:557
            O000O00000OOO0OO0 ["关键字计数"]=1 #line:558
            if len (O000O00000OOO0OO0 )>0 :#line:560
                OO0O00OO00OO0OOO0 =pd .pivot_table (O000O00000OOO0OO0 .drop_duplicates ("报告编码"),values =["关键字计数"],index ="关键字标记",columns =O0O0000O000O0OO0O ,aggfunc ={"关键字计数":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:570
                OO0O00OO00OO0OOO0 =OO0O00OO00OO0OOO0 [:-1 ]#line:571
                OO0O00OO00OO0OOO0 .columns =OO0O00OO00OO0OOO0 .columns .droplevel (0 )#line:572
                OO0O00OO00OO0OOO0 =OO0O00OO00OO0OOO0 .reset_index ()#line:573
                if len (OO0O00OO00OO0OOO0 )>0 :#line:576
                    O00OO000O0OOOOO00 =str (Counter (TOOLS_get_list0 ("use(关键字查找列).file",O000O00000OOO0OO0 ,1000 ))).replace ("Counter({","{")#line:577
                    O00OO000O0OOOOO00 =O00OO000O0OOOOO00 .replace ("})","}")#line:578
                    O00OO000O0OOOOO00 =ast .literal_eval (O00OO000O0OOOOO00 )#line:579
                    OO0O00OO00OO0OOO0 .loc [0 ,"事件分类"]=str (TOOLS_get_list (OO0O00OO00OO0OOO0 .loc [0 ,"关键字标记"])[0 ])#line:581
                    OO0O00OO00OO0OOO0 .loc [0 ,"该分类下各项计数"]=str ({OOO0O0O000O000OOO :OO000O00OOO0OOOOO for OOO0O0O000O000OOO ,OO000O00OOO0OOOOO in O00OO000O0OOOOO00 .items ()if STAT_judge_x (str (OOO0O0O000O000OOO ),TOOLS_get_list (OOO00O0O00O00000O ))==1 })#line:582
                    OO0O00OO00OO0OOO0 .loc [0 ,"其他分类各项计数"]=str ({O0000O0O0OO00O00O :OOOOO00O0OO0O000O for O0000O0O0OO00O00O ,OOOOO00O0OO0O000O in O00OO000O0OOOOO00 .items ()if STAT_judge_x (str (O0000O0O0OO00O00O ),TOOLS_get_list (OOO00O0O00O00000O ))!=1 })#line:583
                    OO0O00OO00OO0OOO0 ["查找位置"]=O000OOOOO00000OOO ["查找位置"]#line:584
                    OOOOO00OO0O0OO0O0 .append (OO0O00OO00OO0OOO0 )#line:587
        O00OO0O0O0O0OO0OO =pd .concat (OOOOO00OO0O0OO0O0 )#line:588
        O00OO0O0O0O0OO0OO =O00OO0O0O0O0OO0OO .sort_values (by =["All"],ascending =[False ],na_position ="last")#line:593
        O00OO0O0O0O0OO0OO =O00OO0O0O0O0OO0OO .reset_index ()#line:594
        O00OO0O0O0O0OO0OO ["All占比"]=round (O00OO0O0O0O0OO0OO ["All"]/O0000OO0O0OO00OO0 *100 ,2 )#line:596
        O00OO0O0O0O0OO0OO =O00OO0O0O0O0OO0OO .rename (columns ={"All":"总数量","All占比":"总数量占比"})#line:597
        for O00OOOOOOOO0000OO ,O0O0000O0OO00O0O0 in OO0OO0OOOO0000O00 .iterrows ():#line:600
            O00OO0O0O0O0OO0OO .loc [(O00OO0O0O0O0OO0OO ["关键字标记"].astype (str )==str (O0O0000O0OO00O0O0 ["值"])),"排除值"]=O0O0000O0OO00O0O0 ["排除值"]#line:601
            O00OO0O0O0O0OO0OO .loc [(O00OO0O0O0O0OO0OO ["关键字标记"].astype (str )==str (O0O0000O0OO00O0O0 ["值"])),"查找位置"]=O0O0000O0OO00O0O0 ["查找位置"]#line:602
        O00OO0O0O0O0OO0OO ["排除值"]=O00OO0O0O0O0OO0OO ["排除值"].fillna ("-没有排除值-")#line:604
        O00OO0O0O0O0OO0OO ["报表类型"]="PSUR"#line:607
        del O00OO0O0O0O0OO0OO ["index"]#line:608
        try :#line:609
            del O00OO0O0O0O0OO0OO ["未正确设置"]#line:610
        except :#line:611
            pass #line:612
        return O00OO0O0O0O0OO0OO #line:613
    def df_find_all_keword_risk (OOO0O0OOOO0OOO0O0 ,O000000OO00O0OO00 ,*OO000OOOOO0OOOO0O ):#line:616
        ""#line:617
        global TT_biaozhun #line:618
        O000O0O00OO0O0000 =OOO0O0OOOO0OOO0O0 .df .copy ()#line:620
        O0OO0000O0OO00O0O =time .time ()#line:621
        O0O000OO0000O0OOO =TT_biaozhun ["关键字表"].copy ()#line:623
        OO000O00000OOOOO0 ="作用对象"#line:625
        O000OO00O000000O0 ="报告编码"#line:627
        O0O0OOO00OOO00OO0 =O000O0O00OO0O0000 .groupby ([OO000O00000OOOOO0 ]).agg (总数量 =(O000OO00O000000O0 ,"nunique"),).reset_index ()#line:630
        O00O0OOOO00OO00OO =[OO000O00000OOOOO0 ,O000000OO00O0OO00 ]#line:632
        OOO0OO000O00000O0 =O000O0O00OO0O0000 .groupby (O00O0OOOO00OO00OO ).agg (该元素总数量 =(OO000O00000OOOOO0 ,"count"),).reset_index ()#line:636
        OOOO0O0O000OO00O0 =[]#line:638
        OO00OO000O0O0OOO0 =0 #line:642
        O0O00O00O0000OOO0 =int (len (O0O0OOO00OOO00OO0 ))#line:643
        for O000O0OO0O0OO0000 ,O00OOOO0OOO00OOO0 in zip (O0O0OOO00OOO00OO0 [OO000O00000OOOOO0 ].values ,O0O0OOO00OOO00OO0 ["总数量"].values ):#line:644
            OO00OO000O0O0OOO0 +=1 #line:645
            O0O0O00OO00OOO0O0 =O000O0O00OO0O0000 [(O000O0O00OO0O0000 [OO000O00000OOOOO0 ]==O000O0OO0O0OO0000 )].copy ()#line:646
            for OOOOO000OOO0OO0O0 ,OO0O00OOO0000OO00 ,OOOOO000OO0O00OO0 in zip (O0O000OO0000O0OOO ["值"].values ,O0O000OO0000O0OOO ["查找位置"].values ,O0O000OO0000O0OOO ["排除值"].values ):#line:648
                    O0OOO0OOO0O00OOOO =O0O0O00OO00OOO0O0 .copy ()#line:649
                    O0O0OOO0O0OOOOOO0 =TOOLS_get_list (OOOOO000OOO0OO0O0 )[0 ]#line:650
                    O0OOO0OOO0O00OOOO ["关键字查找列"]=""#line:652
                    for O000O0000O00O00OO in TOOLS_get_list (OO0O00OOO0000OO00 ):#line:653
                        O0OOO0OOO0O00OOOO ["关键字查找列"]=O0OOO0OOO0O00OOOO ["关键字查找列"]+O0OOO0OOO0O00OOOO [O000O0000O00O00OO ].astype ("str")#line:654
                    O0OOO0OOO0O00OOOO .loc [O0OOO0OOO0O00OOOO ["关键字查找列"].str .contains (OOOOO000OOO0OO0O0 ,na =False ),"关键字"]=O0O0OOO0O0OOOOOO0 #line:656
                    if str (OOOOO000OO0O00OO0 )!="nan":#line:661
                        O0OOO0OOO0O00OOOO =O0OOO0OOO0O00OOOO .loc [~O0OOO0OOO0O00OOOO ["关键字查找列"].str .contains (OOOOO000OO0O00OO0 ,na =False )].copy ()#line:662
                    if (len (O0OOO0OOO0O00OOOO ))<1 :#line:664
                        continue #line:666
                    OOOO00OOOOO00000O =STAT_find_keyword_risk (O0OOO0OOO0O00OOOO ,[OO000O00000OOOOO0 ,"关键字"],"关键字",O000000OO00O0OO00 ,int (O00OOOO0OOO00OOO0 ))#line:668
                    if len (OOOO00OOOOO00000O )>0 :#line:669
                        OOOO00OOOOO00000O ["关键字组合"]=OOOOO000OOO0OO0O0 #line:670
                        OOOO00OOOOO00000O ["排除值"]=OOOOO000OO0O00OO0 #line:671
                        OOOO00OOOOO00000O ["关键字查找列"]=OO0O00OOO0000OO00 #line:672
                        OOOO0O0O000OO00O0 .append (OOOO00OOOOO00000O )#line:673
        if len (OOOO0O0O000OO00O0 )<1 :#line:676
            showinfo (title ="错误信息",message ="该注册证号未检索到任何关键字，规则制定存在缺陷。")#line:677
            return 0 #line:678
        O00O0O0O000O00O00 =pd .concat (OOOO0O0O000OO00O0 )#line:679
        O00O0O0O000O00O00 =pd .merge (O00O0O0O000O00O00 ,OOO0OO000O00000O0 ,on =O00O0OOOO00OO00OO ,how ="left")#line:682
        O00O0O0O000O00O00 ["关键字数量比例"]=round (O00O0O0O000O00O00 ["计数"]/O00O0O0O000O00O00 ["该元素总数量"],2 )#line:683
        O00O0O0O000O00O00 =O00O0O0O000O00O00 .reset_index (drop =True )#line:685
        if len (O00O0O0O000O00O00 )>0 :#line:688
            O00O0O0O000O00O00 ["风险评分"]=0 #line:689
            O00O0O0O000O00O00 ["报表类型"]="keyword_findrisk"+O000000OO00O0OO00 #line:690
            O00O0O0O000O00O00 .loc [(O00O0O0O000O00O00 ["计数"]>=3 ),"风险评分"]=O00O0O0O000O00O00 ["风险评分"]+3 #line:691
            O00O0O0O000O00O00 .loc [(O00O0O0O000O00O00 ["计数"]>=(O00O0O0O000O00O00 ["数量均值"]+O00O0O0O000O00O00 ["数量标准差"])),"风险评分"]=O00O0O0O000O00O00 ["风险评分"]+1 #line:692
            O00O0O0O000O00O00 .loc [(O00O0O0O000O00O00 ["计数"]>=O00O0O0O000O00O00 ["数量CI"]),"风险评分"]=O00O0O0O000O00O00 ["风险评分"]+1 #line:693
            O00O0O0O000O00O00 .loc [(O00O0O0O000O00O00 ["关键字数量比例"]>0.5 )&(O00O0O0O000O00O00 ["计数"]>=3 ),"风险评分"]=O00O0O0O000O00O00 ["风险评分"]+1 #line:694
            O00O0O0O000O00O00 =O00O0O0O000O00O00 .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:696
        OOOO0OO00000O0OOO =O00O0O0O000O00O00 .columns .to_list ()#line:706
        O000O000O000OO0O0 =OOOO0OO00000O0OOO [OOOO0OO00000O0OOO .index ("关键字")+1 ]#line:707
        O000O000OO00OO000 =pd .pivot_table (O00O0O0O000O00O00 ,index =O000O000O000OO0O0 ,columns ="关键字",values =["计数"],aggfunc ={"计数":"sum"},fill_value ="0",margins =True ,dropna =False ,)#line:718
        O000O000OO00OO000 .columns =O000O000OO00OO000 .columns .droplevel (0 )#line:719
        O000O000OO00OO000 =pd .merge (O000O000OO00OO000 ,O00O0O0O000O00O00 [[O000O000O000OO0O0 ,"该元素总数量"]].drop_duplicates (O000O000O000OO0O0 ),on =[O000O000O000OO0O0 ],how ="left")#line:722
        del O000O000OO00OO000 ["All"]#line:724
        O000O000OO00OO000 .iloc [-1 ,-1 ]=O000O000OO00OO000 ["该元素总数量"].sum (axis =0 )#line:725
        print ("耗时：",(time .time ()-O0OO0000O0OO00O0O ))#line:727
        return O000O000OO00OO000 #line:730
def Tread_TOOLS_bar (OO0O0OO00O0O00O0O ):#line:738
         ""#line:739
         O0OOO00OOO0OOOO0O =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:740
         O00000O0O0OOO0O0O =[pd .read_excel (OO0OO00OOOOO0O0O0 ,header =0 ,sheet_name =0 )for OO0OO00OOOOO0O0O0 in O0OOO00OOO0OOOO0O ]#line:741
         O000O00O00O0O00O0 =pd .concat (O00000O0O0OOO0O0O ,ignore_index =True )#line:742
         OOOO000O00O0O00OO =pd .pivot_table (O000O00O00O0O00O0 ,index ="对象",columns ="关键词",values =OO0O0OO00O0O00O0O ,aggfunc ="sum",fill_value ="0",margins =True ,dropna =False ,).reset_index ()#line:752
         del OOOO000O00O0O00OO ["All"]#line:754
         OOOO000O00O0O00OO =OOOO000O00O0O00OO [:-1 ]#line:755
         Tread_TOOLS_tree_Level_2 (OOOO000O00O0O00OO ,0 ,0 )#line:757
def Tread_TOOLS_analysis (OO0O00OO000OO0000 ):#line:762
    ""#line:763
    import datetime #line:764
    global TT_ori #line:765
    global TT_biaozhun #line:766
    if len (TT_ori )==0 :#line:768
       showinfo (title ="提示",message ="您尚未导入原始数据。")#line:769
       return 0 #line:770
    if len (TT_biaozhun )==0 :#line:771
       showinfo (title ="提示",message ="您尚未导入规则。")#line:772
       return 0 #line:773
    OOOO0O0OOO0O00OOO =TT_biaozhun ["设置"]#line:775
    TT_ori ["作用对象"]=""#line:776
    for O0O000O0OO00OOOOO in TOOLS_get_list (OOOO0O0OOO0O00OOO .loc [0 ,"值"]):#line:777
        TT_ori ["作用对象"]=TT_ori ["作用对象"]+"-"+TT_ori [O0O000O0OO00OOOOO ].fillna ("未填写").astype ("str")#line:778
    OOOOO00OOO0O00OO0 =Toplevel ()#line:781
    OOOOO00OOO0O00OO0 .title ("单品分析")#line:782
    OO0OO0O000OOOO000 =OOOOO00OOO0O00OO0 .winfo_screenwidth ()#line:783
    OOO0O00O0OO00OO0O =OOOOO00OOO0O00OO0 .winfo_screenheight ()#line:785
    O000O0O00OOOOO000 =580 #line:787
    O0O0OOOO00000O0O0 =80 #line:788
    O0OO0O0O0000O0OOO =(OO0OO0O000OOOO000 -O000O0O00OOOOO000 )/1.7 #line:790
    O0OOOOOO0OOO000OO =(OOO0O00O0OO00OO0O -O0O0OOOO00000O0O0 )/2 #line:791
    OOOOO00OOO0O00OO0 .geometry ("%dx%d+%d+%d"%(O000O0O00OOOOO000 ,O0O0OOOO00000O0O0 ,O0OO0O0O0000O0OOO ,O0OOOOOO0OOO000OO ))#line:792
    OO0OO00O0000O0O00 =Label (OOOOO00OOO0O00OO0 ,text ="作用对象：")#line:795
    OO0OO00O0000O0O00 .grid (row =1 ,column =0 ,sticky ="w")#line:796
    O0O0O0O0OO0000OO0 =StringVar ()#line:797
    O0O00O0O0OO000OO0 =ttk .Combobox (OOOOO00OOO0O00OO0 ,width =25 ,height =10 ,state ="readonly",textvariable =O0O0O0O0OO0000OO0 )#line:800
    O0O00O0O0OO000OO0 ["values"]=list (set (TT_ori ["作用对象"].to_list ()))#line:801
    O0O00O0O0OO000OO0 .current (0 )#line:802
    O0O00O0O0OO000OO0 .grid (row =1 ,column =1 )#line:803
    O0OO00OO0O0OOO000 =Label (OOOOO00OOO0O00OO0 ,text ="分析对象：")#line:805
    O0OO00OO0O0OOO000 .grid (row =1 ,column =2 ,sticky ="w")#line:806
    O0OOOO0OO000000O0 =StringVar ()#line:809
    O0000OO00OOO0O000 =ttk .Combobox (OOOOO00OOO0O00OO0 ,width =15 ,height =10 ,state ="readonly",textvariable =O0OOOO0OO000000O0 )#line:812
    O0000OO00OOO0O000 ["values"]=["事件发生月份","事件发生季度","产品批号","型号","规格"]#line:813
    O0000OO00OOO0O000 .current (0 )#line:815
    O0000OO00OOO0O000 .grid (row =1 ,column =3 )#line:816
    OOOOO0000OOO0OOO0 =Label (OOOOO00OOO0O00OO0 ,text ="事件发生起止时间：")#line:821
    OOOOO0000OOO0OOO0 .grid (row =2 ,column =0 ,sticky ="w")#line:822
    O0OOO00000O0OOO00 =Entry (OOOOO00OOO0O00OO0 ,width =10 )#line:824
    O0OOO00000O0OOO00 .insert (0 ,min (TT_ori ["事件发生日期"].dt .date ))#line:825
    O0OOO00000O0OOO00 .grid (row =2 ,column =1 ,sticky ="w")#line:826
    OO0OOOO0OOOO00OOO =Entry (OOOOO00OOO0O00OO0 ,width =10 )#line:828
    OO0OOOO0OOOO00OOO .insert (0 ,max (TT_ori ["事件发生日期"].dt .date ))#line:829
    OO0OOOO0OOOO00OOO .grid (row =2 ,column =2 ,sticky ="w")#line:830
    O0O0O0OO0O0O000O0 =Button (OOOOO00OOO0O00OO0 ,text ="原始查看",width =10 ,bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :thread_it (Tread_TOOLS_doing ,TT_ori ,O0O00O0O0OO000OO0 .get (),O0000OO00OOO0O000 .get (),O0OOO00000O0OOO00 .get (),OO0OOOO0OOOO00OOO .get (),1 ))#line:840
    O0O0O0OO0O0O000O0 .grid (row =3 ,column =2 ,sticky ="w")#line:841
    O0O0O0OO0O0O000O0 =Button (OOOOO00OOO0O00OO0 ,text ="分类查看",width =10 ,bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :thread_it (Tread_TOOLS_doing ,TT_ori ,O0O00O0O0OO000OO0 .get (),O0000OO00OOO0O000 .get (),O0OOO00000O0OOO00 .get (),OO0OOOO0OOOO00OOO .get (),0 ))#line:851
    O0O0O0OO0O0O000O0 .grid (row =3 ,column =3 ,sticky ="w")#line:852
    O0O0O0OO0O0O000O0 =Button (OOOOO00OOO0O00OO0 ,text ="趋势分析",width =10 ,bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :thread_it (Tread_TOOLS_doing ,TT_ori ,O0O00O0O0OO000OO0 .get (),O0000OO00OOO0O000 .get (),O0OOO00000O0OOO00 .get (),OO0OOOO0OOOO00OOO .get (),2 ))#line:862
    O0O0O0OO0O0O000O0 .grid (row =3 ,column =1 ,sticky ="w")#line:863
def Tread_TOOLS_doing (OO0O00O0000O0O0OO ,O00OOO00OOO0OOOO0 ,O0O0O0OOOO0000OOO ,O0OOOOO0OOO00O0O0 ,OO00OOO0O0O00000O ,OOO0OOOO0O0O0OOO0 ):#line:865
    ""#line:866
    global TT_biaozhun #line:867
    OO0O00O0000O0O0OO =OO0O00O0000O0O0OO [(OO0O00O0000O0O0OO ["作用对象"]==O00OOO00OOO0OOOO0 )].copy ()#line:868
    O0OOOOO0OOO00O0O0 =pd .to_datetime (O0OOOOO0OOO00O0O0 )#line:870
    OO00OOO0O0O00000O =pd .to_datetime (OO00OOO0O0O00000O )#line:871
    OO0O00O0000O0O0OO =OO0O00O0000O0O0OO [((OO0O00O0000O0O0OO ["事件发生日期"]>=O0OOOOO0OOO00O0O0 )&(OO0O00O0000O0O0OO ["事件发生日期"]<=OO00OOO0O0O00000O ))]#line:872
    text .insert (END ,"\n数据数量："+str (len (OO0O00O0000O0O0OO )))#line:873
    text .see (END )#line:874
    if OOO0OOOO0O0O0OOO0 ==0 :#line:876
        Tread_TOOLS_check (OO0O00O0000O0O0OO ,TT_biaozhun ["关键字表"],0 )#line:877
        return 0 #line:878
    if OOO0OOOO0O0O0OOO0 ==1 :#line:879
        Tread_TOOLS_tree_Level_2 (OO0O00O0000O0O0OO ,1 ,OO0O00O0000O0O0OO )#line:880
        return 0 #line:881
    if len (OO0O00O0000O0O0OO )<1 :#line:882
        showinfo (title ="错误信息",message ="没有符合筛选条件的报告。")#line:883
        return 0 #line:884
    Tread_TOOLS_check (OO0O00O0000O0O0OO ,TT_biaozhun ["关键字表"],1 )#line:885
    Tread_TOOLS_tree_Level_2 (Tread_TOOLS_Countall (OO0O00O0000O0O0OO ).df_find_all_keword_risk (O0O0O0OOOO0000OOO ),1 ,0 ,O0O0O0OOOO0000OOO )#line:888
def STAT_countx (O0O0OO000O0OO000O ):#line:898
    ""#line:899
    return O0O0OO000O0OO000O .value_counts ().to_dict ()#line:900
def STAT_countpx (O0O00O0O00O0O0O0O ,OO0OOO00O0OO000O0 ):#line:902
    ""#line:903
    return len (O0O00O0O00O0O0O0O [(O0O00O0O00O0O0O0O ==OO0OOO00O0OO000O0 )])#line:904
def STAT_countnpx (OO0O00O0OO0OOO0OO ,OOOO00O000O0OO0OO ):#line:906
    ""#line:907
    return len (OO0O00O0OO0OOO0OO [(OO0O00O0OO0OOO0OO not in OOOO00O000O0OO0OO )])#line:908
def STAT_get_max (OO0OOO000O0O00OOO ):#line:910
    ""#line:911
    return OO0OOO000O0O00OOO .value_counts ().max ()#line:912
def STAT_get_mean (OO000O0OO0O0000OO ):#line:914
    ""#line:915
    return round (OO000O0OO0O0000OO .value_counts ().mean (),2 )#line:916
def STAT_get_std (OO0000O00OOOOOO0O ):#line:918
    ""#line:919
    return round (OO0000O00OOOOOO0O .value_counts ().std (ddof =1 ),2 )#line:920
def STAT_get_95ci (OOOO0OOO0OOO0OOO0 ):#line:922
    ""#line:923
    return round (np .percentile (OOOO0OOO0OOO0OOO0 .value_counts (),97.5 ),2 )#line:924
def STAT_get_mean_std_ci (O00O00O00OOO0OOOO ,OOOOO0O0OO00O0O00 ):#line:926
    ""#line:927
    warnings .filterwarnings ("ignore")#line:928
    O0000OOO00O0O000O =TOOLS_strdict_to_pd (str (O00O00O00OOO0OOOO ))["content"].values /OOOOO0O0OO00O0O00 #line:929
    O0OOO0OO0O0OO00OO =round (O0000OOO00O0O000O .mean (),2 )#line:930
    O00OO0O0O0O0OOO00 =round (O0000OOO00O0O000O .std (ddof =1 ),2 )#line:931
    O00OOO0OO0OOO0000 =round (np .percentile (O0000OOO00O0O000O ,97.5 ),2 )#line:932
    return pd .Series ((O0OOO0OO0O0OO00OO ,O00OO0O0O0O0OOO00 ,O00OOO0OO0OOO0000 ))#line:933
def STAT_findx_value (O0OO0OO0OO0OO00O0 ,O0O00O0OOOOOO00OO ):#line:935
    ""#line:936
    warnings .filterwarnings ("ignore")#line:937
    OO0O0O0O00OO00OOO =TOOLS_strdict_to_pd (str (O0OO0OO0OO0OO00O0 ))#line:938
    O0O0O000O0O00O0OO =OO0O0O0O00OO00OOO .where (OO0O0O0O00OO00OOO ["index"]==str (O0O00O0OOOOOO00OO ))#line:940
    print (O0O0O000O0O00O0OO )#line:941
    return O0O0O000O0O00O0OO #line:942
def STAT_judge_x (OO0OO0O0OO0O00000 ,O0OOO000O00O0O00O ):#line:944
    ""#line:945
    for OOO0OOOOO0O0OO00O in O0OOO000O00O0O00O :#line:946
        if OO0OO0O0OO0O00000 .find (OOO0OOOOO0O0OO00O )>-1 :#line:947
            return 1 #line:948
def STAT_basic_risk (O0O0O00O0OO0OOO0O ,O0OO0O0O0OO0OO000 ,OO00O00000OO0OO0O ,O00000O00000O0O0O ,OO00OOO0O0OOO0000 ):#line:951
    ""#line:952
    O0O0O00O0OO0OOO0O ["风险评分"]=0 #line:953
    O0O0O00O0OO0OOO0O .loc [((O0O0O00O0OO0OOO0O [O0OO0O0O0OO0OO000 ]>=3 )&(O0O0O00O0OO0OOO0O [OO00O00000OO0OO0O ]>=1 ))|(O0O0O00O0OO0OOO0O [O0OO0O0O0OO0OO000 ]>=5 ),"风险评分"]=O0O0O00O0OO0OOO0O ["风险评分"]+5 #line:954
    O0O0O00O0OO0OOO0O .loc [(O0O0O00O0OO0OOO0O [OO00O00000OO0OO0O ]>=3 ),"风险评分"]=O0O0O00O0OO0OOO0O ["风险评分"]+1 #line:955
    O0O0O00O0OO0OOO0O .loc [(O0O0O00O0OO0OOO0O [O00000O00000O0O0O ]>=1 ),"风险评分"]=O0O0O00O0OO0OOO0O ["风险评分"]+10 #line:956
    O0O0O00O0OO0OOO0O ["风险评分"]=O0O0O00O0OO0OOO0O ["风险评分"]+O0O0O00O0OO0OOO0O [OO00OOO0O0OOO0000 ]/100 #line:957
    return O0O0O00O0OO0OOO0O #line:958
def STAT_find_keyword_risk (O0O000000O000O000 ,OO0OOOOO0O00O00OO ,O0OOOO0OOO00O00OO ,OO0O0000O0O000O00 ,O00OOO0O0O00OOO00 ):#line:962
        ""#line:963
        O0O00O0O0OOO000OO =O0O000000O000O000 .groupby (OO0OOOOO0O00O00OO ).agg (证号关键字总数量 =(O0OOOO0OOO00O00OO ,"count"),包含元素个数 =(OO0O0000O0O000O00 ,"nunique"),包含元素 =(OO0O0000O0O000O00 ,STAT_countx ),).reset_index ()#line:968
        O00O00OOO00000O00 =OO0OOOOO0O00O00OO .copy ()#line:970
        O00O00OOO00000O00 .append (OO0O0000O0O000O00 )#line:971
        O0O0OOO00OOOO0OO0 =O0O000000O000O000 .groupby (O00O00OOO00000O00 ).agg (计数 =(OO0O0000O0O000O00 ,"count"),).reset_index ()#line:974
        O0OO0OOOOO0000OOO =O00O00OOO00000O00 .copy ()#line:977
        O0OO0OOOOO0000OOO .remove ("关键字")#line:978
        OO0O0O0OOOOOOO00O =O0O000000O000O000 .groupby (O0OO0OOOOO0000OOO ).agg (该元素总数 =(OO0O0000O0O000O00 ,"count"),).reset_index ()#line:981
        O0O0OOO00OOOO0OO0 ["证号总数"]=O00OOO0O0O00OOO00 #line:983
        OO0OO00O000OOOOOO =pd .merge (O0O0OOO00OOOO0OO0 ,O0O00O0O0OOO000OO ,on =OO0OOOOO0O00O00OO ,how ="left")#line:984
        if len (OO0OO00O000OOOOOO )>0 :#line:986
            OO0OO00O000OOOOOO [['数量均值','数量标准差','数量CI']]=OO0OO00O000OOOOOO .包含元素 .apply (lambda O0OOO0OO0OO00OO00 :STAT_get_mean_std_ci (O0OOO0OO0OO00OO00 ,1 ))#line:987
        return OO0OO00O000OOOOOO #line:988
def STAT_find_risk (O00O00OO0O00OO0O0 ,OO000O0OO0O0O0OO0 ,O0OOOOOO0OO0O00OO ,OOOO00OOOOOOOOOOO ):#line:994
        ""#line:995
        O0OO0OO0O000O000O =O00O00OO0O00OO0O0 .groupby (OO000O0OO0O0O0OO0 ).agg (证号总数量 =(O0OOOOOO0OO0O00OO ,"count"),包含元素个数 =(OOOO00OOOOOOOOOOO ,"nunique"),包含元素 =(OOOO00OOOOOOOOOOO ,STAT_countx ),均值 =(OOOO00OOOOOOOOOOO ,STAT_get_mean ),标准差 =(OOOO00OOOOOOOOOOO ,STAT_get_std ),CI上限 =(OOOO00OOOOOOOOOOO ,STAT_get_95ci ),).reset_index ()#line:1003
        O0OOOO00O0O0000O0 =OO000O0OO0O0O0OO0 .copy ()#line:1005
        O0OOOO00O0O0000O0 .append (OOOO00OOOOOOOOOOO )#line:1006
        OOO0OOO0OOOO0OO0O =O00O00OO0O00OO0O0 .groupby (O0OOOO00O0O0000O0 ).agg (计数 =(OOOO00OOOOOOOOOOO ,"count"),严重伤害数 =("伤害",lambda O0O0000OO00OOOOO0 :STAT_countpx (O0O0000OO00OOOOO0 .values ,"严重伤害")),死亡数量 =("伤害",lambda OOOOOOO0O0OO000OO :STAT_countpx (OOOOOOO0O0OO000OO .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:1013
        OOOO0OO0O0OO0OOO0 =pd .merge (OOO0OOO0OOOO0OO0O ,O0OO0OO0O000O000O ,on =OO000O0OO0O0O0OO0 ,how ="left")#line:1015
        OOOO0OO0O0OO0OOO0 ["风险评分"]=0 #line:1017
        OOOO0OO0O0OO0OOO0 ["报表类型"]="dfx_findrisk"+OOOO00OOOOOOOOOOO #line:1018
        OOOO0OO0O0OO0OOO0 .loc [((OOOO0OO0O0OO0OOO0 ["计数"]>=3 )&(OOOO0OO0O0OO0OOO0 ["严重伤害数"]>=1 )|(OOOO0OO0O0OO0OOO0 ["计数"]>=5 )),"风险评分"]=OOOO0OO0O0OO0OOO0 ["风险评分"]+5 #line:1019
        OOOO0OO0O0OO0OOO0 .loc [(OOOO0OO0O0OO0OOO0 ["计数"]>=(OOOO0OO0O0OO0OOO0 ["均值"]+OOOO0OO0O0OO0OOO0 ["标准差"])),"风险评分"]=OOOO0OO0O0OO0OOO0 ["风险评分"]+1 #line:1020
        OOOO0OO0O0OO0OOO0 .loc [(OOOO0OO0O0OO0OOO0 ["计数"]>=OOOO0OO0O0OO0OOO0 ["CI上限"]),"风险评分"]=OOOO0OO0O0OO0OOO0 ["风险评分"]+1 #line:1021
        OOOO0OO0O0OO0OOO0 .loc [(OOOO0OO0O0OO0OOO0 ["严重伤害数"]>=3 )&(OOOO0OO0O0OO0OOO0 ["风险评分"]>=7 ),"风险评分"]=OOOO0OO0O0OO0OOO0 ["风险评分"]+1 #line:1022
        OOOO0OO0O0OO0OOO0 .loc [(OOOO0OO0O0OO0OOO0 ["死亡数量"]>=1 ),"风险评分"]=OOOO0OO0O0OO0OOO0 ["风险评分"]+10 #line:1023
        OOOO0OO0O0OO0OOO0 ["风险评分"]=OOOO0OO0O0OO0OOO0 ["风险评分"]+OOOO0OO0O0OO0OOO0 ["单位个数"]/100 #line:1024
        OOOO0OO0O0OO0OOO0 =OOOO0OO0O0OO0OOO0 .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:1025
        return OOOO0OO0O0OO0OOO0 #line:1027
def TOOLS_get_list (OO000000OOO0OOO0O ):#line:1029
    ""#line:1030
    OO000000OOO0OOO0O =str (OO000000OOO0OOO0O )#line:1031
    O0OO0OOOO0OOO00OO =[]#line:1032
    O0OO0OOOO0OOO00OO .append (OO000000OOO0OOO0O )#line:1033
    O0OO0OOOO0OOO00OO =",".join (O0OO0OOOO0OOO00OO )#line:1034
    O0OO0OOOO0OOO00OO =O0OO0OOOO0OOO00OO .split ("|")#line:1035
    OOO000O0O0OOO0O00 =O0OO0OOOO0OOO00OO [:]#line:1036
    O0OO0OOOO0OOO00OO =list (set (O0OO0OOOO0OOO00OO ))#line:1037
    O0OO0OOOO0OOO00OO .sort (key =OOO000O0O0OOO0O00 .index )#line:1038
    return O0OO0OOOO0OOO00OO #line:1039
def TOOLS_get_list0 (OOO00OOOO00OO0000 ,O0O0OO000O00OO0O0 ,*O0O00O000O0O0O0OO ):#line:1041
    ""#line:1042
    OOO00OOOO00OO0000 =str (OOO00OOOO00OO0000 )#line:1043
    if pd .notnull (OOO00OOOO00OO0000 ):#line:1045
        try :#line:1046
            if "use("in str (OOO00OOOO00OO0000 ):#line:1047
                OOO0O00000O00000O =OOO00OOOO00OO0000 #line:1048
                OOOO0OOO0000O00O0 =re .compile (r"[(](.*?)[)]",re .S )#line:1049
                OOOO0O0OO0OOOOO0O =re .findall (OOOO0OOO0000O00O0 ,OOO0O00000O00000O )#line:1050
                O0O0OOOO0O0OO0O00 =[]#line:1051
                if ").list"in OOO00OOOO00OO0000 :#line:1052
                    OOOO0O000O00OO00O ="配置表/"+str (OOOO0O0OO0OOOOO0O [0 ])+".xls"#line:1053
                    OO0O00000OOO000O0 =pd .read_excel (OOOO0O000O00OO00O ,sheet_name =OOOO0O0OO0OOOOO0O [0 ],header =0 ,index_col =0 ).reset_index ()#line:1056
                    OO0O00000OOO000O0 ["检索关键字"]=OO0O00000OOO000O0 ["检索关键字"].astype (str )#line:1057
                    O0O0OOOO0O0OO0O00 =OO0O00000OOO000O0 ["检索关键字"].tolist ()+O0O0OOOO0O0OO0O00 #line:1058
                if ").file"in OOO00OOOO00OO0000 :#line:1059
                    O0O0OOOO0O0OO0O00 =O0O0OO000O00OO0O0 [OOOO0O0OO0OOOOO0O [0 ]].astype (str ).tolist ()+O0O0OOOO0O0OO0O00 #line:1061
                try :#line:1064
                    if "报告类型-新的"in O0O0OO000O00OO0O0 .columns :#line:1065
                        O0O0OOOO0O0OO0O00 =",".join (O0O0OOOO0O0OO0O00 )#line:1066
                        O0O0OOOO0O0OO0O00 =O0O0OOOO0O0OO0O00 .split (";")#line:1067
                        O0O0OOOO0O0OO0O00 =",".join (O0O0OOOO0O0OO0O00 )#line:1068
                        O0O0OOOO0O0OO0O00 =O0O0OOOO0O0OO0O00 .split ("；")#line:1069
                        O0O0OOOO0O0OO0O00 =[OO00OO00O0OOOO000 .replace ("（严重）","")for OO00OO00O0OOOO000 in O0O0OOOO0O0OO0O00 ]#line:1070
                        O0O0OOOO0O0OO0O00 =[OOO00O0000000O0OO .replace ("（一般）","")for OOO00O0000000O0OO in O0O0OOOO0O0OO0O00 ]#line:1071
                except :#line:1072
                    pass #line:1073
                O0O0OOOO0O0OO0O00 =",".join (O0O0OOOO0O0OO0O00 )#line:1076
                O0O0OOOO0O0OO0O00 =O0O0OOOO0O0OO0O00 .split ("、")#line:1077
                O0O0OOOO0O0OO0O00 =",".join (O0O0OOOO0O0OO0O00 )#line:1078
                O0O0OOOO0O0OO0O00 =O0O0OOOO0O0OO0O00 .split ("，")#line:1079
                O0O0OOOO0O0OO0O00 =",".join (O0O0OOOO0O0OO0O00 )#line:1080
                O0O0OOOO0O0OO0O00 =O0O0OOOO0O0OO0O00 .split (",")#line:1081
                O0O000O00O00OOO0O =O0O0OOOO0O0OO0O00 [:]#line:1083
                try :#line:1084
                    if O0O00O000O0O0O0OO [0 ]==1000 :#line:1085
                      pass #line:1086
                except :#line:1087
                      O0O0OOOO0O0OO0O00 =list (set (O0O0OOOO0O0OO0O00 ))#line:1088
                O0O0OOOO0O0OO0O00 .sort (key =O0O000O00O00OOO0O .index )#line:1089
            else :#line:1091
                OOO00OOOO00OO0000 =str (OOO00OOOO00OO0000 )#line:1092
                O0O0OOOO0O0OO0O00 =[]#line:1093
                O0O0OOOO0O0OO0O00 .append (OOO00OOOO00OO0000 )#line:1094
                O0O0OOOO0O0OO0O00 =",".join (O0O0OOOO0O0OO0O00 )#line:1095
                O0O0OOOO0O0OO0O00 =O0O0OOOO0O0OO0O00 .split ("、")#line:1096
                O0O0OOOO0O0OO0O00 =",".join (O0O0OOOO0O0OO0O00 )#line:1097
                O0O0OOOO0O0OO0O00 =O0O0OOOO0O0OO0O00 .split ("，")#line:1098
                O0O0OOOO0O0OO0O00 =",".join (O0O0OOOO0O0OO0O00 )#line:1099
                O0O0OOOO0O0OO0O00 =O0O0OOOO0O0OO0O00 .split (",")#line:1100
                O0O000O00O00OOO0O =O0O0OOOO0O0OO0O00 [:]#line:1102
                try :#line:1103
                    if O0O00O000O0O0O0OO [0 ]==1000 :#line:1104
                      O0O0OOOO0O0OO0O00 =list (set (O0O0OOOO0O0OO0O00 ))#line:1105
                except :#line:1106
                      pass #line:1107
                O0O0OOOO0O0OO0O00 .sort (key =O0O000O00O00OOO0O .index )#line:1108
                O0O0OOOO0O0OO0O00 .sort (key =O0O000O00O00OOO0O .index )#line:1109
        except ValueError2 :#line:1111
            showinfo (title ="提示信息",message ="创建单元格支持多个甚至表单（文件）传入的方法，返回一个经过整理的清单出错，任务终止。")#line:1112
            return False #line:1113
    return O0O0OOOO0O0OO0O00 #line:1115
def TOOLS_strdict_to_pd (OOOO00OO0O0O0O000 ):#line:1116
    ""#line:1117
    return pd .DataFrame .from_dict (eval (OOOO00OO0O0O0O000 ),orient ="index",columns =["content"]).reset_index ()#line:1118
def Tread_TOOLS_view_dict (OOOO00OO00000O000 ,O0OO0OO0O0OO0O00O ):#line:1120
    ""#line:1121
    O0000OO00OO0O0000 =Toplevel ()#line:1122
    O0000OO00OO0O0000 .title ("查看数据")#line:1123
    O0000OO00OO0O0000 .geometry ("700x500")#line:1124
    O0O00O0000O0O0000 =Scrollbar (O0000OO00OO0O0000 )#line:1126
    O0000OOO0OO0O00OO =Text (O0000OO00OO0O0000 ,height =100 ,width =150 )#line:1127
    O0O00O0000O0O0000 .pack (side =RIGHT ,fill =Y )#line:1128
    O0000OOO0OO0O00OO .pack ()#line:1129
    O0O00O0000O0O0000 .config (command =O0000OOO0OO0O00OO .yview )#line:1130
    O0000OOO0OO0O00OO .config (yscrollcommand =O0O00O0000O0O0000 .set )#line:1131
    if O0OO0OO0O0OO0O00O ==1 :#line:1132
        O0000OOO0OO0O00OO .insert (END ,OOOO00OO00000O000 )#line:1134
        O0000OOO0OO0O00OO .insert (END ,"\n\n")#line:1135
        return 0 #line:1136
    for OO00OO0000000000O in range (len (OOOO00OO00000O000 )):#line:1137
        O0000OOO0OO0O00OO .insert (END ,OOOO00OO00000O000 .iloc [OO00OO0000000000O ,0 ])#line:1138
        O0000OOO0OO0O00OO .insert (END ,":")#line:1139
        O0000OOO0OO0O00OO .insert (END ,OOOO00OO00000O000 .iloc [OO00OO0000000000O ,1 ])#line:1140
        O0000OOO0OO0O00OO .insert (END ,"\n\n")#line:1141
def Tread_TOOLS_fashenglv (OO000OOOO0000OOOO ,OO0O0OO0OOO000O0O ):#line:1144
    global TT_biaozhun #line:1145
    OO000OOOO0000OOOO =pd .merge (OO000OOOO0000OOOO ,TT_biaozhun [OO0O0OO0OOO000O0O ],on =[OO0O0OO0OOO000O0O ],how ="left").reset_index (drop =True )#line:1146
    OOOOO00O00OOOOO00 =OO000OOOO0000OOOO ["使用次数"].mean ()#line:1148
    OO000OOOO0000OOOO ["使用次数"]=OO000OOOO0000OOOO ["使用次数"].fillna (int (OOOOO00O00OOOOO00 ))#line:1149
    OO0OOO00O0000O0OO =OO000OOOO0000OOOO ["使用次数"][:-1 ].sum ()#line:1150
    OO000OOOO0000OOOO .iloc [-1 ,-1 ]=OO0OOO00O0000O0OO #line:1151
    O0OO0O0OOOOO0000O =[O0OO0O0O0OO0000OO for O0OO0O0O0OO0000OO in OO000OOOO0000OOOO .columns if (O0OO0O0O0OO0000OO not in ["使用次数",OO0O0OO0OOO000O0O ])]#line:1152
    for OOOO000000OOO00OO ,O0OO000OO0000OOO0 in OO000OOOO0000OOOO .iterrows ():#line:1153
        for O0O0OOOOO0O0OOO00 in O0OO0O0OOOOO0000O :#line:1154
            OO000OOOO0000OOOO .loc [OOOO000000OOO00OO ,O0O0OOOOO0O0OOO00 ]=int (O0OO000OO0000OOO0 [O0O0OOOOO0O0OOO00 ])/int (O0OO000OO0000OOO0 ["使用次数"])#line:1155
    del OO000OOOO0000OOOO ["使用次数"]#line:1156
    Tread_TOOLS_tree_Level_2 (OO000OOOO0000OOOO ,1 ,1 ,OO0O0OO0OOO000O0O )#line:1157
def TOOLS_save_dict (O00O0OO0OOO0O000O ):#line:1159
    ""#line:1160
    O0O00O0OOOO000O00 =filedialog .asksaveasfilename (title =u"保存文件",initialfile ="【排序后的原始数据】.xls",defaultextension ="xls",filetypes =[("Excel 97-2003 工作簿","*.xls")],)#line:1166
    try :#line:1167
        O00O0OO0OOO0O000O ["详细描述T"]=O00O0OO0OOO0O000O ["详细描述T"].astype (str )#line:1168
    except :#line:1169
        pass #line:1170
    try :#line:1171
        O00O0OO0OOO0O000O ["报告编码"]=O00O0OO0OOO0O000O ["报告编码"].astype (str )#line:1172
    except :#line:1173
        pass #line:1174
    try :#line:1175
        OOO000OOOO0O000O0 =re .search ("\【(.*?)\】",O0O00O0OOOO000O00 )#line:1176
        O00O0OO0OOO0O000O ["对象"]=OOO000OOOO0O000O0 .group (1 )#line:1177
    except :#line:1178
        pass #line:1179
    OOO0OO0OO000OOOO0 =pd .ExcelWriter (O0O00O0OOOO000O00 ,engine ="xlsxwriter")#line:1180
    O00O0OO0OOO0O000O .to_excel (OOO0OO0OO000OOOO0 ,sheet_name ="字典数据")#line:1181
    OOO0OO0OO000OOOO0 .close ()#line:1182
    showinfo (title ="提示",message ="文件写入成功。")#line:1183
def Tread_TOOLS_DRAW_histbar (O000O00OO0OO0OO00 ):#line:1187
    ""#line:1188
    OOOOOO0OO0O0OOOO0 =Toplevel ()#line:1191
    OOOOOO0OO0O0OOOO0 .title ("直方图")#line:1192
    O0O0O0O0OOO0OOOOO =ttk .Frame (OOOOOO0OO0O0OOOO0 ,height =20 )#line:1193
    O0O0O0O0OOO0OOOOO .pack (side =TOP )#line:1194
    OO0O0O0O000O0000O =Figure (figsize =(12 ,6 ),dpi =100 )#line:1196
    OO0OOOO0O0000O000 =FigureCanvasTkAgg (OO0O0O0O000O0000O ,master =OOOOOO0OO0O0OOOO0 )#line:1197
    OO0OOOO0O0000O000 .draw ()#line:1198
    OO0OOOO0O0000O000 .get_tk_widget ().pack (expand =1 )#line:1199
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1201
    plt .rcParams ['axes.unicode_minus']=False #line:1202
    OOOO0000000O00OO0 =NavigationToolbar2Tk (OO0OOOO0O0000O000 ,OOOOOO0OO0O0OOOO0 )#line:1204
    OOOO0000000O00OO0 .update ()#line:1205
    OO0OOOO0O0000O000 .get_tk_widget ().pack ()#line:1206
    OOO000000O0OO00OO =OO0O0O0O000O0000O .add_subplot (111 )#line:1208
    OOO000000O0OO00OO .set_title ("直方图")#line:1210
    OO0OO0OO0OO0OOO00 =O000O00OO0OO0OO00 .columns .to_list ()#line:1212
    OO0OO0OO0OO0OOO00 .remove ("对象")#line:1213
    OOOO0OO00000OOO00 =np .arange (len (OO0OO0OO0OO0OOO00 ))#line:1214
    for O00O0O0OOO0OO0O00 in OO0OO0OO0OO0OOO00 :#line:1218
        O000O00OO0OO0OO00 [O00O0O0OOO0OO0O00 ]=O000O00OO0OO0OO00 [O00O0O0OOO0OO0O00 ].astype (float )#line:1219
    O000O00OO0OO0OO00 ['数据']=O000O00OO0OO0OO00 [OO0OO0OO0OO0OOO00 ].values .tolist ()#line:1221
    O0O0OO00OOO00000O =0 #line:1222
    for O0O00O00O000O0OOO ,O00OO00O0OOOO0O0O in O000O00OO0OO0OO00 .iterrows ():#line:1223
        OOO000000O0OO00OO .bar ([OO00O00OOOO000O0O +O0O0OO00OOO00000O for OO00O00OOOO000O0O in OOOO0OO00000OOO00 ],O000O00OO0OO0OO00 .loc [O0O00O00O000O0OOO ,'数据'],label =OO0OO0OO0OO0OOO00 ,width =0.1 )#line:1224
        for OOO0OOO00OOOOO0OO ,OO00O000O00OOO00O in zip ([OO000OOO00O0OOO0O +O0O0OO00OOO00000O for OO000OOO00O0OOO0O in OOOO0OO00000OOO00 ],O000O00OO0OO0OO00 .loc [O0O00O00O000O0OOO ,'数据']):#line:1227
           OOO000000O0OO00OO .text (OOO0OOO00OOOOO0OO -0.015 ,OO00O000O00OOO00O +0.07 ,str (int (OO00O000O00OOO00O )),color ='black',size =8 )#line:1228
        O0O0OO00OOO00000O =O0O0OO00OOO00000O +0.1 #line:1230
    OOO000000O0OO00OO .set_xticklabels (O000O00OO0OO0OO00 .columns .to_list (),rotation =-90 ,fontsize =8 )#line:1232
    OOO000000O0OO00OO .legend (O000O00OO0OO0OO00 ["对象"])#line:1236
    OO0OOOO0O0000O000 .draw ()#line:1239
def Tread_TOOLS_DRAW_make_risk_plot (OO0000OO000OO0O0O ,OO00OOO0OO0O000OO ,O0O0O0OO0OO00OO0O ,O0OO0O00OOO0OO000 ,OOOO0O00O0000000O ):#line:1241
    ""#line:1242
    OO00O0O00O0O00OOO =Toplevel ()#line:1245
    OO00O0O00O0O00OOO .title (O0OO0O00OOO0OO000 )#line:1246
    OOO00OO000OOOOOOO =ttk .Frame (OO00O0O00O0O00OOO ,height =20 )#line:1247
    OOO00OO000OOOOOOO .pack (side =TOP )#line:1248
    OO0OOO0OO0O000OO0 =Figure (figsize =(12 ,6 ),dpi =100 )#line:1250
    OO000O0O00O0O0O00 =FigureCanvasTkAgg (OO0OOO0OO0O000OO0 ,master =OO00O0O00O0O00OOO )#line:1251
    OO000O0O00O0O0O00 .draw ()#line:1252
    OO000O0O00O0O0O00 .get_tk_widget ().pack (expand =1 )#line:1253
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1255
    plt .rcParams ['axes.unicode_minus']=False #line:1256
    O0OOOOO00O0OOO000 =NavigationToolbar2Tk (OO000O0O00O0O0O00 ,OO00O0O00O0O00OOO )#line:1258
    O0OOOOO00O0OOO000 .update ()#line:1259
    OO000O0O00O0O0O00 .get_tk_widget ().pack ()#line:1260
    OOOOO0OOO000O0OO0 =OO0OOO0OO0O000OO0 .add_subplot (111 )#line:1262
    OOOOO0OOO000O0OO0 .set_title (O0OO0O00OOO0OO000 )#line:1264
    OO0O0OO0O0O0O0OOO =OO0000OO000OO0O0O [OO00OOO0OO0O000OO ]#line:1265
    if OOOO0O00O0000000O !=999 :#line:1268
        OOOOO0OOO000O0OO0 .set_xticklabels (OO0O0OO0O0O0O0OOO ,rotation =-90 ,fontsize =8 )#line:1269
    OOO00OOO00OO0OO0O =range (0 ,len (OO0O0OO0O0O0O0OOO ),1 )#line:1272
    for O00OOO0OO00O000O0 in O0O0O0OO0OO00OO0O :#line:1277
        O00OO00000O0OOO00 =OO0000OO000OO0O0O [O00OOO0OO00O000O0 ].astype (float )#line:1278
        if O00OOO0OO00O000O0 =="关注区域":#line:1280
            OOOOO0OOO000O0OO0 .plot (list (OO0O0OO0O0O0O0OOO ),list (O00OO00000O0OOO00 ),label =str (O00OOO0OO00O000O0 ),color ="red")#line:1281
        else :#line:1282
            OOOOO0OOO000O0OO0 .plot (list (OO0O0OO0O0O0O0OOO ),list (O00OO00000O0OOO00 ),label =str (O00OOO0OO00O000O0 ))#line:1283
        if OOOO0O00O0000000O ==100 :#line:1286
            for O0OO0OOO00O00OOO0 ,O00O0OO00O000OOO0 in zip (OO0O0OO0O0O0O0OOO ,O00OO00000O0OOO00 ):#line:1287
                if O00O0OO00O000OOO0 ==max (O00OO00000O0OOO00 )and O00O0OO00O000OOO0 >=3 and len (O0O0O0OO0OO00OO0O )!=1 :#line:1288
                     OOOOO0OOO000O0OO0 .text (O0OO0OOO00O00OOO0 ,O00O0OO00O000OOO0 ,(str (O00OOO0OO00O000O0 )+":"+str (int (O00O0OO00O000OOO0 ))),color ='black',size =8 )#line:1289
                if len (O0O0O0OO0OO00OO0O )==1 and O00O0OO00O000OOO0 >=0.01 :#line:1290
                     OOOOO0OOO000O0OO0 .text (O0OO0OOO00O00OOO0 ,O00O0OO00O000OOO0 ,str (int (O00O0OO00O000OOO0 )),color ='black',size =8 )#line:1291
    if len (O0O0O0OO0OO00OO0O )==1 :#line:1301
        OO00OO00O0O0O00OO =OO0000OO000OO0O0O [O0O0O0OO0OO00OO0O ].astype (float ).values #line:1302
        O000O0OO0OO0O0O00 =OO00OO00O0O0O00OO .mean ()#line:1303
        OOOOOO00OOOOOOO00 =OO00OO00O0O0O00OO .std ()#line:1304
        OOO000000OO0OO0OO =O000O0OO0OO0O0O00 +3 *OOOOOO00OOOOOOO00 #line:1305
        OOOOO00O0OO000O0O =OOOOOO00OOOOOOO00 -3 *OOOOOO00OOOOOOO00 #line:1306
        OOOOO0OOO000O0OO0 .axhline (O000O0OO0OO0O0O00 ,color ='r',linestyle ='--',label ='Mean')#line:1308
        OOOOO0OOO000O0OO0 .axhline (OOO000000OO0OO0OO ,color ='g',linestyle ='--',label ='UCL(μ+3σ)')#line:1309
        OOOOO0OOO000O0OO0 .axhline (OOOOO00O0OO000O0O ,color ='g',linestyle ='--',label ='LCL(μ-3σ)')#line:1310
    OOOOO0OOO000O0OO0 .set_title ("控制图")#line:1312
    OOOOO0OOO000O0OO0 .set_xlabel ("项")#line:1313
    OO0OOO0OO0O000OO0 .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:1314
    O000OOOO00O0O000O =OOOOO0OOO000O0OO0 .get_position ()#line:1315
    OOOOO0OOO000O0OO0 .set_position ([O000OOOO00O0O000O .x0 ,O000OOOO00O0O000O .y0 ,O000OOOO00O0O000O .width *0.7 ,O000OOOO00O0O000O .height ])#line:1316
    OOOOO0OOO000O0OO0 .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:1317
    OO00O0OOO000O0OOO =StringVar ()#line:1320
    O00O0O0O00OO00OO0 =ttk .Combobox (OOO00OO000OOOOOOO ,width =15 ,textvariable =OO00O0OOO000O0OOO ,state ='readonly')#line:1321
    O00O0O0O00OO00OO0 ['values']=O0O0O0OO0OO00OO0O #line:1322
    O00O0O0O00OO00OO0 .pack (side =LEFT )#line:1323
    O00O0O0O00OO00OO0 .current (0 )#line:1324
    O0OO0OO0OOOO0000O =Button (OOO00OO000OOOOOOO ,text ="控制图（单项）",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (OO0000OO000OO0O0O ,OO00OOO0OO0O000OO ,[O0O0OOOO0OOO0O00O for O0O0OOOO0OOO0O00O in O0O0O0OO0OO00OO0O if OO00O0OOO000O0OOO .get ()in O0O0OOOO0OOO0O00O ],O0OO0O00OOO0OO000 ,OOOO0O00O0000000O ))#line:1334
    O0OO0OO0OOOO0000O .pack (side =LEFT ,anchor ="ne")#line:1335
    O0OO000O0O0OOOO00 =Button (OOO00OO000OOOOOOO ,text ="去除标记",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (OO0000OO000OO0O0O ,OO00OOO0OO0O000OO ,O0O0O0OO0OO00OO0O ,O0OO0O00OOO0OO000 ,0 ))#line:1343
    O0OO000O0O0OOOO00 .pack (side =LEFT ,anchor ="ne")#line:1345
    OO000O0O00O0O0O00 .draw ()#line:1346
def Tread_TOOLS_draw (O00000000OOO000O0 ,O000O0O0O000O0000 ,O0O0O0000OOO0O0OO ,O0O000OOO00OOO00O ,OOO00O0000O00O0OO ):#line:1348
    ""#line:1349
    warnings .filterwarnings ("ignore")#line:1350
    O00O000OO0OO0O00O =Toplevel ()#line:1351
    O00O000OO0OO0O00O .title (O000O0O0O000O0000 )#line:1352
    OO00O00OOOOO00O0O =ttk .Frame (O00O000OO0OO0O00O ,height =20 )#line:1353
    OO00O00OOOOO00O0O .pack (side =TOP )#line:1354
    OOO0O00OOO00OO00O =Figure (figsize =(12 ,6 ),dpi =100 )#line:1356
    O0OO0O0O0OOOOOOO0 =FigureCanvasTkAgg (OOO0O00OOO00OO00O ,master =O00O000OO0OO0O00O )#line:1357
    O0OO0O0O0OOOOOOO0 .draw ()#line:1358
    O0OO0O0O0OOOOOOO0 .get_tk_widget ().pack (expand =1 )#line:1359
    O0000000O000O0O00 =OOO0O00OOO00OO00O .add_subplot (111 )#line:1360
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1362
    plt .rcParams ['axes.unicode_minus']=False #line:1363
    O0O0OOOO0OOO00OO0 =NavigationToolbar2Tk (O0OO0O0O0OOOOOOO0 ,O00O000OO0OO0O00O )#line:1365
    O0O0OOOO0OOO00OO0 .update ()#line:1366
    O0OO0O0O0OOOOOOO0 .get_tk_widget ().pack ()#line:1368
    try :#line:1371
        OOO000OO00OOO00O0 =O00000000OOO000O0 .columns #line:1372
        O00000000OOO000O0 =O00000000OOO000O0 .sort_values (by =O0O000OOO00OOO00O ,ascending =[False ],na_position ="last")#line:1373
    except :#line:1374
        OO00OOO0O0OO000OO =eval (O00000000OOO000O0 )#line:1375
        OO00OOO0O0OO000OO =pd .DataFrame .from_dict (OO00OOO0O0OO000OO ,TT_orient =O0O0O0000OOO0O0OO ,columns =[O0O000OOO00OOO00O ]).reset_index ()#line:1378
        O00000000OOO000O0 =OO00OOO0O0OO000OO .sort_values (by =O0O000OOO00OOO00O ,ascending =[False ],na_position ="last")#line:1379
    if ("日期"in O000O0O0O000O0000 or "时间"in O000O0O0O000O0000 or "季度"in O000O0O0O000O0000 )and "饼图"not in OOO00O0000O00O0OO :#line:1383
        O00000000OOO000O0 [O0O0O0000OOO0O0OO ]=pd .to_datetime (O00000000OOO000O0 [O0O0O0000OOO0O0OO ],format ="%Y/%m/%d").dt .date #line:1384
        O00000000OOO000O0 =O00000000OOO000O0 .sort_values (by =O0O0O0000OOO0O0OO ,ascending =[True ],na_position ="last")#line:1385
    elif "批号"in O000O0O0O000O0000 :#line:1386
        O00000000OOO000O0 [O0O0O0000OOO0O0OO ]=O00000000OOO000O0 [O0O0O0000OOO0O0OO ].astype (str )#line:1387
        O00000000OOO000O0 =O00000000OOO000O0 .sort_values (by =O0O0O0000OOO0O0OO ,ascending =[True ],na_position ="last")#line:1388
        O0000000O000O0O00 .set_xticklabels (O00000000OOO000O0 [O0O0O0000OOO0O0OO ],rotation =-90 ,fontsize =8 )#line:1389
    else :#line:1390
        O00000000OOO000O0 [O0O0O0000OOO0O0OO ]=O00000000OOO000O0 [O0O0O0000OOO0O0OO ].astype (str )#line:1391
        O0000000O000O0O00 .set_xticklabels (O00000000OOO000O0 [O0O0O0000OOO0O0OO ],rotation =-90 ,fontsize =8 )#line:1392
    O0000O000O0O000O0 =O00000000OOO000O0 [O0O000OOO00OOO00O ]#line:1394
    O00O0000O0OO00O00 =range (0 ,len (O0000O000O0O000O0 ),1 )#line:1395
    O0000000O000O0O00 .set_title (O000O0O0O000O0000 )#line:1397
    if OOO00O0000O00O0OO =="柱状图":#line:1401
        O0000000O000O0O00 .bar (x =O00000000OOO000O0 [O0O0O0000OOO0O0OO ],height =O0000O000O0O000O0 ,width =0.2 ,color ="#87CEFA")#line:1402
    elif OOO00O0000O00O0OO =="饼图":#line:1403
        O0000000O000O0O00 .pie (x =O0000O000O0O000O0 ,labels =O00000000OOO000O0 [O0O0O0000OOO0O0OO ],autopct ="%0.2f%%")#line:1404
    elif OOO00O0000O00O0OO =="折线图":#line:1405
        O0000000O000O0O00 .plot (O00000000OOO000O0 [O0O0O0000OOO0O0OO ],O0000O000O0O000O0 ,lw =0.5 ,ls ='-',c ="r",alpha =0.5 )#line:1406
    elif "帕累托图"in str (OOO00O0000O00O0OO ):#line:1408
        OO000OOO00OOOOOO0 =O00000000OOO000O0 [O0O000OOO00OOO00O ].fillna (0 )#line:1409
        OOO0O0O0OO0OOO0O0 =OO000OOO00OOOOOO0 .cumsum ()/OO000OOO00OOOOOO0 .sum ()*100 #line:1413
        O00000000OOO000O0 ["百分比"]=round (O00000000OOO000O0 ["数量"]/OO000OOO00OOOOOO0 .sum ()*100 ,2 )#line:1414
        O00000000OOO000O0 ["累计百分比"]=round (OOO0O0O0OO0OOO0O0 ,2 )#line:1415
        OOOO00O000OOOO00O =OOO0O0O0OO0OOO0O0 [OOO0O0O0OO0OOO0O0 >0.8 ].index [0 ]#line:1416
        O00OO00O00OO00O0O =OO000OOO00OOOOOO0 .index .tolist ().index (OOOO00O000OOOO00O )#line:1417
        O0000000O000O0O00 .bar (x =O00000000OOO000O0 [O0O0O0000OOO0O0OO ],height =OO000OOO00OOOOOO0 ,color ="C0",label =O0O000OOO00OOO00O )#line:1421
        O000OOOOOOOOOOOOO =O0000000O000O0O00 .twinx ()#line:1422
        O000OOOOOOOOOOOOO .plot (O00000000OOO000O0 [O0O0O0000OOO0O0OO ],OOO0O0O0OO0OOO0O0 ,color ="C1",alpha =0.6 ,label ="累计比例")#line:1423
        O000OOOOOOOOOOOOO .yaxis .set_major_formatter (PercentFormatter ())#line:1424
        O0000000O000O0O00 .tick_params (axis ="y",colors ="C0")#line:1429
        O000OOOOOOOOOOOOO .tick_params (axis ="y",colors ="C1")#line:1430
        for O0OOOOO0OO0O000O0 ,OO0O000OOOOOO00OO ,OOOOO00OOOO0O0O0O ,O0OO00OOO0OO0OO0O in zip (O00000000OOO000O0 [O0O0O0000OOO0O0OO ],OO000OOO00OOOOOO0 ,O00000000OOO000O0 ["百分比"],O00000000OOO000O0 ["累计百分比"]):#line:1432
            O0000000O000O0O00 .text (O0OOOOO0OO0O000O0 ,OO0O000OOOOOO00OO +0.1 ,str (int (OO0O000OOOOOO00OO ))+", "+str (int (OOOOO00OOOO0O0O0O ))+"%,"+str (int (O0OO00OOO0OO0OO0O ))+"%",color ='black',size =8 )#line:1433
        if "超级帕累托图"in str (OOO00O0000O00O0OO ):#line:1436
            OO000000OOO0OO0O0 =re .compile (r'[(](.*?)[)]',re .S )#line:1437
            O000OO000OO00OO0O =re .findall (OO000000OOO0OO0O0 ,OOO00O0000O00O0OO )[0 ]#line:1438
            O0000000O000O0O00 .bar (x =O00000000OOO000O0 [O0O0O0000OOO0O0OO ],height =O00000000OOO000O0 [O000OO000OO00OO0O ],color ="orangered",label =O000OO000OO00OO0O )#line:1439
    OOO0O00OOO00OO00O .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:1444
    OO00OO0O00OO000OO =O0000000O000O0O00 .get_position ()#line:1445
    O0000000O000O0O00 .set_position ([OO00OO0O00OO000OO .x0 ,OO00OO0O00OO000OO .y0 ,OO00OO0O00OO000OO .width *0.7 ,OO00OO0O00OO000OO .height ])#line:1446
    O0000000O000O0O00 .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:1447
    O0OO0O0O0OOOOOOO0 .draw ()#line:1450
    if len (O0000O000O0O000O0 )<=20 and OOO00O0000O00O0OO !="饼图"and OOO00O0000O00O0OO !="帕累托图":#line:1453
        for OOO000O00OO00000O ,O0O0O00OOOOO00000 in zip (O00O0000O0OO00O00 ,O0000O000O0O000O0 ):#line:1454
            OOOO00OO00OO0O000 =str (O0O0O00OOOOO00000 )#line:1455
            OO00O0OOOOO0OOO00 =(OOO000O00OO00000O ,O0O0O00OOOOO00000 +0.3 )#line:1456
            O0000000O000O0O00 .annotate (OOOO00OO00OO0O000 ,xy =OO00O0OOOOO0OOO00 ,fontsize =8 ,color ="black",ha ="center",va ="baseline")#line:1457
    O00OO0000OOO0OOO0 =Button (OO00O00OOOOO00O0O ,relief =GROOVE ,activebackground ="green",text ="保存原始数据",command =lambda :TOOLS_save_dict (O00000000OOO000O0 ),)#line:1467
    O00OO0000OOO0OOO0 .pack (side =RIGHT )#line:1468
    OOO0OOOO00000O0O0 =Button (OO00O00OOOOO00O0O ,relief =GROOVE ,text ="查看原始数据",command =lambda :Tread_TOOLS_view_dict (O00000000OOO000O0 ,1 ))#line:1472
    OOO0OOOO00000O0O0 .pack (side =RIGHT )#line:1473
    O0OOOO0OO00OOO0OO =Button (OO00O00OOOOO00O0O ,relief =GROOVE ,text ="饼图",command =lambda :Tread_TOOLS_draw (O00000000OOO000O0 ,O000O0O0O000O0000 ,O0O0O0000OOO0O0OO ,O0O000OOO00OOO00O ,"饼图"),)#line:1481
    O0OOOO0OO00OOO0OO .pack (side =LEFT )#line:1482
    O0OOOO0OO00OOO0OO =Button (OO00O00OOOOO00O0O ,relief =GROOVE ,text ="柱状图",command =lambda :Tread_TOOLS_draw (O00000000OOO000O0 ,O000O0O0O000O0000 ,O0O0O0000OOO0O0OO ,O0O000OOO00OOO00O ,"柱状图"),)#line:1489
    O0OOOO0OO00OOO0OO .pack (side =LEFT )#line:1490
    O0OOOO0OO00OOO0OO =Button (OO00O00OOOOO00O0O ,relief =GROOVE ,text ="折线图",command =lambda :Tread_TOOLS_draw (O00000000OOO000O0 ,O000O0O0O000O0000 ,O0O0O0000OOO0O0OO ,O0O000OOO00OOO00O ,"折线图"),)#line:1496
    O0OOOO0OO00OOO0OO .pack (side =LEFT )#line:1497
    O0OOOO0OO00OOO0OO =Button (OO00O00OOOOO00O0O ,relief =GROOVE ,text ="帕累托图",command =lambda :Tread_TOOLS_draw (O00000000OOO000O0 ,O000O0O0O000O0000 ,O0O0O0000OOO0O0OO ,O0O000OOO00OOO00O ,"帕累托图"),)#line:1504
    O0OOOO0OO00OOO0OO .pack (side =LEFT )#line:1505
def helper ():#line:1511
    ""#line:1512
    O000OO000OOO00OOO =Toplevel ()#line:1513
    O000OO000OOO00OOO .title ("程序使用帮助")#line:1514
    O000OO000OOO00OOO .geometry ("700x500")#line:1515
    O00OO00O0OOO00OOO =Scrollbar (O000OO000OOO00OOO )#line:1517
    O0OOO0000O0OOOO00 =Text (O000OO000OOO00OOO ,height =80 ,width =150 ,bg ="#FFFFFF",font ="微软雅黑")#line:1518
    O00OO00O0OOO00OOO .pack (side =RIGHT ,fill =Y )#line:1519
    O0OOO0000O0OOOO00 .pack ()#line:1520
    O00OO00O0OOO00OOO .config (command =O0OOO0000O0OOOO00 .yview )#line:1521
    O0OOO0000O0OOOO00 .config (yscrollcommand =O00OO00O0OOO00OOO .set )#line:1522
    O0OOO0000O0OOOO00 .insert (END ,"\n  本程序用于趋势分析,供广东省内参与医疗器械警戒试点的企业免费使用。如您有相关问题或改进建议，请联系以下人员：\n\n    佛山市药品不良反应监测中心\n    蔡权周 \n    微信：18575757461 \n    邮箱：411703730@qq.com")#line:1527
    O0OOO0000O0OOOO00 .config (state =DISABLED )#line:1528
def Tread_TOOLS_CLEAN (O00O0OO0OOO000OOO ):#line:1532
        ""#line:1533
        O00O0OO0OOO000OOO ["报告编码"]=O00O0OO0OOO000OOO ["报告编码"].astype ("str")#line:1535
        O00O0OO0OOO000OOO ["产品批号"]=O00O0OO0OOO000OOO ["产品批号"].astype ("str")#line:1537
        O00O0OO0OOO000OOO ["型号"]=O00O0OO0OOO000OOO ["型号"].astype ("str")#line:1538
        O00O0OO0OOO000OOO ["规格"]=O00O0OO0OOO000OOO ["规格"].astype ("str")#line:1539
        O00O0OO0OOO000OOO ["注册证编号/曾用注册证编号"]=O00O0OO0OOO000OOO ["注册证编号/曾用注册证编号"].str .replace ("(","（",regex =False )#line:1541
        O00O0OO0OOO000OOO ["注册证编号/曾用注册证编号"]=O00O0OO0OOO000OOO ["注册证编号/曾用注册证编号"].str .replace (")","）",regex =False )#line:1542
        O00O0OO0OOO000OOO ["注册证编号/曾用注册证编号"]=O00O0OO0OOO000OOO ["注册证编号/曾用注册证编号"].str .replace ("*","※",regex =False )#line:1543
        O00O0OO0OOO000OOO ["产品名称"]=O00O0OO0OOO000OOO ["产品名称"].str .replace ("*","※",regex =False )#line:1545
        O00O0OO0OOO000OOO ["产品批号"]=O00O0OO0OOO000OOO ["产品批号"].str .replace ("(","（",regex =False )#line:1547
        O00O0OO0OOO000OOO ["产品批号"]=O00O0OO0OOO000OOO ["产品批号"].str .replace (")","）",regex =False )#line:1548
        O00O0OO0OOO000OOO ["产品批号"]=O00O0OO0OOO000OOO ["产品批号"].str .replace ("*","※",regex =False )#line:1549
        O00O0OO0OOO000OOO ['事件发生日期']=pd .to_datetime (O00O0OO0OOO000OOO ['事件发生日期'],format ='%Y-%m-%d',errors ='coerce')#line:1552
        O00O0OO0OOO000OOO ["事件发生月份"]=O00O0OO0OOO000OOO ["事件发生日期"].dt .to_period ("M").astype (str )#line:1556
        O00O0OO0OOO000OOO ["事件发生季度"]=O00O0OO0OOO000OOO ["事件发生日期"].dt .to_period ("Q").astype (str )#line:1557
        O00O0OO0OOO000OOO ["注册证编号/曾用注册证编号"]=O00O0OO0OOO000OOO ["注册证编号/曾用注册证编号"].fillna ("未填写")#line:1561
        O00O0OO0OOO000OOO ["产品批号"]=O00O0OO0OOO000OOO ["产品批号"].fillna ("未填写")#line:1562
        O00O0OO0OOO000OOO ["型号"]=O00O0OO0OOO000OOO ["型号"].fillna ("未填写")#line:1563
        O00O0OO0OOO000OOO ["规格"]=O00O0OO0OOO000OOO ["规格"].fillna ("未填写")#line:1564
        return O00O0OO0OOO000OOO #line:1566
def thread_it (O00OOOOO0OOO0OO0O ,*O0OO00O0000O0O0OO ):#line:1570
    ""#line:1571
    OOOOOOOO00O0O00OO =threading .Thread (target =O00OOOOO0OOO0OO0O ,args =O0OO00O0000O0O0OO )#line:1573
    OOOOOOOO00O0O00OO .setDaemon (True )#line:1575
    OOOOOOOO00O0O00OO .start ()#line:1577
def showWelcome ():#line:1580
    ""#line:1581
    OOO00OOO0OOOO0OO0 =roox .winfo_screenwidth ()#line:1582
    OO0O0OO00000O0OOO =roox .winfo_screenheight ()#line:1584
    roox .overrideredirect (True )#line:1586
    roox .attributes ("-alpha",1 )#line:1587
    OOOO0O0OO0OO0000O =(OOO00OOO0OOOO0OO0 -475 )/2 #line:1588
    OOO0OOOO0OOO0O000 =(OO0O0OO00000O0OOO -200 )/2 #line:1589
    roox .geometry ("675x140+%d+%d"%(OOOO0O0OO0OO0000O ,OOO0OOOO0OOO0O000 ))#line:1591
    roox ["bg"]="royalblue"#line:1592
    O0OOO00OO0OO0OOOO =Label (roox ,text ="医疗器械警戒趋势分析工具",fg ="white",bg ="royalblue",font =("微软雅黑",20 ))#line:1595
    O0OOO00OO0OO0OOOO .place (x =0 ,y =15 ,width =675 ,height =90 )#line:1596
    OOO000OO000O0O000 =Label (roox ,text ="Trend Analysis Tools V"+str (version_now ),fg ="white",bg ="cornflowerblue",font =("微软雅黑",15 ),)#line:1603
    OOO000OO000O0O000 .place (x =0 ,y =90 ,width =675 ,height =50 )#line:1604
def closeWelcome ():#line:1607
    ""#line:1608
    for O00OO000O0O00O0OO in range (2 ):#line:1609
        root .attributes ("-alpha",0 )#line:1610
        time .sleep (1 )#line:1611
    root .attributes ("-alpha",1 )#line:1612
    roox .destroy ()#line:1613
if __name__ =='__main__':#line:1617
    pass #line:1618
root =Tk ()#line:1619
root .title ("医疗器械警戒趋势分析工具Trend Analysis Tools V"+str (version_now ))#line:1620
sw_root =root .winfo_screenwidth ()#line:1621
sh_root =root .winfo_screenheight ()#line:1623
ww_root =700 #line:1625
wh_root =620 #line:1626
x_root =(sw_root -ww_root )/2 #line:1628
y_root =(sh_root -wh_root )/2 #line:1629
root .geometry ("%dx%d+%d+%d"%(ww_root ,wh_root ,x_root ,y_root ))#line:1630
root .configure (bg ="steelblue")#line:1631
try :#line:1634
    frame0 =ttk .Frame (root ,width =100 ,height =20 )#line:1635
    frame0 .pack (side =LEFT )#line:1636
    B_open_files1 =Button (frame0 ,text ="导入原始数据",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_fileopen ,0 ),)#line:1649
    B_open_files1 .pack ()#line:1650
    B_open_files3 =Button (frame0 ,text ="导入分析规则",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_fileopen ,1 ),)#line:1663
    B_open_files3 .pack ()#line:1664
    B_open_files3 =Button (frame0 ,text ="趋势统计分析",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_analysis ,0 ),)#line:1679
    B_open_files3 .pack ()#line:1680
    B_open_files3 =Button (frame0 ,text ="直方图（数量）",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_bar ,"数量"))#line:1693
    B_open_files3 .pack ()#line:1694
    B_open_files3 =Button (frame0 ,text ="直方图（占比）",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_bar ,"百分比"))#line:1705
    B_open_files3 .pack ()#line:1706
    B_open_files3 =Button (frame0 ,text ="查看帮助文件",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (helper ))#line:1717
    B_open_files3 .pack ()#line:1718
    B_open_files3 =Button (frame0 ,text ="更改用户分组",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (display_random_number ))#line:1729
    B_open_files3 .pack ()#line:1730
except :#line:1731
    pass #line:1732
text =ScrolledText (root ,height =400 ,width =400 ,bg ="#FFFFFF",font ="微软雅黑")#line:1736
text .pack ()#line:1737
text .insert (END ,"\n  本程序用于趋势分析,供广东省内参与医疗器械警戒试点的企业免费使用。如您有相关问题或改进建议，请联系以下人员：\n\n    佛山市药品不良反应监测中心\n    蔡权周 \n    微信：18575757461 \n    邮箱：411703730@qq.com")#line:1742
text .insert (END ,"\n\n")#line:1743
def A000 ():#line:1745
    pass #line:1746
setting_cfg =read_setting_cfg ()#line:1750
generate_random_file ()#line:1751
setting_cfg =open_setting_cfg ()#line:1752
if setting_cfg ["settingdir"]==0 :#line:1753
    showinfo (title ="提示",message ="未发现默认配置文件夹，请选择一个。如该配置文件夹中并无配置文件，将生成默认配置文件。")#line:1754
    filepathu =filedialog .askdirectory ()#line:1755
    path =get_directory_path (filepathu )#line:1756
    update_setting_cfg ("settingdir",path )#line:1757
setting_cfg =open_setting_cfg ()#line:1758
random_number =int (setting_cfg ["sidori"])#line:1759
input_number =int (str (setting_cfg ["sidfinal"])[0 :6 ])#line:1760
day_end =convert_and_compare_dates (str (setting_cfg ["sidfinal"])[6 :14 ])#line:1761
sid =random_number *2 +183576 #line:1762
if input_number ==sid and day_end =="未过期":#line:1763
    usergroup ="用户组=1"#line:1764
    text .insert (END ,usergroup +"   有效期至：")#line:1765
    text .insert (END ,datetime .strptime (str (int (int (str (setting_cfg ["sidfinal"])[6 :14 ])/4 )),"%Y%m%d"))#line:1766
else :#line:1767
    text .insert (END ,usergroup )#line:1768
text .insert (END ,"\n配置文件路径："+setting_cfg ["settingdir"]+"\n")#line:1769
aaass =update_software ("treadtools")#line:1770
text .insert (END ,aaass )#line:1771
roox =Toplevel ()#line:1774
tMain =threading .Thread (target =showWelcome )#line:1775
tMain .start ()#line:1776
t1 =threading .Thread (target =closeWelcome )#line:1777
t1 .start ()#line:1778
root .lift ()#line:1782
root .attributes ("-topmost",True )#line:1783
root .attributes ("-topmost",False )#line:1784
root .mainloop ()#line:1785
