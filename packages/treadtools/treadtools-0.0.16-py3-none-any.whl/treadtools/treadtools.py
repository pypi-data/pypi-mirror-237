#!/usr/bin/env python
# coding: utf-8
# 趋势分析工具Trend Analysis Tools 
# 开发人：蔡权周
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
version_now ="0.0.15"#line:57
usergroup ="用户组=0"#line:58
setting_cfg =""#line:59
csdir =str (os .path .abspath (__file__ )).replace (str (__file__ ),"")#line:61
if csdir =="":#line:62
    csdir =str (os .path .dirname (__file__ ))#line:63
    csdir =csdir +csdir .split ("treadtools" )[0 ][-1 ]#line:64
def extract_zip_file (O000O0OOOO00O000O ,OO00O0O00OOOO0O0O ):#line:73
    import zipfile #line:75
    if OO00O0O00OOOO0O0O =="":#line:76
        return 0 #line:77
    with zipfile .ZipFile (O000O0OOOO00O000O ,'r')as OO00O0O0O0OOOOO0O :#line:78
        for OOOOO000O0OO000O0 in OO00O0O0O0OOOOO0O .infolist ():#line:79
            OOOOO000O0OO000O0 .filename =OOOOO000O0OO000O0 .filename .encode ('cp437').decode ('gbk')#line:81
            OO00O0O0O0OOOOO0O .extract (OOOOO000O0OO000O0 ,OO00O0O00OOOO0O0O )#line:82
def get_directory_path (OOO0O000OOO0OOOO0 ):#line:88
    global csdir #line:90
    if not (os .path .isfile (os .path .join (OOO0O000OOO0OOOO0 ,'规则文件.xls'))):#line:92
        extract_zip_file (csdir +"def.py",OOO0O000OOO0OOOO0 )#line:97
    if OOO0O000OOO0OOOO0 =="":#line:99
        quit ()#line:100
    return OOO0O000OOO0OOOO0 #line:101
def convert_and_compare_dates (O0O0OOO0OOOOOOO0O ):#line:105
    import datetime #line:106
    OO0O00OOOO0OO0O0O =datetime .datetime .now ()#line:107
    try :#line:109
       OOO0OO0O0000O0O00 =datetime .datetime .strptime (str (int (int (O0O0OOO0OOOOOOO0O )/4 )),"%Y%m%d")#line:110
    except :#line:111
        print ("fail")#line:112
        return "已过期"#line:113
    if OOO0OO0O0000O0O00 >OO0O00OOOO0OO0O0O :#line:115
        return "未过期"#line:117
    else :#line:118
        return "已过期"#line:119
def read_setting_cfg ():#line:121
    global csdir #line:122
    if os .path .exists (csdir +'setting.cfg'):#line:124
        text .insert (END ,"已完成初始化\n")#line:125
        with open (csdir +'setting.cfg','r')as O0000OOOOO0OO00OO :#line:126
            O0O00OO000OO0O00O =eval (O0000OOOOO0OO00OO .read ())#line:127
    else :#line:128
        O00O0O0O0OO000000 =csdir +'setting.cfg'#line:130
        with open (O00O0O0O0OO000000 ,'w')as O0000OOOOO0OO00OO :#line:131
            O0000OOOOO0OO00OO .write ('{"settingdir": 0, "sidori": 0, "sidfinal": "11111180000808"}')#line:132
        text .insert (END ,"未初始化，正在初始化...\n")#line:133
        O0O00OO000OO0O00O =read_setting_cfg ()#line:134
    return O0O00OO000OO0O00O #line:135
def open_setting_cfg ():#line:138
    global csdir #line:139
    with open (csdir +"setting.cfg","r")as O0OOOOOOO0000O00O :#line:141
        OO0O0OOOO0000OOO0 =eval (O0OOOOOOO0000O00O .read ())#line:143
    return OO0O0OOOO0000OOO0 #line:144
def update_setting_cfg (OO000O00OO00OO0OO ,OO0O0OOOOOOOOO00O ):#line:146
    global csdir #line:147
    with open (csdir +"setting.cfg","r")as O0O000O0OO000O0OO :#line:149
        OOO0O000OOO0O0OOO =eval (O0O000O0OO000O0OO .read ())#line:151
    if OOO0O000OOO0O0OOO [OO000O00OO00OO0OO ]==0 or OOO0O000OOO0O0OOO [OO000O00OO00OO0OO ]=="11111180000808":#line:153
        OOO0O000OOO0O0OOO [OO000O00OO00OO0OO ]=OO0O0OOOOOOOOO00O #line:154
        with open (csdir +"setting.cfg","w")as O0O000O0OO000O0OO :#line:156
            O0O000O0OO000O0OO .write (str (OOO0O000OOO0O0OOO ))#line:157
def generate_random_file ():#line:160
    O00OOO0O0000OOOO0 =random .randint (200000 ,299999 )#line:162
    update_setting_cfg ("sidori",O00OOO0O0000OOOO0 )#line:164
def display_random_number ():#line:166
    global csdir #line:167
    OOO00OOOOO000O000 =Toplevel ()#line:168
    OOO00OOOOO000O000 .title ("ID")#line:169
    O0000OO00OOO0O000 =OOO00OOOOO000O000 .winfo_screenwidth ()#line:171
    OOOOO0O0O000O0O00 =OOO00OOOOO000O000 .winfo_screenheight ()#line:172
    OO0OO0OOO00O0O0OO =80 #line:174
    OOOOO0O0OO0O0OO0O =70 #line:175
    O00O0O000OOO00000 =(O0000OO00OOO0O000 -OO0OO0OOO00O0O0OO )/2 #line:177
    O0OOOOO000O0O000O =(OOOOO0O0O000O0O00 -OOOOO0O0OO0O0OO0O )/2 #line:178
    OOO00OOOOO000O000 .geometry ("%dx%d+%d+%d"%(OO0OO0OOO00O0O0OO ,OOOOO0O0OO0O0OO0O ,O00O0O000OOO00000 ,O0OOOOO000O0O000O ))#line:179
    with open (csdir +"setting.cfg","r")as O000O00O0OOO0O0O0 :#line:182
        O0OOOOO0O0OOOO0OO =eval (O000O00O0OOO0O0O0 .read ())#line:184
    O0O000OO0O0O000O0 =int (O0OOOOO0O0OOOO0OO ["sidori"])#line:185
    OO00O000OOOOO0OOO =O0O000OO0O0O000O0 *2 +183576 #line:186
    print (OO00O000OOOOO0OOO )#line:188
    OO0OO00OO00OOOO0O =ttk .Label (OOO00OOOOO000O000 ,text =f"机器码: {O0O000OO0O0O000O0}")#line:190
    O0O0000OOO00000OO =ttk .Entry (OOO00OOOOO000O000 )#line:191
    OO0OO00OO00OOOO0O .pack ()#line:194
    O0O0000OOO00000OO .pack ()#line:195
    ttk .Button (OOO00OOOOO000O000 ,text ="验证",command =lambda :check_input (O0O0000OOO00000OO .get (),OO00O000OOOOO0OOO )).pack ()#line:199
def check_input (O0O00O00O0O0OOO0O ,OOOOOOO000OOO0000 ):#line:201
    try :#line:205
        OO0OOO00OOOOO0OOO =int (str (O0O00O00O0O0OOO0O )[0 :6 ])#line:206
        OO00OO0OOOO000OOO =convert_and_compare_dates (str (O0O00O00O0O0OOO0O )[6 :14 ])#line:207
    except :#line:208
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:209
        return 0 #line:210
    if OO0OOO00OOOOO0OOO ==OOOOOOO000OOO0000 and OO00OO0OOOO000OOO =="未过期":#line:212
        update_setting_cfg ("sidfinal",O0O00O00O0O0OOO0O )#line:213
        showinfo (title ="提示",message ="注册成功,请重新启动程序。")#line:214
        quit ()#line:215
    else :#line:216
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:217
def Tread_TOOLS_fileopen (O0OOOO00O00O0O0OO ):#line:225
    ""#line:226
    global TT_ori #line:227
    global TT_ori_backup #line:228
    global TT_biaozhun #line:229
    warnings .filterwarnings ('ignore')#line:230
    if O0OOOO00O00O0O0OO ==0 :#line:232
        O00000OOOO0OOO00O =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:233
        OO0OOOO0000O000OO =[pd .read_excel (OOO0O0OO0OO0OOO00 ,header =0 ,sheet_name =0 )for OOO0O0OO0OO0OOO00 in O00000OOOO0OOO00O ]#line:234
        O0O00O000OOO0O0O0 =pd .concat (OO0OOOO0000O000OO ,ignore_index =True ).drop_duplicates ()#line:235
        try :#line:236
            O0O00O000OOO0O0O0 =O0O00O000OOO0O0O0 .loc [:,~TT_ori .columns .str .contains ("^Unnamed")]#line:237
        except :#line:238
            pass #line:239
        TT_ori_backup =O0O00O000OOO0O0O0 .copy ()#line:240
        TT_ori =Tread_TOOLS_CLEAN (O0O00O000OOO0O0O0 ).copy ()#line:241
        text .insert (END ,"\n原始数据导入成功，行数："+str (len (TT_ori )))#line:243
        text .insert (END ,"\n数据校验：\n")#line:244
        text .insert (END ,TT_ori )#line:245
        text .see (END )#line:246
    if O0OOOO00O00O0O0OO ==1 :#line:248
        O000OOO0OO00O0O00 =filedialog .askopenfilename (filetypes =[("XLS",".xls")])#line:249
        TT_biaozhun ["关键字表"]=pd .read_excel (O000OOO0OO00O0O00 ,sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:250
        TT_biaozhun ["产品批号"]=pd .read_excel (O000OOO0OO00O0O00 ,sheet_name ="产品批号",header =0 ,index_col =0 ,).reset_index ()#line:251
        TT_biaozhun ["事件发生月份"]=pd .read_excel (O000OOO0OO00O0O00 ,sheet_name ="事件发生月份",header =0 ,index_col =0 ,).reset_index ()#line:252
        TT_biaozhun ["事件发生季度"]=pd .read_excel (O000OOO0OO00O0O00 ,sheet_name ="事件发生季度",header =0 ,index_col =0 ,).reset_index ()#line:253
        TT_biaozhun ["规格"]=pd .read_excel (O000OOO0OO00O0O00 ,sheet_name ="规格",header =0 ,index_col =0 ,).reset_index ()#line:254
        TT_biaozhun ["型号"]=pd .read_excel (O000OOO0OO00O0O00 ,sheet_name ="型号",header =0 ,index_col =0 ,).reset_index ()#line:255
        TT_biaozhun ["设置"]=pd .read_excel (O000OOO0OO00O0O00 ,sheet_name ="设置",header =0 ,index_col =0 ,).reset_index ()#line:256
        Tread_TOOLS_check (TT_ori ,TT_biaozhun ["关键字表"],0 )#line:257
        text .insert (END ,"\n标准导入成功，行数："+str (len (TT_biaozhun )))#line:258
        text .see (END )#line:259
def Tread_TOOLS_check (O0OOOOO0OO0O0O0O0 ,OOOOO0OOOO000O00O ,O0OOOO0O0000OOO00 ):#line:261
        ""#line:262
        global TT_ori #line:263
        O0000OO000OOO00O0 =Tread_TOOLS_Countall (O0OOOOO0OO0O0O0O0 ).df_psur (OOOOO0OOOO000O00O )#line:264
        if O0OOOO0O0000OOO00 ==0 :#line:266
            Tread_TOOLS_tree_Level_2 (O0000OO000OOO00O0 ,0 ,TT_ori .copy ())#line:268
        O0000OO000OOO00O0 ["核验"]=0 #line:271
        O0000OO000OOO00O0 .loc [(O0000OO000OOO00O0 ["关键字标记"].str .contains ("-其他关键字-",na =False )),"核验"]=O0000OO000OOO00O0 .loc [(O0000OO000OOO00O0 ["关键字标记"].str .contains ("-其他关键字-",na =False )),"总数量"]#line:272
        if O0000OO000OOO00O0 ["核验"].sum ()>0 :#line:273
            showinfo (title ="温馨提示",message ="存在未定义类型的报告"+str (O0000OO000OOO00O0 ["核验"].sum ())+"条，趋势分析可能会存在遗漏，建议修正该错误再进行下一步。")#line:274
def Tread_TOOLS_tree_Level_2 (O0OOOOO00O00OOOO0 ,O000000O000O00000 ,OO00O0000O0000O0O ,*OO0O0O0OOOO0O0O0O ):#line:276
    ""#line:277
    global TT_ori_backup #line:279
    OO00000OOOO000O00 =O0OOOOO00O00OOOO0 .columns .values .tolist ()#line:281
    O000000O000O00000 =0 #line:282
    OOOO000O0O0OO0OO0 =O0OOOOO00O00OOOO0 .loc [:]#line:283
    OOO0O0OO000000O0O =0 #line:287
    try :#line:288
        O00O00OO00O0O0O0O =OO0O0O0OOOO0O0O0O [0 ]#line:289
        OOO0O0OO000000O0O =1 #line:290
    except :#line:291
        pass #line:292
    OO0O0OOO0O00000O0 =Toplevel ()#line:295
    OO0O0OOO0O00000O0 .title ("报表查看器")#line:296
    OO0OOO0000OO0OOOO =OO0O0OOO0O00000O0 .winfo_screenwidth ()#line:297
    O0O000OOOOO0O0OOO =OO0O0OOO0O00000O0 .winfo_screenheight ()#line:299
    O0000OO0O000O0000 =1300 #line:301
    OO0000O0O00O0OOO0 =600 #line:302
    OO0O00O00000O0000 =(OO0OOO0000OO0OOOO -O0000OO0O000O0000 )/2 #line:304
    OO0000OO0O00O0O0O =(O0O000OOOOO0O0OOO -OO0000O0O00O0OOO0 )/2 #line:305
    OO0O0OOO0O00000O0 .geometry ("%dx%d+%d+%d"%(O0000OO0O000O0000 ,OO0000O0O00O0OOO0 ,OO0O00O00000O0000 ,OO0000OO0O00O0O0O ))#line:306
    O00O00000O0000O0O =ttk .Frame (OO0O0OOO0O00000O0 ,width =1300 ,height =20 )#line:307
    O00O00000O0000O0O .pack (side =BOTTOM )#line:308
    O0O00000OOO00OOOO =ttk .Frame (OO0O0OOO0O00000O0 ,width =1300 ,height =20 )#line:310
    O0O00000OOO00OOOO .pack (side =TOP )#line:311
    if 1 >0 :#line:315
        O00OOOO0OO0O00000 =Button (O00O00000O0000O0O ,text ="控制图(所有)",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (OOOO000O0O0OO0OO0 [:-1 ],O00O00OO00O0O0O0O ,[O00000OOOOO0O0000 for O00000OOOOO0O0000 in OOOO000O0O0OO0OO0 .columns if (O00000OOOOO0O0000 not in [O00O00OO00O0O0O0O ])],"关键字趋势图",100 ),)#line:325
        if OOO0O0OO000000O0O ==1 :#line:326
            O00OOOO0OO0O00000 .pack (side =LEFT )#line:327
        O00OOOO0OO0O00000 =Button (O00O00000O0000O0O ,text ="控制图(总数量)",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (OOOO000O0O0OO0OO0 [:-1 ],O00O00OO00O0O0O0O ,[O00O00O0OO0000OO0 for O00O00O0OO0000OO0 in OOOO000O0O0OO0OO0 .columns if (O00O00O0OO0000OO0 in ["该元素总数量"])],"关键字趋势图",100 ),)#line:337
        if OOO0O0OO000000O0O ==1 :#line:338
            O00OOOO0OO0O00000 .pack (side =LEFT )#line:339
        OOOO00OO00O0O00OO =Button (O00O00000O0000O0O ,text ="导出",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_save_dict (OOOO000O0O0OO0OO0 ),)#line:349
        OOOO00OO00O0O00OO .pack (side =LEFT )#line:350
        OOOO00OO00O0O00OO =Button (O00O00000O0000O0O ,text ="发生率测算",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_fashenglv (OOOO000O0O0OO0OO0 ,O00O00OO00O0O0O0O ),)#line:360
        if "关键字标记"not in OOOO000O0O0OO0OO0 .columns and "报告编码"not in OOOO000O0O0OO0OO0 .columns :#line:361
            if "对象"not in OOOO000O0O0OO0OO0 .columns :#line:362
                OOOO00OO00O0O00OO .pack (side =LEFT )#line:363
        OOOO00OO00O0O00OO =Button (O00O00000O0000O0O ,text ="直方图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_histbar (OOOO000O0O0OO0OO0 .copy ()),)#line:373
        if "对象"in OOOO000O0O0OO0OO0 .columns :#line:374
            OOOO00OO00O0O00OO .pack (side =LEFT )#line:375
        OO0O0OO0OO0O00OO0 =Button (O00O00000O0000O0O ,text ="行数:"+str (len (OOOO000O0O0OO0OO0 )),bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",)#line:385
        OO0O0OO0OO0O00OO0 .pack (side =LEFT )#line:386
    OOO0OO0OO00O0000O =OOOO000O0O0OO0OO0 .values .tolist ()#line:389
    O0OO0OOO0O0000OOO =OOOO000O0O0OO0OO0 .columns .values .tolist ()#line:390
    OO00OO00O00O00000 =ttk .Treeview (O0O00000OOO00OOOO ,columns =O0OO0OOO0O0000OOO ,show ="headings",height =45 )#line:391
    for OO0OOO0O000000O0O in O0OO0OOO0O0000OOO :#line:393
        OO00OO00O00O00000 .heading (OO0OOO0O000000O0O ,text =OO0OOO0O000000O0O )#line:394
    for O0O0OO0OOOO00O00O in OOO0OO0OO00O0000O :#line:395
        OO00OO00O00O00000 .insert ("","end",values =O0O0OO0OOOO00O00O )#line:396
    for O0O000OOOOOO00000 in O0OO0OOO0O0000OOO :#line:397
        OO00OO00O00O00000 .column (O0O000OOOOOO00000 ,minwidth =0 ,width =120 ,stretch =NO )#line:398
    O0O000O0O00OO000O =Scrollbar (O0O00000OOO00OOOO ,orient ="vertical")#line:400
    O0O000O0O00OO000O .pack (side =RIGHT ,fill =Y )#line:401
    O0O000O0O00OO000O .config (command =OO00OO00O00O00000 .yview )#line:402
    OO00OO00O00O00000 .config (yscrollcommand =O0O000O0O00OO000O .set )#line:403
    O0O0000OOOO000O00 =Scrollbar (O0O00000OOO00OOOO ,orient ="horizontal")#line:405
    O0O0000OOOO000O00 .pack (side =BOTTOM ,fill =X )#line:406
    O0O0000OOOO000O00 .config (command =OO00OO00O00O00000 .xview )#line:407
    OO00OO00O00O00000 .config (yscrollcommand =O0O000O0O00OO000O .set )#line:408
    def O0O00OOOO0O000OOO (O00OO0000O0O0O00O ,OO0OO00OO00OO0OOO ,O0O000O0000O0O0OO ):#line:410
        for OO0000OOOOO00000O in OO00OO00O00O00000 .selection ():#line:413
            OOO00O0OO0OO0O0OO =OO00OO00O00O00000 .item (OO0000OOOOO00000O ,"values")#line:414
            O0OO0OO0O00OOO0O0 =dict (zip (OO0OO00OO00OO0OOO ,OOO00O0OO0OO0O0OO ))#line:415
        if "该分类下各项计数"in OO0OO00OO00OO0OOO :#line:417
            OO0OO0000OOOOOOOO =OO00O0000O0000O0O .copy ()#line:418
            OO0OO0000OOOOOOOO ["关键字查找列"]=""#line:419
            for OO00OO0O00O00OO00 in TOOLS_get_list (O0OO0OO0O00OOO0O0 ["查找位置"]):#line:420
                OO0OO0000OOOOOOOO ["关键字查找列"]=OO0OO0000OOOOOOOO ["关键字查找列"]+OO0OO0000OOOOOOOO [OO00OO0O00O00OO00 ].astype ("str")#line:421
            O00OOO0O0OO0OOO0O =OO0OO0000OOOOOOOO .loc [OO0OO0000OOOOOOOO ["关键字查找列"].str .contains (O0OO0OO0O00OOO0O0 ["关键字标记"],na =False )].copy ()#line:422
            O00OOO0O0OO0OOO0O =O00OOO0O0OO0OOO0O .loc [~O00OOO0O0OO0OOO0O ["关键字查找列"].str .contains (O0OO0OO0O00OOO0O0 ["排除值"],na =False )].copy ()#line:423
            Tread_TOOLS_tree_Level_2 (O00OOO0O0OO0OOO0O ,0 ,O00OOO0O0OO0OOO0O )#line:429
            return 0 #line:430
        if "报告编码"in OO0OO00OO00OO0OOO :#line:432
            OO00O000OO00OOOO0 =Toplevel ()#line:433
            O0OOOOO0OO0OO0OOO =OO00O000OO00OOOO0 .winfo_screenwidth ()#line:434
            O0O00OO0OOOOOO0O0 =OO00O000OO00OOOO0 .winfo_screenheight ()#line:436
            O0O0OO00O0OOO00O0 =800 #line:438
            O0OOOOOOO0O0OO000 =600 #line:439
            OO00OO0O00O00OO00 =(O0OOOOO0OO0OO0OOO -O0O0OO00O0OOO00O0 )/2 #line:441
            OO0O0O00OO0OO0O0O =(O0O00OO0OOOOOO0O0 -O0OOOOOOO0O0OO000 )/2 #line:442
            OO00O000OO00OOOO0 .geometry ("%dx%d+%d+%d"%(O0O0OO00O0OOO00O0 ,O0OOOOOOO0O0OO000 ,OO00OO0O00O00OO00 ,OO0O0O00OO0OO0O0O ))#line:443
            O0O0000O0O0OO0OOO =ScrolledText (OO00O000OO00OOOO0 ,height =1100 ,width =1100 ,bg ="#FFFFFF")#line:447
            O0O0000O0O0OO0OOO .pack (padx =10 ,pady =10 )#line:448
            def O00000OOOOO00O0O0 (event =None ):#line:449
                O0O0000O0O0OO0OOO .event_generate ('<<Copy>>')#line:450
            def OO0OOOOOO0O000000 (OOOO0OO0O0OOO00OO ,OOOOOO00O000000OO ):#line:451
                O000OO00OOOO0O00O =open (OOOOOO00O000000OO ,"w",encoding ='utf-8')#line:452
                O000OO00OOOO0O00O .write (OOOO0OO0O0OOO00OO )#line:453
                O000OO00OOOO0O00O .flush ()#line:455
                showinfo (title ="提示信息",message ="保存成功。")#line:456
            OOOOO0OO0OO0OO00O =Menu (O0O0000O0O0OO0OOO ,tearoff =False ,)#line:458
            OOOOO0OO0OO0OO00O .add_command (label ="复制",command =O00000OOOOO00O0O0 )#line:459
            OOOOO0OO0OO0OO00O .add_command (label ="导出",command =lambda :thread_it (OO0OOOOOO0O000000 ,O0O0000O0O0OO0OOO .get (1.0 ,'end'),filedialog .asksaveasfilename (title =u"保存文件",initialfile =O0OO0OO0O00OOO0O0 ["报告编码"],defaultextension ="txt",filetypes =[("txt","*.txt")])))#line:460
            def OO0OO0000O0O00O00 (OO0OO0OOO00OOO000 ):#line:462
                OOOOO0OO0OO0OO00O .post (OO0OO0OOO00OOO000 .x_root ,OO0OO0OOO00OOO000 .y_root )#line:463
            O0O0000O0O0OO0OOO .bind ("<Button-3>",OO0OO0000O0O00O00 )#line:464
            OO00O000OO00OOOO0 .title (O0OO0OO0O00OOO0O0 ["报告编码"])#line:466
            for O000O0OOOOO00O00O in range (len (OO0OO00OO00OO0OOO )):#line:467
                O0O0000O0O0OO0OOO .insert (END ,OO0OO00OO00OO0OOO [O000O0OOOOO00O00O ])#line:469
                O0O0000O0O0OO0OOO .insert (END ,"：")#line:470
                O0O0000O0O0OO0OOO .insert (END ,O0OO0OO0O00OOO0O0 [OO0OO00OO00OO0OOO [O000O0OOOOO00O00O ]])#line:471
                O0O0000O0O0OO0OOO .insert (END ,"\n")#line:472
            O0O0000O0O0OO0OOO .config (state =DISABLED )#line:473
            return 0 #line:474
        OO0O0O00OO0OO0O0O =OOO00O0OO0OO0O0OO [1 :-1 ]#line:477
        OO00OO0O00O00OO00 =O0O000O0000O0O0OO .columns .tolist ()#line:479
        OO00OO0O00O00OO00 =OO00OO0O00O00OO00 [1 :-1 ]#line:480
        OOO00O0OOOOOO0O0O ={'关键词':OO00OO0O00O00OO00 ,'数量':OO0O0O00OO0OO0O0O }#line:482
        OOO00O0OOOOOO0O0O =pd .DataFrame .from_dict (OOO00O0OOOOOO0O0O )#line:483
        OOO00O0OOOOOO0O0O ["数量"]=OOO00O0OOOOOO0O0O ["数量"].astype (float )#line:484
        Tread_TOOLS_draw (OOO00O0OOOOOO0O0O ,"帕累托图",'关键词','数量',"帕累托图")#line:485
        return 0 #line:486
    OO00OO00O00O00000 .bind ("<Double-1>",lambda OO0O000OOOO00OOOO :O0O00OOOO0O000OOO (OO0O000OOOO00OOOO ,O0OO0OOO0O0000OOO ,OOOO000O0O0OO0OO0 ),)#line:494
    OO00OO00O00O00000 .pack ()#line:495
class Tread_TOOLS_Countall ():#line:497
    ""#line:498
    def __init__ (O0OO0O0O0O000O000 ,OOOOOOOO0OOOOO0O0 ):#line:499
        ""#line:500
        O0OO0O0O0O000O000 .df =OOOOOOOO0OOOOO0O0 #line:501
    def df_psur (O0O0O0000OO0O0O0O ,O0000000000O0OOO0 ,*O000O00OO0OO000O0 ):#line:503
        ""#line:504
        global TT_biaozhun #line:505
        O0O000OO0OOO00O00 =O0O0O0000OO0O0O0O .df .copy ()#line:506
        O0000O0OO00OO0O0O =len (O0O000OO0OOO00O00 .drop_duplicates ("报告编码"))#line:508
        O0OO0O0O00O0OOOOO =O0000000000O0OOO0 .copy ()#line:511
        OO0OOO0OO0O00OO00 =TT_biaozhun ["设置"]#line:514
        if OO0OOO0OO0O00OO00 .loc [1 ,"值"]:#line:515
            O0OO0000O00OO00OO =OO0OOO0OO0O00OO00 .loc [1 ,"值"]#line:516
        else :#line:517
            O0OO0000O00OO00OO ="透视列"#line:518
            O0O000OO0OOO00O00 [O0OO0000O00OO00OO ]="未正确设置"#line:519
        O00O0O00O0OOO000O =""#line:521
        O000OO000O0O00000 ="-其他关键字-"#line:522
        for O000O000OOOO0OO00 ,O0O0O00O000OOO00O in O0OO0O0O00O0OOOOO .iterrows ():#line:523
            O000OO000O0O00000 =O000OO000O0O00000 +"|"+str (O0O0O00O000OOO00O ["值"])#line:524
            OO00000OO0OO000O0 =O0O0O00O000OOO00O #line:525
        OO00000OO0OO000O0 [3 ]=O000OO000O0O00000 #line:526
        OO00000OO0OO000O0 [2 ]="-其他关键字-|"#line:527
        O0OO0O0O00O0OOOOO .loc [len (O0OO0O0O00O0OOOOO )]=OO00000OO0OO000O0 #line:528
        O0OO0O0O00O0OOOOO =O0OO0O0O00O0OOOOO .reset_index (drop =True )#line:529
        O0O000OO0OOO00O00 ["关键字查找列"]=""#line:533
        for OO00000O0OO000O00 in TOOLS_get_list (O0OO0O0O00O0OOOOO .loc [0 ,"查找位置"]):#line:534
            O0O000OO0OOO00O00 ["关键字查找列"]=O0O000OO0OOO00O00 ["关键字查找列"]+O0O000OO0OOO00O00 [OO00000O0OO000O00 ].astype ("str")#line:535
        O0O0OOOO0OOO0OOOO =[]#line:538
        for O000O000OOOO0OO00 ,O0O0O00O000OOO00O in O0OO0O0O00O0OOOOO .iterrows ():#line:539
            O00O000O00000O00O =O0O0O00O000OOO00O ["值"]#line:540
            OO0O00O0O0OO000O0 =O0O000OO0OOO00O00 .loc [O0O000OO0OOO00O00 ["关键字查找列"].str .contains (O00O000O00000O00O ,na =False )].copy ()#line:541
            if str (O0O0O00O000OOO00O ["排除值"])!="nan":#line:542
                OO0O00O0O0OO000O0 =OO0O00O0O0OO000O0 .loc [~OO0O00O0O0OO000O0 ["关键字查找列"].str .contains (str (O0O0O00O000OOO00O ["排除值"]),na =False )].copy ()#line:543
            OO0O00O0O0OO000O0 ["关键字标记"]=str (O00O000O00000O00O )#line:545
            OO0O00O0O0OO000O0 ["关键字计数"]=1 #line:546
            if len (OO0O00O0O0OO000O0 )>0 :#line:548
                O000000O00OOO0OO0 =pd .pivot_table (OO0O00O0O0OO000O0 .drop_duplicates ("报告编码"),values =["关键字计数"],index ="关键字标记",columns =O0OO0000O00OO00OO ,aggfunc ={"关键字计数":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:558
                O000000O00OOO0OO0 =O000000O00OOO0OO0 [:-1 ]#line:559
                O000000O00OOO0OO0 .columns =O000000O00OOO0OO0 .columns .droplevel (0 )#line:560
                O000000O00OOO0OO0 =O000000O00OOO0OO0 .reset_index ()#line:561
                if len (O000000O00OOO0OO0 )>0 :#line:564
                    O00O0OO0000OO0OOO =str (Counter (TOOLS_get_list0 ("use(关键字查找列).file",OO0O00O0O0OO000O0 ,1000 ))).replace ("Counter({","{")#line:565
                    O00O0OO0000OO0OOO =O00O0OO0000OO0OOO .replace ("})","}")#line:566
                    O00O0OO0000OO0OOO =ast .literal_eval (O00O0OO0000OO0OOO )#line:567
                    O000000O00OOO0OO0 .loc [0 ,"事件分类"]=str (TOOLS_get_list (O000000O00OOO0OO0 .loc [0 ,"关键字标记"])[0 ])#line:569
                    O000000O00OOO0OO0 .loc [0 ,"该分类下各项计数"]=str ({O0O0OOOO000O00000 :O00OO0OOO00000OO0 for O0O0OOOO000O00000 ,O00OO0OOO00000OO0 in O00O0OO0000OO0OOO .items ()if STAT_judge_x (str (O0O0OOOO000O00000 ),TOOLS_get_list (O00O000O00000O00O ))==1 })#line:570
                    O000000O00OOO0OO0 .loc [0 ,"其他分类各项计数"]=str ({OOO00O0O0OOOO00OO :O0OOO00O0OO0O0O0O for OOO00O0O0OOOO00OO ,O0OOO00O0OO0O0O0O in O00O0OO0000OO0OOO .items ()if STAT_judge_x (str (OOO00O0O0OOOO00OO ),TOOLS_get_list (O00O000O00000O00O ))!=1 })#line:571
                    O000000O00OOO0OO0 ["查找位置"]=O0O0O00O000OOO00O ["查找位置"]#line:572
                    O0O0OOOO0OOO0OOOO .append (O000000O00OOO0OO0 )#line:575
        O00O0O00O0OOO000O =pd .concat (O0O0OOOO0OOO0OOOO )#line:576
        O00O0O00O0OOO000O =O00O0O00O0OOO000O .sort_values (by =["All"],ascending =[False ],na_position ="last")#line:581
        O00O0O00O0OOO000O =O00O0O00O0OOO000O .reset_index ()#line:582
        O00O0O00O0OOO000O ["All占比"]=round (O00O0O00O0OOO000O ["All"]/O0000O0OO00OO0O0O *100 ,2 )#line:584
        O00O0O00O0OOO000O =O00O0O00O0OOO000O .rename (columns ={"All":"总数量","All占比":"总数量占比"})#line:585
        for O0OO0O0O0OO0OOO00 ,O00O00O0O0O00OOO0 in O0OO0O0O00O0OOOOO .iterrows ():#line:588
            O00O0O00O0OOO000O .loc [(O00O0O00O0OOO000O ["关键字标记"].astype (str )==str (O00O00O0O0O00OOO0 ["值"])),"排除值"]=O00O00O0O0O00OOO0 ["排除值"]#line:589
            O00O0O00O0OOO000O .loc [(O00O0O00O0OOO000O ["关键字标记"].astype (str )==str (O00O00O0O0O00OOO0 ["值"])),"查找位置"]=O00O00O0O0O00OOO0 ["查找位置"]#line:590
        O00O0O00O0OOO000O ["排除值"]=O00O0O00O0OOO000O ["排除值"].fillna ("-没有排除值-")#line:592
        O00O0O00O0OOO000O ["报表类型"]="PSUR"#line:595
        del O00O0O00O0OOO000O ["index"]#line:596
        try :#line:597
            del O00O0O00O0OOO000O ["未正确设置"]#line:598
        except :#line:599
            pass #line:600
        return O00O0O00O0OOO000O #line:601
    def df_find_all_keword_risk (O00O00OOOO0O0OOOO ,O0000O00000000000 ,*O0OO0O00O0O0OOOOO ):#line:604
        ""#line:605
        global TT_biaozhun #line:606
        OOOOOOO0O000OOOO0 =O00O00OOOO0O0OOOO .df .copy ()#line:608
        O0OO000OOOO0OO000 =time .time ()#line:609
        OO000OOOOOO0OOOOO =TT_biaozhun ["关键字表"].copy ()#line:611
        O0O0O00O0O0O00O00 ="作用对象"#line:613
        O000OOOO000OO0O0O ="报告编码"#line:615
        O0OOO0000OO0OOOOO =OOOOOOO0O000OOOO0 .groupby ([O0O0O00O0O0O00O00 ]).agg (总数量 =(O000OOOO000OO0O0O ,"nunique"),).reset_index ()#line:618
        O0OOOO0OO00O0O00O =[O0O0O00O0O0O00O00 ,O0000O00000000000 ]#line:620
        O0OO0O0000OOOOOOO =OOOOOOO0O000OOOO0 .groupby (O0OOOO0OO00O0O00O ).agg (该元素总数量 =(O0O0O00O0O0O00O00 ,"count"),).reset_index ()#line:624
        O00OOOOO0000OOOOO =[]#line:626
        O0OOO0OO00O00000O =0 #line:630
        O000O000OOO0O0O00 =int (len (O0OOO0000OO0OOOOO ))#line:631
        for OO000OOOOO00OO000 ,OOOO00OO00000OOO0 in zip (O0OOO0000OO0OOOOO [O0O0O00O0O0O00O00 ].values ,O0OOO0000OO0OOOOO ["总数量"].values ):#line:632
            O0OOO0OO00O00000O +=1 #line:633
            O000OOOO0OOOO0000 =OOOOOOO0O000OOOO0 [(OOOOOOO0O000OOOO0 [O0O0O00O0O0O00O00 ]==OO000OOOOO00OO000 )].copy ()#line:634
            for O0OOOOOO00O0O000O ,O00O00OOO00OO0O0O ,OOO00OO0O0OO0OO0O in zip (OO000OOOOOO0OOOOO ["值"].values ,OO000OOOOOO0OOOOO ["查找位置"].values ,OO000OOOOOO0OOOOO ["排除值"].values ):#line:636
                    O000O0O0OO00O0O0O =O000OOOO0OOOO0000 .copy ()#line:637
                    O0O000000O0OOOOO0 =TOOLS_get_list (O0OOOOOO00O0O000O )[0 ]#line:638
                    O000O0O0OO00O0O0O ["关键字查找列"]=""#line:640
                    for OO000OOO0OOOO0000 in TOOLS_get_list (O00O00OOO00OO0O0O ):#line:641
                        O000O0O0OO00O0O0O ["关键字查找列"]=O000O0O0OO00O0O0O ["关键字查找列"]+O000O0O0OO00O0O0O [OO000OOO0OOOO0000 ].astype ("str")#line:642
                    O000O0O0OO00O0O0O .loc [O000O0O0OO00O0O0O ["关键字查找列"].str .contains (O0OOOOOO00O0O000O ,na =False ),"关键字"]=O0O000000O0OOOOO0 #line:644
                    if str (OOO00OO0O0OO0OO0O )!="nan":#line:649
                        O000O0O0OO00O0O0O =O000O0O0OO00O0O0O .loc [~O000O0O0OO00O0O0O ["关键字查找列"].str .contains (OOO00OO0O0OO0OO0O ,na =False )].copy ()#line:650
                    if (len (O000O0O0OO00O0O0O ))<1 :#line:652
                        continue #line:654
                    O0OOOOO0OOO00OOO0 =STAT_find_keyword_risk (O000O0O0OO00O0O0O ,[O0O0O00O0O0O00O00 ,"关键字"],"关键字",O0000O00000000000 ,int (OOOO00OO00000OOO0 ))#line:656
                    if len (O0OOOOO0OOO00OOO0 )>0 :#line:657
                        O0OOOOO0OOO00OOO0 ["关键字组合"]=O0OOOOOO00O0O000O #line:658
                        O0OOOOO0OOO00OOO0 ["排除值"]=OOO00OO0O0OO0OO0O #line:659
                        O0OOOOO0OOO00OOO0 ["关键字查找列"]=O00O00OOO00OO0O0O #line:660
                        O00OOOOO0000OOOOO .append (O0OOOOO0OOO00OOO0 )#line:661
        if len (O00OOOOO0000OOOOO )<1 :#line:664
            showinfo (title ="错误信息",message ="该注册证号未检索到任何关键字，规则制定存在缺陷。")#line:665
            return 0 #line:666
        OO00OOO00OOO0OOO0 =pd .concat (O00OOOOO0000OOOOO )#line:667
        OO00OOO00OOO0OOO0 =pd .merge (OO00OOO00OOO0OOO0 ,O0OO0O0000OOOOOOO ,on =O0OOOO0OO00O0O00O ,how ="left")#line:670
        OO00OOO00OOO0OOO0 ["关键字数量比例"]=round (OO00OOO00OOO0OOO0 ["计数"]/OO00OOO00OOO0OOO0 ["该元素总数量"],2 )#line:671
        OO00OOO00OOO0OOO0 =OO00OOO00OOO0OOO0 .reset_index (drop =True )#line:673
        if len (OO00OOO00OOO0OOO0 )>0 :#line:676
            OO00OOO00OOO0OOO0 ["风险评分"]=0 #line:677
            OO00OOO00OOO0OOO0 ["报表类型"]="keyword_findrisk"+O0000O00000000000 #line:678
            OO00OOO00OOO0OOO0 .loc [(OO00OOO00OOO0OOO0 ["计数"]>=3 ),"风险评分"]=OO00OOO00OOO0OOO0 ["风险评分"]+3 #line:679
            OO00OOO00OOO0OOO0 .loc [(OO00OOO00OOO0OOO0 ["计数"]>=(OO00OOO00OOO0OOO0 ["数量均值"]+OO00OOO00OOO0OOO0 ["数量标准差"])),"风险评分"]=OO00OOO00OOO0OOO0 ["风险评分"]+1 #line:680
            OO00OOO00OOO0OOO0 .loc [(OO00OOO00OOO0OOO0 ["计数"]>=OO00OOO00OOO0OOO0 ["数量CI"]),"风险评分"]=OO00OOO00OOO0OOO0 ["风险评分"]+1 #line:681
            OO00OOO00OOO0OOO0 .loc [(OO00OOO00OOO0OOO0 ["关键字数量比例"]>0.5 )&(OO00OOO00OOO0OOO0 ["计数"]>=3 ),"风险评分"]=OO00OOO00OOO0OOO0 ["风险评分"]+1 #line:682
            OO00OOO00OOO0OOO0 =OO00OOO00OOO0OOO0 .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:684
        O00O0O0OOOO0O00OO =OO00OOO00OOO0OOO0 .columns .to_list ()#line:694
        O0OOO0000O0000O00 =O00O0O0OOOO0O00OO [O00O0O0OOOO0O00OO .index ("关键字")+1 ]#line:695
        O00OOOOO0O0OO00OO =pd .pivot_table (OO00OOO00OOO0OOO0 ,index =O0OOO0000O0000O00 ,columns ="关键字",values =["计数"],aggfunc ={"计数":"sum"},fill_value ="0",margins =True ,dropna =False ,)#line:706
        O00OOOOO0O0OO00OO .columns =O00OOOOO0O0OO00OO .columns .droplevel (0 )#line:707
        O00OOOOO0O0OO00OO =pd .merge (O00OOOOO0O0OO00OO ,OO00OOO00OOO0OOO0 [[O0OOO0000O0000O00 ,"该元素总数量"]].drop_duplicates (O0OOO0000O0000O00 ),on =[O0OOO0000O0000O00 ],how ="left")#line:710
        del O00OOOOO0O0OO00OO ["All"]#line:712
        O00OOOOO0O0OO00OO .iloc [-1 ,-1 ]=O00OOOOO0O0OO00OO ["该元素总数量"].sum (axis =0 )#line:713
        print ("耗时：",(time .time ()-O0OO000OOOO0OO000 ))#line:715
        return O00OOOOO0O0OO00OO #line:718
def Tread_TOOLS_bar (O00000O0O0OO0O0O0 ):#line:726
         ""#line:727
         OOO0OOO0O0OO000OO =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:728
         OOOOO0OO0O0000OOO =[pd .read_excel (O0O0OO0OO00O0000O ,header =0 ,sheet_name =0 )for O0O0OO0OO00O0000O in OOO0OOO0O0OO000OO ]#line:729
         OOOOOOO0OO00OOO0O =pd .concat (OOOOO0OO0O0000OOO ,ignore_index =True )#line:730
         OOOO000O0OOOOO0OO =pd .pivot_table (OOOOOOO0OO00OOO0O ,index ="对象",columns ="关键词",values =O00000O0O0OO0O0O0 ,aggfunc ="sum",fill_value ="0",margins =True ,dropna =False ,).reset_index ()#line:740
         del OOOO000O0OOOOO0OO ["All"]#line:742
         OOOO000O0OOOOO0OO =OOOO000O0OOOOO0OO [:-1 ]#line:743
         Tread_TOOLS_tree_Level_2 (OOOO000O0OOOOO0OO ,0 ,0 )#line:745
def Tread_TOOLS_analysis (O0OOO0O0OOO0OO0O0 ):#line:750
    ""#line:751
    import datetime #line:752
    global TT_ori #line:753
    global TT_biaozhun #line:754
    if len (TT_ori )==0 :#line:756
       showinfo (title ="提示",message ="您尚未导入原始数据。")#line:757
       return 0 #line:758
    if len (TT_biaozhun )==0 :#line:759
       showinfo (title ="提示",message ="您尚未导入规则。")#line:760
       return 0 #line:761
    OOO0O00O00O000OOO =TT_biaozhun ["设置"]#line:763
    TT_ori ["作用对象"]=""#line:764
    for OO0O0OOOOOO000OOO in TOOLS_get_list (OOO0O00O00O000OOO .loc [0 ,"值"]):#line:765
        TT_ori ["作用对象"]=TT_ori ["作用对象"]+"-"+TT_ori [OO0O0OOOOOO000OOO ].fillna ("未填写").astype ("str")#line:766
    OOOOO000O0O0000OO =Toplevel ()#line:769
    OOOOO000O0O0000OO .title ("单品分析")#line:770
    O000O000OO0O0O00O =OOOOO000O0O0000OO .winfo_screenwidth ()#line:771
    O0O0O0O0OO00OOO00 =OOOOO000O0O0000OO .winfo_screenheight ()#line:773
    OOO0O00O0OO000OO0 =580 #line:775
    O00O000000OOO0000 =80 #line:776
    OOO0O0O00O0O000OO =(O000O000OO0O0O00O -OOO0O00O0OO000OO0 )/1.7 #line:778
    O0O000OOOO0O0O0O0 =(O0O0O0O0OO00OOO00 -O00O000000OOO0000 )/2 #line:779
    OOOOO000O0O0000OO .geometry ("%dx%d+%d+%d"%(OOO0O00O0OO000OO0 ,O00O000000OOO0000 ,OOO0O0O00O0O000OO ,O0O000OOOO0O0O0O0 ))#line:780
    O00OO0OOOO0OO0O0O =Label (OOOOO000O0O0000OO ,text ="作用对象：")#line:783
    O00OO0OOOO0OO0O0O .grid (row =1 ,column =0 ,sticky ="w")#line:784
    OOOO00OO0O000OO00 =StringVar ()#line:785
    O0000OOOOO00O0O0O =ttk .Combobox (OOOOO000O0O0000OO ,width =25 ,height =10 ,state ="readonly",textvariable =OOOO00OO0O000OO00 )#line:788
    O0000OOOOO00O0O0O ["values"]=list (set (TT_ori ["作用对象"].to_list ()))#line:789
    O0000OOOOO00O0O0O .current (0 )#line:790
    O0000OOOOO00O0O0O .grid (row =1 ,column =1 )#line:791
    OOOO00O00O0OOO000 =Label (OOOOO000O0O0000OO ,text ="分析对象：")#line:793
    OOOO00O00O0OOO000 .grid (row =1 ,column =2 ,sticky ="w")#line:794
    OO0OOOO0O0O0O0OO0 =StringVar ()#line:797
    O000OOOO0OO0O0OO0 =ttk .Combobox (OOOOO000O0O0000OO ,width =15 ,height =10 ,state ="readonly",textvariable =OO0OOOO0O0O0O0OO0 )#line:800
    O000OOOO0OO0O0OO0 ["values"]=["事件发生月份","事件发生季度","产品批号","型号","规格"]#line:801
    O000OOOO0OO0O0OO0 .current (0 )#line:803
    O000OOOO0OO0O0OO0 .grid (row =1 ,column =3 )#line:804
    O0OOO0OOO000O00OO =Label (OOOOO000O0O0000OO ,text ="事件发生起止时间：")#line:809
    O0OOO0OOO000O00OO .grid (row =2 ,column =0 ,sticky ="w")#line:810
    O0OO0OOOO00O00OO0 =Entry (OOOOO000O0O0000OO ,width =10 )#line:812
    O0OO0OOOO00O00OO0 .insert (0 ,min (TT_ori ["事件发生日期"].dt .date ))#line:813
    O0OO0OOOO00O00OO0 .grid (row =2 ,column =1 ,sticky ="w")#line:814
    OO0OO0OO00OOO0OOO =Entry (OOOOO000O0O0000OO ,width =10 )#line:816
    OO0OO0OO00OOO0OOO .insert (0 ,max (TT_ori ["事件发生日期"].dt .date ))#line:817
    OO0OO0OO00OOO0OOO .grid (row =2 ,column =2 ,sticky ="w")#line:818
    O000O0OOO0OOOOOO0 =Button (OOOOO000O0O0000OO ,text ="原始查看",width =10 ,bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :thread_it (Tread_TOOLS_doing ,TT_ori ,O0000OOOOO00O0O0O .get (),O000OOOO0OO0O0OO0 .get (),O0OO0OOOO00O00OO0 .get (),OO0OO0OO00OOO0OOO .get (),1 ))#line:828
    O000O0OOO0OOOOOO0 .grid (row =3 ,column =2 ,sticky ="w")#line:829
    O000O0OOO0OOOOOO0 =Button (OOOOO000O0O0000OO ,text ="分类查看",width =10 ,bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :thread_it (Tread_TOOLS_doing ,TT_ori ,O0000OOOOO00O0O0O .get (),O000OOOO0OO0O0OO0 .get (),O0OO0OOOO00O00OO0 .get (),OO0OO0OO00OOO0OOO .get (),0 ))#line:839
    O000O0OOO0OOOOOO0 .grid (row =3 ,column =3 ,sticky ="w")#line:840
    O000O0OOO0OOOOOO0 =Button (OOOOO000O0O0000OO ,text ="趋势分析",width =10 ,bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :thread_it (Tread_TOOLS_doing ,TT_ori ,O0000OOOOO00O0O0O .get (),O000OOOO0OO0O0OO0 .get (),O0OO0OOOO00O00OO0 .get (),OO0OO0OO00OOO0OOO .get (),2 ))#line:850
    O000O0OOO0OOOOOO0 .grid (row =3 ,column =1 ,sticky ="w")#line:851
def Tread_TOOLS_doing (OOOO00000OOOO0O00 ,O0OOO00OO00OO0O0O ,O000OOO0OO0000O00 ,O0OO00OO0O0OO00O0 ,OO000O00OO000OOOO ,O0O0O0OO0O00OOO0O ):#line:853
    ""#line:854
    global TT_biaozhun #line:855
    OOOO00000OOOO0O00 =OOOO00000OOOO0O00 [(OOOO00000OOOO0O00 ["作用对象"]==O0OOO00OO00OO0O0O )].copy ()#line:856
    O0OO00OO0O0OO00O0 =pd .to_datetime (O0OO00OO0O0OO00O0 )#line:858
    OO000O00OO000OOOO =pd .to_datetime (OO000O00OO000OOOO )#line:859
    OOOO00000OOOO0O00 =OOOO00000OOOO0O00 [((OOOO00000OOOO0O00 ["事件发生日期"]>=O0OO00OO0O0OO00O0 )&(OOOO00000OOOO0O00 ["事件发生日期"]<=OO000O00OO000OOOO ))]#line:860
    text .insert (END ,"\n数据数量："+str (len (OOOO00000OOOO0O00 )))#line:861
    text .see (END )#line:862
    if O0O0O0OO0O00OOO0O ==0 :#line:864
        Tread_TOOLS_check (OOOO00000OOOO0O00 ,TT_biaozhun ["关键字表"],0 )#line:865
        return 0 #line:866
    if O0O0O0OO0O00OOO0O ==1 :#line:867
        Tread_TOOLS_tree_Level_2 (OOOO00000OOOO0O00 ,1 ,OOOO00000OOOO0O00 )#line:868
        return 0 #line:869
    if len (OOOO00000OOOO0O00 )<1 :#line:870
        showinfo (title ="错误信息",message ="没有符合筛选条件的报告。")#line:871
        return 0 #line:872
    Tread_TOOLS_check (OOOO00000OOOO0O00 ,TT_biaozhun ["关键字表"],1 )#line:873
    Tread_TOOLS_tree_Level_2 (Tread_TOOLS_Countall (OOOO00000OOOO0O00 ).df_find_all_keword_risk (O000OOO0OO0000O00 ),1 ,0 ,O000OOO0OO0000O00 )#line:876
def STAT_countx (OOO0OOOO0O0000OOO ):#line:886
    ""#line:887
    return OOO0OOOO0O0000OOO .value_counts ().to_dict ()#line:888
def STAT_countpx (OO0OO000O000OOOOO ,OO0OO000O0OO0O00O ):#line:890
    ""#line:891
    return len (OO0OO000O000OOOOO [(OO0OO000O000OOOOO ==OO0OO000O0OO0O00O )])#line:892
def STAT_countnpx (OOO0OOO00O0OO000O ,O000000O0OO00OO0O ):#line:894
    ""#line:895
    return len (OOO0OOO00O0OO000O [(OOO0OOO00O0OO000O not in O000000O0OO00OO0O )])#line:896
def STAT_get_max (O00000OO0O0OO0000 ):#line:898
    ""#line:899
    return O00000OO0O0OO0000 .value_counts ().max ()#line:900
def STAT_get_mean (OO0O00O0000OOOOOO ):#line:902
    ""#line:903
    return round (OO0O00O0000OOOOOO .value_counts ().mean (),2 )#line:904
def STAT_get_std (O0OOOOOO0O000OOOO ):#line:906
    ""#line:907
    return round (O0OOOOOO0O000OOOO .value_counts ().std (ddof =1 ),2 )#line:908
def STAT_get_95ci (O00OO0O00O0OOO0OO ):#line:910
    ""#line:911
    return round (np .percentile (O00OO0O00O0OOO0OO .value_counts (),97.5 ),2 )#line:912
def STAT_get_mean_std_ci (OO0O00OOO0000OO0O ,O00OO0O000O000O00 ):#line:914
    ""#line:915
    warnings .filterwarnings ("ignore")#line:916
    OO00OOOO0O0O0O00O =TOOLS_strdict_to_pd (str (OO0O00OOO0000OO0O ))["content"].values /O00OO0O000O000O00 #line:917
    O00OOO00O0O0O0OOO =round (OO00OOOO0O0O0O00O .mean (),2 )#line:918
    O0OOO00OO000OOO0O =round (OO00OOOO0O0O0O00O .std (ddof =1 ),2 )#line:919
    OOO0OO00OOOO00OO0 =round (np .percentile (OO00OOOO0O0O0O00O ,97.5 ),2 )#line:920
    return pd .Series ((O00OOO00O0O0O0OOO ,O0OOO00OO000OOO0O ,OOO0OO00OOOO00OO0 ))#line:921
def STAT_findx_value (OOOO00OOO0O0O0OO0 ,O0O0000OOOOO0OOOO ):#line:923
    ""#line:924
    warnings .filterwarnings ("ignore")#line:925
    OO0000O0O0OO00OO0 =TOOLS_strdict_to_pd (str (OOOO00OOO0O0O0OO0 ))#line:926
    OOO00O0OO00OOOOO0 =OO0000O0O0OO00OO0 .where (OO0000O0O0OO00OO0 ["index"]==str (O0O0000OOOOO0OOOO ))#line:928
    print (OOO00O0OO00OOOOO0 )#line:929
    return OOO00O0OO00OOOOO0 #line:930
def STAT_judge_x (O000OOO00OOO0O00O ,O000OOOOOO000O0OO ):#line:932
    ""#line:933
    for O0O000OOO0OOO0OO0 in O000OOOOOO000O0OO :#line:934
        if O000OOO00OOO0O00O .find (O0O000OOO0OOO0OO0 )>-1 :#line:935
            return 1 #line:936
def STAT_basic_risk (OOOO00OO00OO00000 ,OO000O0000000O0O0 ,OOOO000OOO00O0O00 ,O0OOO0OO00OO00000 ,OO0O0O0OOOOOOO000 ):#line:939
    ""#line:940
    OOOO00OO00OO00000 ["风险评分"]=0 #line:941
    OOOO00OO00OO00000 .loc [((OOOO00OO00OO00000 [OO000O0000000O0O0 ]>=3 )&(OOOO00OO00OO00000 [OOOO000OOO00O0O00 ]>=1 ))|(OOOO00OO00OO00000 [OO000O0000000O0O0 ]>=5 ),"风险评分"]=OOOO00OO00OO00000 ["风险评分"]+5 #line:942
    OOOO00OO00OO00000 .loc [(OOOO00OO00OO00000 [OOOO000OOO00O0O00 ]>=3 ),"风险评分"]=OOOO00OO00OO00000 ["风险评分"]+1 #line:943
    OOOO00OO00OO00000 .loc [(OOOO00OO00OO00000 [O0OOO0OO00OO00000 ]>=1 ),"风险评分"]=OOOO00OO00OO00000 ["风险评分"]+10 #line:944
    OOOO00OO00OO00000 ["风险评分"]=OOOO00OO00OO00000 ["风险评分"]+OOOO00OO00OO00000 [OO0O0O0OOOOOOO000 ]/100 #line:945
    return OOOO00OO00OO00000 #line:946
def STAT_find_keyword_risk (OO000000O0O00O0OO ,O0OOO000O000OO000 ,O0000O0O00OO0OOOO ,OO0OO0OO0OOOOOOO0 ,OO0000OOOOOO00000 ):#line:950
        ""#line:951
        O0OO0OOOO0000O000 =OO000000O0O00O0OO .groupby (O0OOO000O000OO000 ).agg (证号关键字总数量 =(O0000O0O00OO0OOOO ,"count"),包含元素个数 =(OO0OO0OO0OOOOOOO0 ,"nunique"),包含元素 =(OO0OO0OO0OOOOOOO0 ,STAT_countx ),).reset_index ()#line:956
        O00OOOOOOOO00OOOO =O0OOO000O000OO000 .copy ()#line:958
        O00OOOOOOOO00OOOO .append (OO0OO0OO0OOOOOOO0 )#line:959
        OO00OOOO000OOOOO0 =OO000000O0O00O0OO .groupby (O00OOOOOOOO00OOOO ).agg (计数 =(OO0OO0OO0OOOOOOO0 ,"count"),).reset_index ()#line:962
        O000O0000OOOOOO0O =O00OOOOOOOO00OOOO .copy ()#line:965
        O000O0000OOOOOO0O .remove ("关键字")#line:966
        OO0O0O0OO00O0OOOO =OO000000O0O00O0OO .groupby (O000O0000OOOOOO0O ).agg (该元素总数 =(OO0OO0OO0OOOOOOO0 ,"count"),).reset_index ()#line:969
        OO00OOOO000OOOOO0 ["证号总数"]=OO0000OOOOOO00000 #line:971
        O0O0OO00O0OOO0O0O =pd .merge (OO00OOOO000OOOOO0 ,O0OO0OOOO0000O000 ,on =O0OOO000O000OO000 ,how ="left")#line:972
        if len (O0O0OO00O0OOO0O0O )>0 :#line:974
            O0O0OO00O0OOO0O0O [['数量均值','数量标准差','数量CI']]=O0O0OO00O0OOO0O0O .包含元素 .apply (lambda OOO0OOO000O0O0O0O :STAT_get_mean_std_ci (OOO0OOO000O0O0O0O ,1 ))#line:975
        return O0O0OO00O0OOO0O0O #line:976
def STAT_find_risk (O0O0O0O000000OOOO ,O00O000O0OO00OO00 ,OO0O0OO000OOOO000 ,OOOOO000O00O00OO0 ):#line:982
        ""#line:983
        O0O0O000000O0O0OO =O0O0O0O000000OOOO .groupby (O00O000O0OO00OO00 ).agg (证号总数量 =(OO0O0OO000OOOO000 ,"count"),包含元素个数 =(OOOOO000O00O00OO0 ,"nunique"),包含元素 =(OOOOO000O00O00OO0 ,STAT_countx ),均值 =(OOOOO000O00O00OO0 ,STAT_get_mean ),标准差 =(OOOOO000O00O00OO0 ,STAT_get_std ),CI上限 =(OOOOO000O00O00OO0 ,STAT_get_95ci ),).reset_index ()#line:991
        O0OOOO000OO0OO0OO =O00O000O0OO00OO00 .copy ()#line:993
        O0OOOO000OO0OO0OO .append (OOOOO000O00O00OO0 )#line:994
        OO0000O0OOOOO000O =O0O0O0O000000OOOO .groupby (O0OOOO000OO0OO0OO ).agg (计数 =(OOOOO000O00O00OO0 ,"count"),严重伤害数 =("伤害",lambda O0OOO00000O000O00 :STAT_countpx (O0OOO00000O000O00 .values ,"严重伤害")),死亡数量 =("伤害",lambda O0OOOOOOO00O00OO0 :STAT_countpx (O0OOOOOOO00O00OO0 .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:1001
        OOO000000O00O0O00 =pd .merge (OO0000O0OOOOO000O ,O0O0O000000O0O0OO ,on =O00O000O0OO00OO00 ,how ="left")#line:1003
        OOO000000O00O0O00 ["风险评分"]=0 #line:1005
        OOO000000O00O0O00 ["报表类型"]="dfx_findrisk"+OOOOO000O00O00OO0 #line:1006
        OOO000000O00O0O00 .loc [((OOO000000O00O0O00 ["计数"]>=3 )&(OOO000000O00O0O00 ["严重伤害数"]>=1 )|(OOO000000O00O0O00 ["计数"]>=5 )),"风险评分"]=OOO000000O00O0O00 ["风险评分"]+5 #line:1007
        OOO000000O00O0O00 .loc [(OOO000000O00O0O00 ["计数"]>=(OOO000000O00O0O00 ["均值"]+OOO000000O00O0O00 ["标准差"])),"风险评分"]=OOO000000O00O0O00 ["风险评分"]+1 #line:1008
        OOO000000O00O0O00 .loc [(OOO000000O00O0O00 ["计数"]>=OOO000000O00O0O00 ["CI上限"]),"风险评分"]=OOO000000O00O0O00 ["风险评分"]+1 #line:1009
        OOO000000O00O0O00 .loc [(OOO000000O00O0O00 ["严重伤害数"]>=3 )&(OOO000000O00O0O00 ["风险评分"]>=7 ),"风险评分"]=OOO000000O00O0O00 ["风险评分"]+1 #line:1010
        OOO000000O00O0O00 .loc [(OOO000000O00O0O00 ["死亡数量"]>=1 ),"风险评分"]=OOO000000O00O0O00 ["风险评分"]+10 #line:1011
        OOO000000O00O0O00 ["风险评分"]=OOO000000O00O0O00 ["风险评分"]+OOO000000O00O0O00 ["单位个数"]/100 #line:1012
        OOO000000O00O0O00 =OOO000000O00O0O00 .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:1013
        return OOO000000O00O0O00 #line:1015
def TOOLS_get_list (O0000O0OO0OO0O000 ):#line:1017
    ""#line:1018
    O0000O0OO0OO0O000 =str (O0000O0OO0OO0O000 )#line:1019
    OO0O000O000000OOO =[]#line:1020
    OO0O000O000000OOO .append (O0000O0OO0OO0O000 )#line:1021
    OO0O000O000000OOO =",".join (OO0O000O000000OOO )#line:1022
    OO0O000O000000OOO =OO0O000O000000OOO .split ("|")#line:1023
    O00OO000000O0O000 =OO0O000O000000OOO [:]#line:1024
    OO0O000O000000OOO =list (set (OO0O000O000000OOO ))#line:1025
    OO0O000O000000OOO .sort (key =O00OO000000O0O000 .index )#line:1026
    return OO0O000O000000OOO #line:1027
def TOOLS_get_list0 (OOO0000000000OOOO ,O00OO0O0O000O0O00 ,*O00OOOOO00OOOOO00 ):#line:1029
    ""#line:1030
    OOO0000000000OOOO =str (OOO0000000000OOOO )#line:1031
    if pd .notnull (OOO0000000000OOOO ):#line:1033
        try :#line:1034
            if "use("in str (OOO0000000000OOOO ):#line:1035
                OOO0O00O00O0OO0OO =OOO0000000000OOOO #line:1036
                O000O00OOOOOO0OO0 =re .compile (r"[(](.*?)[)]",re .S )#line:1037
                OO00000O0OO000OOO =re .findall (O000O00OOOOOO0OO0 ,OOO0O00O00O0OO0OO )#line:1038
                OO0OOO0OOO0O00O00 =[]#line:1039
                if ").list"in OOO0000000000OOOO :#line:1040
                    OO000OOO00OOO0OOO ="配置表/"+str (OO00000O0OO000OOO [0 ])+".xls"#line:1041
                    O0OO0O000O0OOOOO0 =pd .read_excel (OO000OOO00OOO0OOO ,sheet_name =OO00000O0OO000OOO [0 ],header =0 ,index_col =0 ).reset_index ()#line:1044
                    O0OO0O000O0OOOOO0 ["检索关键字"]=O0OO0O000O0OOOOO0 ["检索关键字"].astype (str )#line:1045
                    OO0OOO0OOO0O00O00 =O0OO0O000O0OOOOO0 ["检索关键字"].tolist ()+OO0OOO0OOO0O00O00 #line:1046
                if ").file"in OOO0000000000OOOO :#line:1047
                    OO0OOO0OOO0O00O00 =O00OO0O0O000O0O00 [OO00000O0OO000OOO [0 ]].astype (str ).tolist ()+OO0OOO0OOO0O00O00 #line:1049
                try :#line:1052
                    if "报告类型-新的"in O00OO0O0O000O0O00 .columns :#line:1053
                        OO0OOO0OOO0O00O00 =",".join (OO0OOO0OOO0O00O00 )#line:1054
                        OO0OOO0OOO0O00O00 =OO0OOO0OOO0O00O00 .split (";")#line:1055
                        OO0OOO0OOO0O00O00 =",".join (OO0OOO0OOO0O00O00 )#line:1056
                        OO0OOO0OOO0O00O00 =OO0OOO0OOO0O00O00 .split ("；")#line:1057
                        OO0OOO0OOO0O00O00 =[OOO0OO000O0OO000O .replace ("（严重）","")for OOO0OO000O0OO000O in OO0OOO0OOO0O00O00 ]#line:1058
                        OO0OOO0OOO0O00O00 =[O0OOOOO0000OO0O0O .replace ("（一般）","")for O0OOOOO0000OO0O0O in OO0OOO0OOO0O00O00 ]#line:1059
                except :#line:1060
                    pass #line:1061
                OO0OOO0OOO0O00O00 =",".join (OO0OOO0OOO0O00O00 )#line:1064
                OO0OOO0OOO0O00O00 =OO0OOO0OOO0O00O00 .split ("、")#line:1065
                OO0OOO0OOO0O00O00 =",".join (OO0OOO0OOO0O00O00 )#line:1066
                OO0OOO0OOO0O00O00 =OO0OOO0OOO0O00O00 .split ("，")#line:1067
                OO0OOO0OOO0O00O00 =",".join (OO0OOO0OOO0O00O00 )#line:1068
                OO0OOO0OOO0O00O00 =OO0OOO0OOO0O00O00 .split (",")#line:1069
                O0O0O0000OOO00OOO =OO0OOO0OOO0O00O00 [:]#line:1071
                try :#line:1072
                    if O00OOOOO00OOOOO00 [0 ]==1000 :#line:1073
                      pass #line:1074
                except :#line:1075
                      OO0OOO0OOO0O00O00 =list (set (OO0OOO0OOO0O00O00 ))#line:1076
                OO0OOO0OOO0O00O00 .sort (key =O0O0O0000OOO00OOO .index )#line:1077
            else :#line:1079
                OOO0000000000OOOO =str (OOO0000000000OOOO )#line:1080
                OO0OOO0OOO0O00O00 =[]#line:1081
                OO0OOO0OOO0O00O00 .append (OOO0000000000OOOO )#line:1082
                OO0OOO0OOO0O00O00 =",".join (OO0OOO0OOO0O00O00 )#line:1083
                OO0OOO0OOO0O00O00 =OO0OOO0OOO0O00O00 .split ("、")#line:1084
                OO0OOO0OOO0O00O00 =",".join (OO0OOO0OOO0O00O00 )#line:1085
                OO0OOO0OOO0O00O00 =OO0OOO0OOO0O00O00 .split ("，")#line:1086
                OO0OOO0OOO0O00O00 =",".join (OO0OOO0OOO0O00O00 )#line:1087
                OO0OOO0OOO0O00O00 =OO0OOO0OOO0O00O00 .split (",")#line:1088
                O0O0O0000OOO00OOO =OO0OOO0OOO0O00O00 [:]#line:1090
                try :#line:1091
                    if O00OOOOO00OOOOO00 [0 ]==1000 :#line:1092
                      OO0OOO0OOO0O00O00 =list (set (OO0OOO0OOO0O00O00 ))#line:1093
                except :#line:1094
                      pass #line:1095
                OO0OOO0OOO0O00O00 .sort (key =O0O0O0000OOO00OOO .index )#line:1096
                OO0OOO0OOO0O00O00 .sort (key =O0O0O0000OOO00OOO .index )#line:1097
        except ValueError2 :#line:1099
            showinfo (title ="提示信息",message ="创建单元格支持多个甚至表单（文件）传入的方法，返回一个经过整理的清单出错，任务终止。")#line:1100
            return False #line:1101
    return OO0OOO0OOO0O00O00 #line:1103
def TOOLS_strdict_to_pd (O0OO00O0000OO00OO ):#line:1104
    ""#line:1105
    return pd .DataFrame .from_dict (eval (O0OO00O0000OO00OO ),orient ="index",columns =["content"]).reset_index ()#line:1106
def Tread_TOOLS_view_dict (O0O000OOO00O0OO0O ,OOO00O0O0O00O0OO0 ):#line:1108
    ""#line:1109
    OOO0OO0O0OOO000OO =Toplevel ()#line:1110
    OOO0OO0O0OOO000OO .title ("查看数据")#line:1111
    OOO0OO0O0OOO000OO .geometry ("700x500")#line:1112
    OO0000OO00O0O00O0 =Scrollbar (OOO0OO0O0OOO000OO )#line:1114
    O00O0OOOO0O0O0OO0 =Text (OOO0OO0O0OOO000OO ,height =100 ,width =150 )#line:1115
    OO0000OO00O0O00O0 .pack (side =RIGHT ,fill =Y )#line:1116
    O00O0OOOO0O0O0OO0 .pack ()#line:1117
    OO0000OO00O0O00O0 .config (command =O00O0OOOO0O0O0OO0 .yview )#line:1118
    O00O0OOOO0O0O0OO0 .config (yscrollcommand =OO0000OO00O0O00O0 .set )#line:1119
    if OOO00O0O0O00O0OO0 ==1 :#line:1120
        O00O0OOOO0O0O0OO0 .insert (END ,O0O000OOO00O0OO0O )#line:1122
        O00O0OOOO0O0O0OO0 .insert (END ,"\n\n")#line:1123
        return 0 #line:1124
    for O00O00OOOOO000000 in range (len (O0O000OOO00O0OO0O )):#line:1125
        O00O0OOOO0O0O0OO0 .insert (END ,O0O000OOO00O0OO0O .iloc [O00O00OOOOO000000 ,0 ])#line:1126
        O00O0OOOO0O0O0OO0 .insert (END ,":")#line:1127
        O00O0OOOO0O0O0OO0 .insert (END ,O0O000OOO00O0OO0O .iloc [O00O00OOOOO000000 ,1 ])#line:1128
        O00O0OOOO0O0O0OO0 .insert (END ,"\n\n")#line:1129
def Tread_TOOLS_fashenglv (O00000OOO0000OO0O ,OOOOOOOO00OOO0OOO ):#line:1132
    global TT_biaozhun #line:1133
    O00000OOO0000OO0O =pd .merge (O00000OOO0000OO0O ,TT_biaozhun [OOOOOOOO00OOO0OOO ],on =[OOOOOOOO00OOO0OOO ],how ="left").reset_index (drop =True )#line:1134
    OO0O0OO0O00O0000O =O00000OOO0000OO0O ["使用次数"].mean ()#line:1136
    O00000OOO0000OO0O ["使用次数"]=O00000OOO0000OO0O ["使用次数"].fillna (int (OO0O0OO0O00O0000O ))#line:1137
    OO00OO0O00OO0O0O0 =O00000OOO0000OO0O ["使用次数"][:-1 ].sum ()#line:1138
    O00000OOO0000OO0O .iloc [-1 ,-1 ]=OO00OO0O00OO0O0O0 #line:1139
    O0O0000OOOOO0OO00 =[O0000000OOOOO00OO for O0000000OOOOO00OO in O00000OOO0000OO0O .columns if (O0000000OOOOO00OO not in ["使用次数",OOOOOOOO00OOO0OOO ])]#line:1140
    for O000O0O0O0O0OOO0O ,O000000000O0OOOO0 in O00000OOO0000OO0O .iterrows ():#line:1141
        for O0O0O00OO0OO00O00 in O0O0000OOOOO0OO00 :#line:1142
            O00000OOO0000OO0O .loc [O000O0O0O0O0OOO0O ,O0O0O00OO0OO00O00 ]=int (O000000000O0OOOO0 [O0O0O00OO0OO00O00 ])/int (O000000000O0OOOO0 ["使用次数"])#line:1143
    del O00000OOO0000OO0O ["使用次数"]#line:1144
    Tread_TOOLS_tree_Level_2 (O00000OOO0000OO0O ,1 ,1 ,OOOOOOOO00OOO0OOO )#line:1145
def TOOLS_save_dict (OO00O0O0O00000O00 ):#line:1147
    ""#line:1148
    O0OO0OOO0OOO0OO00 =filedialog .asksaveasfilename (title =u"保存文件",initialfile ="【排序后的原始数据】.xls",defaultextension ="xls",filetypes =[("Excel 97-2003 工作簿","*.xls")],)#line:1154
    try :#line:1155
        OO00O0O0O00000O00 ["详细描述T"]=OO00O0O0O00000O00 ["详细描述T"].astype (str )#line:1156
    except :#line:1157
        pass #line:1158
    try :#line:1159
        OO00O0O0O00000O00 ["报告编码"]=OO00O0O0O00000O00 ["报告编码"].astype (str )#line:1160
    except :#line:1161
        pass #line:1162
    try :#line:1163
        OO00O0O0OO0O00OO0 =re .search ("\【(.*?)\】",O0OO0OOO0OOO0OO00 )#line:1164
        OO00O0O0O00000O00 ["对象"]=OO00O0O0OO0O00OO0 .group (1 )#line:1165
    except :#line:1166
        pass #line:1167
    O00OO000000O0OOOO =pd .ExcelWriter (O0OO0OOO0OOO0OO00 ,engine ="xlsxwriter")#line:1168
    OO00O0O0O00000O00 .to_excel (O00OO000000O0OOOO ,sheet_name ="字典数据")#line:1169
    O00OO000000O0OOOO .close ()#line:1170
    showinfo (title ="提示",message ="文件写入成功。")#line:1171
def Tread_TOOLS_DRAW_histbar (O00O000OO0O000O00 ):#line:1175
    ""#line:1176
    OO0O0OO00OO00000O =Toplevel ()#line:1179
    OO0O0OO00OO00000O .title ("直方图")#line:1180
    OO00OO000O00O00O0 =ttk .Frame (OO0O0OO00OO00000O ,height =20 )#line:1181
    OO00OO000O00O00O0 .pack (side =TOP )#line:1182
    O00O00000OOO0000O =Figure (figsize =(12 ,6 ),dpi =100 )#line:1184
    OO0OO0OOO0O0OOOOO =FigureCanvasTkAgg (O00O00000OOO0000O ,master =OO0O0OO00OO00000O )#line:1185
    OO0OO0OOO0O0OOOOO .draw ()#line:1186
    OO0OO0OOO0O0OOOOO .get_tk_widget ().pack (expand =1 )#line:1187
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1189
    plt .rcParams ['axes.unicode_minus']=False #line:1190
    OOOOO0O0O00OOOOOO =NavigationToolbar2Tk (OO0OO0OOO0O0OOOOO ,OO0O0OO00OO00000O )#line:1192
    OOOOO0O0O00OOOOOO .update ()#line:1193
    OO0OO0OOO0O0OOOOO .get_tk_widget ().pack ()#line:1194
    OO00O0OOOO00O0OOO =O00O00000OOO0000O .add_subplot (111 )#line:1196
    OO00O0OOOO00O0OOO .set_title ("直方图")#line:1198
    O0O0OOO0O00OOOOO0 =O00O000OO0O000O00 .columns .to_list ()#line:1200
    O0O0OOO0O00OOOOO0 .remove ("对象")#line:1201
    OOOOOOO0OO0OO00OO =np .arange (len (O0O0OOO0O00OOOOO0 ))#line:1202
    for O00O000O0000O0OO0 in O0O0OOO0O00OOOOO0 :#line:1206
        O00O000OO0O000O00 [O00O000O0000O0OO0 ]=O00O000OO0O000O00 [O00O000O0000O0OO0 ].astype (float )#line:1207
    O00O000OO0O000O00 ['数据']=O00O000OO0O000O00 [O0O0OOO0O00OOOOO0 ].values .tolist ()#line:1209
    OOO00O0O00O00OOO0 =0 #line:1210
    for O0000OO0OO0000O0O ,OO00OOO0O000O00O0 in O00O000OO0O000O00 .iterrows ():#line:1211
        OO00O0OOOO00O0OOO .bar ([O0000OOO0OOOO0O0O +OOO00O0O00O00OOO0 for O0000OOO0OOOO0O0O in OOOOOOO0OO0OO00OO ],O00O000OO0O000O00 .loc [O0000OO0OO0000O0O ,'数据'],label =O0O0OOO0O00OOOOO0 ,width =0.1 )#line:1212
        for OO0000O0OOO00O000 ,OOO0O0OOO000OOO0O in zip ([O00O00000O000OO00 +OOO00O0O00O00OOO0 for O00O00000O000OO00 in OOOOOOO0OO0OO00OO ],O00O000OO0O000O00 .loc [O0000OO0OO0000O0O ,'数据']):#line:1215
           OO00O0OOOO00O0OOO .text (OO0000O0OOO00O000 -0.015 ,OOO0O0OOO000OOO0O +0.07 ,str (int (OOO0O0OOO000OOO0O )),color ='black',size =8 )#line:1216
        OOO00O0O00O00OOO0 =OOO00O0O00O00OOO0 +0.1 #line:1218
    OO00O0OOOO00O0OOO .set_xticklabels (O00O000OO0O000O00 .columns .to_list (),rotation =-90 ,fontsize =8 )#line:1220
    OO00O0OOOO00O0OOO .legend (O00O000OO0O000O00 ["对象"])#line:1224
    OO0OO0OOO0O0OOOOO .draw ()#line:1227
def Tread_TOOLS_DRAW_make_risk_plot (O00000OOO0OOOO00O ,O00O0OOO000O00000 ,O000O0O0OOO000O0O ,OO0000OOO000000OO ,OOOO000O00O0OOO0O ):#line:1229
    ""#line:1230
    OOO0O00O0OOO0O0OO =Toplevel ()#line:1233
    OOO0O00O0OOO0O0OO .title (OO0000OOO000000OO )#line:1234
    OOOO0OOOOO0OO00O0 =ttk .Frame (OOO0O00O0OOO0O0OO ,height =20 )#line:1235
    OOOO0OOOOO0OO00O0 .pack (side =TOP )#line:1236
    OOOOOO000O0O00OOO =Figure (figsize =(12 ,6 ),dpi =100 )#line:1238
    OOO0O000O0OO0O00O =FigureCanvasTkAgg (OOOOOO000O0O00OOO ,master =OOO0O00O0OOO0O0OO )#line:1239
    OOO0O000O0OO0O00O .draw ()#line:1240
    OOO0O000O0OO0O00O .get_tk_widget ().pack (expand =1 )#line:1241
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1243
    plt .rcParams ['axes.unicode_minus']=False #line:1244
    O0O0OOO0O00OOO0OO =NavigationToolbar2Tk (OOO0O000O0OO0O00O ,OOO0O00O0OOO0O0OO )#line:1246
    O0O0OOO0O00OOO0OO .update ()#line:1247
    OOO0O000O0OO0O00O .get_tk_widget ().pack ()#line:1248
    O0OO000OOOOOOO0O0 =OOOOOO000O0O00OOO .add_subplot (111 )#line:1250
    O0OO000OOOOOOO0O0 .set_title (OO0000OOO000000OO )#line:1252
    OO0OO0OOOO00O0000 =O00000OOO0OOOO00O [O00O0OOO000O00000 ]#line:1253
    if OOOO000O00O0OOO0O !=999 :#line:1256
        O0OO000OOOOOOO0O0 .set_xticklabels (OO0OO0OOOO00O0000 ,rotation =-90 ,fontsize =8 )#line:1257
    OOO00O0OOO000O000 =range (0 ,len (OO0OO0OOOO00O0000 ),1 )#line:1260
    for O0O0000OO0OO00OO0 in O000O0O0OOO000O0O :#line:1265
        O00O00O0O0O0O00O0 =O00000OOO0OOOO00O [O0O0000OO0OO00OO0 ].astype (float )#line:1266
        if O0O0000OO0OO00OO0 =="关注区域":#line:1268
            O0OO000OOOOOOO0O0 .plot (list (OO0OO0OOOO00O0000 ),list (O00O00O0O0O0O00O0 ),label =str (O0O0000OO0OO00OO0 ),color ="red")#line:1269
        else :#line:1270
            O0OO000OOOOOOO0O0 .plot (list (OO0OO0OOOO00O0000 ),list (O00O00O0O0O0O00O0 ),label =str (O0O0000OO0OO00OO0 ))#line:1271
        if OOOO000O00O0OOO0O ==100 :#line:1274
            for O0000000OO0OOO0O0 ,O0OO0000000O00O00 in zip (OO0OO0OOOO00O0000 ,O00O00O0O0O0O00O0 ):#line:1275
                if O0OO0000000O00O00 ==max (O00O00O0O0O0O00O0 )and O0OO0000000O00O00 >=3 and len (O000O0O0OOO000O0O )!=1 :#line:1276
                     O0OO000OOOOOOO0O0 .text (O0000000OO0OOO0O0 ,O0OO0000000O00O00 ,(str (O0O0000OO0OO00OO0 )+":"+str (int (O0OO0000000O00O00 ))),color ='black',size =8 )#line:1277
                if len (O000O0O0OOO000O0O )==1 and O0OO0000000O00O00 >=0.01 :#line:1278
                     O0OO000OOOOOOO0O0 .text (O0000000OO0OOO0O0 ,O0OO0000000O00O00 ,str (int (O0OO0000000O00O00 )),color ='black',size =8 )#line:1279
    if len (O000O0O0OOO000O0O )==1 :#line:1289
        OOO000O0O000OO000 =O00000OOO0OOOO00O [O000O0O0OOO000O0O ].astype (float ).values #line:1290
        OO00000OOO0OO0OO0 =OOO000O0O000OO000 .mean ()#line:1291
        OO000OOO00O0O0OO0 =OOO000O0O000OO000 .std ()#line:1292
        OO0O0OO000OO000O0 =OO00000OOO0OO0OO0 +3 *OO000OOO00O0O0OO0 #line:1293
        O00OOO000OO0O00OO =OO000OOO00O0O0OO0 -3 *OO000OOO00O0O0OO0 #line:1294
        O0OO000OOOOOOO0O0 .axhline (OO00000OOO0OO0OO0 ,color ='r',linestyle ='--',label ='Mean')#line:1296
        O0OO000OOOOOOO0O0 .axhline (OO0O0OO000OO000O0 ,color ='g',linestyle ='--',label ='UCL(μ+3σ)')#line:1297
        O0OO000OOOOOOO0O0 .axhline (O00OOO000OO0O00OO ,color ='g',linestyle ='--',label ='LCL(μ-3σ)')#line:1298
    O0OO000OOOOOOO0O0 .set_title ("控制图")#line:1300
    O0OO000OOOOOOO0O0 .set_xlabel ("项")#line:1301
    OOOOOO000O0O00OOO .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:1302
    OO0OO00O0O0OOO0O0 =O0OO000OOOOOOO0O0 .get_position ()#line:1303
    O0OO000OOOOOOO0O0 .set_position ([OO0OO00O0O0OOO0O0 .x0 ,OO0OO00O0O0OOO0O0 .y0 ,OO0OO00O0O0OOO0O0 .width *0.7 ,OO0OO00O0O0OOO0O0 .height ])#line:1304
    O0OO000OOOOOOO0O0 .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:1305
    O0000O0O0OOO00O0O =StringVar ()#line:1308
    O0O00OO0O0OO0OOOO =ttk .Combobox (OOOO0OOOOO0OO00O0 ,width =15 ,textvariable =O0000O0O0OOO00O0O ,state ='readonly')#line:1309
    O0O00OO0O0OO0OOOO ['values']=O000O0O0OOO000O0O #line:1310
    O0O00OO0O0OO0OOOO .pack (side =LEFT )#line:1311
    O0O00OO0O0OO0OOOO .current (0 )#line:1312
    OOO000OOO0O00OOO0 =Button (OOOO0OOOOO0OO00O0 ,text ="控制图（单项）",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (O00000OOO0OOOO00O ,O00O0OOO000O00000 ,[OO0OOO0O0OOOOOOO0 for OO0OOO0O0OOOOOOO0 in O000O0O0OOO000O0O if O0000O0O0OOO00O0O .get ()in OO0OOO0O0OOOOOOO0 ],OO0000OOO000000OO ,OOOO000O00O0OOO0O ))#line:1322
    OOO000OOO0O00OOO0 .pack (side =LEFT ,anchor ="ne")#line:1323
    O00O0OOO0OO00OO00 =Button (OOOO0OOOOO0OO00O0 ,text ="去除标记",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (O00000OOO0OOOO00O ,O00O0OOO000O00000 ,O000O0O0OOO000O0O ,OO0000OOO000000OO ,0 ))#line:1331
    O00O0OOO0OO00OO00 .pack (side =LEFT ,anchor ="ne")#line:1333
    OOO0O000O0OO0O00O .draw ()#line:1334
def Tread_TOOLS_draw (OOO0O00000OO0O0OO ,O0O0OO0O0000OOO0O ,OO00OOOO00O0OOO0O ,OO000000O0O0O0OOO ,O0O0OOOOO0OO0O000 ):#line:1336
    ""#line:1337
    warnings .filterwarnings ("ignore")#line:1338
    OO00OOO00O0O0OOOO =Toplevel ()#line:1339
    OO00OOO00O0O0OOOO .title (O0O0OO0O0000OOO0O )#line:1340
    O00OO0OO00OO0OOO0 =ttk .Frame (OO00OOO00O0O0OOOO ,height =20 )#line:1341
    O00OO0OO00OO0OOO0 .pack (side =TOP )#line:1342
    OOOO000OOOOO0O0O0 =Figure (figsize =(12 ,6 ),dpi =100 )#line:1344
    OO000O0O0OOOO000O =FigureCanvasTkAgg (OOOO000OOOOO0O0O0 ,master =OO00OOO00O0O0OOOO )#line:1345
    OO000O0O0OOOO000O .draw ()#line:1346
    OO000O0O0OOOO000O .get_tk_widget ().pack (expand =1 )#line:1347
    O000O0O0OOO0OOOOO =OOOO000OOOOO0O0O0 .add_subplot (111 )#line:1348
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1350
    plt .rcParams ['axes.unicode_minus']=False #line:1351
    OOO00OO00000OO0O0 =NavigationToolbar2Tk (OO000O0O0OOOO000O ,OO00OOO00O0O0OOOO )#line:1353
    OOO00OO00000OO0O0 .update ()#line:1354
    OO000O0O0OOOO000O .get_tk_widget ().pack ()#line:1356
    try :#line:1359
        OOO0OOOOOOO00O0O0 =OOO0O00000OO0O0OO .columns #line:1360
        OOO0O00000OO0O0OO =OOO0O00000OO0O0OO .sort_values (by =OO000000O0O0O0OOO ,ascending =[False ],na_position ="last")#line:1361
    except :#line:1362
        OOO00OOOOOOO0O00O =eval (OOO0O00000OO0O0OO )#line:1363
        OOO00OOOOOOO0O00O =pd .DataFrame .from_dict (OOO00OOOOOOO0O00O ,TT_orient =OO00OOOO00O0OOO0O ,columns =[OO000000O0O0O0OOO ]).reset_index ()#line:1366
        OOO0O00000OO0O0OO =OOO00OOOOOOO0O00O .sort_values (by =OO000000O0O0O0OOO ,ascending =[False ],na_position ="last")#line:1367
    if ("日期"in O0O0OO0O0000OOO0O or "时间"in O0O0OO0O0000OOO0O or "季度"in O0O0OO0O0000OOO0O )and "饼图"not in O0O0OOOOO0OO0O000 :#line:1371
        OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ]=pd .to_datetime (OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ],format ="%Y/%m/%d").dt .date #line:1372
        OOO0O00000OO0O0OO =OOO0O00000OO0O0OO .sort_values (by =OO00OOOO00O0OOO0O ,ascending =[True ],na_position ="last")#line:1373
    elif "批号"in O0O0OO0O0000OOO0O :#line:1374
        OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ]=OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ].astype (str )#line:1375
        OOO0O00000OO0O0OO =OOO0O00000OO0O0OO .sort_values (by =OO00OOOO00O0OOO0O ,ascending =[True ],na_position ="last")#line:1376
        O000O0O0OOO0OOOOO .set_xticklabels (OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ],rotation =-90 ,fontsize =8 )#line:1377
    else :#line:1378
        OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ]=OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ].astype (str )#line:1379
        O000O0O0OOO0OOOOO .set_xticklabels (OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ],rotation =-90 ,fontsize =8 )#line:1380
    OO000000O0000OO00 =OOO0O00000OO0O0OO [OO000000O0O0O0OOO ]#line:1382
    OOOO000O00OO0O0O0 =range (0 ,len (OO000000O0000OO00 ),1 )#line:1383
    O000O0O0OOO0OOOOO .set_title (O0O0OO0O0000OOO0O )#line:1385
    if O0O0OOOOO0OO0O000 =="柱状图":#line:1389
        O000O0O0OOO0OOOOO .bar (x =OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ],height =OO000000O0000OO00 ,width =0.2 ,color ="#87CEFA")#line:1390
    elif O0O0OOOOO0OO0O000 =="饼图":#line:1391
        O000O0O0OOO0OOOOO .pie (x =OO000000O0000OO00 ,labels =OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ],autopct ="%0.2f%%")#line:1392
    elif O0O0OOOOO0OO0O000 =="折线图":#line:1393
        O000O0O0OOO0OOOOO .plot (OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ],OO000000O0000OO00 ,lw =0.5 ,ls ='-',c ="r",alpha =0.5 )#line:1394
    elif "帕累托图"in str (O0O0OOOOO0OO0O000 ):#line:1396
        OOO000O0O00000O0O =OOO0O00000OO0O0OO [OO000000O0O0O0OOO ].fillna (0 )#line:1397
        OOOOO00O000OO0OO0 =OOO000O0O00000O0O .cumsum ()/OOO000O0O00000O0O .sum ()*100 #line:1401
        OOO0O00000OO0O0OO ["百分比"]=round (OOO0O00000OO0O0OO ["数量"]/OOO000O0O00000O0O .sum ()*100 ,2 )#line:1402
        OOO0O00000OO0O0OO ["累计百分比"]=round (OOOOO00O000OO0OO0 ,2 )#line:1403
        O00000O0OOO00O000 =OOOOO00O000OO0OO0 [OOOOO00O000OO0OO0 >0.8 ].index [0 ]#line:1404
        OO0O0OOOOOO0000O0 =OOO000O0O00000O0O .index .tolist ().index (O00000O0OOO00O000 )#line:1405
        O000O0O0OOO0OOOOO .bar (x =OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ],height =OOO000O0O00000O0O ,color ="C0",label =OO000000O0O0O0OOO )#line:1409
        OOO0000OO0O00OOOO =O000O0O0OOO0OOOOO .twinx ()#line:1410
        OOO0000OO0O00OOOO .plot (OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ],OOOOO00O000OO0OO0 ,color ="C1",alpha =0.6 ,label ="累计比例")#line:1411
        OOO0000OO0O00OOOO .yaxis .set_major_formatter (PercentFormatter ())#line:1412
        O000O0O0OOO0OOOOO .tick_params (axis ="y",colors ="C0")#line:1417
        OOO0000OO0O00OOOO .tick_params (axis ="y",colors ="C1")#line:1418
        for O0O0O000O00OOOOO0 ,O00O00000O0O0OOO0 ,O0OOOO00OO00OO000 ,O0O00OO0O000O00O0 in zip (OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ],OOO000O0O00000O0O ,OOO0O00000OO0O0OO ["百分比"],OOO0O00000OO0O0OO ["累计百分比"]):#line:1420
            O000O0O0OOO0OOOOO .text (O0O0O000O00OOOOO0 ,O00O00000O0O0OOO0 +0.1 ,str (int (O00O00000O0O0OOO0 ))+", "+str (int (O0OOOO00OO00OO000 ))+"%,"+str (int (O0O00OO0O000O00O0 ))+"%",color ='black',size =8 )#line:1421
        if "超级帕累托图"in str (O0O0OOOOO0OO0O000 ):#line:1424
            O0OOOO0000O00O000 =re .compile (r'[(](.*?)[)]',re .S )#line:1425
            O00O0OOO0O00OOO0O =re .findall (O0OOOO0000O00O000 ,O0O0OOOOO0OO0O000 )[0 ]#line:1426
            O000O0O0OOO0OOOOO .bar (x =OOO0O00000OO0O0OO [OO00OOOO00O0OOO0O ],height =OOO0O00000OO0O0OO [O00O0OOO0O00OOO0O ],color ="orangered",label =O00O0OOO0O00OOO0O )#line:1427
    OOOO000OOOOO0O0O0 .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:1432
    OO0O00O0OO00O0000 =O000O0O0OOO0OOOOO .get_position ()#line:1433
    O000O0O0OOO0OOOOO .set_position ([OO0O00O0OO00O0000 .x0 ,OO0O00O0OO00O0000 .y0 ,OO0O00O0OO00O0000 .width *0.7 ,OO0O00O0OO00O0000 .height ])#line:1434
    O000O0O0OOO0OOOOO .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:1435
    OO000O0O0OOOO000O .draw ()#line:1438
    if len (OO000000O0000OO00 )<=20 and O0O0OOOOO0OO0O000 !="饼图"and O0O0OOOOO0OO0O000 !="帕累托图":#line:1441
        for O0O00O00O0OOO0OOO ,O00O000O00OOO0OOO in zip (OOOO000O00OO0O0O0 ,OO000000O0000OO00 ):#line:1442
            OO0O0OO0OO00OO000 =str (O00O000O00OOO0OOO )#line:1443
            O00O0OOOO0O00O0O0 =(O0O00O00O0OOO0OOO ,O00O000O00OOO0OOO +0.3 )#line:1444
            O000O0O0OOO0OOOOO .annotate (OO0O0OO0OO00OO000 ,xy =O00O0OOOO0O00O0O0 ,fontsize =8 ,color ="black",ha ="center",va ="baseline")#line:1445
    OO000O0OO00000OOO =Button (O00OO0OO00OO0OOO0 ,relief =GROOVE ,activebackground ="green",text ="保存原始数据",command =lambda :TOOLS_save_dict (OOO0O00000OO0O0OO ),)#line:1455
    OO000O0OO00000OOO .pack (side =RIGHT )#line:1456
    OO00OO0000O000000 =Button (O00OO0OO00OO0OOO0 ,relief =GROOVE ,text ="查看原始数据",command =lambda :Tread_TOOLS_view_dict (OOO0O00000OO0O0OO ,1 ))#line:1460
    OO00OO0000O000000 .pack (side =RIGHT )#line:1461
    OO00O0O00O0OO000O =Button (O00OO0OO00OO0OOO0 ,relief =GROOVE ,text ="饼图",command =lambda :Tread_TOOLS_draw (OOO0O00000OO0O0OO ,O0O0OO0O0000OOO0O ,OO00OOOO00O0OOO0O ,OO000000O0O0O0OOO ,"饼图"),)#line:1469
    OO00O0O00O0OO000O .pack (side =LEFT )#line:1470
    OO00O0O00O0OO000O =Button (O00OO0OO00OO0OOO0 ,relief =GROOVE ,text ="柱状图",command =lambda :Tread_TOOLS_draw (OOO0O00000OO0O0OO ,O0O0OO0O0000OOO0O ,OO00OOOO00O0OOO0O ,OO000000O0O0O0OOO ,"柱状图"),)#line:1477
    OO00O0O00O0OO000O .pack (side =LEFT )#line:1478
    OO00O0O00O0OO000O =Button (O00OO0OO00OO0OOO0 ,relief =GROOVE ,text ="折线图",command =lambda :Tread_TOOLS_draw (OOO0O00000OO0O0OO ,O0O0OO0O0000OOO0O ,OO00OOOO00O0OOO0O ,OO000000O0O0O0OOO ,"折线图"),)#line:1484
    OO00O0O00O0OO000O .pack (side =LEFT )#line:1485
    OO00O0O00O0OO000O =Button (O00OO0OO00OO0OOO0 ,relief =GROOVE ,text ="帕累托图",command =lambda :Tread_TOOLS_draw (OOO0O00000OO0O0OO ,O0O0OO0O0000OOO0O ,OO00OOOO00O0OOO0O ,OO000000O0O0O0OOO ,"帕累托图"),)#line:1492
    OO00O0O00O0OO000O .pack (side =LEFT )#line:1493
def helper ():#line:1499
    ""#line:1500
    OO00OO0OOOO0O00O0 =Toplevel ()#line:1501
    OO00OO0OOOO0O00O0 .title ("程序使用帮助")#line:1502
    OO00OO0OOOO0O00O0 .geometry ("700x500")#line:1503
    O000OO000O00OOOOO =Scrollbar (OO00OO0OOOO0O00O0 )#line:1505
    OOO0O0O00O000OO00 =Text (OO00OO0OOOO0O00O0 ,height =80 ,width =150 ,bg ="#FFFFFF",font ="微软雅黑")#line:1506
    O000OO000O00OOOOO .pack (side =RIGHT ,fill =Y )#line:1507
    OOO0O0O00O000OO00 .pack ()#line:1508
    O000OO000O00OOOOO .config (command =OOO0O0O00O000OO00 .yview )#line:1509
    OOO0O0O00O000OO00 .config (yscrollcommand =O000OO000O00OOOOO .set )#line:1510
    OOO0O0O00O000OO00 .insert (END ,"\n  本程序用于趋势分析,供广东省内参与医疗器械警戒试点的企业免费使用。如您有相关问题或改进建议，请联系以下人员：\n\n    佛山市药品不良反应监测中心\n    蔡权周 \n    微信：18575757461 \n    邮箱：411703730@qq.com")#line:1515
    OOO0O0O00O000OO00 .config (state =DISABLED )#line:1516
def Tread_TOOLS_CLEAN (OOOO0O00OO00O00OO ):#line:1520
        ""#line:1521
        OOOO0O00OO00O00OO ["报告编码"]=OOOO0O00OO00O00OO ["报告编码"].astype ("str")#line:1523
        OOOO0O00OO00O00OO ["产品批号"]=OOOO0O00OO00O00OO ["产品批号"].astype ("str")#line:1525
        OOOO0O00OO00O00OO ["型号"]=OOOO0O00OO00O00OO ["型号"].astype ("str")#line:1526
        OOOO0O00OO00O00OO ["规格"]=OOOO0O00OO00O00OO ["规格"].astype ("str")#line:1527
        OOOO0O00OO00O00OO ["注册证编号/曾用注册证编号"]=OOOO0O00OO00O00OO ["注册证编号/曾用注册证编号"].str .replace ("(","（",regex =False )#line:1529
        OOOO0O00OO00O00OO ["注册证编号/曾用注册证编号"]=OOOO0O00OO00O00OO ["注册证编号/曾用注册证编号"].str .replace (")","）",regex =False )#line:1530
        OOOO0O00OO00O00OO ["注册证编号/曾用注册证编号"]=OOOO0O00OO00O00OO ["注册证编号/曾用注册证编号"].str .replace ("*","※",regex =False )#line:1531
        OOOO0O00OO00O00OO ["产品名称"]=OOOO0O00OO00O00OO ["产品名称"].str .replace ("*","※",regex =False )#line:1533
        OOOO0O00OO00O00OO ["产品批号"]=OOOO0O00OO00O00OO ["产品批号"].str .replace ("(","（",regex =False )#line:1535
        OOOO0O00OO00O00OO ["产品批号"]=OOOO0O00OO00O00OO ["产品批号"].str .replace (")","）",regex =False )#line:1536
        OOOO0O00OO00O00OO ["产品批号"]=OOOO0O00OO00O00OO ["产品批号"].str .replace ("*","※",regex =False )#line:1537
        OOOO0O00OO00O00OO ['事件发生日期']=pd .to_datetime (OOOO0O00OO00O00OO ['事件发生日期'],format ='%Y-%m-%d',errors ='coerce')#line:1540
        OOOO0O00OO00O00OO ["事件发生月份"]=OOOO0O00OO00O00OO ["事件发生日期"].dt .to_period ("M").astype (str )#line:1544
        OOOO0O00OO00O00OO ["事件发生季度"]=OOOO0O00OO00O00OO ["事件发生日期"].dt .to_period ("Q").astype (str )#line:1545
        OOOO0O00OO00O00OO ["注册证编号/曾用注册证编号"]=OOOO0O00OO00O00OO ["注册证编号/曾用注册证编号"].fillna ("未填写")#line:1549
        OOOO0O00OO00O00OO ["产品批号"]=OOOO0O00OO00O00OO ["产品批号"].fillna ("未填写")#line:1550
        OOOO0O00OO00O00OO ["型号"]=OOOO0O00OO00O00OO ["型号"].fillna ("未填写")#line:1551
        OOOO0O00OO00O00OO ["规格"]=OOOO0O00OO00O00OO ["规格"].fillna ("未填写")#line:1552
        return OOOO0O00OO00O00OO #line:1554
def thread_it (OO0OOOOOOO0O0O00O ,*OOOO0OO00OO0OO0OO ):#line:1558
    ""#line:1559
    O0OO0O00O00O00000 =threading .Thread (target =OO0OOOOOOO0O0O00O ,args =OOOO0OO00OO0OO0OO )#line:1561
    O0OO0O00O00O00000 .setDaemon (True )#line:1563
    O0OO0O00O00O00000 .start ()#line:1565
def showWelcome ():#line:1568
    ""#line:1569
    O00O0OOO0000OOO00 =roox .winfo_screenwidth ()#line:1570
    O0O0OOOO0O000OO0O =roox .winfo_screenheight ()#line:1572
    roox .overrideredirect (True )#line:1574
    roox .attributes ("-alpha",1 )#line:1575
    OOO0OO0000O0OOOO0 =(O00O0OOO0000OOO00 -475 )/2 #line:1576
    O0OO000O0O00O0000 =(O0O0OOOO0O000OO0O -200 )/2 #line:1577
    roox .geometry ("675x140+%d+%d"%(OOO0OO0000O0OOOO0 ,O0OO000O0O00O0000 ))#line:1579
    roox ["bg"]="royalblue"#line:1580
    OOOO000O0O0OOO000 =Label (roox ,text ="医疗器械警戒趋势分析工具",fg ="white",bg ="royalblue",font =("微软雅黑",20 ))#line:1583
    OOOO000O0O0OOO000 .place (x =0 ,y =15 ,width =675 ,height =90 )#line:1584
    O0OOOOO0O0O00O00O =Label (roox ,text ="Trend Analysis Tools V"+str (version_now ),fg ="white",bg ="cornflowerblue",font =("微软雅黑",15 ),)#line:1591
    O0OOOOO0O0O00O00O .place (x =0 ,y =90 ,width =675 ,height =50 )#line:1592
def closeWelcome ():#line:1595
    ""#line:1596
    for OO0O000OO0OO0O0O0 in range (2 ):#line:1597
        root .attributes ("-alpha",0 )#line:1598
        time .sleep (1 )#line:1599
    root .attributes ("-alpha",1 )#line:1600
    roox .destroy ()#line:1601
if __name__ =='__main__':#line:1605
    pass #line:1606
root =Tk ()#line:1607
root .title ("医疗器械警戒趋势分析工具Trend Analysis Tools V"+str (version_now ))#line:1608
sw_root =root .winfo_screenwidth ()#line:1609
sh_root =root .winfo_screenheight ()#line:1611
ww_root =700 #line:1613
wh_root =620 #line:1614
x_root =(sw_root -ww_root )/2 #line:1616
y_root =(sh_root -wh_root )/2 #line:1617
root .geometry ("%dx%d+%d+%d"%(ww_root ,wh_root ,x_root ,y_root ))#line:1618
root .configure (bg ="steelblue")#line:1619
try :#line:1622
    frame0 =ttk .Frame (root ,width =100 ,height =20 )#line:1623
    frame0 .pack (side =LEFT )#line:1624
    B_open_files1 =Button (frame0 ,text ="导入原始数据",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_fileopen ,0 ),)#line:1637
    B_open_files1 .pack ()#line:1638
    B_open_files3 =Button (frame0 ,text ="导入分析规则",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_fileopen ,1 ),)#line:1651
    B_open_files3 .pack ()#line:1652
    B_open_files3 =Button (frame0 ,text ="趋势统计分析",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_analysis ,0 ),)#line:1667
    B_open_files3 .pack ()#line:1668
    B_open_files3 =Button (frame0 ,text ="直方图（数量）",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_bar ,"数量"))#line:1681
    B_open_files3 .pack ()#line:1682
    B_open_files3 =Button (frame0 ,text ="直方图（占比）",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_bar ,"百分比"))#line:1693
    B_open_files3 .pack ()#line:1694
    B_open_files3 =Button (frame0 ,text ="查看帮助文件",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (helper ))#line:1705
    B_open_files3 .pack ()#line:1706
    B_open_files3 =Button (frame0 ,text ="更改用户分组",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (display_random_number ))#line:1717
    B_open_files3 .pack ()#line:1718
except :#line:1719
    pass #line:1720
text =ScrolledText (root ,height =400 ,width =400 ,bg ="#FFFFFF",font ="微软雅黑")#line:1724
text .pack ()#line:1725
text .insert (END ,"\n  本程序用于趋势分析,供广东省内参与医疗器械警戒试点的企业免费使用。如您有相关问题或改进建议，请联系以下人员：\n\n    佛山市药品不良反应监测中心\n    蔡权周 \n    微信：18575757461 \n    邮箱：411703730@qq.com")#line:1730
text .insert (END ,"\n\n")#line:1731
def A000 ():#line:1733
    pass #line:1734
setting_cfg =read_setting_cfg ()#line:1738
generate_random_file ()#line:1739
setting_cfg =open_setting_cfg ()#line:1740
if setting_cfg ["settingdir"]==0 :#line:1741
    showinfo (title ="提示",message ="未发现默认配置文件夹，请选择一个。如该配置文件夹中并无配置文件，将生成默认配置文件。")#line:1742
    filepathu =filedialog .askdirectory ()#line:1743
    path =get_directory_path (filepathu )#line:1744
    update_setting_cfg ("settingdir",path )#line:1745
setting_cfg =open_setting_cfg ()#line:1746
random_number =int (setting_cfg ["sidori"])#line:1747
input_number =int (str (setting_cfg ["sidfinal"])[0 :6 ])#line:1748
day_end =convert_and_compare_dates (str (setting_cfg ["sidfinal"])[6 :14 ])#line:1749
sid =random_number *2 +183576 #line:1750
if input_number ==sid and day_end =="未过期":#line:1751
    usergroup ="用户组=1"#line:1752
    text .insert (END ,usergroup +"   有效期至：")#line:1753
    text .insert (END ,datetime .strptime (str (int (int (str (setting_cfg ["sidfinal"])[6 :14 ])/4 )),"%Y%m%d"))#line:1754
else :#line:1755
    text .insert (END ,usergroup )#line:1756
text .insert (END ,"\n配置文件路径："+setting_cfg ["settingdir"]+"\n")#line:1757
roox =Toplevel ()#line:1761
tMain =threading .Thread (target =showWelcome )#line:1762
tMain .start ()#line:1763
t1 =threading .Thread (target =closeWelcome )#line:1764
t1 .start ()#line:1765
root .lift ()#line:1769
root .attributes ("-topmost",True )#line:1770
root .attributes ("-topmost",False )#line:1771
root .mainloop ()#line:1772
