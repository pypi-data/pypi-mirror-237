#!/usr/bin/env python
# coding: utf-8
# 趋势分析工具Trend Analysis Tools 
# 开发人：蔡权周
# 第一部分：导入基本模块及初始化 ########################################################################
# 导入一些基本模块
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
version_now ="0.0.9"#line:57
usergroup ="用户组=0"#line:58
setting_cfg =""#line:59
csdir =str (os .path .abspath (__file__ )).replace (str (__file__ ),"")#line:61
def extract_zip_file (O00OOOOO00000O00O ,OO0OO000O000O0OO0 ):#line:70
    import zipfile #line:72
    if OO0OO000O000O0OO0 =="":#line:73
        return 0 #line:74
    with zipfile .ZipFile (O00OOOOO00000O00O ,'r')as O00O0O000OO0OO0OO :#line:75
        for OOOO0000OO0OOO000 in O00O0O000OO0OO0OO .infolist ():#line:76
            OOOO0000OO0OOO000 .filename =OOOO0000OO0OOO000 .filename .encode ('cp437').decode ('gbk')#line:78
            O00O0O000OO0OO0OO .extract (OOOO0000OO0OOO000 ,OO0OO000O000O0OO0 )#line:79
def get_directory_path (O00OO0OOOO0O000O0 ):#line:85
    global csdir #line:87
    if not (os .path .isfile (os .path .join (O00OO0OOOO0O000O0 ,'规则文件.xls'))):#line:89
        extract_zip_file (csdir +"def.py",O00OO0OOOO0O000O0 )#line:94
    if O00OO0OOOO0O000O0 =="":#line:96
        quit ()#line:97
    return O00OO0OOOO0O000O0 #line:98
def convert_and_compare_dates (O0O000OO00O0OOOOO ):#line:102
    import datetime #line:103
    OOOO0O000OOO0OOOO =datetime .datetime .now ()#line:104
    try :#line:106
       OO00O00O000OOOO00 =datetime .datetime .strptime (str (int (int (O0O000OO00O0OOOOO )/4 )),"%Y%m%d")#line:107
    except :#line:108
        print ("fail")#line:109
        return "已过期"#line:110
    if OO00O00O000OOOO00 >OOOO0O000OOO0OOOO :#line:112
        return "未过期"#line:114
    else :#line:115
        return "已过期"#line:116
def read_setting_cfg ():#line:118
    global csdir #line:119
    if os .path .exists (csdir +'setting.cfg'):#line:121
        text .insert (END ,"已完成初始化\n")#line:122
        with open (csdir +'setting.cfg','r')as OOOO0OOOO0000O0OO :#line:123
            O000OO0000OO00000 =eval (OOOO0OOOO0000O0OO .read ())#line:124
    else :#line:125
        O0O00O0OO0OOOO000 =csdir +'setting.cfg'#line:127
        with open (O0O00O0OO0OOOO000 ,'w')as OOOO0OOOO0000O0OO :#line:128
            OOOO0OOOO0000O0OO .write ('{"settingdir": 0, "sidori": 0, "sidfinal": "11111180000808"}')#line:129
        text .insert (END ,"未初始化，正在初始化...\n")#line:130
        O000OO0000OO00000 =read_setting_cfg ()#line:131
    return O000OO0000OO00000 #line:132
def open_setting_cfg ():#line:135
    global csdir #line:136
    with open (csdir +"setting.cfg","r")as OOOOOO00O00OO00OO :#line:138
        O00OO0OO0OOO0O0OO =eval (OOOOOO00O00OO00OO .read ())#line:140
    return O00OO0OO0OOO0O0OO #line:141
def update_setting_cfg (O0OO0OO0O0O0OO0OO ,OO0OO00O000O0O000 ):#line:143
    global csdir #line:144
    with open (csdir +"setting.cfg","r")as O00O000OO00OOOO00 :#line:146
        OOO00O0OO00O00OO0 =eval (O00O000OO00OOOO00 .read ())#line:148
    if OOO00O0OO00O00OO0 [O0OO0OO0O0O0OO0OO ]==0 or OOO00O0OO00O00OO0 [O0OO0OO0O0O0OO0OO ]=="11111180000808":#line:150
        OOO00O0OO00O00OO0 [O0OO0OO0O0O0OO0OO ]=OO0OO00O000O0O000 #line:151
        with open (csdir +"setting.cfg","w")as O00O000OO00OOOO00 :#line:153
            O00O000OO00OOOO00 .write (str (OOO00O0OO00O00OO0 ))#line:154
def generate_random_file ():#line:157
    OO00O000OO0O0OOO0 =random .randint (200000 ,299999 )#line:159
    update_setting_cfg ("sidori",OO00O000OO0O0OOO0 )#line:161
def display_random_number ():#line:163
    global csdir #line:164
    OOO000O0O00OO0O00 =Toplevel ()#line:165
    OOO000O0O00OO0O00 .title ("ID")#line:166
    O000OO0OOO0O0OOO0 =OOO000O0O00OO0O00 .winfo_screenwidth ()#line:168
    O0O0OOO00O00O00O0 =OOO000O0O00OO0O00 .winfo_screenheight ()#line:169
    OO00O0OOOOO00O000 =80 #line:171
    OO000OO0OO00OOOO0 =70 #line:172
    OOO0OOO00O00O000O =(O000OO0OOO0O0OOO0 -OO00O0OOOOO00O000 )/2 #line:174
    O0000OOOOO0O0OOOO =(O0O0OOO00O00O00O0 -OO000OO0OO00OOOO0 )/2 #line:175
    OOO000O0O00OO0O00 .geometry ("%dx%d+%d+%d"%(OO00O0OOOOO00O000 ,OO000OO0OO00OOOO0 ,OOO0OOO00O00O000O ,O0000OOOOO0O0OOOO ))#line:176
    with open (csdir +"setting.cfg","r")as O0O0O0OOOO0O0OOO0 :#line:179
        OOOO0O0O0O00OOO00 =eval (O0O0O0OOOO0O0OOO0 .read ())#line:181
    O0OO0OO0O0OO00OOO =int (OOOO0O0O0O00OOO00 ["sidori"])#line:182
    OO000OO0000O0O00O =O0OO0OO0O0OO00OOO *2 +183576 #line:183
    print (OO000OO0000O0O00O )#line:185
    OO00OO00000000OO0 =ttk .Label (OOO000O0O00OO0O00 ,text =f"机器码: {O0OO0OO0O0OO00OOO}")#line:187
    O0O0000O00OO00O00 =ttk .Entry (OOO000O0O00OO0O00 )#line:188
    OO00OO00000000OO0 .pack ()#line:191
    O0O0000O00OO00O00 .pack ()#line:192
    ttk .Button (OOO000O0O00OO0O00 ,text ="验证",command =lambda :check_input (O0O0000O00OO00O00 .get (),OO000OO0000O0O00O )).pack ()#line:196
def check_input (O0O0000000000OOOO ,OO00O00OO0OOO000O ):#line:198
    try :#line:202
        OOO0OOO00OO0OOO0O =int (str (O0O0000000000OOOO )[0 :6 ])#line:203
        O0OO0OO00O0OO0OOO =convert_and_compare_dates (str (O0O0000000000OOOO )[6 :14 ])#line:204
    except :#line:205
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:206
        return 0 #line:207
    if OOO0OOO00OO0OOO0O ==OO00O00OO0OOO000O and O0OO0OO00O0OO0OOO =="未过期":#line:209
        update_setting_cfg ("sidfinal",O0O0000000000OOOO )#line:210
        showinfo (title ="提示",message ="注册成功,请重新启动程序。")#line:211
        quit ()#line:212
    else :#line:213
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:214
def Tread_TOOLS_fileopen (O0OO0O000O0O0OOO0 ):#line:222
    ""#line:223
    global TT_ori #line:224
    global TT_ori_backup #line:225
    global TT_biaozhun #line:226
    warnings .filterwarnings ('ignore')#line:227
    if O0OO0O000O0O0OOO0 ==0 :#line:229
        O000OOOO0000OO0OO =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:230
        OOOO0O00000O0OOO0 =[pd .read_excel (OOOOO0O0O00OOO0OO ,header =0 ,sheet_name =0 )for OOOOO0O0O00OOO0OO in O000OOOO0000OO0OO ]#line:231
        O0O00OO0OOOO000OO =pd .concat (OOOO0O00000O0OOO0 ,ignore_index =True ).drop_duplicates ()#line:232
        try :#line:233
            O0O00OO0OOOO000OO =O0O00OO0OOOO000OO .loc [:,~TT_ori .columns .str .contains ("^Unnamed")]#line:234
        except :#line:235
            pass #line:236
        TT_ori_backup =O0O00OO0OOOO000OO .copy ()#line:237
        TT_ori =Tread_TOOLS_CLEAN (O0O00OO0OOOO000OO ).copy ()#line:238
        text .insert (END ,"\n原始数据导入成功，行数："+str (len (TT_ori )))#line:240
        text .insert (END ,"\n数据校验：\n")#line:241
        text .insert (END ,TT_ori )#line:242
        text .see (END )#line:243
    if O0OO0O000O0O0OOO0 ==1 :#line:245
        OO00OO0OO000O000O =filedialog .askopenfilename (filetypes =[("XLS",".xls")])#line:246
        TT_biaozhun ["关键字表"]=pd .read_excel (OO00OO0OO000O000O ,sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:247
        TT_biaozhun ["产品批号"]=pd .read_excel (OO00OO0OO000O000O ,sheet_name ="产品批号",header =0 ,index_col =0 ,).reset_index ()#line:248
        TT_biaozhun ["事件发生月份"]=pd .read_excel (OO00OO0OO000O000O ,sheet_name ="事件发生月份",header =0 ,index_col =0 ,).reset_index ()#line:249
        TT_biaozhun ["事件发生季度"]=pd .read_excel (OO00OO0OO000O000O ,sheet_name ="事件发生季度",header =0 ,index_col =0 ,).reset_index ()#line:250
        TT_biaozhun ["规格"]=pd .read_excel (OO00OO0OO000O000O ,sheet_name ="规格",header =0 ,index_col =0 ,).reset_index ()#line:251
        TT_biaozhun ["型号"]=pd .read_excel (OO00OO0OO000O000O ,sheet_name ="型号",header =0 ,index_col =0 ,).reset_index ()#line:252
        TT_biaozhun ["设置"]=pd .read_excel (OO00OO0OO000O000O ,sheet_name ="设置",header =0 ,index_col =0 ,).reset_index ()#line:253
        Tread_TOOLS_check (TT_ori ,TT_biaozhun ["关键字表"],0 )#line:254
        text .insert (END ,"\n标准导入成功，行数："+str (len (TT_biaozhun )))#line:255
        text .see (END )#line:256
def Tread_TOOLS_check (O0O00OO0OOOOOOOO0 ,OOOO00O00O0O0O0O0 ,O00000O0O0OOOOOO0 ):#line:258
        ""#line:259
        global TT_ori #line:260
        OOOO000OO0OO0OOO0 =Tread_TOOLS_Countall (O0O00OO0OOOOOOOO0 ).df_psur (OOOO00O00O0O0O0O0 )#line:261
        if O00000O0O0OOOOOO0 ==0 :#line:263
            Tread_TOOLS_tree_Level_2 (OOOO000OO0OO0OOO0 ,0 ,TT_ori .copy ())#line:265
        OOOO000OO0OO0OOO0 ["核验"]=0 #line:268
        OOOO000OO0OO0OOO0 .loc [(OOOO000OO0OO0OOO0 ["关键字标记"].str .contains ("-其他关键字-",na =False )),"核验"]=OOOO000OO0OO0OOO0 .loc [(OOOO000OO0OO0OOO0 ["关键字标记"].str .contains ("-其他关键字-",na =False )),"总数量"]#line:269
        if OOOO000OO0OO0OOO0 ["核验"].sum ()>0 :#line:270
            showinfo (title ="温馨提示",message ="存在未定义类型的报告"+str (OOOO000OO0OO0OOO0 ["核验"].sum ())+"条，趋势分析可能会存在遗漏，建议修正该错误再进行下一步。")#line:271
def Tread_TOOLS_tree_Level_2 (OOOO000OOO000OOO0 ,OOO0O00OO00OOOOOO ,OO00O00O00O0OO000 ,*O0OOOO0OOOOOO000O ):#line:273
    ""#line:274
    global TT_ori_backup #line:276
    OOO0OO00OOO000000 =OOOO000OOO000OOO0 .columns .values .tolist ()#line:278
    OOO0O00OO00OOOOOO =0 #line:279
    OOOOO0O0000O00O00 =OOOO000OOO000OOO0 .loc [:]#line:280
    O00O0OO0OOO0OOO00 =0 #line:284
    try :#line:285
        OO000OO0O0O0OOO00 =O0OOOO0OOOOOO000O [0 ]#line:286
        O00O0OO0OOO0OOO00 =1 #line:287
    except :#line:288
        pass #line:289
    O0OOO0000000OO00O =Toplevel ()#line:292
    O0OOO0000000OO00O .title ("报表查看器")#line:293
    OOOOO000O0O0O0O00 =O0OOO0000000OO00O .winfo_screenwidth ()#line:294
    OOO00OO00O0000O00 =O0OOO0000000OO00O .winfo_screenheight ()#line:296
    O00O00O000O0OOOO0 =1300 #line:298
    O00OO000OO0OOOO00 =600 #line:299
    O0OO0OO0OO0O000OO =(OOOOO000O0O0O0O00 -O00O00O000O0OOOO0 )/2 #line:301
    O0O00OOOO0000OOOO =(OOO00OO00O0000O00 -O00OO000OO0OOOO00 )/2 #line:302
    O0OOO0000000OO00O .geometry ("%dx%d+%d+%d"%(O00O00O000O0OOOO0 ,O00OO000OO0OOOO00 ,O0OO0OO0OO0O000OO ,O0O00OOOO0000OOOO ))#line:303
    OOO0O00O0OO0O00O0 =ttk .Frame (O0OOO0000000OO00O ,width =1300 ,height =20 )#line:304
    OOO0O00O0OO0O00O0 .pack (side =BOTTOM )#line:305
    OO0OO000OO0OOOO00 =ttk .Frame (O0OOO0000000OO00O ,width =1300 ,height =20 )#line:307
    OO0OO000OO0OOOO00 .pack (side =TOP )#line:308
    if 1 >0 :#line:312
        OOO0O000000000OO0 =Button (OOO0O00O0OO0O00O0 ,text ="控制图(所有)",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (OOOOO0O0000O00O00 [:-1 ],OO000OO0O0O0OOO00 ,[OO0O000OO000O0OO0 for OO0O000OO000O0OO0 in OOOOO0O0000O00O00 .columns if (OO0O000OO000O0OO0 not in [OO000OO0O0O0OOO00 ])],"关键字趋势图",100 ),)#line:322
        if O00O0OO0OOO0OOO00 ==1 :#line:323
            OOO0O000000000OO0 .pack (side =LEFT )#line:324
        OOO0O000000000OO0 =Button (OOO0O00O0OO0O00O0 ,text ="控制图(总数量)",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (OOOOO0O0000O00O00 [:-1 ],OO000OO0O0O0OOO00 ,[OOO0OOOO000OOO00O for OOO0OOOO000OOO00O in OOOOO0O0000O00O00 .columns if (OOO0OOOO000OOO00O in ["该元素总数量"])],"关键字趋势图",100 ),)#line:334
        if O00O0OO0OOO0OOO00 ==1 :#line:335
            OOO0O000000000OO0 .pack (side =LEFT )#line:336
        OOOO00OO0O0000OO0 =Button (OOO0O00O0OO0O00O0 ,text ="导出",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_save_dict (OOOOO0O0000O00O00 ),)#line:346
        OOOO00OO0O0000OO0 .pack (side =LEFT )#line:347
        OOOO00OO0O0000OO0 =Button (OOO0O00O0OO0O00O0 ,text ="发生率测算",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_fashenglv (OOOOO0O0000O00O00 ,OO000OO0O0O0OOO00 ),)#line:357
        if "关键字标记"not in OOOOO0O0000O00O00 .columns and "报告编码"not in OOOOO0O0000O00O00 .columns :#line:358
            if "对象"not in OOOOO0O0000O00O00 .columns :#line:359
                OOOO00OO0O0000OO0 .pack (side =LEFT )#line:360
        OOOO00OO0O0000OO0 =Button (OOO0O00O0OO0O00O0 ,text ="直方图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_histbar (OOOOO0O0000O00O00 .copy ()),)#line:370
        if "对象"in OOOOO0O0000O00O00 .columns :#line:371
            OOOO00OO0O0000OO0 .pack (side =LEFT )#line:372
        O0OO0O000OOOOO0OO =Button (OOO0O00O0OO0O00O0 ,text ="行数:"+str (len (OOOOO0O0000O00O00 )),bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",)#line:382
        O0OO0O000OOOOO0OO .pack (side =LEFT )#line:383
    OOO0O0O0OOOO0OOO0 =OOOOO0O0000O00O00 .values .tolist ()#line:386
    O00OOOOO0O0O000OO =OOOOO0O0000O00O00 .columns .values .tolist ()#line:387
    OOO0O00O000OO0000 =ttk .Treeview (OO0OO000OO0OOOO00 ,columns =O00OOOOO0O0O000OO ,show ="headings",height =45 )#line:388
    for OO000O0O00000O0O0 in O00OOOOO0O0O000OO :#line:390
        OOO0O00O000OO0000 .heading (OO000O0O00000O0O0 ,text =OO000O0O00000O0O0 )#line:391
    for O00000O0O00O00O0O in OOO0O0O0OOOO0OOO0 :#line:392
        OOO0O00O000OO0000 .insert ("","end",values =O00000O0O00O00O0O )#line:393
    for OO00O0O0O0O0O0OOO in O00OOOOO0O0O000OO :#line:394
        OOO0O00O000OO0000 .column (OO00O0O0O0O0O0OOO ,minwidth =0 ,width =120 ,stretch =NO )#line:395
    OO0OOO0OO0OOO0O00 =Scrollbar (OO0OO000OO0OOOO00 ,orient ="vertical")#line:397
    OO0OOO0OO0OOO0O00 .pack (side =RIGHT ,fill =Y )#line:398
    OO0OOO0OO0OOO0O00 .config (command =OOO0O00O000OO0000 .yview )#line:399
    OOO0O00O000OO0000 .config (yscrollcommand =OO0OOO0OO0OOO0O00 .set )#line:400
    OOOOOO00OO0O0OO0O =Scrollbar (OO0OO000OO0OOOO00 ,orient ="horizontal")#line:402
    OOOOOO00OO0O0OO0O .pack (side =BOTTOM ,fill =X )#line:403
    OOOOOO00OO0O0OO0O .config (command =OOO0O00O000OO0000 .xview )#line:404
    OOO0O00O000OO0000 .config (yscrollcommand =OO0OOO0OO0OOO0O00 .set )#line:405
    def OO0O000OO00OOO000 (OOO000O00000000O0 ,O000O0OO0O0O0OO00 ,O0O000O0O0OO0O0OO ):#line:407
        for OOO0O0O00OOOOO0O0 in OOO0O00O000OO0000 .selection ():#line:410
            OOO0OOOO0OO0O0OOO =OOO0O00O000OO0000 .item (OOO0O0O00OOOOO0O0 ,"values")#line:411
            OOO0000O0O00OOO0O =dict (zip (O000O0OO0O0O0OO00 ,OOO0OOOO0OO0O0OOO ))#line:412
        if "该分类下各项计数"in O000O0OO0O0O0OO00 :#line:414
            OO00OOO000O0OOOOO =OO00O00O00O0OO000 .copy ()#line:415
            OO00OOO000O0OOOOO ["关键字查找列"]=""#line:416
            for OO00OOOO00OOOO0OO in TOOLS_get_list (OOO0000O0O00OOO0O ["查找位置"]):#line:417
                OO00OOO000O0OOOOO ["关键字查找列"]=OO00OOO000O0OOOOO ["关键字查找列"]+OO00OOO000O0OOOOO [OO00OOOO00OOOO0OO ].astype ("str")#line:418
            O00O0OO0O0O000000 =OO00OOO000O0OOOOO .loc [OO00OOO000O0OOOOO ["关键字查找列"].str .contains (OOO0000O0O00OOO0O ["关键字标记"],na =False )].copy ()#line:419
            O00O0OO0O0O000000 =O00O0OO0O0O000000 .loc [~O00O0OO0O0O000000 ["关键字查找列"].str .contains (OOO0000O0O00OOO0O ["排除值"],na =False )].copy ()#line:420
            Tread_TOOLS_tree_Level_2 (O00O0OO0O0O000000 ,0 ,O00O0OO0O0O000000 )#line:426
            return 0 #line:427
        if "报告编码"in O000O0OO0O0O0OO00 :#line:429
            OO0OO00O000OO0OO0 =Toplevel ()#line:430
            O000O0OOO0000O0O0 =OO0OO00O000OO0OO0 .winfo_screenwidth ()#line:431
            O0OOOO00OOOO00O00 =OO0OO00O000OO0OO0 .winfo_screenheight ()#line:433
            OO0O0OO000OOOOOOO =800 #line:435
            OOO0000OOOOOOO0OO =600 #line:436
            OO00OOOO00OOOO0OO =(O000O0OOO0000O0O0 -OO0O0OO000OOOOOOO )/2 #line:438
            O0000O0O0OO0OOOOO =(O0OOOO00OOOO00O00 -OOO0000OOOOOOO0OO )/2 #line:439
            OO0OO00O000OO0OO0 .geometry ("%dx%d+%d+%d"%(OO0O0OO000OOOOOOO ,OOO0000OOOOOOO0OO ,OO00OOOO00OOOO0OO ,O0000O0O0OO0OOOOO ))#line:440
            O00O0000O00OO00OO =ScrolledText (OO0OO00O000OO0OO0 ,height =1100 ,width =1100 ,bg ="#FFFFFF")#line:444
            O00O0000O00OO00OO .pack (padx =10 ,pady =10 )#line:445
            def O000O0O000O00OO00 (event =None ):#line:446
                O00O0000O00OO00OO .event_generate ('<<Copy>>')#line:447
            def O0O0O000OO00000OO (O000O0O000O0OO0O0 ,O00OOOOOOOO0000O0 ):#line:448
                O00OOO00OO00O0O0O =open (O00OOOOOOOO0000O0 ,"w",encoding ='utf-8')#line:449
                O00OOO00OO00O0O0O .write (O000O0O000O0OO0O0 )#line:450
                O00OOO00OO00O0O0O .flush ()#line:452
                showinfo (title ="提示信息",message ="保存成功。")#line:453
            OOOO0O0000O000OOO =Menu (O00O0000O00OO00OO ,tearoff =False ,)#line:455
            OOOO0O0000O000OOO .add_command (label ="复制",command =O000O0O000O00OO00 )#line:456
            OOOO0O0000O000OOO .add_command (label ="导出",command =lambda :thread_it (O0O0O000OO00000OO ,O00O0000O00OO00OO .get (1.0 ,'end'),filedialog .asksaveasfilename (title =u"保存文件",initialfile =OOO0000O0O00OOO0O ["报告编码"],defaultextension ="txt",filetypes =[("txt","*.txt")])))#line:457
            def O0OO0OOO0000O0O0O (O0O0O0O0O00O000O0 ):#line:459
                OOOO0O0000O000OOO .post (O0O0O0O0O00O000O0 .x_root ,O0O0O0O0O00O000O0 .y_root )#line:460
            O00O0000O00OO00OO .bind ("<Button-3>",O0OO0OOO0000O0O0O )#line:461
            OO0OO00O000OO0OO0 .title (OOO0000O0O00OOO0O ["报告编码"])#line:463
            for OOO0O000OO0OOOOO0 in range (len (O000O0OO0O0O0OO00 )):#line:464
                O00O0000O00OO00OO .insert (END ,O000O0OO0O0O0OO00 [OOO0O000OO0OOOOO0 ])#line:466
                O00O0000O00OO00OO .insert (END ,"：")#line:467
                O00O0000O00OO00OO .insert (END ,OOO0000O0O00OOO0O [O000O0OO0O0O0OO00 [OOO0O000OO0OOOOO0 ]])#line:468
                O00O0000O00OO00OO .insert (END ,"\n")#line:469
            O00O0000O00OO00OO .config (state =DISABLED )#line:470
            return 0 #line:471
        O0000O0O0OO0OOOOO =OOO0OOOO0OO0O0OOO [1 :-1 ]#line:474
        OO00OOOO00OOOO0OO =O0O000O0O0OO0O0OO .columns .tolist ()#line:476
        OO00OOOO00OOOO0OO =OO00OOOO00OOOO0OO [1 :-1 ]#line:477
        O0OOO00OO0OOOOO00 ={'关键词':OO00OOOO00OOOO0OO ,'数量':O0000O0O0OO0OOOOO }#line:479
        O0OOO00OO0OOOOO00 =pd .DataFrame .from_dict (O0OOO00OO0OOOOO00 )#line:480
        O0OOO00OO0OOOOO00 ["数量"]=O0OOO00OO0OOOOO00 ["数量"].astype (float )#line:481
        Tread_TOOLS_draw (O0OOO00OO0OOOOO00 ,"帕累托图",'关键词','数量',"帕累托图")#line:482
        return 0 #line:483
    OOO0O00O000OO0000 .bind ("<Double-1>",lambda O000OOOO0O00OOOOO :OO0O000OO00OOO000 (O000OOOO0O00OOOOO ,O00OOOOO0O0O000OO ,OOOOO0O0000O00O00 ),)#line:491
    OOO0O00O000OO0000 .pack ()#line:492
class Tread_TOOLS_Countall ():#line:494
    ""#line:495
    def __init__ (OOO0O0O00O00O00OO ,O00O00O0OO0O0OO00 ):#line:496
        ""#line:497
        OOO0O0O00O00O00OO .df =O00O00O0OO0O0OO00 #line:498
    def df_psur (O0000O000O00O0O0O ,OOOO00OO0O000O00O ,*O0O00OO00O00OOO00 ):#line:500
        ""#line:501
        global TT_biaozhun #line:502
        OO0OO00O0OOOO0O00 =O0000O000O00O0O0O .df .copy ()#line:503
        O000O0O0O00OO0O0O =len (OO0OO00O0OOOO0O00 .drop_duplicates ("报告编码"))#line:505
        OOOOOO00OOO0OO0OO =OOOO00OO0O000O00O .copy ()#line:508
        O0OO00OOOO0OOO00O =TT_biaozhun ["设置"]#line:511
        if O0OO00OOOO0OOO00O .loc [1 ,"值"]:#line:512
            OOOOO0OO000O0OOOO =O0OO00OOOO0OOO00O .loc [1 ,"值"]#line:513
        else :#line:514
            OOOOO0OO000O0OOOO ="透视列"#line:515
            OO0OO00O0OOOO0O00 [OOOOO0OO000O0OOOO ]="未正确设置"#line:516
        O000OOOOOO0O00OOO =""#line:518
        OOOOOOOO0O0000O00 ="-其他关键字-"#line:519
        for OOOOOO0O00O000OO0 ,OO0O0O00O0000O0OO in OOOOOO00OOO0OO0OO .iterrows ():#line:520
            OOOOOOOO0O0000O00 =OOOOOOOO0O0000O00 +"|"+str (OO0O0O00O0000O0OO ["值"])#line:521
            OOOO00O0000O00OOO =OO0O0O00O0000O0OO #line:522
        OOOO00O0000O00OOO [3 ]=OOOOOOOO0O0000O00 #line:523
        OOOO00O0000O00OOO [2 ]="-其他关键字-|"#line:524
        OOOOOO00OOO0OO0OO .loc [len (OOOOOO00OOO0OO0OO )]=OOOO00O0000O00OOO #line:525
        OOOOOO00OOO0OO0OO =OOOOOO00OOO0OO0OO .reset_index (drop =True )#line:526
        OO0OO00O0OOOO0O00 ["关键字查找列"]=""#line:530
        for OO00O0O000O0OO000 in TOOLS_get_list (OOOOOO00OOO0OO0OO .loc [0 ,"查找位置"]):#line:531
            OO0OO00O0OOOO0O00 ["关键字查找列"]=OO0OO00O0OOOO0O00 ["关键字查找列"]+OO0OO00O0OOOO0O00 [OO00O0O000O0OO000 ].astype ("str")#line:532
        O0OO0000OOO0O0000 =[]#line:535
        for OOOOOO0O00O000OO0 ,OO0O0O00O0000O0OO in OOOOOO00OOO0OO0OO .iterrows ():#line:536
            O0OOOOO0OOOOOO00O =OO0O0O00O0000O0OO ["值"]#line:537
            OO00OO00OOO00O0O0 =OO0OO00O0OOOO0O00 .loc [OO0OO00O0OOOO0O00 ["关键字查找列"].str .contains (O0OOOOO0OOOOOO00O ,na =False )].copy ()#line:538
            if str (OO0O0O00O0000O0OO ["排除值"])!="nan":#line:539
                OO00OO00OOO00O0O0 =OO00OO00OOO00O0O0 .loc [~OO00OO00OOO00O0O0 ["关键字查找列"].str .contains (str (OO0O0O00O0000O0OO ["排除值"]),na =False )].copy ()#line:540
            OO00OO00OOO00O0O0 ["关键字标记"]=str (O0OOOOO0OOOOOO00O )#line:542
            OO00OO00OOO00O0O0 ["关键字计数"]=1 #line:543
            if len (OO00OO00OOO00O0O0 )>0 :#line:545
                O0OO00OO0O00OO000 =pd .pivot_table (OO00OO00OOO00O0O0 .drop_duplicates ("报告编码"),values =["关键字计数"],index ="关键字标记",columns =OOOOO0OO000O0OOOO ,aggfunc ={"关键字计数":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:555
                O0OO00OO0O00OO000 =O0OO00OO0O00OO000 [:-1 ]#line:556
                O0OO00OO0O00OO000 .columns =O0OO00OO0O00OO000 .columns .droplevel (0 )#line:557
                O0OO00OO0O00OO000 =O0OO00OO0O00OO000 .reset_index ()#line:558
                if len (O0OO00OO0O00OO000 )>0 :#line:561
                    O000OO00O00O0000O =str (Counter (TOOLS_get_list0 ("use(关键字查找列).file",OO00OO00OOO00O0O0 ,1000 ))).replace ("Counter({","{")#line:562
                    O000OO00O00O0000O =O000OO00O00O0000O .replace ("})","}")#line:563
                    O000OO00O00O0000O =ast .literal_eval (O000OO00O00O0000O )#line:564
                    O0OO00OO0O00OO000 .loc [0 ,"事件分类"]=str (TOOLS_get_list (O0OO00OO0O00OO000 .loc [0 ,"关键字标记"])[0 ])#line:566
                    O0OO00OO0O00OO000 .loc [0 ,"该分类下各项计数"]=str ({OO00OO0OO0OOO000O :O00O0000OOOO00OOO for OO00OO0OO0OOO000O ,O00O0000OOOO00OOO in O000OO00O00O0000O .items ()if STAT_judge_x (str (OO00OO0OO0OOO000O ),TOOLS_get_list (O0OOOOO0OOOOOO00O ))==1 })#line:567
                    O0OO00OO0O00OO000 .loc [0 ,"其他分类各项计数"]=str ({O0OOOOO00O00OOOOO :O000O0O0O00O0O000 for O0OOOOO00O00OOOOO ,O000O0O0O00O0O000 in O000OO00O00O0000O .items ()if STAT_judge_x (str (O0OOOOO00O00OOOOO ),TOOLS_get_list (O0OOOOO0OOOOOO00O ))!=1 })#line:568
                    O0OO00OO0O00OO000 ["查找位置"]=OO0O0O00O0000O0OO ["查找位置"]#line:569
                    O0OO0000OOO0O0000 .append (O0OO00OO0O00OO000 )#line:572
        O000OOOOOO0O00OOO =pd .concat (O0OO0000OOO0O0000 )#line:573
        O000OOOOOO0O00OOO =O000OOOOOO0O00OOO .sort_values (by =["All"],ascending =[False ],na_position ="last")#line:578
        O000OOOOOO0O00OOO =O000OOOOOO0O00OOO .reset_index ()#line:579
        O000OOOOOO0O00OOO ["All占比"]=round (O000OOOOOO0O00OOO ["All"]/O000O0O0O00OO0O0O *100 ,2 )#line:581
        O000OOOOOO0O00OOO =O000OOOOOO0O00OOO .rename (columns ={"All":"总数量","All占比":"总数量占比"})#line:582
        for O000O0O00OOO0OOOO ,OO0OOO0000O0OOOOO in OOOOOO00OOO0OO0OO .iterrows ():#line:585
            O000OOOOOO0O00OOO .loc [(O000OOOOOO0O00OOO ["关键字标记"].astype (str )==str (OO0OOO0000O0OOOOO ["值"])),"排除值"]=OO0OOO0000O0OOOOO ["排除值"]#line:586
            O000OOOOOO0O00OOO .loc [(O000OOOOOO0O00OOO ["关键字标记"].astype (str )==str (OO0OOO0000O0OOOOO ["值"])),"查找位置"]=OO0OOO0000O0OOOOO ["查找位置"]#line:587
        O000OOOOOO0O00OOO ["排除值"]=O000OOOOOO0O00OOO ["排除值"].fillna ("-没有排除值-")#line:589
        O000OOOOOO0O00OOO ["报表类型"]="PSUR"#line:592
        del O000OOOOOO0O00OOO ["index"]#line:593
        try :#line:594
            del O000OOOOOO0O00OOO ["未正确设置"]#line:595
        except :#line:596
            pass #line:597
        return O000OOOOOO0O00OOO #line:598
    def df_find_all_keword_risk (O000O0OOO000OO00O ,OOOOOO00000OO000O ,*O0O00OOO0O00OOO00 ):#line:601
        ""#line:602
        global TT_biaozhun #line:603
        O0OOO00O0O0O000OO =O000O0OOO000OO00O .df .copy ()#line:605
        O0OO00OOOOOO0O000 =time .time ()#line:606
        OO0O00O00O00OOOO0 =TT_biaozhun ["关键字表"].copy ()#line:608
        O0O0OO00000O0000O ="作用对象"#line:610
        O0O0OOO0O00O00OOO ="报告编码"#line:612
        O00O0O0OOOOO0OOO0 =O0OOO00O0O0O000OO .groupby ([O0O0OO00000O0000O ]).agg (总数量 =(O0O0OOO0O00O00OOO ,"nunique"),).reset_index ()#line:615
        O0OO0O000000000OO =[O0O0OO00000O0000O ,OOOOOO00000OO000O ]#line:617
        OOOO00OO00OOOOO00 =O0OOO00O0O0O000OO .groupby (O0OO0O000000000OO ).agg (该元素总数量 =(O0O0OO00000O0000O ,"count"),).reset_index ()#line:621
        O0OOOOOOO0OO0OOOO =[]#line:623
        O0OOO0000O0OOOO0O =0 #line:627
        O0O0O0OOO00O000O0 =int (len (O00O0O0OOOOO0OOO0 ))#line:628
        for OO00O00O0000O00O0 ,O0OO00O00O0O0OOO0 in zip (O00O0O0OOOOO0OOO0 [O0O0OO00000O0000O ].values ,O00O0O0OOOOO0OOO0 ["总数量"].values ):#line:629
            O0OOO0000O0OOOO0O +=1 #line:630
            O0OO0000OO00O0O0O =O0OOO00O0O0O000OO [(O0OOO00O0O0O000OO [O0O0OO00000O0000O ]==OO00O00O0000O00O0 )].copy ()#line:631
            for O00O0000OO0O00O0O ,O000OO0O00OOOO0O0 ,O0000O000OOOOOO0O in zip (OO0O00O00O00OOOO0 ["值"].values ,OO0O00O00O00OOOO0 ["查找位置"].values ,OO0O00O00O00OOOO0 ["排除值"].values ):#line:633
                    O0O000OOOOO0OO00O =O0OO0000OO00O0O0O .copy ()#line:634
                    OOO00O0OO00O0000O =TOOLS_get_list (O00O0000OO0O00O0O )[0 ]#line:635
                    O0O000OOOOO0OO00O ["关键字查找列"]=""#line:637
                    for OOO000O00O0000O00 in TOOLS_get_list (O000OO0O00OOOO0O0 ):#line:638
                        O0O000OOOOO0OO00O ["关键字查找列"]=O0O000OOOOO0OO00O ["关键字查找列"]+O0O000OOOOO0OO00O [OOO000O00O0000O00 ].astype ("str")#line:639
                    O0O000OOOOO0OO00O .loc [O0O000OOOOO0OO00O ["关键字查找列"].str .contains (O00O0000OO0O00O0O ,na =False ),"关键字"]=OOO00O0OO00O0000O #line:641
                    if str (O0000O000OOOOOO0O )!="nan":#line:646
                        O0O000OOOOO0OO00O =O0O000OOOOO0OO00O .loc [~O0O000OOOOO0OO00O ["关键字查找列"].str .contains (O0000O000OOOOOO0O ,na =False )].copy ()#line:647
                    if (len (O0O000OOOOO0OO00O ))<1 :#line:649
                        continue #line:651
                    OOO000O0OO0O00OO0 =STAT_find_keyword_risk (O0O000OOOOO0OO00O ,[O0O0OO00000O0000O ,"关键字"],"关键字",OOOOOO00000OO000O ,int (O0OO00O00O0O0OOO0 ))#line:653
                    if len (OOO000O0OO0O00OO0 )>0 :#line:654
                        OOO000O0OO0O00OO0 ["关键字组合"]=O00O0000OO0O00O0O #line:655
                        OOO000O0OO0O00OO0 ["排除值"]=O0000O000OOOOOO0O #line:656
                        OOO000O0OO0O00OO0 ["关键字查找列"]=O000OO0O00OOOO0O0 #line:657
                        O0OOOOOOO0OO0OOOO .append (OOO000O0OO0O00OO0 )#line:658
        if len (O0OOOOOOO0OO0OOOO )<1 :#line:661
            showinfo (title ="错误信息",message ="该注册证号未检索到任何关键字，规则制定存在缺陷。")#line:662
            return 0 #line:663
        O000OO0O0OOOO00OO =pd .concat (O0OOOOOOO0OO0OOOO )#line:664
        O000OO0O0OOOO00OO =pd .merge (O000OO0O0OOOO00OO ,OOOO00OO00OOOOO00 ,on =O0OO0O000000000OO ,how ="left")#line:667
        O000OO0O0OOOO00OO ["关键字数量比例"]=round (O000OO0O0OOOO00OO ["计数"]/O000OO0O0OOOO00OO ["该元素总数量"],2 )#line:668
        O000OO0O0OOOO00OO =O000OO0O0OOOO00OO .reset_index (drop =True )#line:670
        if len (O000OO0O0OOOO00OO )>0 :#line:673
            O000OO0O0OOOO00OO ["风险评分"]=0 #line:674
            O000OO0O0OOOO00OO ["报表类型"]="keyword_findrisk"+OOOOOO00000OO000O #line:675
            O000OO0O0OOOO00OO .loc [(O000OO0O0OOOO00OO ["计数"]>=3 ),"风险评分"]=O000OO0O0OOOO00OO ["风险评分"]+3 #line:676
            O000OO0O0OOOO00OO .loc [(O000OO0O0OOOO00OO ["计数"]>=(O000OO0O0OOOO00OO ["数量均值"]+O000OO0O0OOOO00OO ["数量标准差"])),"风险评分"]=O000OO0O0OOOO00OO ["风险评分"]+1 #line:677
            O000OO0O0OOOO00OO .loc [(O000OO0O0OOOO00OO ["计数"]>=O000OO0O0OOOO00OO ["数量CI"]),"风险评分"]=O000OO0O0OOOO00OO ["风险评分"]+1 #line:678
            O000OO0O0OOOO00OO .loc [(O000OO0O0OOOO00OO ["关键字数量比例"]>0.5 )&(O000OO0O0OOOO00OO ["计数"]>=3 ),"风险评分"]=O000OO0O0OOOO00OO ["风险评分"]+1 #line:679
            O000OO0O0OOOO00OO =O000OO0O0OOOO00OO .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:681
        OOO000O0O00OOO000 =O000OO0O0OOOO00OO .columns .to_list ()#line:691
        OOO0OOO000OO00OO0 =OOO000O0O00OOO000 [OOO000O0O00OOO000 .index ("关键字")+1 ]#line:692
        OOO000OOO0O00O0O0 =pd .pivot_table (O000OO0O0OOOO00OO ,index =OOO0OOO000OO00OO0 ,columns ="关键字",values =["计数"],aggfunc ={"计数":"sum"},fill_value ="0",margins =True ,dropna =False ,)#line:703
        OOO000OOO0O00O0O0 .columns =OOO000OOO0O00O0O0 .columns .droplevel (0 )#line:704
        OOO000OOO0O00O0O0 =pd .merge (OOO000OOO0O00O0O0 ,O000OO0O0OOOO00OO [[OOO0OOO000OO00OO0 ,"该元素总数量"]].drop_duplicates (OOO0OOO000OO00OO0 ),on =[OOO0OOO000OO00OO0 ],how ="left")#line:707
        del OOO000OOO0O00O0O0 ["All"]#line:709
        OOO000OOO0O00O0O0 .iloc [-1 ,-1 ]=OOO000OOO0O00O0O0 ["该元素总数量"].sum (axis =0 )#line:710
        print ("耗时：",(time .time ()-O0OO00OOOOOO0O000 ))#line:712
        return OOO000OOO0O00O0O0 #line:715
def Tread_TOOLS_bar (O0OO0OO00O00O0O0O ):#line:723
         ""#line:724
         O0OO0OO0OO0O000O0 =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:725
         O000O00O000000000 =[pd .read_excel (OOOOOOO0O00OOO000 ,header =0 ,sheet_name =0 )for OOOOOOO0O00OOO000 in O0OO0OO0OO0O000O0 ]#line:726
         OO0OOO0O0OOOO0O0O =pd .concat (O000O00O000000000 ,ignore_index =True )#line:727
         O00OO00OOOOOO00OO =pd .pivot_table (OO0OOO0O0OOOO0O0O ,index ="对象",columns ="关键词",values =O0OO0OO00O00O0O0O ,aggfunc ="sum",fill_value ="0",margins =True ,dropna =False ,).reset_index ()#line:737
         del O00OO00OOOOOO00OO ["All"]#line:739
         O00OO00OOOOOO00OO =O00OO00OOOOOO00OO [:-1 ]#line:740
         Tread_TOOLS_tree_Level_2 (O00OO00OOOOOO00OO ,0 ,0 )#line:742
def Tread_TOOLS_analysis (OO00O000OOO0OO000 ):#line:747
    ""#line:748
    import datetime #line:749
    global TT_ori #line:750
    global TT_biaozhun #line:751
    if len (TT_ori )==0 :#line:753
       showinfo (title ="提示",message ="您尚未导入原始数据。")#line:754
       return 0 #line:755
    if len (TT_biaozhun )==0 :#line:756
       showinfo (title ="提示",message ="您尚未导入规则。")#line:757
       return 0 #line:758
    OOO0OOOO0O00OOOOO =TT_biaozhun ["设置"]#line:760
    TT_ori ["作用对象"]=""#line:761
    for OO00OO0O0OOO0O0O0 in TOOLS_get_list (OOO0OOOO0O00OOOOO .loc [0 ,"值"]):#line:762
        TT_ori ["作用对象"]=TT_ori ["作用对象"]+"-"+TT_ori [OO00OO0O0OOO0O0O0 ].fillna ("未填写").astype ("str")#line:763
    OOOO0000O000O0O00 =Toplevel ()#line:766
    OOOO0000O000O0O00 .title ("单品分析")#line:767
    OOO0O0OO0OOOO0O0O =OOOO0000O000O0O00 .winfo_screenwidth ()#line:768
    OOOOO000OOOOO00OO =OOOO0000O000O0O00 .winfo_screenheight ()#line:770
    OO000OOOOOOOO00O0 =580 #line:772
    OOO0OOO0OOOO0000O =80 #line:773
    O00O00OOO00OOOOOO =(OOO0O0OO0OOOO0O0O -OO000OOOOOOOO00O0 )/1.7 #line:775
    OOOOOOOO0OOO0O0O0 =(OOOOO000OOOOO00OO -OOO0OOO0OOOO0000O )/2 #line:776
    OOOO0000O000O0O00 .geometry ("%dx%d+%d+%d"%(OO000OOOOOOOO00O0 ,OOO0OOO0OOOO0000O ,O00O00OOO00OOOOOO ,OOOOOOOO0OOO0O0O0 ))#line:777
    OO0000O00O0O0OO0O =Label (OOOO0000O000O0O00 ,text ="作用对象：")#line:780
    OO0000O00O0O0OO0O .grid (row =1 ,column =0 ,sticky ="w")#line:781
    O000OOOO0OO00OOO0 =StringVar ()#line:782
    OO0OOO0O00OO0OOO0 =ttk .Combobox (OOOO0000O000O0O00 ,width =25 ,height =10 ,state ="readonly",textvariable =O000OOOO0OO00OOO0 )#line:785
    OO0OOO0O00OO0OOO0 ["values"]=list (set (TT_ori ["作用对象"].to_list ()))#line:786
    OO0OOO0O00OO0OOO0 .current (0 )#line:787
    OO0OOO0O00OO0OOO0 .grid (row =1 ,column =1 )#line:788
    O000O00O00O00000O =Label (OOOO0000O000O0O00 ,text ="分析对象：")#line:790
    O000O00O00O00000O .grid (row =1 ,column =2 ,sticky ="w")#line:791
    OOO0OOO0OOO0O00O0 =StringVar ()#line:794
    OOO0O0OO00O0OO000 =ttk .Combobox (OOOO0000O000O0O00 ,width =15 ,height =10 ,state ="readonly",textvariable =OOO0OOO0OOO0O00O0 )#line:797
    OOO0O0OO00O0OO000 ["values"]=["事件发生月份","事件发生季度","产品批号","型号","规格"]#line:798
    OOO0O0OO00O0OO000 .current (0 )#line:800
    OOO0O0OO00O0OO000 .grid (row =1 ,column =3 )#line:801
    O00000OO00OOO0OOO =Label (OOOO0000O000O0O00 ,text ="事件发生起止时间：")#line:806
    O00000OO00OOO0OOO .grid (row =2 ,column =0 ,sticky ="w")#line:807
    OO0O0O0OOOO0O0000 =Entry (OOOO0000O000O0O00 ,width =10 )#line:809
    OO0O0O0OOOO0O0000 .insert (0 ,min (TT_ori ["事件发生日期"].dt .date ))#line:810
    OO0O0O0OOOO0O0000 .grid (row =2 ,column =1 ,sticky ="w")#line:811
    OOO0000000O0OO0OO =Entry (OOOO0000O000O0O00 ,width =10 )#line:813
    OOO0000000O0OO0OO .insert (0 ,max (TT_ori ["事件发生日期"].dt .date ))#line:814
    OOO0000000O0OO0OO .grid (row =2 ,column =2 ,sticky ="w")#line:815
    OOO00O000OO00O00O =Button (OOOO0000O000O0O00 ,text ="原始查看",width =10 ,bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :thread_it (Tread_TOOLS_doing ,TT_ori ,OO0OOO0O00OO0OOO0 .get (),OOO0O0OO00O0OO000 .get (),OO0O0O0OOOO0O0000 .get (),OOO0000000O0OO0OO .get (),1 ))#line:825
    OOO00O000OO00O00O .grid (row =3 ,column =2 ,sticky ="w")#line:826
    OOO00O000OO00O00O =Button (OOOO0000O000O0O00 ,text ="分类查看",width =10 ,bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :thread_it (Tread_TOOLS_doing ,TT_ori ,OO0OOO0O00OO0OOO0 .get (),OOO0O0OO00O0OO000 .get (),OO0O0O0OOOO0O0000 .get (),OOO0000000O0OO0OO .get (),0 ))#line:836
    OOO00O000OO00O00O .grid (row =3 ,column =3 ,sticky ="w")#line:837
    OOO00O000OO00O00O =Button (OOOO0000O000O0O00 ,text ="趋势分析",width =10 ,bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :thread_it (Tread_TOOLS_doing ,TT_ori ,OO0OOO0O00OO0OOO0 .get (),OOO0O0OO00O0OO000 .get (),OO0O0O0OOOO0O0000 .get (),OOO0000000O0OO0OO .get (),2 ))#line:847
    OOO00O000OO00O00O .grid (row =3 ,column =1 ,sticky ="w")#line:848
def Tread_TOOLS_doing (O0OOOOOO0O000O000 ,O0O00OOOO0O0O0000 ,OOO0OOOO00000OOOO ,O0OO0OO0O0O0OO0O0 ,O0000OO0000O0O000 ,OOO0000OO0O00O0O0 ):#line:850
    ""#line:851
    global TT_biaozhun #line:852
    O0OOOOOO0O000O000 =O0OOOOOO0O000O000 [(O0OOOOOO0O000O000 ["作用对象"]==O0O00OOOO0O0O0000 )].copy ()#line:853
    O0OO0OO0O0O0OO0O0 =pd .to_datetime (O0OO0OO0O0O0OO0O0 )#line:855
    O0000OO0000O0O000 =pd .to_datetime (O0000OO0000O0O000 )#line:856
    O0OOOOOO0O000O000 =O0OOOOOO0O000O000 [((O0OOOOOO0O000O000 ["事件发生日期"]>=O0OO0OO0O0O0OO0O0 )&(O0OOOOOO0O000O000 ["事件发生日期"]<=O0000OO0000O0O000 ))]#line:857
    text .insert (END ,"\n数据数量："+str (len (O0OOOOOO0O000O000 )))#line:858
    text .see (END )#line:859
    if OOO0000OO0O00O0O0 ==0 :#line:861
        Tread_TOOLS_check (O0OOOOOO0O000O000 ,TT_biaozhun ["关键字表"],0 )#line:862
        return 0 #line:863
    if OOO0000OO0O00O0O0 ==1 :#line:864
        Tread_TOOLS_tree_Level_2 (O0OOOOOO0O000O000 ,1 ,O0OOOOOO0O000O000 )#line:865
        return 0 #line:866
    if len (O0OOOOOO0O000O000 )<1 :#line:867
        showinfo (title ="错误信息",message ="没有符合筛选条件的报告。")#line:868
        return 0 #line:869
    Tread_TOOLS_check (O0OOOOOO0O000O000 ,TT_biaozhun ["关键字表"],1 )#line:870
    Tread_TOOLS_tree_Level_2 (Tread_TOOLS_Countall (O0OOOOOO0O000O000 ).df_find_all_keword_risk (OOO0OOOO00000OOOO ),1 ,0 ,OOO0OOOO00000OOOO )#line:873
def STAT_countx (OOOOO00OO000OO00O ):#line:883
    ""#line:884
    return OOOOO00OO000OO00O .value_counts ().to_dict ()#line:885
def STAT_countpx (O0O00OOO000O0O00O ,OOOO00OOO00OOOOO0 ):#line:887
    ""#line:888
    return len (O0O00OOO000O0O00O [(O0O00OOO000O0O00O ==OOOO00OOO00OOOOO0 )])#line:889
def STAT_countnpx (OO00O0O00O00OOOOO ,O0OO0OO00OOO00OO0 ):#line:891
    ""#line:892
    return len (OO00O0O00O00OOOOO [(OO00O0O00O00OOOOO not in O0OO0OO00OOO00OO0 )])#line:893
def STAT_get_max (OO0000000O0O0O00O ):#line:895
    ""#line:896
    return OO0000000O0O0O00O .value_counts ().max ()#line:897
def STAT_get_mean (OOOOO00O0O000000O ):#line:899
    ""#line:900
    return round (OOOOO00O0O000000O .value_counts ().mean (),2 )#line:901
def STAT_get_std (OOOO000OOOOOO0000 ):#line:903
    ""#line:904
    return round (OOOO000OOOOOO0000 .value_counts ().std (ddof =1 ),2 )#line:905
def STAT_get_95ci (O000O000O00OO0000 ):#line:907
    ""#line:908
    return round (np .percentile (O000O000O00OO0000 .value_counts (),97.5 ),2 )#line:909
def STAT_get_mean_std_ci (OO0OO0O0O0O000O0O ,OOO0O00OO0O00O0OO ):#line:911
    ""#line:912
    warnings .filterwarnings ("ignore")#line:913
    OO00O0O00OOO0OO00 =TOOLS_strdict_to_pd (str (OO0OO0O0O0O000O0O ))["content"].values /OOO0O00OO0O00O0OO #line:914
    OO0O000O00OOOO000 =round (OO00O0O00OOO0OO00 .mean (),2 )#line:915
    O00O0O000O00O000O =round (OO00O0O00OOO0OO00 .std (ddof =1 ),2 )#line:916
    OOOOO0OO0000O0000 =round (np .percentile (OO00O0O00OOO0OO00 ,97.5 ),2 )#line:917
    return pd .Series ((OO0O000O00OOOO000 ,O00O0O000O00O000O ,OOOOO0OO0000O0000 ))#line:918
def STAT_findx_value (OO000000OOOO00000 ,OOOOO0O0O0O000OOO ):#line:920
    ""#line:921
    warnings .filterwarnings ("ignore")#line:922
    O00OOO0OO00OOO00O =TOOLS_strdict_to_pd (str (OO000000OOOO00000 ))#line:923
    O0OOO0O00O0OO0000 =O00OOO0OO00OOO00O .where (O00OOO0OO00OOO00O ["index"]==str (OOOOO0O0O0O000OOO ))#line:925
    print (O0OOO0O00O0OO0000 )#line:926
    return O0OOO0O00O0OO0000 #line:927
def STAT_judge_x (OO0O0O000000O00OO ,OOO0000O0OOO000OO ):#line:929
    ""#line:930
    for OO0O0OOO0000O000O in OOO0000O0OOO000OO :#line:931
        if OO0O0O000000O00OO .find (OO0O0OOO0000O000O )>-1 :#line:932
            return 1 #line:933
def STAT_basic_risk (OOOO0000OOO00O000 ,O00OOO0O00OO0OO0O ,OO000O0O000000000 ,OO0O00OOO00OOOOOO ,O00OO0O0O00OO0OO0 ):#line:936
    ""#line:937
    OOOO0000OOO00O000 ["风险评分"]=0 #line:938
    OOOO0000OOO00O000 .loc [((OOOO0000OOO00O000 [O00OOO0O00OO0OO0O ]>=3 )&(OOOO0000OOO00O000 [OO000O0O000000000 ]>=1 ))|(OOOO0000OOO00O000 [O00OOO0O00OO0OO0O ]>=5 ),"风险评分"]=OOOO0000OOO00O000 ["风险评分"]+5 #line:939
    OOOO0000OOO00O000 .loc [(OOOO0000OOO00O000 [OO000O0O000000000 ]>=3 ),"风险评分"]=OOOO0000OOO00O000 ["风险评分"]+1 #line:940
    OOOO0000OOO00O000 .loc [(OOOO0000OOO00O000 [OO0O00OOO00OOOOOO ]>=1 ),"风险评分"]=OOOO0000OOO00O000 ["风险评分"]+10 #line:941
    OOOO0000OOO00O000 ["风险评分"]=OOOO0000OOO00O000 ["风险评分"]+OOOO0000OOO00O000 [O00OO0O0O00OO0OO0 ]/100 #line:942
    return OOOO0000OOO00O000 #line:943
def STAT_find_keyword_risk (O00OOO0000O000O00 ,OO0O0O00OO0OO0O0O ,O00OO0OOO0O0O0O00 ,OO0OOOO00OOO0OOO0 ,O0O0O0OO000O0OOOO ):#line:947
        ""#line:948
        O00OOOO0000OOO000 =O00OOO0000O000O00 .groupby (OO0O0O00OO0OO0O0O ).agg (证号关键字总数量 =(O00OO0OOO0O0O0O00 ,"count"),包含元素个数 =(OO0OOOO00OOO0OOO0 ,"nunique"),包含元素 =(OO0OOOO00OOO0OOO0 ,STAT_countx ),).reset_index ()#line:953
        O0OOO0O000O0OOOOO =OO0O0O00OO0OO0O0O .copy ()#line:955
        O0OOO0O000O0OOOOO .append (OO0OOOO00OOO0OOO0 )#line:956
        OO0O0O0O0000OOOOO =O00OOO0000O000O00 .groupby (O0OOO0O000O0OOOOO ).agg (计数 =(OO0OOOO00OOO0OOO0 ,"count"),).reset_index ()#line:959
        OO00O0OO00O0O0O00 =O0OOO0O000O0OOOOO .copy ()#line:962
        OO00O0OO00O0O0O00 .remove ("关键字")#line:963
        O0OOOOO00OOO0OO0O =O00OOO0000O000O00 .groupby (OO00O0OO00O0O0O00 ).agg (该元素总数 =(OO0OOOO00OOO0OOO0 ,"count"),).reset_index ()#line:966
        OO0O0O0O0000OOOOO ["证号总数"]=O0O0O0OO000O0OOOO #line:968
        OOO0O000000OO0OOO =pd .merge (OO0O0O0O0000OOOOO ,O00OOOO0000OOO000 ,on =OO0O0O00OO0OO0O0O ,how ="left")#line:969
        if len (OOO0O000000OO0OOO )>0 :#line:971
            OOO0O000000OO0OOO [['数量均值','数量标准差','数量CI']]=OOO0O000000OO0OOO .包含元素 .apply (lambda O00OOOOO00OO000OO :STAT_get_mean_std_ci (O00OOOOO00OO000OO ,1 ))#line:972
        return OOO0O000000OO0OOO #line:973
def STAT_find_risk (O0O00O0OOO0OOOO0O ,O000O0OOOOOO00OOO ,O0OOO000OO00OO00O ,O0000O0O0O0O0OOOO ):#line:979
        ""#line:980
        OOO00O00OOO0OO0OO =O0O00O0OOO0OOOO0O .groupby (O000O0OOOOOO00OOO ).agg (证号总数量 =(O0OOO000OO00OO00O ,"count"),包含元素个数 =(O0000O0O0O0O0OOOO ,"nunique"),包含元素 =(O0000O0O0O0O0OOOO ,STAT_countx ),均值 =(O0000O0O0O0O0OOOO ,STAT_get_mean ),标准差 =(O0000O0O0O0O0OOOO ,STAT_get_std ),CI上限 =(O0000O0O0O0O0OOOO ,STAT_get_95ci ),).reset_index ()#line:988
        O00000O0OO0OO0O00 =O000O0OOOOOO00OOO .copy ()#line:990
        O00000O0OO0OO0O00 .append (O0000O0O0O0O0OOOO )#line:991
        OOO0O0OO0OO0O00O0 =O0O00O0OOO0OOOO0O .groupby (O00000O0OO0OO0O00 ).agg (计数 =(O0000O0O0O0O0OOOO ,"count"),严重伤害数 =("伤害",lambda OO0O0O000OO0O0OO0 :STAT_countpx (OO0O0O000OO0O0OO0 .values ,"严重伤害")),死亡数量 =("伤害",lambda OO0O0OO000O000000 :STAT_countpx (OO0O0OO000O000000 .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:998
        OOO0OOO0O00OOO0OO =pd .merge (OOO0O0OO0OO0O00O0 ,OOO00O00OOO0OO0OO ,on =O000O0OOOOOO00OOO ,how ="left")#line:1000
        OOO0OOO0O00OOO0OO ["风险评分"]=0 #line:1002
        OOO0OOO0O00OOO0OO ["报表类型"]="dfx_findrisk"+O0000O0O0O0O0OOOO #line:1003
        OOO0OOO0O00OOO0OO .loc [((OOO0OOO0O00OOO0OO ["计数"]>=3 )&(OOO0OOO0O00OOO0OO ["严重伤害数"]>=1 )|(OOO0OOO0O00OOO0OO ["计数"]>=5 )),"风险评分"]=OOO0OOO0O00OOO0OO ["风险评分"]+5 #line:1004
        OOO0OOO0O00OOO0OO .loc [(OOO0OOO0O00OOO0OO ["计数"]>=(OOO0OOO0O00OOO0OO ["均值"]+OOO0OOO0O00OOO0OO ["标准差"])),"风险评分"]=OOO0OOO0O00OOO0OO ["风险评分"]+1 #line:1005
        OOO0OOO0O00OOO0OO .loc [(OOO0OOO0O00OOO0OO ["计数"]>=OOO0OOO0O00OOO0OO ["CI上限"]),"风险评分"]=OOO0OOO0O00OOO0OO ["风险评分"]+1 #line:1006
        OOO0OOO0O00OOO0OO .loc [(OOO0OOO0O00OOO0OO ["严重伤害数"]>=3 )&(OOO0OOO0O00OOO0OO ["风险评分"]>=7 ),"风险评分"]=OOO0OOO0O00OOO0OO ["风险评分"]+1 #line:1007
        OOO0OOO0O00OOO0OO .loc [(OOO0OOO0O00OOO0OO ["死亡数量"]>=1 ),"风险评分"]=OOO0OOO0O00OOO0OO ["风险评分"]+10 #line:1008
        OOO0OOO0O00OOO0OO ["风险评分"]=OOO0OOO0O00OOO0OO ["风险评分"]+OOO0OOO0O00OOO0OO ["单位个数"]/100 #line:1009
        OOO0OOO0O00OOO0OO =OOO0OOO0O00OOO0OO .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:1010
        return OOO0OOO0O00OOO0OO #line:1012
def TOOLS_get_list (O00O0O0O00OOOOOOO ):#line:1014
    ""#line:1015
    O00O0O0O00OOOOOOO =str (O00O0O0O00OOOOOOO )#line:1016
    O000OOO000O00O000 =[]#line:1017
    O000OOO000O00O000 .append (O00O0O0O00OOOOOOO )#line:1018
    O000OOO000O00O000 =",".join (O000OOO000O00O000 )#line:1019
    O000OOO000O00O000 =O000OOO000O00O000 .split ("|")#line:1020
    OOO0000O0OOO00OO0 =O000OOO000O00O000 [:]#line:1021
    O000OOO000O00O000 =list (set (O000OOO000O00O000 ))#line:1022
    O000OOO000O00O000 .sort (key =OOO0000O0OOO00OO0 .index )#line:1023
    return O000OOO000O00O000 #line:1024
def TOOLS_get_list0 (OOO000000OO0O0OOO ,OO00OOO000000OO0O ,*O00O0000O0O000000 ):#line:1026
    ""#line:1027
    OOO000000OO0O0OOO =str (OOO000000OO0O0OOO )#line:1028
    if pd .notnull (OOO000000OO0O0OOO ):#line:1030
        try :#line:1031
            if "use("in str (OOO000000OO0O0OOO ):#line:1032
                O0000O00OOO0OO0O0 =OOO000000OO0O0OOO #line:1033
                O0OO0OO0OO0000O00 =re .compile (r"[(](.*?)[)]",re .S )#line:1034
                OOO0O0OO0O00O0O00 =re .findall (O0OO0OO0OO0000O00 ,O0000O00OOO0OO0O0 )#line:1035
                OOOOOO00O0O000000 =[]#line:1036
                if ").list"in OOO000000OO0O0OOO :#line:1037
                    O0OO00O000OO000OO ="配置表/"+str (OOO0O0OO0O00O0O00 [0 ])+".xls"#line:1038
                    OOOO000O0O000OOOO =pd .read_excel (O0OO00O000OO000OO ,sheet_name =OOO0O0OO0O00O0O00 [0 ],header =0 ,index_col =0 ).reset_index ()#line:1041
                    OOOO000O0O000OOOO ["检索关键字"]=OOOO000O0O000OOOO ["检索关键字"].astype (str )#line:1042
                    OOOOOO00O0O000000 =OOOO000O0O000OOOO ["检索关键字"].tolist ()+OOOOOO00O0O000000 #line:1043
                if ").file"in OOO000000OO0O0OOO :#line:1044
                    OOOOOO00O0O000000 =OO00OOO000000OO0O [OOO0O0OO0O00O0O00 [0 ]].astype (str ).tolist ()+OOOOOO00O0O000000 #line:1046
                try :#line:1049
                    if "报告类型-新的"in OO00OOO000000OO0O .columns :#line:1050
                        OOOOOO00O0O000000 =",".join (OOOOOO00O0O000000 )#line:1051
                        OOOOOO00O0O000000 =OOOOOO00O0O000000 .split (";")#line:1052
                        OOOOOO00O0O000000 =",".join (OOOOOO00O0O000000 )#line:1053
                        OOOOOO00O0O000000 =OOOOOO00O0O000000 .split ("；")#line:1054
                        OOOOOO00O0O000000 =[OOO00000000O0OO0O .replace ("（严重）","")for OOO00000000O0OO0O in OOOOOO00O0O000000 ]#line:1055
                        OOOOOO00O0O000000 =[O000000O00O00OO00 .replace ("（一般）","")for O000000O00O00OO00 in OOOOOO00O0O000000 ]#line:1056
                except :#line:1057
                    pass #line:1058
                OOOOOO00O0O000000 =",".join (OOOOOO00O0O000000 )#line:1061
                OOOOOO00O0O000000 =OOOOOO00O0O000000 .split ("、")#line:1062
                OOOOOO00O0O000000 =",".join (OOOOOO00O0O000000 )#line:1063
                OOOOOO00O0O000000 =OOOOOO00O0O000000 .split ("，")#line:1064
                OOOOOO00O0O000000 =",".join (OOOOOO00O0O000000 )#line:1065
                OOOOOO00O0O000000 =OOOOOO00O0O000000 .split (",")#line:1066
                O00OOO0OOOO000OOO =OOOOOO00O0O000000 [:]#line:1068
                try :#line:1069
                    if O00O0000O0O000000 [0 ]==1000 :#line:1070
                      pass #line:1071
                except :#line:1072
                      OOOOOO00O0O000000 =list (set (OOOOOO00O0O000000 ))#line:1073
                OOOOOO00O0O000000 .sort (key =O00OOO0OOOO000OOO .index )#line:1074
            else :#line:1076
                OOO000000OO0O0OOO =str (OOO000000OO0O0OOO )#line:1077
                OOOOOO00O0O000000 =[]#line:1078
                OOOOOO00O0O000000 .append (OOO000000OO0O0OOO )#line:1079
                OOOOOO00O0O000000 =",".join (OOOOOO00O0O000000 )#line:1080
                OOOOOO00O0O000000 =OOOOOO00O0O000000 .split ("、")#line:1081
                OOOOOO00O0O000000 =",".join (OOOOOO00O0O000000 )#line:1082
                OOOOOO00O0O000000 =OOOOOO00O0O000000 .split ("，")#line:1083
                OOOOOO00O0O000000 =",".join (OOOOOO00O0O000000 )#line:1084
                OOOOOO00O0O000000 =OOOOOO00O0O000000 .split (",")#line:1085
                O00OOO0OOOO000OOO =OOOOOO00O0O000000 [:]#line:1087
                try :#line:1088
                    if O00O0000O0O000000 [0 ]==1000 :#line:1089
                      OOOOOO00O0O000000 =list (set (OOOOOO00O0O000000 ))#line:1090
                except :#line:1091
                      pass #line:1092
                OOOOOO00O0O000000 .sort (key =O00OOO0OOOO000OOO .index )#line:1093
                OOOOOO00O0O000000 .sort (key =O00OOO0OOOO000OOO .index )#line:1094
        except ValueError2 :#line:1096
            showinfo (title ="提示信息",message ="创建单元格支持多个甚至表单（文件）传入的方法，返回一个经过整理的清单出错，任务终止。")#line:1097
            return False #line:1098
    return OOOOOO00O0O000000 #line:1100
def TOOLS_strdict_to_pd (OOOO00O0O000O0O00 ):#line:1101
    ""#line:1102
    return pd .DataFrame .from_dict (eval (OOOO00O0O000O0O00 ),orient ="index",columns =["content"]).reset_index ()#line:1103
def Tread_TOOLS_view_dict (O0O0O000OO0O00O00 ,O0000OOOO00O0OOO0 ):#line:1105
    ""#line:1106
    O0O0OOOO0000OOOO0 =Toplevel ()#line:1107
    O0O0OOOO0000OOOO0 .title ("查看数据")#line:1108
    O0O0OOOO0000OOOO0 .geometry ("700x500")#line:1109
    O0OO0O0O00000OOOO =Scrollbar (O0O0OOOO0000OOOO0 )#line:1111
    O0O0O0OO000OOO0OO =Text (O0O0OOOO0000OOOO0 ,height =100 ,width =150 )#line:1112
    O0OO0O0O00000OOOO .pack (side =RIGHT ,fill =Y )#line:1113
    O0O0O0OO000OOO0OO .pack ()#line:1114
    O0OO0O0O00000OOOO .config (command =O0O0O0OO000OOO0OO .yview )#line:1115
    O0O0O0OO000OOO0OO .config (yscrollcommand =O0OO0O0O00000OOOO .set )#line:1116
    if O0000OOOO00O0OOO0 ==1 :#line:1117
        O0O0O0OO000OOO0OO .insert (END ,O0O0O000OO0O00O00 )#line:1119
        O0O0O0OO000OOO0OO .insert (END ,"\n\n")#line:1120
        return 0 #line:1121
    for OOOO00OOO0OO0000O in range (len (O0O0O000OO0O00O00 )):#line:1122
        O0O0O0OO000OOO0OO .insert (END ,O0O0O000OO0O00O00 .iloc [OOOO00OOO0OO0000O ,0 ])#line:1123
        O0O0O0OO000OOO0OO .insert (END ,":")#line:1124
        O0O0O0OO000OOO0OO .insert (END ,O0O0O000OO0O00O00 .iloc [OOOO00OOO0OO0000O ,1 ])#line:1125
        O0O0O0OO000OOO0OO .insert (END ,"\n\n")#line:1126
def Tread_TOOLS_fashenglv (OO000OOOOO000O00O ,O0000OO000O0OOO00 ):#line:1129
    global TT_biaozhun #line:1130
    OO000OOOOO000O00O =pd .merge (OO000OOOOO000O00O ,TT_biaozhun [O0000OO000O0OOO00 ],on =[O0000OO000O0OOO00 ],how ="left").reset_index (drop =True )#line:1131
    O000O00OOO00O0O00 =OO000OOOOO000O00O ["使用次数"].mean ()#line:1133
    OO000OOOOO000O00O ["使用次数"]=OO000OOOOO000O00O ["使用次数"].fillna (int (O000O00OOO00O0O00 ))#line:1134
    O0O0O000OO0000OO0 =OO000OOOOO000O00O ["使用次数"][:-1 ].sum ()#line:1135
    OO000OOOOO000O00O .iloc [-1 ,-1 ]=O0O0O000OO0000OO0 #line:1136
    O000O0OOO000O0O0O =[OO0OO000OOOO000OO for OO0OO000OOOO000OO in OO000OOOOO000O00O .columns if (OO0OO000OOOO000OO not in ["使用次数",O0000OO000O0OOO00 ])]#line:1137
    for OO000OOOO0OOO0OOO ,O0O00OO00000OO0OO in OO000OOOOO000O00O .iterrows ():#line:1138
        for O00O00000O0O0000O in O000O0OOO000O0O0O :#line:1139
            OO000OOOOO000O00O .loc [OO000OOOO0OOO0OOO ,O00O00000O0O0000O ]=int (O0O00OO00000OO0OO [O00O00000O0O0000O ])/int (O0O00OO00000OO0OO ["使用次数"])#line:1140
    del OO000OOOOO000O00O ["使用次数"]#line:1141
    Tread_TOOLS_tree_Level_2 (OO000OOOOO000O00O ,1 ,1 ,O0000OO000O0OOO00 )#line:1142
def TOOLS_save_dict (OOOOOOOO00OO00OO0 ):#line:1144
    ""#line:1145
    OO00OOOOOOOO0OOOO =filedialog .asksaveasfilename (title =u"保存文件",initialfile ="【排序后的原始数据】.xls",defaultextension ="xls",filetypes =[("Excel 97-2003 工作簿","*.xls")],)#line:1151
    try :#line:1152
        OOOOOOOO00OO00OO0 ["详细描述T"]=OOOOOOOO00OO00OO0 ["详细描述T"].astype (str )#line:1153
    except :#line:1154
        pass #line:1155
    try :#line:1156
        OOOOOOOO00OO00OO0 ["报告编码"]=OOOOOOOO00OO00OO0 ["报告编码"].astype (str )#line:1157
    except :#line:1158
        pass #line:1159
    try :#line:1160
        O00OOOOOOO0O00O0O =re .search ("\【(.*?)\】",OO00OOOOOOOO0OOOO )#line:1161
        OOOOOOOO00OO00OO0 ["对象"]=O00OOOOOOO0O00O0O .group (1 )#line:1162
    except :#line:1163
        pass #line:1164
    O00OO0O000OO0O00O =pd .ExcelWriter (OO00OOOOOOOO0OOOO ,engine ="xlsxwriter")#line:1165
    OOOOOOOO00OO00OO0 .to_excel (O00OO0O000OO0O00O ,sheet_name ="字典数据")#line:1166
    O00OO0O000OO0O00O .close ()#line:1167
    showinfo (title ="提示",message ="文件写入成功。")#line:1168
def Tread_TOOLS_DRAW_histbar (OOOOO00OOOOO0O0OO ):#line:1172
    ""#line:1173
    O000O0O0OOO000OOO =Toplevel ()#line:1176
    O000O0O0OOO000OOO .title ("直方图")#line:1177
    O00O0O000O0000O0O =ttk .Frame (O000O0O0OOO000OOO ,height =20 )#line:1178
    O00O0O000O0000O0O .pack (side =TOP )#line:1179
    O0000OOOOOO00O0OO =Figure (figsize =(12 ,6 ),dpi =100 )#line:1181
    O0OO000OOOO0OO0OO =FigureCanvasTkAgg (O0000OOOOOO00O0OO ,master =O000O0O0OOO000OOO )#line:1182
    O0OO000OOOO0OO0OO .draw ()#line:1183
    O0OO000OOOO0OO0OO .get_tk_widget ().pack (expand =1 )#line:1184
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1186
    plt .rcParams ['axes.unicode_minus']=False #line:1187
    OO0OO00O0OOOO00OO =NavigationToolbar2Tk (O0OO000OOOO0OO0OO ,O000O0O0OOO000OOO )#line:1189
    OO0OO00O0OOOO00OO .update ()#line:1190
    O0OO000OOOO0OO0OO .get_tk_widget ().pack ()#line:1191
    O0OOOOOOOOOOO00OO =O0000OOOOOO00O0OO .add_subplot (111 )#line:1193
    O0OOOOOOOOOOO00OO .set_title ("直方图")#line:1195
    O0OOO00O0OO0OOO0O =OOOOO00OOOOO0O0OO .columns .to_list ()#line:1197
    O0OOO00O0OO0OOO0O .remove ("对象")#line:1198
    OO00OOOO0OOO0OO0O =np .arange (len (O0OOO00O0OO0OOO0O ))#line:1199
    for OOO0OOOOOOOOO000O in O0OOO00O0OO0OOO0O :#line:1203
        OOOOO00OOOOO0O0OO [OOO0OOOOOOOOO000O ]=OOOOO00OOOOO0O0OO [OOO0OOOOOOOOO000O ].astype (float )#line:1204
    OOOOO00OOOOO0O0OO ['数据']=OOOOO00OOOOO0O0OO [O0OOO00O0OO0OOO0O ].values .tolist ()#line:1206
    OO00000OO0O00OOO0 =0 #line:1207
    for O0OO00OO00O0O0OOO ,O00O0OOO0O00OO000 in OOOOO00OOOOO0O0OO .iterrows ():#line:1208
        O0OOOOOOOOOOO00OO .bar ([O00O0O0000OO00OO0 +OO00000OO0O00OOO0 for O00O0O0000OO00OO0 in OO00OOOO0OOO0OO0O ],OOOOO00OOOOO0O0OO .loc [O0OO00OO00O0O0OOO ,'数据'],label =O0OOO00O0OO0OOO0O ,width =0.1 )#line:1209
        for OOOO0OO000O00OO00 ,OO000OOOOOO00OO0O in zip ([OOOO0OOOO00OO000O +OO00000OO0O00OOO0 for OOOO0OOOO00OO000O in OO00OOOO0OOO0OO0O ],OOOOO00OOOOO0O0OO .loc [O0OO00OO00O0O0OOO ,'数据']):#line:1212
           O0OOOOOOOOOOO00OO .text (OOOO0OO000O00OO00 -0.015 ,OO000OOOOOO00OO0O +0.07 ,str (int (OO000OOOOOO00OO0O )),color ='black',size =8 )#line:1213
        OO00000OO0O00OOO0 =OO00000OO0O00OOO0 +0.1 #line:1215
    O0OOOOOOOOOOO00OO .set_xticklabels (OOOOO00OOOOO0O0OO .columns .to_list (),rotation =-90 ,fontsize =8 )#line:1217
    O0OOOOOOOOOOO00OO .legend (OOOOO00OOOOO0O0OO ["对象"])#line:1221
    O0OO000OOOO0OO0OO .draw ()#line:1224
def Tread_TOOLS_DRAW_make_risk_plot (O00OOO0OO00O00OO0 ,OO0OO00OO0OOOO0O0 ,OOOOO0O00OO0O00O0 ,OO0O0O00O0OOO0000 ,OO00O000OO0OO0O00 ):#line:1226
    ""#line:1227
    O0O00OO0O00O0O0O0 =Toplevel ()#line:1230
    O0O00OO0O00O0O0O0 .title (OO0O0O00O0OOO0000 )#line:1231
    OOOOOOO00O0000000 =ttk .Frame (O0O00OO0O00O0O0O0 ,height =20 )#line:1232
    OOOOOOO00O0000000 .pack (side =TOP )#line:1233
    O00OO0OOOO0OOO00O =Figure (figsize =(12 ,6 ),dpi =100 )#line:1235
    OO000OOO00OOO0OO0 =FigureCanvasTkAgg (O00OO0OOOO0OOO00O ,master =O0O00OO0O00O0O0O0 )#line:1236
    OO000OOO00OOO0OO0 .draw ()#line:1237
    OO000OOO00OOO0OO0 .get_tk_widget ().pack (expand =1 )#line:1238
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1240
    plt .rcParams ['axes.unicode_minus']=False #line:1241
    O00OOO0O0OOOOO0OO =NavigationToolbar2Tk (OO000OOO00OOO0OO0 ,O0O00OO0O00O0O0O0 )#line:1243
    O00OOO0O0OOOOO0OO .update ()#line:1244
    OO000OOO00OOO0OO0 .get_tk_widget ().pack ()#line:1245
    O000O00O00OOOOOO0 =O00OO0OOOO0OOO00O .add_subplot (111 )#line:1247
    O000O00O00OOOOOO0 .set_title (OO0O0O00O0OOO0000 )#line:1249
    O000OOOO0O0O0OO00 =O00OOO0OO00O00OO0 [OO0OO00OO0OOOO0O0 ]#line:1250
    if OO00O000OO0OO0O00 !=999 :#line:1253
        O000O00O00OOOOOO0 .set_xticklabels (O000OOOO0O0O0OO00 ,rotation =-90 ,fontsize =8 )#line:1254
    OO0O0000O00000O00 =range (0 ,len (O000OOOO0O0O0OO00 ),1 )#line:1257
    for O0000O0OO00OO00O0 in OOOOO0O00OO0O00O0 :#line:1262
        OOO000O0OOO00O0OO =O00OOO0OO00O00OO0 [O0000O0OO00OO00O0 ].astype (float )#line:1263
        if O0000O0OO00OO00O0 =="关注区域":#line:1265
            O000O00O00OOOOOO0 .plot (list (O000OOOO0O0O0OO00 ),list (OOO000O0OOO00O0OO ),label =str (O0000O0OO00OO00O0 ),color ="red")#line:1266
        else :#line:1267
            O000O00O00OOOOOO0 .plot (list (O000OOOO0O0O0OO00 ),list (OOO000O0OOO00O0OO ),label =str (O0000O0OO00OO00O0 ))#line:1268
        if OO00O000OO0OO0O00 ==100 :#line:1271
            for OO0O00OO0000OO0O0 ,OO000O00000OO0OOO in zip (O000OOOO0O0O0OO00 ,OOO000O0OOO00O0OO ):#line:1272
                if OO000O00000OO0OOO ==max (OOO000O0OOO00O0OO )and OO000O00000OO0OOO >=3 and len (OOOOO0O00OO0O00O0 )!=1 :#line:1273
                     O000O00O00OOOOOO0 .text (OO0O00OO0000OO0O0 ,OO000O00000OO0OOO ,(str (O0000O0OO00OO00O0 )+":"+str (int (OO000O00000OO0OOO ))),color ='black',size =8 )#line:1274
                if len (OOOOO0O00OO0O00O0 )==1 and OO000O00000OO0OOO >=0.01 :#line:1275
                     O000O00O00OOOOOO0 .text (OO0O00OO0000OO0O0 ,OO000O00000OO0OOO ,str (int (OO000O00000OO0OOO )),color ='black',size =8 )#line:1276
    if len (OOOOO0O00OO0O00O0 )==1 :#line:1286
        OO0OOO0000OOO0000 =O00OOO0OO00O00OO0 [OOOOO0O00OO0O00O0 ].astype (float ).values #line:1287
        O0O0O0OOOO0OO0OOO =OO0OOO0000OOO0000 .mean ()#line:1288
        O0O000OO0O00OO00O =OO0OOO0000OOO0000 .std ()#line:1289
        O0OO0O00000OO0OO0 =O0O0O0OOOO0OO0OOO +3 *O0O000OO0O00OO00O #line:1290
        O0O0OO00O0O000O0O =O0O000OO0O00OO00O -3 *O0O000OO0O00OO00O #line:1291
        O000O00O00OOOOOO0 .axhline (O0O0O0OOOO0OO0OOO ,color ='r',linestyle ='--',label ='Mean')#line:1293
        O000O00O00OOOOOO0 .axhline (O0OO0O00000OO0OO0 ,color ='g',linestyle ='--',label ='UCL(μ+3σ)')#line:1294
        O000O00O00OOOOOO0 .axhline (O0O0OO00O0O000O0O ,color ='g',linestyle ='--',label ='LCL(μ-3σ)')#line:1295
    O000O00O00OOOOOO0 .set_title ("控制图")#line:1297
    O000O00O00OOOOOO0 .set_xlabel ("项")#line:1298
    O00OO0OOOO0OOO00O .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:1299
    O000O0000OOOOO0OO =O000O00O00OOOOOO0 .get_position ()#line:1300
    O000O00O00OOOOOO0 .set_position ([O000O0000OOOOO0OO .x0 ,O000O0000OOOOO0OO .y0 ,O000O0000OOOOO0OO .width *0.7 ,O000O0000OOOOO0OO .height ])#line:1301
    O000O00O00OOOOOO0 .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:1302
    OOO0OOOO0000OO000 =StringVar ()#line:1305
    O0OOO000O0O0O00OO =ttk .Combobox (OOOOOOO00O0000000 ,width =15 ,textvariable =OOO0OOOO0000OO000 ,state ='readonly')#line:1306
    O0OOO000O0O0O00OO ['values']=OOOOO0O00OO0O00O0 #line:1307
    O0OOO000O0O0O00OO .pack (side =LEFT )#line:1308
    O0OOO000O0O0O00OO .current (0 )#line:1309
    OO0OO0OOOO0O00O00 =Button (OOOOOOO00O0000000 ,text ="控制图（单项）",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (O00OOO0OO00O00OO0 ,OO0OO00OO0OOOO0O0 ,[OO00OO00OOOOO0OOO for OO00OO00OOOOO0OOO in OOOOO0O00OO0O00O0 if OOO0OOOO0000OO000 .get ()in OO00OO00OOOOO0OOO ],OO0O0O00O0OOO0000 ,OO00O000OO0OO0O00 ))#line:1319
    OO0OO0OOOO0O00O00 .pack (side =LEFT ,anchor ="ne")#line:1320
    O0OO00OOOO00OO000 =Button (OOOOOOO00O0000000 ,text ="去除标记",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (O00OOO0OO00O00OO0 ,OO0OO00OO0OOOO0O0 ,OOOOO0O00OO0O00O0 ,OO0O0O00O0OOO0000 ,0 ))#line:1328
    O0OO00OOOO00OO000 .pack (side =LEFT ,anchor ="ne")#line:1330
    OO000OOO00OOO0OO0 .draw ()#line:1331
def Tread_TOOLS_draw (OO0OO0OOO000OO00O ,OOOO00O00OOO000O0 ,O00O0O0O0O00O0O00 ,OO0O00OOOOO000O0O ,O0O0O0OOOOO0OOOOO ):#line:1333
    ""#line:1334
    warnings .filterwarnings ("ignore")#line:1335
    OO000OOO0O0OO0OO0 =Toplevel ()#line:1336
    OO000OOO0O0OO0OO0 .title (OOOO00O00OOO000O0 )#line:1337
    OOOOO00O00000000O =ttk .Frame (OO000OOO0O0OO0OO0 ,height =20 )#line:1338
    OOOOO00O00000000O .pack (side =TOP )#line:1339
    OOOO0OO0O00OO00OO =Figure (figsize =(12 ,6 ),dpi =100 )#line:1341
    OO000OO00O00O0O0O =FigureCanvasTkAgg (OOOO0OO0O00OO00OO ,master =OO000OOO0O0OO0OO0 )#line:1342
    OO000OO00O00O0O0O .draw ()#line:1343
    OO000OO00O00O0O0O .get_tk_widget ().pack (expand =1 )#line:1344
    OOO00O000O0OO0OO0 =OOOO0OO0O00OO00OO .add_subplot (111 )#line:1345
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1347
    plt .rcParams ['axes.unicode_minus']=False #line:1348
    OO00OOO0O0000OO00 =NavigationToolbar2Tk (OO000OO00O00O0O0O ,OO000OOO0O0OO0OO0 )#line:1350
    OO00OOO0O0000OO00 .update ()#line:1351
    OO000OO00O00O0O0O .get_tk_widget ().pack ()#line:1353
    try :#line:1356
        OO0O0OO0O0O0O00OO =OO0OO0OOO000OO00O .columns #line:1357
        OO0OO0OOO000OO00O =OO0OO0OOO000OO00O .sort_values (by =OO0O00OOOOO000O0O ,ascending =[False ],na_position ="last")#line:1358
    except :#line:1359
        O00OOO000O0O00O0O =eval (OO0OO0OOO000OO00O )#line:1360
        O00OOO000O0O00O0O =pd .DataFrame .from_dict (O00OOO000O0O00O0O ,TT_orient =O00O0O0O0O00O0O00 ,columns =[OO0O00OOOOO000O0O ]).reset_index ()#line:1363
        OO0OO0OOO000OO00O =O00OOO000O0O00O0O .sort_values (by =OO0O00OOOOO000O0O ,ascending =[False ],na_position ="last")#line:1364
    if ("日期"in OOOO00O00OOO000O0 or "时间"in OOOO00O00OOO000O0 or "季度"in OOOO00O00OOO000O0 )and "饼图"not in O0O0O0OOOOO0OOOOO :#line:1368
        OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ]=pd .to_datetime (OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ],format ="%Y/%m/%d").dt .date #line:1369
        OO0OO0OOO000OO00O =OO0OO0OOO000OO00O .sort_values (by =O00O0O0O0O00O0O00 ,ascending =[True ],na_position ="last")#line:1370
    elif "批号"in OOOO00O00OOO000O0 :#line:1371
        OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ]=OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ].astype (str )#line:1372
        OO0OO0OOO000OO00O =OO0OO0OOO000OO00O .sort_values (by =O00O0O0O0O00O0O00 ,ascending =[True ],na_position ="last")#line:1373
        OOO00O000O0OO0OO0 .set_xticklabels (OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ],rotation =-90 ,fontsize =8 )#line:1374
    else :#line:1375
        OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ]=OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ].astype (str )#line:1376
        OOO00O000O0OO0OO0 .set_xticklabels (OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ],rotation =-90 ,fontsize =8 )#line:1377
    O0O0OO0O00000000O =OO0OO0OOO000OO00O [OO0O00OOOOO000O0O ]#line:1379
    O00000OO0000O0OOO =range (0 ,len (O0O0OO0O00000000O ),1 )#line:1380
    OOO00O000O0OO0OO0 .set_title (OOOO00O00OOO000O0 )#line:1382
    if O0O0O0OOOOO0OOOOO =="柱状图":#line:1386
        OOO00O000O0OO0OO0 .bar (x =OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ],height =O0O0OO0O00000000O ,width =0.2 ,color ="#87CEFA")#line:1387
    elif O0O0O0OOOOO0OOOOO =="饼图":#line:1388
        OOO00O000O0OO0OO0 .pie (x =O0O0OO0O00000000O ,labels =OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ],autopct ="%0.2f%%")#line:1389
    elif O0O0O0OOOOO0OOOOO =="折线图":#line:1390
        OOO00O000O0OO0OO0 .plot (OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ],O0O0OO0O00000000O ,lw =0.5 ,ls ='-',c ="r",alpha =0.5 )#line:1391
    elif "帕累托图"in str (O0O0O0OOOOO0OOOOO ):#line:1393
        O0000OOOO0O0OO0O0 =OO0OO0OOO000OO00O [OO0O00OOOOO000O0O ].fillna (0 )#line:1394
        OO0000O0O0OO00OO0 =O0000OOOO0O0OO0O0 .cumsum ()/O0000OOOO0O0OO0O0 .sum ()*100 #line:1398
        OO0OO0OOO000OO00O ["百分比"]=round (OO0OO0OOO000OO00O ["数量"]/O0000OOOO0O0OO0O0 .sum ()*100 ,2 )#line:1399
        OO0OO0OOO000OO00O ["累计百分比"]=round (OO0000O0O0OO00OO0 ,2 )#line:1400
        O00000OO0OO00OOO0 =OO0000O0O0OO00OO0 [OO0000O0O0OO00OO0 >0.8 ].index [0 ]#line:1401
        O00OO0O00O00OOOOO =O0000OOOO0O0OO0O0 .index .tolist ().index (O00000OO0OO00OOO0 )#line:1402
        OOO00O000O0OO0OO0 .bar (x =OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ],height =O0000OOOO0O0OO0O0 ,color ="C0",label =OO0O00OOOOO000O0O )#line:1406
        OOO0OO0OO0O00OOO0 =OOO00O000O0OO0OO0 .twinx ()#line:1407
        OOO0OO0OO0O00OOO0 .plot (OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ],OO0000O0O0OO00OO0 ,color ="C1",alpha =0.6 ,label ="累计比例")#line:1408
        OOO0OO0OO0O00OOO0 .yaxis .set_major_formatter (PercentFormatter ())#line:1409
        OOO00O000O0OO0OO0 .tick_params (axis ="y",colors ="C0")#line:1414
        OOO0OO0OO0O00OOO0 .tick_params (axis ="y",colors ="C1")#line:1415
        for OOOO000O0OO00O0OO ,O00OOO0O000000O0O ,OO0OOO0O00OOOO0O0 ,O000O00OOOOO00000 in zip (OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ],O0000OOOO0O0OO0O0 ,OO0OO0OOO000OO00O ["百分比"],OO0OO0OOO000OO00O ["累计百分比"]):#line:1417
            OOO00O000O0OO0OO0 .text (OOOO000O0OO00O0OO ,O00OOO0O000000O0O +0.1 ,str (int (O00OOO0O000000O0O ))+", "+str (int (OO0OOO0O00OOOO0O0 ))+"%,"+str (int (O000O00OOOOO00000 ))+"%",color ='black',size =8 )#line:1418
        if "超级帕累托图"in str (O0O0O0OOOOO0OOOOO ):#line:1421
            O000OOO000O000O0O =re .compile (r'[(](.*?)[)]',re .S )#line:1422
            O0000000O0O0OOOOO =re .findall (O000OOO000O000O0O ,O0O0O0OOOOO0OOOOO )[0 ]#line:1423
            OOO00O000O0OO0OO0 .bar (x =OO0OO0OOO000OO00O [O00O0O0O0O00O0O00 ],height =OO0OO0OOO000OO00O [O0000000O0O0OOOOO ],color ="orangered",label =O0000000O0O0OOOOO )#line:1424
    OOOO0OO0O00OO00OO .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:1429
    O000O00OOOO000O0O =OOO00O000O0OO0OO0 .get_position ()#line:1430
    OOO00O000O0OO0OO0 .set_position ([O000O00OOOO000O0O .x0 ,O000O00OOOO000O0O .y0 ,O000O00OOOO000O0O .width *0.7 ,O000O00OOOO000O0O .height ])#line:1431
    OOO00O000O0OO0OO0 .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:1432
    OO000OO00O00O0O0O .draw ()#line:1435
    if len (O0O0OO0O00000000O )<=20 and O0O0O0OOOOO0OOOOO !="饼图"and O0O0O0OOOOO0OOOOO !="帕累托图":#line:1438
        for O0OO0O000OO00OOOO ,O00OOOOO00O0O00O0 in zip (O00000OO0000O0OOO ,O0O0OO0O00000000O ):#line:1439
            OO0OOO00O00O00000 =str (O00OOOOO00O0O00O0 )#line:1440
            OO0O0OOOO0OOO000O =(O0OO0O000OO00OOOO ,O00OOOOO00O0O00O0 +0.3 )#line:1441
            OOO00O000O0OO0OO0 .annotate (OO0OOO00O00O00000 ,xy =OO0O0OOOO0OOO000O ,fontsize =8 ,color ="black",ha ="center",va ="baseline")#line:1442
    O0000000O000000O0 =Button (OOOOO00O00000000O ,relief =GROOVE ,activebackground ="green",text ="保存原始数据",command =lambda :TOOLS_save_dict (OO0OO0OOO000OO00O ),)#line:1452
    O0000000O000000O0 .pack (side =RIGHT )#line:1453
    O0O0O0OOOOOO0OOOO =Button (OOOOO00O00000000O ,relief =GROOVE ,text ="查看原始数据",command =lambda :Tread_TOOLS_view_dict (OO0OO0OOO000OO00O ,1 ))#line:1457
    O0O0O0OOOOOO0OOOO .pack (side =RIGHT )#line:1458
    OO0O00OOOO0O0OO0O =Button (OOOOO00O00000000O ,relief =GROOVE ,text ="饼图",command =lambda :Tread_TOOLS_draw (OO0OO0OOO000OO00O ,OOOO00O00OOO000O0 ,O00O0O0O0O00O0O00 ,OO0O00OOOOO000O0O ,"饼图"),)#line:1466
    OO0O00OOOO0O0OO0O .pack (side =LEFT )#line:1467
    OO0O00OOOO0O0OO0O =Button (OOOOO00O00000000O ,relief =GROOVE ,text ="柱状图",command =lambda :Tread_TOOLS_draw (OO0OO0OOO000OO00O ,OOOO00O00OOO000O0 ,O00O0O0O0O00O0O00 ,OO0O00OOOOO000O0O ,"柱状图"),)#line:1474
    OO0O00OOOO0O0OO0O .pack (side =LEFT )#line:1475
    OO0O00OOOO0O0OO0O =Button (OOOOO00O00000000O ,relief =GROOVE ,text ="折线图",command =lambda :Tread_TOOLS_draw (OO0OO0OOO000OO00O ,OOOO00O00OOO000O0 ,O00O0O0O0O00O0O00 ,OO0O00OOOOO000O0O ,"折线图"),)#line:1481
    OO0O00OOOO0O0OO0O .pack (side =LEFT )#line:1482
    OO0O00OOOO0O0OO0O =Button (OOOOO00O00000000O ,relief =GROOVE ,text ="帕累托图",command =lambda :Tread_TOOLS_draw (OO0OO0OOO000OO00O ,OOOO00O00OOO000O0 ,O00O0O0O0O00O0O00 ,OO0O00OOOOO000O0O ,"帕累托图"),)#line:1489
    OO0O00OOOO0O0OO0O .pack (side =LEFT )#line:1490
def helper ():#line:1496
    ""#line:1497
    OOOO000O00O0000OO =Toplevel ()#line:1498
    OOOO000O00O0000OO .title ("程序使用帮助")#line:1499
    OOOO000O00O0000OO .geometry ("700x500")#line:1500
    O0OOO0O0OO0O0000O =Scrollbar (OOOO000O00O0000OO )#line:1502
    O0OOO00O000O0OOOO =Text (OOOO000O00O0000OO ,height =80 ,width =150 ,bg ="#FFFFFF",font ="微软雅黑")#line:1503
    O0OOO0O0OO0O0000O .pack (side =RIGHT ,fill =Y )#line:1504
    O0OOO00O000O0OOOO .pack ()#line:1505
    O0OOO0O0OO0O0000O .config (command =O0OOO00O000O0OOOO .yview )#line:1506
    O0OOO00O000O0OOOO .config (yscrollcommand =O0OOO0O0OO0O0000O .set )#line:1507
    O0OOO00O000O0OOOO .insert (END ,"\n  本程序用于趋势分析,供广东省内参与医疗器械警戒试点的企业免费使用。如您有相关问题或改进建议，请联系以下人员：\n\n    佛山市药品不良反应监测中心\n    蔡权周 \n    微信：18575757461 \n    邮箱：411703730@qq.com")#line:1512
    O0OOO00O000O0OOOO .config (state =DISABLED )#line:1513
def Tread_TOOLS_CLEAN (OOOO0O000O0OO00O0 ):#line:1517
        ""#line:1518
        OOOO0O000O0OO00O0 ["报告编码"]=OOOO0O000O0OO00O0 ["报告编码"].astype ("str")#line:1520
        OOOO0O000O0OO00O0 ["产品批号"]=OOOO0O000O0OO00O0 ["产品批号"].astype ("str")#line:1522
        OOOO0O000O0OO00O0 ["型号"]=OOOO0O000O0OO00O0 ["型号"].astype ("str")#line:1523
        OOOO0O000O0OO00O0 ["规格"]=OOOO0O000O0OO00O0 ["规格"].astype ("str")#line:1524
        OOOO0O000O0OO00O0 ["注册证编号/曾用注册证编号"]=OOOO0O000O0OO00O0 ["注册证编号/曾用注册证编号"].str .replace ("(","（",regex =False )#line:1526
        OOOO0O000O0OO00O0 ["注册证编号/曾用注册证编号"]=OOOO0O000O0OO00O0 ["注册证编号/曾用注册证编号"].str .replace (")","）",regex =False )#line:1527
        OOOO0O000O0OO00O0 ["注册证编号/曾用注册证编号"]=OOOO0O000O0OO00O0 ["注册证编号/曾用注册证编号"].str .replace ("*","※",regex =False )#line:1528
        OOOO0O000O0OO00O0 ["产品名称"]=OOOO0O000O0OO00O0 ["产品名称"].str .replace ("*","※",regex =False )#line:1530
        OOOO0O000O0OO00O0 ["产品批号"]=OOOO0O000O0OO00O0 ["产品批号"].str .replace ("(","（",regex =False )#line:1532
        OOOO0O000O0OO00O0 ["产品批号"]=OOOO0O000O0OO00O0 ["产品批号"].str .replace (")","）",regex =False )#line:1533
        OOOO0O000O0OO00O0 ["产品批号"]=OOOO0O000O0OO00O0 ["产品批号"].str .replace ("*","※",regex =False )#line:1534
        OOOO0O000O0OO00O0 ['事件发生日期']=pd .to_datetime (OOOO0O000O0OO00O0 ['事件发生日期'],format ='%Y-%m-%d',errors ='coerce')#line:1537
        OOOO0O000O0OO00O0 ["事件发生月份"]=OOOO0O000O0OO00O0 ["事件发生日期"].dt .to_period ("M").astype (str )#line:1541
        OOOO0O000O0OO00O0 ["事件发生季度"]=OOOO0O000O0OO00O0 ["事件发生日期"].dt .to_period ("Q").astype (str )#line:1542
        OOOO0O000O0OO00O0 ["注册证编号/曾用注册证编号"]=OOOO0O000O0OO00O0 ["注册证编号/曾用注册证编号"].fillna ("未填写")#line:1546
        OOOO0O000O0OO00O0 ["产品批号"]=OOOO0O000O0OO00O0 ["产品批号"].fillna ("未填写")#line:1547
        OOOO0O000O0OO00O0 ["型号"]=OOOO0O000O0OO00O0 ["型号"].fillna ("未填写")#line:1548
        OOOO0O000O0OO00O0 ["规格"]=OOOO0O000O0OO00O0 ["规格"].fillna ("未填写")#line:1549
        return OOOO0O000O0OO00O0 #line:1551
def thread_it (O0O0OOO000OO0O000 ,*OOO00O000OO0O0OO0 ):#line:1555
    ""#line:1556
    OOOOO0O0O000OO0OO =threading .Thread (target =O0O0OOO000OO0O000 ,args =OOO00O000OO0O0OO0 )#line:1558
    OOOOO0O0O000OO0OO .setDaemon (True )#line:1560
    OOOOO0O0O000OO0OO .start ()#line:1562
def showWelcome ():#line:1565
    ""#line:1566
    OOOOO0000O00O0000 =roox .winfo_screenwidth ()#line:1567
    O0OOOOO0O00OOO0OO =roox .winfo_screenheight ()#line:1569
    roox .overrideredirect (True )#line:1571
    roox .attributes ("-alpha",1 )#line:1572
    OO00O0O00O000O00O =(OOOOO0000O00O0000 -475 )/2 #line:1573
    OO0O0OOOOOOOO000O =(O0OOOOO0O00OOO0OO -200 )/2 #line:1574
    roox .geometry ("675x140+%d+%d"%(OO00O0O00O000O00O ,OO0O0OOOOOOOO000O ))#line:1576
    roox ["bg"]="royalblue"#line:1577
    O0O0000O00O00000O =Label (roox ,text ="医疗器械警戒趋势分析工具",fg ="white",bg ="royalblue",font =("微软雅黑",20 ))#line:1580
    O0O0000O00O00000O .place (x =0 ,y =15 ,width =675 ,height =90 )#line:1581
    OO00OOO0OO0000OO0 =Label (roox ,text ="Trend Analysis Tools V"+str (version_now ),fg ="white",bg ="cornflowerblue",font =("微软雅黑",15 ),)#line:1588
    OO00OOO0OO0000OO0 .place (x =0 ,y =90 ,width =675 ,height =50 )#line:1589
def closeWelcome ():#line:1592
    ""#line:1593
    for OOO00000000OO0000 in range (2 ):#line:1594
        root .attributes ("-alpha",0 )#line:1595
        time .sleep (1 )#line:1596
    root .attributes ("-alpha",1 )#line:1597
    roox .destroy ()#line:1598
if __name__ =='__main__':#line:1602
    pass #line:1603
root =Tk ()#line:1604
root .title ("医疗器械警戒趋势分析工具Trend Analysis Tools V"+str (version_now ))#line:1605
sw_root =root .winfo_screenwidth ()#line:1606
sh_root =root .winfo_screenheight ()#line:1608
ww_root =700 #line:1610
wh_root =620 #line:1611
x_root =(sw_root -ww_root )/2 #line:1613
y_root =(sh_root -wh_root )/2 #line:1614
root .geometry ("%dx%d+%d+%d"%(ww_root ,wh_root ,x_root ,y_root ))#line:1615
root .configure (bg ="steelblue")#line:1616
try :#line:1619
    frame0 =ttk .Frame (root ,width =100 ,height =20 )#line:1620
    frame0 .pack (side =LEFT )#line:1621
    B_open_files1 =Button (frame0 ,text ="导入原始数据",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_fileopen ,0 ),)#line:1634
    B_open_files1 .pack ()#line:1635
    B_open_files3 =Button (frame0 ,text ="导入分析规则",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_fileopen ,1 ),)#line:1648
    B_open_files3 .pack ()#line:1649
    B_open_files3 =Button (frame0 ,text ="趋势统计分析",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_analysis ,0 ),)#line:1664
    B_open_files3 .pack ()#line:1665
    B_open_files3 =Button (frame0 ,text ="直方图（数量）",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_bar ,"数量"))#line:1678
    B_open_files3 .pack ()#line:1679
    B_open_files3 =Button (frame0 ,text ="直方图（占比）",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_bar ,"百分比"))#line:1690
    B_open_files3 .pack ()#line:1691
    B_open_files3 =Button (frame0 ,text ="查看帮助文件",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (helper ))#line:1702
    B_open_files3 .pack ()#line:1703
    B_open_files3 =Button (frame0 ,text ="更改用户分组",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (display_random_number ))#line:1714
    B_open_files3 .pack ()#line:1715
except :#line:1716
    pass #line:1717
text =ScrolledText (root ,height =400 ,width =400 ,bg ="#FFFFFF",font ="微软雅黑")#line:1721
text .pack ()#line:1722
text .insert (END ,"\n  本程序用于趋势分析,供广东省内参与医疗器械警戒试点的企业免费使用。如您有相关问题或改进建议，请联系以下人员：\n\n    佛山市药品不良反应监测中心\n    蔡权周 \n    微信：18575757461 \n    邮箱：411703730@qq.com")#line:1727
text .insert (END ,"\n\n")#line:1728
def A000 ():#line:1730
    pass #line:1731
setting_cfg =read_setting_cfg ()#line:1735
generate_random_file ()#line:1736
setting_cfg =open_setting_cfg ()#line:1737
if setting_cfg ["settingdir"]==0 :#line:1738
    showinfo (title ="提示",message ="未发现默认配置文件夹，请选择一个。如该配置文件夹中并无配置文件，将生成默认配置文件。")#line:1739
    filepathu =filedialog .askdirectory ()#line:1740
    path =get_directory_path (filepathu )#line:1741
    update_setting_cfg ("settingdir",path )#line:1742
setting_cfg =open_setting_cfg ()#line:1743
random_number =int (setting_cfg ["sidori"])#line:1744
input_number =int (str (setting_cfg ["sidfinal"])[0 :6 ])#line:1745
day_end =convert_and_compare_dates (str (setting_cfg ["sidfinal"])[6 :14 ])#line:1746
sid =random_number *2 +183576 #line:1747
if input_number ==sid and day_end =="未过期":#line:1748
    usergroup ="用户组=1"#line:1749
    text .insert (END ,usergroup +"   有效期至：")#line:1750
    text .insert (END ,datetime .strptime (str (int (int (str (setting_cfg ["sidfinal"])[6 :14 ])/4 )),"%Y%m%d"))#line:1751
else :#line:1752
    text .insert (END ,usergroup )#line:1753
text .insert (END ,"\n配置文件路径："+setting_cfg ["settingdir"]+"\n")#line:1754
roox =Toplevel ()#line:1758
tMain =threading .Thread (target =showWelcome )#line:1759
tMain .start ()#line:1760
t1 =threading .Thread (target =closeWelcome )#line:1761
t1 .start ()#line:1762
root .lift ()#line:1766
root .attributes ("-topmost",True )#line:1767
root .attributes ("-topmost",False )#line:1768
root .mainloop ()#line:1769
