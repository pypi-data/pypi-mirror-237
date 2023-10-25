#!/usr/bin/env python
# coding: utf-8
# 阅易评
# 开发人：蔡权周，张博涵
import warnings #line:10
import traceback #line:11
import re #line:12
import xlrd #line:13
import xlwt #line:14
import openpyxl #line:15
import pandas as pd #line:16
import numpy as np #line:17
import math #line:18
import tkinter as Tk #line:19
from tkinter import ttk #line:20
from tkinter import *#line:21
import tkinter .font as tkFont #line:22
from tkinter import filedialog ,dialog ,PhotoImage #line:23
from tkinter .messagebox import showinfo #line:24
from tkinter .scrolledtext import ScrolledText #line:25
import collections #line:26
from collections import Counter #line:27
import datetime #line:28
from datetime import datetime ,timedelta #line:29
from tkinter import END #line:30
import xlsxwriter #line:31
import os #line:32
import time #line:33
import threading #line:34
import matplotlib as plt #line:35
from matplotlib .backends .backend_tkagg import FigureCanvasTkAgg #line:36
from matplotlib .figure import Figure #line:37
from matplotlib .backends .backend_tkagg import NavigationToolbar2Tk #line:38
global ori #line:41
global biaozhun #line:42
global dishi #line:43
biaozhun =""#line:44
dishi =""#line:45
ori =0 #line:46
global modex #line:47
modex =""#line:48
import random #line:50
import requests #line:51
global version_now #line:52
global usergroup #line:53
global setting_cfg #line:54
global csdir #line:55
global peizhidir #line:56
version_now ="0.0.15"#line:57
usergroup ="用户组=0"#line:58
setting_cfg =""#line:59
csdir =str (os .path .abspath (__file__ )).replace (str (__file__ ),"")#line:60
if csdir =="":#line:61
    csdir =str (os .path .dirname (__file__ ))#line:62
    csdir =csdir +csdir .split (package_name )[0 ][-1 ]#line:63
def extract_zip_file (OO0O0O0O00OO0OO00 ,O0000O0OO0O00OOO0 ):#line:71
    import zipfile #line:73
    if O0000O0OO0O00OOO0 =="":#line:74
        return 0 #line:75
    with zipfile .ZipFile (OO0O0O0O00OO0OO00 ,'r')as O0O00OOOOO000OOO0 :#line:76
        for OO00O00OO0O0O000O in O0O00OOOOO000OOO0 .infolist ():#line:77
            OO00O00OO0O0O000O .filename =OO00O00OO0O0O000O .filename .encode ('cp437').decode ('gbk')#line:79
            O0O00OOOOO000OOO0 .extract (OO00O00OO0O0O000O ,O0000O0OO0O00OOO0 )#line:80
def get_directory_path (O0OOO00O0OOO0OOO0 ):#line:86
    global csdir #line:88
    if not (os .path .isfile (os .path .join (O0OOO00O0OOO0OOO0 ,'0（范例）质量评估.xls'))):#line:90
        extract_zip_file (csdir +"def.py",O0OOO00O0OOO0OOO0 )#line:95
    if O0OOO00O0OOO0OOO0 =="":#line:97
        quit ()#line:98
    return O0OOO00O0OOO0OOO0 #line:99
def convert_and_compare_dates (OOO0000OOO000OO00 ):#line:103
    import datetime #line:104
    O00O0O0OO00OO0OO0 =datetime .datetime .now ()#line:105
    try :#line:107
       OOO0OOOOOOO00OO0O =datetime .datetime .strptime (str (int (int (OOO0000OOO000OO00 )/4 )),"%Y%m%d")#line:108
    except :#line:109
        print ("fail")#line:110
        return "已过期"#line:111
    if OOO0OOOOOOO00OO0O >O00O0O0OO00OO0OO0 :#line:113
        return "未过期"#line:115
    else :#line:116
        return "已过期"#line:117
def read_setting_cfg ():#line:119
    global csdir #line:120
    if os .path .exists (csdir +'setting.cfg'):#line:122
        text .insert (END ,"已完成初始化\n")#line:123
        with open (csdir +'setting.cfg','r')as O0O000OOOOOO0O0OO :#line:124
            O000000OO0OO00OO0 =eval (O0O000OOOOOO0O0OO .read ())#line:125
    else :#line:126
        O00OO00O000OO0000 =csdir +'setting.cfg'#line:128
        with open (O00OO00O000OO0000 ,'w')as O0O000OOOOOO0O0OO :#line:129
            O0O000OOOOOO0O0OO .write ('{"settingdir": 0, "sidori": 0, "sidfinal": "11111180000808"}')#line:130
        text .insert (END ,"未初始化，正在初始化...\n")#line:131
        O000000OO0OO00OO0 =read_setting_cfg ()#line:132
    return O000000OO0OO00OO0 #line:133
def open_setting_cfg ():#line:136
    global csdir #line:137
    with open (csdir +"setting.cfg","r")as OOO0OO0OOO0O0OO0O :#line:139
        OO000O00O00OOO0OO =eval (OOO0OO0OOO0O0OO0O .read ())#line:141
    return OO000O00O00OOO0OO #line:142
def update_setting_cfg (OOO0OO0OO000OO000 ,O00OO00OOOOO0O000 ):#line:144
    global csdir #line:145
    with open (csdir +"setting.cfg","r")as OO00O0O00OO000000 :#line:147
        O00OO0000OOO0O0O0 =eval (OO00O0O00OO000000 .read ())#line:149
    if O00OO0000OOO0O0O0 [OOO0OO0OO000OO000 ]==0 or O00OO0000OOO0O0O0 [OOO0OO0OO000OO000 ]=="11111180000808":#line:151
        O00OO0000OOO0O0O0 [OOO0OO0OO000OO000 ]=O00OO00OOOOO0O000 #line:152
        with open (csdir +"setting.cfg","w")as OO00O0O00OO000000 :#line:154
            OO00O0O00OO000000 .write (str (O00OO0000OOO0O0O0 ))#line:155
def generate_random_file ():#line:158
    OO0OOO0OO0O0O0O0O =random .randint (200000 ,299999 )#line:160
    update_setting_cfg ("sidori",OO0OOO0OO0O0O0O0O )#line:162
def display_random_number ():#line:164
    global csdir #line:165
    O00000OO000OO00OO =Toplevel ()#line:166
    O00000OO000OO00OO .title ("ID")#line:167
    OOOO0O000O0O0O000 =O00000OO000OO00OO .winfo_screenwidth ()#line:169
    OOOOO0OOO0OOOO0O0 =O00000OO000OO00OO .winfo_screenheight ()#line:170
    OO00O00O0000O000O =80 #line:172
    OO00OO0OOOO00OOOO =70 #line:173
    OOOOO00000O0O000O =(OOOO0O000O0O0O000 -OO00O00O0000O000O )/2 #line:175
    OOO000000OO0O000O =(OOOOO0OOO0OOOO0O0 -OO00OO0OOOO00OOOO )/2 #line:176
    O00000OO000OO00OO .geometry ("%dx%d+%d+%d"%(OO00O00O0000O000O ,OO00OO0OOOO00OOOO ,OOOOO00000O0O000O ,OOO000000OO0O000O ))#line:177
    with open (csdir +"setting.cfg","r")as O0OOOOO00OO0O0000 :#line:180
        O00000O00OO0OOO0O =eval (O0OOOOO00OO0O0000 .read ())#line:182
    OO0O0OO0O0OOO0O0O =int (O00000O00OO0OOO0O ["sidori"])#line:183
    OOOO00O0OO0O0O000 =OO0O0OO0O0OOO0O0O *2 +183576 #line:184
    print (OOOO00O0OO0O0O000 )#line:186
    O00OOO0OO000OO00O =ttk .Label (O00000OO000OO00OO ,text =f"机器码: {OO0O0OO0O0OOO0O0O}")#line:188
    OO00O0O00O000000O =ttk .Entry (O00000OO000OO00OO )#line:189
    O00OOO0OO000OO00O .pack ()#line:192
    OO00O0O00O000000O .pack ()#line:193
    ttk .Button (O00000OO000OO00OO ,text ="验证",command =lambda :check_input (OO00O0O00O000000O .get (),OOOO00O0OO0O0O000 )).pack ()#line:197
def check_input (OOO0OO000OOOOOOO0 ,OO00O0O00O000O0OO ):#line:199
    try :#line:203
        O0OO0O0OO0OOO0OOO =int (str (OOO0OO000OOOOOOO0 )[0 :6 ])#line:204
        OOO0O000O0OOOOOOO =convert_and_compare_dates (str (OOO0OO000OOOOOOO0 )[6 :14 ])#line:205
    except :#line:206
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:207
        return 0 #line:208
    if O0OO0O0OO0OOO0OOO ==OO00O0O00O000O0OO and OOO0O000O0OOOOOOO =="未过期":#line:210
        update_setting_cfg ("sidfinal",OOO0OO000OOOOOOO0 )#line:211
        showinfo (title ="提示",message ="注册成功,请重新启动程序。")#line:212
        quit ()#line:213
    else :#line:214
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:215
def update_software (OOOO0O0000O0OO000 ):#line:220
    global version_now #line:222
    text .insert (END ,"当前版本为："+version_now +",正在检查更新...(您可以同时执行分析任务)")#line:223
    try :#line:224
        OOOO0O000OOOOO0O0 =requests .get (f"https://pypi.org/pypi/{OOOO0O0000O0OO000}/json",timeout =2 ).json ()["info"]["version"]#line:225
    except :#line:226
        return "...更新失败。"#line:227
    if OOOO0O000OOOOO0O0 >version_now :#line:228
        text .insert (END ,"\n最新版本为："+OOOO0O000OOOOO0O0 +",正在尝试自动更新....")#line:229
        pip .main (['install',OOOO0O0000O0OO000 ,'--upgrade'])#line:231
        text .insert (END ,"\n您可以开展工作。")#line:232
        return "...更新成功。"#line:233
def Topentable (OOO0OO0O00OO0OO0O ):#line:236
    ""#line:237
    global ori #line:238
    global biaozhun #line:239
    global dishi #line:240
    OOO0O00OO0OOOO000 =[]#line:241
    OOO0O000OOOOO00OO =[]#line:242
    OOO00O000OOOOO000 =1 #line:243
    if OOO0OO0O00OO0OO0O ==123 :#line:246
        try :#line:247
            OOO000O0O000O0OOO =filedialog .askopenfilename (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:250
            biaozhun =pd .read_excel (OOO000O0O000O0OOO ,sheet_name =0 ,header =0 ,index_col =0 ).reset_index ()#line:253
        except :#line:254
            showinfo (title ="提示",message ="配置表文件有误或您没有选择。")#line:255
            return 0 #line:256
        try :#line:257
            dishi =pd .read_excel (OOO000O0O000O0OOO ,sheet_name ="地市清单",header =0 ,index_col =0 ).reset_index ()#line:260
        except :#line:261
            showinfo (title ="提示",message ="您选择的配置文件没有地市列表或您没有选择。")#line:262
            return 0 #line:263
        if ("评分项"in biaozhun .columns and "打分标准"in biaozhun .columns and "专家序号"not in biaozhun .columns ):#line:268
            text .insert (END ,"\n您使用自定义的配置表。")#line:269
            text .see (END )#line:270
            showinfo (title ="提示",message ="您将使用自定义的配置表。")#line:271
            return 0 #line:272
        else :#line:273
            showinfo (title ="提示",message ="配置表文件有误，请正确选择。")#line:274
            biaozhun =""#line:275
            return 0 #line:276
    try :#line:279
        if OOO0OO0O00OO0OO0O !=1 :#line:280
            OOOO0OOO000OOO0OO =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:283
        if OOO0OO0O00OO0OO0O ==1 :#line:284
            OOOO0OOO000OOO0OO =filedialog .askopenfilenames (filetypes =[("XLSX",".xlsx"),("XLS",".xls")])#line:287
            for OOOO0O000OOO00O0O in OOOO0OOO000OOO0OO :#line:288
                if ("●专家评分表"in OOOO0O000OOO00O0O )and ("●(最终评分需导入)被抽出的所有数据.xls"not in OOOO0O000OOO00O0O ):#line:289
                    OOO0O00OO0OOOO000 .append (OOOO0O000OOO00O0O )#line:290
                elif "●(最终评分需导入)被抽出的所有数据.xls"in OOOO0O000OOO00O0O :#line:291
                    OOO0O000OOOOO00OO .append (OOOO0O000OOO00O0O )#line:292
                    OOOO0O0O0OO000000 =OOOO0O000OOO00O0O .replace ("●(最终评分需导入)被抽出的所有数据","分数错误信息")#line:293
                    OOO00O000OOOOO000 =0 #line:294
            if OOO00O000OOOOO000 ==1 :#line:295
                showinfo (title ="提示",message ="请一并导入以下文件：●(最终评分需导入)被抽出的所有数据.xls")#line:297
                return 0 #line:298
            OOOO0OOO000OOO0OO =OOO0O00OO0OOOO000 #line:299
        O00O00OOO0OOOOO00 =[pd .read_excel (OOOOO000O00O000O0 ,header =0 ,sheet_name =0 )for OOOOO000O00O000O0 in OOOO0OOO000OOO0OO ]#line:302
        ori =pd .concat (O00O00OOO0OOOOO00 ,ignore_index =True ).drop_duplicates ().reset_index (drop =True )#line:303
        if "报告编码"in ori .columns or "报告表编码"in ori .columns :#line:305
            ori =ori .fillna ("-未填写-")#line:306
        if "报告类型-新的"in ori .columns :#line:309
            biaozhun =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="药品",header =0 ,index_col =0 ).reset_index ()#line:312
            ori ["报告编码"]=ori ["报告表编码"]#line:313
            text .insert (END ,"检测到导入的文件为药品报告，正在进行兼容性数据规整，请稍后...")#line:314
            ori =ori .rename (columns ={"医院名称":"单位名称"})#line:315
            ori =ori .rename (columns ={"报告地区名称":"使用单位、经营企业所属监测机构"})#line:316
            ori =ori .rename (columns ={"报告类型-严重程度":"伤害"})#line:317
            ori ["伤害"]=ori ["伤害"].str .replace ("一般","其他",regex =False )#line:318
            ori ["伤害"]=ori ["伤害"].str .replace ("严重","严重伤害",regex =False )#line:319
            ori .loc [(ori ["不良反应结果"]=="死亡"),"伤害"]="死亡"#line:320
            ori ["上报单位所属地区"]=ori ["使用单位、经营企业所属监测机构"]#line:321
            try :#line:322
                ori ["报告编码"]=ori ["唯一标识"]#line:323
            except :#line:324
                pass #line:325
            ori ["药品信息"]=""#line:329
            OOOO000000OO0OOOO =0 #line:330
            OOO0000OOOOO00O00 =len (ori ["报告编码"].drop_duplicates ())#line:331
            for O0OO00O0O00OO000O in ori ["报告编码"].drop_duplicates ():#line:332
                OOOO000000OO0OOOO =OOOO000000OO0OOOO +1 #line:333
                OO0O0000O00OOOOOO =round (OOOO000000OO0OOOO /OOO0000OOOOO00O00 ,2 )#line:334
                try :#line:335
                    change_schedule (OOOO000000OO0OOOO ,OOO0000OOOOO00O00 )#line:336
                except :#line:337
                    if OO0O0000O00OOOOOO in [0.10 ,0.20 ,0.30 ,0.40 ,0.50 ,0.60 ,0.70 ,0.80 ,0.90 ,0.99 ]:#line:338
                        text .insert (END ,OO0O0000O00OOOOOO )#line:339
                        text .insert (END ,"...")#line:340
                OO0O00000O0O000O0 =ori [(ori ["报告编码"]==O0OO00O0O00OO000O )].sort_values (by =["药品序号"]).reset_index ()#line:342
                for OOOO00OOOOO000000 ,OO00O0OO000OOO0O0 in OO0O00000O0O000O0 .iterrows ():#line:343
                    ori .loc [(ori ["报告编码"]==OO00O0OO000OOO0O0 ["报告编码"]),"药品信息"]=ori ["药品信息"]+"●药品序号："+str (OO00O0OO000OOO0O0 ["药品序号"])+" 性质："+str (OO00O0OO000OOO0O0 ["怀疑/并用"])+"\n批准文号:"+str (OO00O0OO000OOO0O0 ["批准文号"])+"\n商品名称："+str (OO00O0OO000OOO0O0 ["商品名称"])+"\n通用名称："+str (OO00O0OO000OOO0O0 ["通用名称"])+"\n剂型："+str (OO00O0OO000OOO0O0 ["剂型"])+"\n生产厂家："+str (OO00O0OO000OOO0O0 ["生产厂家"])+"\n生产批号："+str (OO00O0OO000OOO0O0 ["生产批号"])+"\n用量："+str (OO00O0OO000OOO0O0 ["用量"])+str (OO00O0OO000OOO0O0 ["用量单位"])+"，"+str (OO00O0OO000OOO0O0 ["用法-日"])+"日"+str (OO00O0OO000OOO0O0 ["用法-次"])+"次\n给药途径:"+str (OO00O0OO000OOO0O0 ["给药途径"])+"\n用药开始时间："+str (OO00O0OO000OOO0O0 ["用药开始时间"])+"\n用药终止时间："+str (OO00O0OO000OOO0O0 ["用药终止时间"])+"\n用药原因："+str (OO00O0OO000OOO0O0 ["用药原因"])+"\n"#line:344
            ori =ori .drop_duplicates ("报告编码")#line:345
        if "皮损部位"in ori .columns :#line:352
            biaozhun =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="化妆品",header =0 ,index_col =0 ).reset_index ()#line:355
            ori ["报告编码"]=ori ["报告表编号"]#line:356
            text .insert (END ,"检测到导入的文件为化妆品报告，正在进行兼容性数据规整，请稍后...")#line:357
            ori ["报告地区名称"]=ori ["报告单位名称"].astype (str )#line:359
            ori ["单位名称"]=ori ["报告单位名称"].astype (str )#line:361
            ori ["伤害"]=ori ["报告类型"].astype (str )#line:362
            ori ["伤害"]=ori ["伤害"].str .replace ("一般","其他",regex =False )#line:363
            ori ["伤害"]=ori ["伤害"].str .replace ("严重","严重伤害",regex =False )#line:364
            ori ["上报单位所属地区"]=ori ["报告地区名称"]#line:366
            try :#line:367
                ori ["报告编码"]=ori ["唯一标识"]#line:368
            except :#line:369
                pass #line:370
            text .insert (END ,"\n正在开展化妆品注册单位规整...")#line:371
            O00O000O00OOOO0O0 =pd .read_excel (peizhidir +"0（范例）注册单位.xlsx",sheet_name ="机构列表",header =0 ,index_col =0 ,).reset_index ()#line:372
            for OOOO00OOOOO000000 ,OO00O0OO000OOO0O0 in O00O000O00OOOO0O0 .iterrows ():#line:374
                ori .loc [(ori ["单位名称"]==OO00O0OO000OOO0O0 ["中文全称"]),"监测机构"]=OO00O0OO000OOO0O0 ["归属地区"]#line:375
                ori .loc [(ori ["单位名称"]==OO00O0OO000OOO0O0 ["中文全称"]),"市级监测机构"]=OO00O0OO000OOO0O0 ["地市"]#line:376
            ori ["监测机构"]=ori ["监测机构"].fillna ("未规整")#line:377
            ori ["市级监测机构"]=ori ["市级监测机构"].fillna ("未规整")#line:378
        try :#line:381
                text .insert (END ,"\n开展报告单位和监测机构名称规整...")#line:382
                OOOOOO00OOOO000O0 =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="报告单位",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:383
                O00O000O00OOOO0O0 =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="监测机构",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:384
                OOOO00OO0O00OO00O =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="地市清单",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:385
                for OOOO00OOOOO000000 ,OO00O0OO000OOO0O0 in OOOOOO00OOOO000O0 .iterrows ():#line:386
                        ori .loc [(ori ["单位名称"]==OO00O0OO000OOO0O0 ["曾用名1"]),"单位名称"]=OO00O0OO000OOO0O0 ["单位名称"]#line:387
                        ori .loc [(ori ["单位名称"]==OO00O0OO000OOO0O0 ["曾用名2"]),"单位名称"]=OO00O0OO000OOO0O0 ["单位名称"]#line:388
                        ori .loc [(ori ["单位名称"]==OO00O0OO000OOO0O0 ["曾用名3"]),"单位名称"]=OO00O0OO000OOO0O0 ["单位名称"]#line:389
                        ori .loc [(ori ["单位名称"]==OO00O0OO000OOO0O0 ["曾用名4"]),"单位名称"]=OO00O0OO000OOO0O0 ["单位名称"]#line:390
                        ori .loc [(ori ["单位名称"]==OO00O0OO000OOO0O0 ["曾用名5"]),"单位名称"]=OO00O0OO000OOO0O0 ["单位名称"]#line:391
                        ori .loc [(ori ["单位名称"]==OO00O0OO000OOO0O0 ["单位名称"]),"使用单位、经营企业所属监测机构"]=OO00O0OO000OOO0O0 ["监测机构"]#line:394
                for OOOO00OOOOO000000 ,OO00O0OO000OOO0O0 in O00O000O00OOOO0O0 .iterrows ():#line:396
                        ori .loc [(ori ["使用单位、经营企业所属监测机构"]==OO00O0OO000OOO0O0 ["曾用名1"]),"使用单位、经营企业所属监测机构"]=OO00O0OO000OOO0O0 ["监测机构"]#line:397
                        ori .loc [(ori ["使用单位、经营企业所属监测机构"]==OO00O0OO000OOO0O0 ["曾用名2"]),"使用单位、经营企业所属监测机构"]=OO00O0OO000OOO0O0 ["监测机构"]#line:398
                        ori .loc [(ori ["使用单位、经营企业所属监测机构"]==OO00O0OO000OOO0O0 ["曾用名3"]),"使用单位、经营企业所属监测机构"]=OO00O0OO000OOO0O0 ["监测机构"]#line:399
                for O00OOOOO000OO00O0 in OOOO00OO0O00OO00O ["地市列表"]:#line:401
                        ori .loc [(ori ["上报单位所属地区"].str .contains (O00OOOOO000OO00O0 ,na =False )),"市级监测机构"]=O00OOOOO000OO00O0 #line:402
                ori .loc [(ori ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构"]="佛山"#line:403
        except :#line:405
                text .insert (END ,"\n报告单位和监测机构名称规整失败.")#line:406
    except :#line:408
        showinfo (title ="提示",message ="导入文件错误,请重试。")#line:409
        return 0 #line:410
    try :#line:413
        ori =ori .loc [:,~ori .columns .str .contains ("Unnamed")]#line:414
    except :#line:415
        pass #line:416
    try :#line:417
        ori ["报告编码"]=ori ["报告编码"].astype (str )#line:418
    except :#line:419
        pass #line:420
    ori =ori .sample (frac =1 ).copy ()#line:423
    ori .reset_index (inplace =True )#line:424
    text .insert (END ,"\n数据读取成功，行数："+str (len (ori )))#line:425
    text .see (END )#line:426
    if OOO0OO0O00OO0OO0O ==0 :#line:429
        if "报告编码"not in ori .columns :#line:430
            showinfo (title ="提示信息",message ="\n在校验过程中，发现您导入的并非原始报告数据，请重新导入。")#line:431
        else :#line:432
            showinfo (title ="提示信息",message ="\n数据读取成功。")#line:433
        return 0 #line:434
    O00OO000O00OOO000 =ori .copy ()#line:437
    O000OO0OO0O0O0O0O ={}#line:438
    O0O0O0OO00000OOO0 =0 #line:439
    if "专家序号"not in O00OO000O00OOO000 .columns :#line:440
        showinfo (title ="提示信息",message ="您导入的并非专家评分文件，请重新导入。")#line:441
        return 0 #line:442
    for OOOO00OOOOO000000 ,OO00O0OO000OOO0O0 in O00OO000O00OOO000 .iterrows ():#line:443
        O0OOO000O00OO0O0O ="专家打分-"+str (OO00O0OO000OOO0O0 ["条目"])#line:444
        try :#line:445
            float (OO00O0OO000OOO0O0 ["评分"])#line:446
            float (OO00O0OO000OOO0O0 ["满分"])#line:447
        except :#line:448
            showinfo (title ="错误提示",message ="因专家评分或满分值输入的不是数字，导致了程序中止，请修正："+"专家序号："+str (int (OO00O0OO000OOO0O0 ["专家序号"]))+"，报告序号："+str (int (OO00O0OO000OOO0O0 ["序号"]))+OO00O0OO000OOO0O0 ["条目"],)#line:457
            ori =0 #line:458
        if float (OO00O0OO000OOO0O0 ["评分"])>float (OO00O0OO000OOO0O0 ["满分"])or float (OO00O0OO000OOO0O0 ["评分"])<0 :#line:459
            O000OO0OO0O0O0O0O [str (OOOO00OOOOO000000 )]=("专家序号："+str (int (OO00O0OO000OOO0O0 ["专家序号"]))+"；  报告序号："+str (int (OO00O0OO000OOO0O0 ["序号"]))+OO00O0OO000OOO0O0 ["条目"])#line:466
            O0O0O0OO00000OOO0 =1 #line:467
    if O0O0O0OO00000OOO0 ==1 :#line:469
        O00000OO0OOO00O00 =pd .DataFrame (list (O000OO0OO0O0O0O0O .items ()),columns =["错误编号","错误信息"])#line:470
        del O00000OO0OOO00O00 ["错误编号"]#line:471
        O0OO0O0OO0O000OOO =OOOO0O0O0OO000000 #line:472
        O00000OO0OOO00O00 =O00000OO0OOO00O00 .sort_values (by =["错误信息"],ascending =True ,na_position ="last")#line:473
        O00O00O0OOOO0000O =pd .ExcelWriter (O0OO0O0OO0O000OOO )#line:474
        O00000OO0OOO00O00 .to_excel (O00O00O0OOOO0000O ,sheet_name ="字典数据")#line:475
        O00O00O0OOOO0000O .close ()#line:476
        showinfo (title ="警告",message ="经检查，部分专家的打分存在错误。请您修正错误的打分文件再重新导入全部的专家打分文件。详见:分数错误信息.xls",)#line:480
        text .insert (END ,"\n经检查，部分专家的打分存在错误。详见:分数错误信息.xls。请您修正错误的打分文件再重新导入全部的专家打分文件。")#line:481
        text .insert (END ,"\n以下是错误信息概况：\n")#line:482
        text .insert (END ,O00000OO0OOO00O00 )#line:483
        text .see (END )#line:484
        return 0 #line:485
    if OOO0OO0O00OO0OO0O ==1 :#line:488
        return ori ,OOO0O000OOOOO00OO #line:489
def Tchouyang (OO00O00O000O00OO0 ):#line:492
    ""#line:493
    try :#line:495
        if OO00O00O000O00OO0 ==0 :#line:496
            showinfo (title ="提示",message ="您尚未导入原始数据。")#line:497
            return 0 #line:498
    except :#line:499
        pass #line:500
    if "详细描述"in OO00O00O000O00OO0 .columns :#line:501
        showinfo (title ="提示",message ="目前工作文件为专家评分文件，请导入原始数据进行抽样。")#line:502
        return 0 #line:503
    O0O000O0OOOOOO0OO =Toplevel ()#line:506
    O0O000O0OOOOOO0OO .title ("随机抽样及随机分组")#line:507
    OO000O0O00O0O0OOO =O0O000O0OOOOOO0OO .winfo_screenwidth ()#line:508
    OO00O0O00OO000OO0 =O0O000O0OOOOOO0OO .winfo_screenheight ()#line:510
    OO0O00O00O0O00OOO =300 #line:512
    O0O0OO000OO0O0OOO =220 #line:513
    OOOOOOOOOOOOOO00O =(OO000O0O00O0O0OOO -OO0O00O00O0O00OOO )/1.7 #line:515
    O0OOOOOOO0O00OO0O =(OO00O0O00OO000OO0 -O0O0OO000OO0O0OOO )/2 #line:516
    O0O000O0OOOOOO0OO .geometry ("%dx%d+%d+%d"%(OO0O00O00O0O00OOO ,O0O0OO000OO0O0OOO ,OOOOOOOOOOOOOO00O ,O0OOOOOOO0O00OO0O ))#line:517
    OOO00O0O0O0O0000O =Label (O0O000O0OOOOOO0OO ,text ="评估对象：")#line:519
    OOO00O0O0O0O0000O .grid (row =1 ,column =0 ,sticky ="w")#line:520
    OO0000OOOOO0OO0OO =StringVar ()#line:521
    OOO000O00O00O0OOO =ttk .Combobox (O0O000O0OOOOOO0OO ,width =25 ,height =10 ,state ="readonly",textvariable =OO0000OOOOO0OO0OO )#line:524
    OOO000O00O00O0OOO ["values"]=["上报单位","县区","地市","省级审核人","上市许可持有人"]#line:525
    OOO000O00O00O0OOO .current (0 )#line:526
    OOO000O00O00O0OOO .grid (row =2 ,column =0 )#line:527
    OO00O0O0OO00000OO =Label (O0O000O0OOOOOO0OO ,text ="-----------------------------------------")#line:529
    OO00O0O0OO00000OO .grid (row =3 ,column =0 ,sticky ="w")#line:530
    OOOOO0OOO0OO0O0O0 =Label (O0O000O0OOOOOO0OO ,text ="死亡报告抽样数量（>1)或比例(<=1)：")#line:532
    OOOOO0OOO0OO0O0O0 .grid (row =4 ,column =0 ,sticky ="w")#line:533
    OO0O0OO0O0O0OOOOO =Entry (O0O000O0OOOOOO0OO ,width =10 )#line:534
    OO0O0OO0O0O0OOOOO .grid (row =4 ,column =1 ,sticky ="w")#line:535
    O00O00O00OO0O0O00 =Label (O0O000O0OOOOOO0OO ,text ="严重报告抽样数量（>1)或比例(<=1)：")#line:537
    O00O00O00OO0O0O00 .grid (row =6 ,column =0 ,sticky ="w")#line:538
    O0OOO00O000O00000 =Entry (O0O000O0OOOOOO0OO ,width =10 )#line:539
    O0OOO00O000O00000 .grid (row =6 ,column =1 ,sticky ="w")#line:540
    O0O00O0O0OO000OOO =Label (O0O000O0OOOOOO0OO ,text ="一般报告抽样数量（>1)或比例(<=1)：")#line:542
    O0O00O0O0OO000OOO .grid (row =8 ,column =0 ,sticky ="w")#line:543
    OO00000O0OOOO000O =Entry (O0O000O0OOOOOO0OO ,width =10 )#line:544
    OO00000O0OOOO000O .grid (row =8 ,column =1 ,sticky ="w")#line:545
    OO00O0O0OO00000OO =Label (O0O000O0OOOOOO0OO ,text ="-----------------------------------------")#line:547
    OO00O0O0OO00000OO .grid (row =9 ,column =0 ,sticky ="w")#line:548
    O000O00OO0OO0O00O =Label (O0O000O0OOOOOO0OO ,text ="抽样后随机分组数（专家数量）：")#line:550
    O0OOOOO0O000OO0O0 =Entry (O0O000O0OOOOOO0OO ,width =10 )#line:551
    O000O00OO0OO0O00O .grid (row =10 ,column =0 ,sticky ="w")#line:552
    O0OOOOO0O000OO0O0 .grid (row =10 ,column =1 ,sticky ="w")#line:553
    OO00O0O0O0OOO0OOO =Button (O0O000O0OOOOOO0OO ,text ="最大覆盖",width =12 ,command =lambda :thread_it (Tdoing0 ,OO00O00O000O00OO0 ,OO00000O0OOOO000O .get (),O0OOO00O000O00000 .get (),OO0O0OO0O0O0OOOOO .get (),O0OOOOO0O000OO0O0 .get (),OOO000O00O00O0OOO .get (),"最大覆盖",1 ,),)#line:570
    OO00O0O0O0OOO0OOO .grid (row =13 ,column =1 ,sticky ="w")#line:571
    OOO00O0O0OO0O0O0O =Button (O0O000O0OOOOOO0OO ,text ="总体随机",width =12 ,command =lambda :thread_it (Tdoing0 ,OO00O00O000O00OO0 ,OO00000O0OOOO000O .get (),O0OOO00O000O00000 .get (),OO0O0OO0O0O0OOOOO .get (),O0OOOOO0O000OO0O0 .get (),OOO000O00O00O0OOO .get (),"总体随机",1 ))#line:572
    OOO00O0O0OO0O0O0O .grid (row =13 ,column =0 ,sticky ='w')#line:573
def Tdoing0 (O0O00O00OO0O0O0O0 ,OOOO00OO00OOOO0O0 ,OO0O0OO0000O0OOO0 ,OOO0OO00O00OO0000 ,OO00OOOO000OOO0O0 ,O00O0OO0O000O0000 ,O000O0000OO0OOO00 ,OOO000O0OOOO0O0O0 ):#line:579
    ""#line:580
    global dishi #line:581
    global biaozhun #line:582
    if (OOOO00OO00OOOO0O0 ==""or OO0O0OO0000O0OOO0 ==""or OOO0OO00O00OO0000 ==""or OO00OOOO000OOO0O0 ==""or O00O0OO0O000O0000 ==""or O000O0000OO0OOO00 ==""):#line:592
        showinfo (title ="提示信息",message ="参数设置不完整。")#line:593
        return 0 #line:594
    if O00O0OO0O000O0000 =="上报单位":#line:595
        O00O0OO0O000O0000 ="单位名称"#line:596
    if O00O0OO0O000O0000 =="县区":#line:597
        O00O0OO0O000O0000 ="使用单位、经营企业所属监测机构"#line:598
    if O00O0OO0O000O0000 =="地市":#line:599
        O00O0OO0O000O0000 ="市级监测机构"#line:600
    if O00O0OO0O000O0000 =="省级审核人":#line:601
        O00O0OO0O000O0000 ="审核人.1"#line:602
        O0O00O00OO0O0O0O0 ["modex"]=1 #line:603
        O0O00O00OO0O0O0O0 ["审核人.1"]=O0O00O00OO0O0O0O0 ["审核人.1"].fillna ("未填写")#line:604
    if O00O0OO0O000O0000 =="上市许可持有人":#line:605
        O00O0OO0O000O0000 ="上市许可持有人名称"#line:606
        O0O00O00OO0O0O0O0 ["modex"]=1 #line:607
        O0O00O00OO0O0O0O0 ["上市许可持有人名称"]=O0O00O00OO0O0O0O0 ["上市许可持有人名称"].fillna ("未填写")#line:608
    if OOO000O0OOOO0O0O0 ==1 :#line:610
        if len (biaozhun )==0 :#line:611
            OOO0O000OOO00O0OO =peizhidir +"0（范例）质量评估.xls"#line:612
            try :#line:613
                if "modex"in O0O00O00OO0O0O0O0 .columns :#line:614
                    O00O0OO000O0O00OO =pd .read_excel (OOO0O000OOO00O0OO ,sheet_name ="器械持有人",header =0 ,index_col =0 ).reset_index ()#line:615
                else :#line:616
                    O00O0OO000O0O00OO =pd .read_excel (OOO0O000OOO00O0OO ,sheet_name =0 ,header =0 ,index_col =0 ).reset_index ()#line:617
                text .insert (END ,"\n您使用配置表文件夹中的“0（范例）质量评估.xls“作为评分标准。")#line:618
                text .see (END )#line:619
            except :#line:622
                O00O0OO000O0O00OO =pd .DataFrame ({"评分项":{0 :"识别代码",1 :"报告人",2 :"联系人",3 :"联系电话",4 :"注册证编号/曾用注册证编号",5 :"产品名称",6 :"型号和规格",7 :"产品批号和产品编号",8 :"生产日期",9 :"有效期至",10 :"事件发生日期",11 :"发现或获知日期",12 :"伤害",13 :"伤害表现",14 :"器械故障表现",15 :"年龄和年龄类型",16 :"性别",17 :"预期治疗疾病或作用",18 :"器械使用日期",19 :"使用场所和场所名称",20 :"使用过程",21 :"合并用药/械情况说明",22 :"事件原因分析和事件原因分析描述",23 :"初步处置情况",},"打分标准":{0 :"",1 :"填写人名或XX科室，得1分",2 :"填写报告填报人员姓名或XX科X医生，得1分",3 :"填写报告填报人员移动电话或所在科室固定电话，得1分",4 :"可利用国家局数据库检索，注册证号与产品名称及事件描述相匹配的，得8分",5 :"可利用国家局数据库检索，注册证号与产品名称及事件描述相匹配的，得4分",6 :"规格和型号任填其一，且内容正确，得4分",7 :"产品批号和编号任填其一，且内容正确，,得4分。\n注意：（1）如果该器械使用年限久远，或在院外用械，批号或编号无法查询追溯的，报告表“使用过程”中给予说明的，得4分；（2）出现YZB格式、YY格式、GB格式等产品标准格式，或“XX生产许XX”等许可证号，得0分；（3）出现和注册证号一样的数字，得0分。",8 :"确保“生产日期”和“有效期至”逻辑正确，“有效期至”晚于“生产日期”，且两者时间间隔应为整月或整年，得2分。",9 :"确保生产日期和有效期逻辑正确。\n注意：如果该器械是使用年限久远的（2014年之前生产产品），或在院外用械，生产日期和有效期无法查询追溯的，并在报告表“使用过程”中给予说明的，该项得4分",10 :"指发生医疗器械不良事件的日期，应与使用过程描述一致，如仅知道事件发生年份，填写当年的1月1日；如仅知道年份和月份，填写当月的第1日；如年月日均未知，填写事件获知日期，并在“使用过程”给予说明。填写正确得2分。\n注意：“事件发生日期”早于“器械使用日期”的，得0分。",11 :"指报告单位发现或知悉该不良事件的日期，填写正确得5分。\n注意：“发现或获知日期”早于“事件发生日期”的，或者早于使用日期的，得0分。",12 :"分为“死亡”、“严重伤害”“其他”，判断正确，得8分。",13 :"描述准确且简明，或者勾选的术语贴切的，得6分；描述较为准确且简明，或选择术语较为贴切，或描述准确但不够简洁，得3分；描述冗长、填成器械故障表现的，得0分。\n注意：对于“严重伤害”事件，需写明实际导致的严重伤害，填写不恰当的或填写“无”的，得0分。伤害表现描述与使用过程中关于伤害的描述不一致的，得0分。对于“其他”未对患者造成伤害的，该项可填“无”或未填写，默认得6分。",14 :"描述准确而简明，或者勾选的术语贴切的，得6分；描述较为准确，或选择术语较为贴切，或描述准确但不够简洁，得3分；描述冗长、填成伤害表现的，得0分。故障表现与使用过程中关于器械故障的描述不一致的，得0分。\n注意：对于不存在器械故障但仍然对患者造成了伤害的，在伤害表现处填写了对应伤害，该项填“无”，默认得6分。",15 :"医疗器械若未用于患者或者未造成患者伤害的，患者信息非必填项，默认得1分。",16 :"医疗器械若未用于患者或者未造成患者伤害的，患者信息非必填项，默认得1分。",17 :"指涉及医疗器械的用途或适用范围，如治疗类医疗器械的预期治疗疾病，检验检查类、辅助治疗类医疗器械的预期作用等。填写完整准确，得4分；未填写、填写不完整或填写错误，得0分。",18 :"需与使用过程描述的日期一致，若器械使用日期和不良事件发生日期不是同一天，填成“不良事件发生日期”的，得0分；填成“有源设备启用日期”的，得0分。如仅知道事件使用年份，填写当年的1月1日；如仅知道年份和月份，填写当月的第1日；如年月日均未知，填写事件获知日期，并在“使用过程”给予说明。",19 :"使用场所为“医疗机构”的，场所名称可以为空，默认得2分；使用场所为“家庭”或“其他”，但勾选为医疗机构的，得0分；如使用场所为“其他”，没有填写实际使用场所或填写错误的，得0分。",20 :"按照以下四个要素进行评分：\n（1）具体操作使用情况（5分）\n详细描述具体操作人员资质、操作使用过程等信息，对于体外诊断医疗器械应填写患者诊疗信息（如疾病情况、用药情况）、样品检测过程与结果等信息。该要素描述准确完整的，得5分；较完整准确的，得2.5分；要素缺失的，得0分。\n（2）不良事件情况（5分）\n详细描述使用过程中出现的非预期结果等信息，对于体外诊断医疗器械应填写发现的异常检测情况，该要素描述完整准确的，得5分；较完整准确的，得2.5分；要素缺失的，得0分。\n（3）对受害者的影响（4分）\n详细描述该事件（可能）对患者造成的伤害，（可能）对临床诊疗造成的影响。有实际伤害的事件，需写明对受害者的伤害情况，包括必要的体征（如体温、脉搏、血压、皮损程度、失血情况等）和相关检查结果（如血小板检查结果）；对于可能造成严重伤害的事件，需写明可能对患者或其他人员造成的伤害。该要素描述完整准确的，得4分；较完整准确的，得2分；要素缺失的，得0分。\n（4）采取的治疗措施及结果（4分）\n有实际伤害的情况，须写明对伤者采取的治疗措施（包括用药、用械、或手术治疗等，及采取各个治疗的时间），以及采取治疗措施后的转归情况。该要素描述完整准确得4分，较完整准确得2分，描述过于笼统简单，如描述为“对症治疗”、“报告医生”、“转院”等，或者要素缺失的，得0分；无实际伤害的，该要素默认得4分。",21 :"有合并用药/械情况但没有填写此项的，得0分；填写不完整的，得2分；评估认为该不良事件过程中不存在合并用药/械情况的，该项不填写可得4分。\n如：输液泵泵速不准，合并用药/械情况应写明输注的药液、并用的输液器信息等。",22 :"原因分析不正确，如对于产品原因（包括说明书等）、操作原因 、患者自身原因 、无法确定的勾选与原因分析的描述的内容不匹配的，得0分，例如勾选了产品原因，但描述中说明该事件可能是未按照说明书要求进行操作导致（操作原因）；原因分析正确，但原因分析描述填成使用过程或者处置方式的，得2分。",23 :"包含产品的初步处置措施和对患者的救治措施等，填写完整得2分，部分完整得1分，填写过于简单得0分。",},"满分分值":{0 :0 ,1 :1 ,2 :1 ,3 :1 ,4 :8 ,5 :4 ,6 :4 ,7 :4 ,8 :2 ,9 :2 ,10 :2 ,11 :5 ,12 :8 ,13 :6 ,14 :6 ,15 :1 ,16 :1 ,17 :4 ,18 :2 ,19 :2 ,20 :18 ,21 :4 ,22 :4 ,23 :2 ,},})#line:704
                text .insert (END ,"\n您使用软件内置的评分标准。")#line:705
                text .see (END )#line:706
            try :#line:708
                dishi =pd .read_excel (OOO0O000OOO00O0OO ,sheet_name ="地市清单",header =0 ,index_col =0 ).reset_index ()#line:711
                text .insert (END ,"\n找到地市清单，将规整地市名称。")#line:712
                for OOO0O00O00OOO000O in dishi ["地市列表"]:#line:713
                    O0O00O00OO0O0O0O0 .loc [(O0O00O00OO0O0O0O0 ["上报单位所属地区"].str .contains (OOO0O00O00OOO000O ,na =False )),"市级监测机构",]=OOO0O00O00OOO000O #line:717
                    O0O00O00OO0O0O0O0 .loc [(O0O00O00OO0O0O0O0 ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构",]="佛山"#line:721
                    O0O00O00OO0O0O0O0 .loc [(O0O00O00OO0O0O0O0 ["市级监测机构"].str .contains ("北海",na =False )),"市级监测机构",]="北海"#line:728
                    O0O00O00OO0O0O0O0 .loc [(O0O00O00OO0O0O0O0 ["联系地址"].str .contains ("北海市",na =False )),"市级监测机构",]="北海"#line:732
                text .see (END )#line:733
            except :#line:734
                text .insert (END ,"\n未找到地市清单或清单有误，不对地市名称进行规整，未维护产品的报表的地市名称将以“未填写”的形式展现。")#line:735
                text .see (END )#line:736
        else :#line:737
            O00O0OO000O0O00OO =biaozhun .copy ()#line:738
            if len (dishi )!=0 :#line:739
                try :#line:740
                    text .insert (END ,"\n找到自定义的地市清单，将规整地市名称。")#line:741
                    for OOO0O00O00OOO000O in dishi ["地市列表"]:#line:742
                        O0O00O00OO0O0O0O0 .loc [(O0O00O00OO0O0O0O0 ["使用单位、经营企业所属监测机构"].str .contains (OOO0O00O00OOO000O ,na =False )),"市级监测机构",]=OOO0O00O00OOO000O #line:746
                    O0O00O00OO0O0O0O0 .loc [(O0O00O00OO0O0O0O0 ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构",]="佛山"#line:750
                    text .see (END )#line:751
                except TRD :#line:752
                    text .insert (END ,"\n导入的自定义配置表中，未找到地市清单或清单有误，不对地市名称进行规整，未维护产品的报表的地市名称将以“未填写”的形式展现。",)#line:756
                    text .see (END )#line:757
            text .insert (END ,"\n您使用了自己导入的配置表作为评分标准。")#line:758
            text .see (END )#line:759
    text .insert (END ,"\n正在抽样，请稍候...已完成30%")#line:760
    O0O00O00OO0O0O0O0 =O0O00O00OO0O0O0O0 .reset_index (drop =True )#line:761
    O0O00O00OO0O0O0O0 ["质量评估模式"]=O0O00O00OO0O0O0O0 [O00O0OO0O000O0000 ]#line:764
    O0O00O00OO0O0O0O0 ["报告时限"]=""#line:765
    O0O00O00OO0O0O0O0 ["报告时限情况"]="超时报告"#line:766
    O0O00O00OO0O0O0O0 ["识别代码"]=range (0 ,len (O0O00O00OO0O0O0O0 ))#line:767
    try :#line:768
        O0O00O00OO0O0O0O0 ["报告时限"]=pd .to_datetime (O0O00O00OO0O0O0O0 ["报告日期"])-pd .to_datetime (O0O00O00OO0O0O0O0 ["发现或获知日期"])#line:771
        O0O00O00OO0O0O0O0 ["报告时限"]=O0O00O00OO0O0O0O0 ["报告时限"].dt .days #line:772
        O0O00O00OO0O0O0O0 .loc [(O0O00O00OO0O0O0O0 ["伤害"]=="死亡")&(O0O00O00OO0O0O0O0 ["报告时限"]<=7 ),"报告时限情况"]="死亡未超时，报告时限："+O0O00O00OO0O0O0O0 ["报告时限"].astype (str )#line:775
        O0O00O00OO0O0O0O0 .loc [(O0O00O00OO0O0O0O0 ["伤害"]=="严重伤害")&(O0O00O00OO0O0O0O0 ["报告时限"]<=20 ),"报告时限情况"]="严重伤害未超时，报告时限："+O0O00O00OO0O0O0O0 ["报告时限"].astype (str )#line:778
        O0O00O00OO0O0O0O0 .loc [(O0O00O00OO0O0O0O0 ["伤害"]=="其他")&(O0O00O00OO0O0O0O0 ["报告时限"]<=30 ),"报告时限情况"]="其他未超时，报告时限："+O0O00O00OO0O0O0O0 ["报告时限"].astype (str )#line:781
        O0O00O00OO0O0O0O0 .loc [(O0O00O00OO0O0O0O0 ["报告时限情况"]=="超时报告"),"报告时限情况"]="！疑似超时报告，报告时限："+O0O00O00OO0O0O0O0 ["报告时限"].astype (str )#line:784
        O0O00O00OO0O0O0O0 ["型号和规格"]=("型号："+O0O00O00OO0O0O0O0 ["型号"].astype (str )+"   \n规格："+O0O00O00OO0O0O0O0 ["规格"].astype (str ))#line:787
        O0O00O00OO0O0O0O0 ["产品批号和产品编号"]=("产品批号："+O0O00O00OO0O0O0O0 ["产品批号"].astype (str )+"   \n产品编号："+O0O00O00OO0O0O0O0 ["产品编号"].astype (str ))#line:793
        O0O00O00OO0O0O0O0 ["使用场所和场所名称"]=("使用场所："+O0O00O00OO0O0O0O0 ["使用场所"].astype (str )+"   \n场所名称："+O0O00O00OO0O0O0O0 ["场所名称"].astype (str ))#line:799
        O0O00O00OO0O0O0O0 ["年龄和年龄类型"]=("年龄："+O0O00O00OO0O0O0O0 ["年龄"].astype (str )+"   \n年龄类型："+O0O00O00OO0O0O0O0 ["年龄类型"].astype (str ))#line:805
        O0O00O00OO0O0O0O0 ["事件原因分析和事件原因分析描述"]=("事件原因分析："+O0O00O00OO0O0O0O0 ["事件原因分析"].astype (str )+"   \n事件原因分析描述："+O0O00O00OO0O0O0O0 ["事件原因分析描述"].astype (str ))#line:811
        O0O00O00OO0O0O0O0 ["是否开展了调查及调查情况"]=("是否开展了调查："+O0O00O00OO0O0O0O0 ["是否开展了调查"].astype (str )+"   \n调查情况："+O0O00O00OO0O0O0O0 ["调查情况"].astype (str ))#line:820
        O0O00O00OO0O0O0O0 ["控制措施情况"]=("是否已采取控制措施："+O0O00O00OO0O0O0O0 ["是否已采取控制措施"].astype (str )+"   \n具体控制措施："+O0O00O00OO0O0O0O0 ["具体控制措施"].astype (str )+"   \n未采取控制措施原因："+O0O00O00OO0O0O0O0 ["未采取控制措施原因"].astype (str ))#line:829
        O0O00O00OO0O0O0O0 ["是否为错报误报报告及错报误报说明"]=("是否为错报误报报告："+O0O00O00OO0O0O0O0 ["是否为错报误报报告"].astype (str )+"   \n错报误报说明："+O0O00O00OO0O0O0O0 ["错报误报说明"].astype (str ))#line:836
        O0O00O00OO0O0O0O0 ["是否合并报告及合并报告编码"]=("是否合并报告："+O0O00O00OO0O0O0O0 ["是否合并报告"].astype (str )+"   \n合并报告编码："+O0O00O00OO0O0O0O0 ["合并报告编码"].astype (str ))#line:843
    except :#line:844
        pass #line:845
    if "报告类型-新的"in O0O00O00OO0O0O0O0 .columns :#line:846
        O0O00O00OO0O0O0O0 ["报告时限"]=pd .to_datetime (O0O00O00OO0O0O0O0 ["报告日期"].astype (str ))-pd .to_datetime (O0O00O00OO0O0O0O0 ["不良反应发生时间"].astype (str ))#line:848
        O0O00O00OO0O0O0O0 ["报告类型"]=O0O00O00OO0O0O0O0 ["报告类型-新的"].astype (str )+O0O00O00OO0O0O0O0 ["伤害"].astype (str )+"    "+O0O00O00OO0O0O0O0 ["严重药品不良反应"].astype (str )#line:849
        O0O00O00OO0O0O0O0 ["报告类型"]=O0O00O00OO0O0O0O0 ["报告类型"].str .replace ("-未填写-","",regex =False )#line:850
        O0O00O00OO0O0O0O0 ["报告类型"]=O0O00O00OO0O0O0O0 ["报告类型"].str .replace ("其他","一般",regex =False )#line:851
        O0O00O00OO0O0O0O0 ["报告类型"]=O0O00O00OO0O0O0O0 ["报告类型"].str .replace ("严重伤害","严重",regex =False )#line:852
        O0O00O00OO0O0O0O0 ["关联性评价和ADR分析"]="停药减药后反应是否减轻或消失："+O0O00O00OO0O0O0O0 ["停药减药后反应是否减轻或消失"].astype (str )+"\n再次使用可疑药是否出现同样反应："+O0O00O00OO0O0O0O0 ["再次使用可疑药是否出现同样反应"].astype (str )+"\n报告人评价："+O0O00O00OO0O0O0O0 ["报告人评价"].astype (str )#line:853
        O0O00O00OO0O0O0O0 ["ADR过程描述以及处理情况"]="不良反应发生时间："+O0O00O00OO0O0O0O0 ["不良反应发生时间"].astype (str )+"\n不良反应过程描述："+O0O00O00OO0O0O0O0 ["不良反应过程描述"].astype (str )+"\n不良反应结果:"+O0O00O00OO0O0O0O0 ["不良反应结果"].astype (str )+"\n对原患疾病影响:"+O0O00O00OO0O0O0O0 ["对原患疾病影响"].astype (str )+"\n后遗症表现："+O0O00O00OO0O0O0O0 ["后遗症表现"].astype (str )+"\n死亡时间:"+O0O00O00OO0O0O0O0 ["死亡时间"].astype (str )+"\n直接死因:"+O0O00O00OO0O0O0O0 ["直接死因"].astype (str )#line:854
        O0O00O00OO0O0O0O0 ["报告者及患者有关情况"]="患者姓名："+O0O00O00OO0O0O0O0 ["患者姓名"].astype (str )+"\n性别："+O0O00O00OO0O0O0O0 ["性别"].astype (str )+"\n出生日期:"+O0O00O00OO0O0O0O0 ["出生日期"].astype (str )+"\n年龄:"+O0O00O00OO0O0O0O0 ["年龄"].astype (str )+O0O00O00OO0O0O0O0 ["年龄单位"].astype (str )+"\n民族："+O0O00O00OO0O0O0O0 ["民族"].astype (str )+"\n体重:"+O0O00O00OO0O0O0O0 ["体重"].astype (str )+"\n原患疾病:"+O0O00O00OO0O0O0O0 ["原患疾病"].astype (str )+"\n病历号/门诊号:"+O0O00O00OO0O0O0O0 ["病历号/门诊号"].astype (str )+"\n既往药品不良反应/事件:"+O0O00O00OO0O0O0O0 ["既往药品不良反应/事件"].astype (str )+"\n家族药品不良反应/事件:"+O0O00O00OO0O0O0O0 ["家族药品不良反应/事件"].astype (str )#line:855
    O0OOOO0O00O00OO00 =filedialog .askdirectory ()#!!!!!!!#line:859
    O00O0O000OOOOO0O0 =1 #line:862
    for O000O0OOO00OOOOOO in O0O00O00OO0O0O0O0 ["伤害"].drop_duplicates ():#line:863
        if O000O0OOO00OOOOOO =="其他":#line:864
            O00000000OO0O0O00 =1 #line:865
            OO00O0OO000O0O000 =O0O00O00OO0O0O0O0 [(O0O00O00OO0O0O0O0 ["伤害"]=="其他")]#line:866
            OO00OOO0OO0O000O0 =Tdoing (OO00O0OO000O0O000 ,OOOO00OO00OOOO0O0 ,OO00OOOO000OOO0O0 ,O00O0OO0O000O0000 ,O000O0000OO0OOO00 ,OOO000O0OOOO0O0O0 )#line:867
            if O00O0O000OOOOO0O0 ==1 :#line:868
                OO0OO0O0OO0O0O0OO =OO00OOO0OO0O000O0 [0 ]#line:869
                O00O0O000OOOOO0O0 =O00O0O000OOOOO0O0 +1 #line:870
            else :#line:871
                OO0OO0O0OO0O0O0OO =pd .concat ([OO0OO0O0OO0O0O0OO ,OO00OOO0OO0O000O0 [0 ]],axis =0 )#line:872
        if O000O0OOO00OOOOOO =="严重伤害":#line:874
            O0000OO0OO0OOO0OO =1 #line:875
            O00OO0OO00O00O0OO =O0O00O00OO0O0O0O0 [(O0O00O00OO0O0O0O0 ["伤害"]=="严重伤害")]#line:876
            O00OOO000O00000OO =Tdoing (O00OO0OO00O00O0OO ,OO0O0OO0000O0OOO0 ,OO00OOOO000OOO0O0 ,O00O0OO0O000O0000 ,O000O0000OO0OOO00 ,OOO000O0OOOO0O0O0 )#line:877
            if O00O0O000OOOOO0O0 ==1 :#line:878
                OO0OO0O0OO0O0O0OO =O00OOO000O00000OO [0 ]#line:879
                O00O0O000OOOOO0O0 =O00O0O000OOOOO0O0 +1 #line:880
            else :#line:881
                OO0OO0O0OO0O0O0OO =pd .concat ([OO0OO0O0OO0O0O0OO ,O00OOO000O00000OO [0 ]],axis =0 )#line:882
        if O000O0OOO00OOOOOO =="死亡":#line:884
            OO0O0000O0O00OO00 =1 #line:885
            O0OO00O0O00O00000 =O0O00O00OO0O0O0O0 [(O0O00O00OO0O0O0O0 ["伤害"]=="死亡")]#line:886
            O0O0O00OOOOO000O0 =Tdoing (O0OO00O0O00O00000 ,OOO0OO00O00OO0000 ,OO00OOOO000OOO0O0 ,O00O0OO0O000O0000 ,O000O0000OO0OOO00 ,OOO000O0OOOO0O0O0 )#line:887
            if O00O0O000OOOOO0O0 ==1 :#line:888
                OO0OO0O0OO0O0O0OO =O0O0O00OOOOO000O0 [0 ]#line:889
                O00O0O000OOOOO0O0 =O00O0O000OOOOO0O0 +1 #line:890
            else :#line:891
                OO0OO0O0OO0O0O0OO =pd .concat ([OO0OO0O0OO0O0O0OO ,O0O0O00OOOOO000O0 [0 ]],axis =0 )#line:892
    text .insert (END ,"\n正在抽样，请稍候...已完成50%")#line:896
    OOO0000OOO0OO000O =pd .ExcelWriter (str (O0OOOO0O00O00OO00 )+"/●(最终评分需导入)被抽出的所有数据"+".xlsx")#line:897
    OO0OO0O0OO0O0O0OO .to_excel (OOO0000OOO0OO000O ,sheet_name ="被抽出的所有数据")#line:898
    OOO0000OOO0OO000O .close ()#line:899
    if OOO000O0OOOO0O0O0 ==1 :#line:902
        O0O0OOOOOO000OO0O =O0O00O00OO0O0O0O0 .copy ()#line:903
        O0O0OOOOOO000OO0O ["原始数量"]=1 #line:904
        O0O000OO0OOOO0OO0 =OO0OO0O0OO0O0O0OO .copy ()#line:905
        O0O000OO0OOOO0OO0 ["抽取数量"]=1 #line:906
        O0O00O0O0O0000OO0 =O0O0OOOOOO000OO0O .groupby ([O00O0OO0O000O0000 ]).aggregate ({"原始数量":"count"})#line:909
        O0O00O0O0O0000OO0 =O0O00O0O0O0000OO0 .sort_values (by =["原始数量"],ascending =False ,na_position ="last")#line:912
        O0O00O0O0O0000OO0 =O0O00O0O0O0000OO0 .reset_index ()#line:913
        O000O00O000O0O000 =pd .pivot_table (O0O000OO0OOOO0OO0 ,values =["抽取数量"],index =O00O0OO0O000O0000 ,columns ="伤害",aggfunc ={"抽取数量":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:924
        O000O00O000O0O000 .columns =O000O00O000O0O000 .columns .droplevel (0 )#line:925
        O000O00O000O0O000 =O000O00O000O0O000 .sort_values (by =["All"],ascending =[False ],na_position ="last")#line:928
        O000O00O000O0O000 =O000O00O000O0O000 .reset_index ()#line:929
        O000O00O000O0O000 =O000O00O000O0O000 .rename (columns ={"All":"抽取总数量"})#line:930
        try :#line:931
            O000O00O000O0O000 =O000O00O000O0O000 .rename (columns ={"一般":"抽取数量(一般)"})#line:932
        except :#line:933
            pass #line:934
        try :#line:935
            O000O00O000O0O000 =O000O00O000O0O000 .rename (columns ={"严重伤害":"抽取数量(严重)"})#line:936
        except :#line:937
            pass #line:938
        try :#line:939
            O000O00O000O0O000 =O000O00O000O0O000 .rename (columns ={"死亡":"抽取数量-死亡"})#line:940
        except :#line:941
            pass #line:942
        OOO0O0O0000000OOO =pd .merge (O0O00O0O0O0000OO0 ,O000O00O000O0O000 ,on =[O00O0OO0O000O0000 ],how ="left")#line:943
        OOO0O0O0000000OOO ["抽取比例"]=round (OOO0O0O0000000OOO ["抽取总数量"]/OOO0O0O0000000OOO ["原始数量"],2 )#line:944
        O0O000OOO0OOO0000 =pd .ExcelWriter (str (O0OOOO0O00O00OO00 )+"/抽样情况分布"+".xlsx")#line:945
        OOO0O0O0000000OOO .to_excel (O0O000OOO0OOO0000 ,sheet_name ="抽样情况分布")#line:946
        O0O000OOO0OOO0000 .close ()#line:947
    OO0OO0O0OO0O0O0OO =OO0OO0O0OO0O0O0OO [O00O0OO000O0O00OO ["评分项"].tolist ()]#line:953
    OOO00OO0O00000OO0 =int (OO00OOOO000OOO0O0 )#line:955
    text .insert (END ,"\n正在抽样，请稍候...已完成70%")#line:957
    for O000O0OOO00OOOOOO in range (OOO00OO0O00000OO0 ):#line:958
        if O000O0OOO00OOOOOO ==0 :#line:959
            O000OOO0000O00O0O =OO0OO0O0OO0O0O0OO [(OO0OO0O0OO0O0O0OO ["伤害"]=="其他")].sample (frac =1 /(OOO00OO0O00000OO0 -O000O0OOO00OOOOOO ),replace =False )#line:963
            O0O00O00OO0OOOO0O =OO0OO0O0OO0O0O0OO [(OO0OO0O0OO0O0O0OO ["伤害"]=="严重伤害")].sample (frac =1 /(OOO00OO0O00000OO0 -O000O0OOO00OOOOOO ),replace =False )#line:966
            OOOO000O000O0O0O0 =OO0OO0O0OO0O0O0OO [(OO0OO0O0OO0O0O0OO ["伤害"]=="死亡")].sample (frac =1 /(OOO00OO0O00000OO0 -O000O0OOO00OOOOOO ),replace =False )#line:969
            O0OO00O00O0O0O0O0 =pd .concat ([O000OOO0000O00O0O ,O0O00O00OO0OOOO0O ,OOOO000O000O0O0O0 ],axis =0 )#line:971
        else :#line:973
            OO0OO0O0OO0O0O0OO =pd .concat ([OO0OO0O0OO0O0O0OO ,O0OO00O00O0O0O0O0 ],axis =0 )#line:974
            OO0OO0O0OO0O0O0OO .drop_duplicates (subset =["识别代码"],keep =False ,inplace =True )#line:975
            O000OOO0000O00O0O =OO0OO0O0OO0O0O0OO [(OO0OO0O0OO0O0O0OO ["伤害"]=="其他")].sample (frac =1 /(OOO00OO0O00000OO0 -O000O0OOO00OOOOOO ),replace =False )#line:978
            O0O00O00OO0OOOO0O =OO0OO0O0OO0O0O0OO [(OO0OO0O0OO0O0O0OO ["伤害"]=="严重伤害")].sample (frac =1 /(OOO00OO0O00000OO0 -O000O0OOO00OOOOOO ),replace =False )#line:981
            OOOO000O000O0O0O0 =OO0OO0O0OO0O0O0OO [(OO0OO0O0OO0O0O0OO ["伤害"]=="死亡")].sample (frac =1 /(OOO00OO0O00000OO0 -O000O0OOO00OOOOOO ),replace =False )#line:984
            O0OO00O00O0O0O0O0 =pd .concat ([O000OOO0000O00O0O ,O0O00O00OO0OOOO0O ,OOOO000O000O0O0O0 ],axis =0 )#line:985
        try :#line:986
            O0OO00O00O0O0O0O0 ["报告编码"]=O0OO00O00O0O0O0O0 ["报告编码"].astype (str )#line:987
        except :#line:988
            pass #line:989
        O00000OO00O0OOOO0 =str (O0OOOO0O00O00OO00 )+"/"+str (O000O0OOO00OOOOOO +1 )+".xlsx"#line:990
        if OOO000O0OOOO0O0O0 ==1 :#line:993
            OO0000000O0O0000O =TeasyreadT (O0OO00O00O0O0O0O0 .copy ())#line:994
            del OO0000000O0O0000O ["逐条查看"]#line:995
            OO0000000O0O0000O ["评分"]=""#line:996
            if len (OO0000000O0O0000O )>0 :#line:997
                for O00000O0000O0OOO0 ,OO000O000O0O0O0O0 in O00O0OO000O0O00OO .iterrows ():#line:998
                    OO0000000O0O0000O .loc [(OO0000000O0O0000O ["条目"]==OO000O000O0O0O0O0 ["评分项"]),"满分"]=OO000O000O0O0O0O0 ["满分分值"]#line:999
                    OO0000000O0O0000O .loc [(OO0000000O0O0000O ["条目"]==OO000O000O0O0O0O0 ["评分项"]),"打分标准"]=OO000O000O0O0O0O0 ["打分标准"]#line:1002
            OO0000000O0O0000O ["专家序号"]=O000O0OOO00OOOOOO +1 #line:1004
            OOO0000OOOOOO00OO =str (O0OOOO0O00O00OO00 )+"/"+"●专家评分表"+str (O000O0OOO00OOOOOO +1 )+".xlsx"#line:1005
            O0O0O00O00O000O0O =pd .ExcelWriter (OOO0000OOOOOO00OO )#line:1006
            OO0000000O0O0000O .to_excel (O0O0O00O00O000O0O ,sheet_name ="字典数据")#line:1007
            O0O0O00O00O000O0O .close ()#line:1008
    text .insert (END ,"\n正在抽样，请稍候...已完成100%")#line:1011
    showinfo (title ="提示信息",message ="抽样和分组成功，请查看以下文件夹："+str (O0OOOO0O00O00OO00 ))#line:1012
    text .insert (END ,"\n抽样和分组成功，请查看以下文件夹："+str (O0OOOO0O00O00OO00 ))#line:1013
    text .insert (END ,"\n抽样概况:\n")#line:1014
    text .insert (END ,OOO0O0O0000000OOO [[O00O0OO0O000O0000 ,"原始数量","抽取总数量"]])#line:1015
    text .see (END )#line:1016
def Tdoing (OOO000OO000O0O000 ,OOO00OO0OO00O0O00 ,O0O00O0OO0OOOOO00 ,O0OOO00O0OOOOO0O0 ,OOOOOOOOO00O000OO ,OOO0O000O00O0OOOO ):#line:1019
    ""#line:1020
    def OO0OOOOOOO0O000O0 (O00OO0OOOOOOO0OO0 ,O00OO0OOOO000OO0O ,O0O00OO0O0000OOOO ):#line:1022
        if float (O00OO0OOOO000OO0O )>1 :#line:1023
            try :#line:1024
                OOO000OO0O0O000O0 =O00OO0OOOOOOO0OO0 .sample (int (O00OO0OOOO000OO0O ),replace =False )#line:1025
            except ValueError :#line:1027
                OOO000OO0O0O000O0 =O00OO0OOOOOOO0OO0 #line:1029
        else :#line:1030
            OOO000OO0O0O000O0 =O00OO0OOOOOOO0OO0 .sample (frac =float (O00OO0OOOO000OO0O ),replace =False )#line:1031
            if len (O00OO0OOOOOOO0OO0 )*float (O00OO0OOOO000OO0O )>len (OOO000OO0O0O000O0 )and O0O00OO0O0000OOOO =="最大覆盖":#line:1033
                OOO00000OOOOOOOO0 =pd .concat ([O00OO0OOOOOOO0OO0 ,OOO000OO0O0O000O0 ],axis =0 )#line:1034
                OOO00000OOOOOOOO0 .drop_duplicates (subset =["识别代码"],keep =False ,inplace =True )#line:1035
                OO0OOO000O000O0OO =OOO00000OOOOOOOO0 .sample (1 ,replace =False )#line:1036
                OOO000OO0O0O000O0 =pd .concat ([OOO000OO0O0O000O0 ,OO0OOO000O000O0OO ],axis =0 )#line:1037
        return OOO000OO0O0O000O0 #line:1038
    if OOOOOOOOO00O000OO =="总体随机":#line:1041
        O0O000O0OO0O0OO0O =OO0OOOOOOO0O000O0 (OOO000OO000O0O000 ,OOO00OO0OO00O0O00 ,OOOOOOOOO00O000OO )#line:1042
    else :#line:1044
        O0O00000OO0000OO0 =1 #line:1045
        for OO00O000OO0O00OO0 in OOO000OO000O0O000 [O0OOO00O0OOOOO0O0 ].drop_duplicates ():#line:1046
            OOO0O00O0OO00O000 =OOO000OO000O0O000 [(OOO000OO000O0O000 [O0OOO00O0OOOOO0O0 ]==OO00O000OO0O00OO0 )].copy ()#line:1047
            if O0O00000OO0000OO0 ==1 :#line:1048
                O0O000O0OO0O0OO0O =OO0OOOOOOO0O000O0 (OOO0O00O0OO00O000 ,OOO00OO0OO00O0O00 ,OOOOOOOOO00O000OO )#line:1049
                O0O00000OO0000OO0 =O0O00000OO0000OO0 +1 #line:1050
            else :#line:1051
                OOOOO000O00000OOO =OO0OOOOOOO0O000O0 (OOO0O00O0OO00O000 ,OOO00OO0OO00O0O00 ,OOOOOOOOO00O000OO )#line:1052
                O0O000O0OO0O0OO0O =pd .concat ([O0O000O0OO0O0OO0O ,OOOOO000O00000OOO ])#line:1053
    O0O000O0OO0O0OO0O =O0O000O0OO0O0OO0O .drop_duplicates ()#line:1054
    return O0O000O0OO0O0OO0O ,1 #line:1055
def Tpinggu ():#line:1058
    ""#line:1059
    OO000OO0OOOOO00OO =Topentable (1 )#line:1060
    OOOOOO0000000O00O =OO000OO0OOOOO00OO [0 ]#line:1061
    O0O0O0O0O0000000O =OO000OO0OOOOO00OO [1 ]#line:1062
    try :#line:1065
        OO000000OO0O00OOO =[pd .read_excel (O0000OOOOOO0O000O ,header =0 ,sheet_name =0 )for O0000OOOOOO0O000O in O0O0O0O0O0000000O ]#line:1069
        OO0O0000O00O0O00O =pd .concat (OO000000OO0O00OOO ,ignore_index =True ).drop_duplicates ()#line:1070
        try :#line:1071
            OO0O0000O00O0O00O =OO0O0000O00O0O00O .loc [:,~OO0O0000O00O0O00O .columns .str .contains ("^Unnamed")]#line:1072
        except :#line:1073
            pass #line:1074
    except :#line:1075
        showinfo (title ="提示信息",message ="载入文件出错，任务终止。")#line:1076
        return 0 #line:1077
    try :#line:1080
        OOOOOO0000000O00O =OOOOOO0000000O00O .reset_index ()#line:1081
    except :#line:1082
        showinfo (title ="提示信息",message ="专家评分文件存在错误，程序中止。")#line:1083
        return 0 #line:1084
    OO0O0000O00O0O00O ["质量评估专用表"]=""#line:1086
    text .insert (END ,"\n打分表导入成功，正在统计，请耐心等待...")#line:1089
    text .insert (END ,"\n正在计算总分，请稍候，已完成20%")#line:1090
    text .see (END )#line:1091
    O00000O0OO0O0O000 =OOOOOO0000000O00O [["序号","条目","详细描述","评分","满分","打分标准","专家序号"]].copy ()#line:1094
    OOO000O00OOO0O0OO =OO0O0000O00O0O00O [["质量评估模式","识别代码"]].copy ()#line:1095
    O00000O0OO0O0O000 .reset_index (inplace =True )#line:1096
    OOO000O00OOO0O0OO .reset_index (inplace =True )#line:1097
    OOO000O00OOO0O0OO =OOO000O00OOO0O0OO .rename (columns ={"识别代码":"序号"})#line:1098
    O00000O0OO0O0O000 =pd .merge (O00000O0OO0O0O000 ,OOO000O00OOO0O0OO ,on =["序号"])#line:1099
    O00000O0OO0O0O000 =O00000O0OO0O0O000 .sort_values (by =["序号","条目"],ascending =True ,na_position ="last")#line:1100
    O00000O0OO0O0O000 =O00000O0OO0O0O000 [["质量评估模式","序号","条目","详细描述","评分","满分","打分标准","专家序号"]]#line:1101
    for O0O0000O00000O000 ,OOO00O000O00O0OO0 in OOOOOO0000000O00O .iterrows ():#line:1103
        OO000OOOO0O0OOO0O ="专家打分-"+str (OOO00O000O00O0OO0 ["条目"])#line:1104
        OO0O0000O00O0O00O .loc [(OO0O0000O00O0O00O ["识别代码"]==OOO00O000O00O0OO0 ["序号"]),OO000OOOO0O0OOO0O ]=OOO00O000O00O0OO0 ["评分"]#line:1105
    del OO0O0000O00O0O00O ["专家打分-识别代码"]#line:1106
    del OO0O0000O00O0O00O ["专家打分-#####分隔符#########"]#line:1107
    try :#line:1108
        OO0O0000O00O0O00O =OO0O0000O00O0O00O .loc [:,~OO0O0000O00O0O00O .columns .str .contains ("^Unnamed")]#line:1109
    except :#line:1110
        pass #line:1111
    text .insert (END ,"\n正在计算总分，请稍候，已完成60%")#line:1112
    text .see (END )#line:1113
    OO0O0O00OO00O0OOO =O0O0O0O0O0000000O [0 ]#line:1116
    try :#line:1117
        O000O000O0O0O0O00 =str (OO0O0O00OO00O0OOO ).replace ("●(最终评分需导入)被抽出的所有数据.xls","")#line:1118
    except :#line:1119
        O000O000O0O0O0O00 =str (OO0O0O00OO00O0OOO )#line:1120
    O000O00OOOO00OO0O =pd .ExcelWriter (str (O000O000O0O0O0O00 )+"各评估对象打分核对文件"+".xlsx")#line:1128
    O00000O0OO0O0O000 .to_excel (O000O00OOOO00OO0O ,sheet_name ="原始打分")#line:1129
    O000O00OOOO00OO0O .close ()#line:1130
    OOOO0OO0OOOOOO000 =Tpinggu2 (OO0O0000O00O0O00O )#line:1134
    text .insert (END ,"\n正在计算总分，请稍候，已完成100%")#line:1136
    text .see (END )#line:1137
    showinfo (title ="提示信息",message ="打分计算成功，请查看文件："+str (O000O000O0O0O0O00 )+"最终打分"+".xlsx")#line:1138
    text .insert (END ,"\n打分计算成功，请查看文件："+str (OO0O0O00OO00O0OOO )+"最终打分"+".xls\n")#line:1139
    OOOO0OO0OOOOOO000 .reset_index (inplace =True )#line:1140
    text .insert (END ,"\n以下是结果概况：\n")#line:1141
    text .insert (END ,OOOO0OO0OOOOOO000 [["评估对象","总分"]])#line:1142
    text .see (END )#line:1143
    OOO0OOO00O0OO00OO =["评估对象","总分"]#line:1147
    for OOO0OO00O00O0000O in OOOO0OO0OOOOOO000 .columns :#line:1148
        if "专家打分"in OOO0OO00O00O0000O :#line:1149
            OOO0OOO00O0OO00OO .append (OOO0OO00O00O0000O )#line:1150
    OO0O00O00O000OOOO =OOOO0OO0OOOOOO000 [OOO0OOO00O0OO00OO ]#line:1151
    OO00O00O0O00000OO =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name =0 ,header =0 ,index_col =0 ).reset_index ()#line:1155
    if "专家打分-不良反应名称"in OOO0OOO00O0OO00OO :#line:1157
        OO00O00O0O00000OO =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="药品",header =0 ,index_col =0 ).reset_index ()#line:1158
    if "专家打分-化妆品名称"in OOO0OOO00O0OO00OO :#line:1160
        OO00O00O0O00000OO =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="化妆品",header =0 ,index_col =0 ).reset_index ()#line:1161
    if "专家打分-是否需要开展产品风险评价"in OOO0OOO00O0OO00OO :#line:1162
        OO00O00O0O00000OO =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="器械持有人",header =0 ,index_col =0 ).reset_index ()#line:1163
    for O0O0000O00000O000 ,OOO00O000O00O0OO0 in OO00O00O0O00000OO .iterrows ():#line:1164
        OOOOO0O00000000O0 ="专家打分-"+str (OOO00O000O00O0OO0 ["评分项"])#line:1165
        try :#line:1166
            warnings .filterwarnings ('ignore')#line:1167
            OO0O00O00O000OOOO .loc [-1 ,OOOOO0O00000000O0 ]=OOO00O000O00O0OO0 ["满分分值"]#line:1168
        except :#line:1169
            pass #line:1170
    del OO0O00O00O000OOOO ["专家打分-识别代码"]#line:1171
    OO0O00O00O000OOOO .iloc [-1 ,0 ]="满分分值"#line:1172
    OO0O00O00O000OOOO .loc [-1 ,"总分"]=100 #line:1173
    if "专家打分-事件原因分析.1"not in OOO0OOO00O0OO00OO :#line:1175
        OO0O00O00O000OOOO .loc [-1 ,"专家打分-报告时限"]=5 #line:1176
    if "专家打分-事件原因分析.1"in OOO0OOO00O0OO00OO :#line:1178
        OO0O00O00O000OOOO .loc [-1 ,"专家打分-报告时限"]=10 #line:1179
    OO0O00O00O000OOOO .columns =OO0O00O00O000OOOO .columns .str .replace ("专家打分-","",regex =False )#line:1182
    if ("专家打分-器械故障表现"in OOO0OOO00O0OO00OO )and ("modex"not in OO0O0000O00O0O00O .columns ):#line:1184
        OO0O00O00O000OOOO .loc [-1 ,"姓名和既往病史"]=2 #line:1185
        OO0O00O00O000OOOO .loc [-1 ,"报告日期"]=1 #line:1186
    else :#line:1187
        del OO0O00O00O000OOOO ["伤害"]#line:1188
    if "专家打分-化妆品名称"in OOO0OOO00O0OO00OO :#line:1190
        del OO0O00O00O000OOOO ["报告时限"]#line:1191
    try :#line:1194
        OO0O00O00O000OOOO =OO0O00O00O000OOOO [["评估对象","总分","伤害.1","是否开展了调查及调查情况","关联性评价","事件原因分析.1","是否需要开展产品风险评价","控制措施情况","是否为错报误报报告及错报误报说明","是否合并报告及合并报告编码","报告时限"]]#line:1195
    except :#line:1196
        pass #line:1197
    try :#line:1198
        OO0O00O00O000OOOO =OO0O00O00O000OOOO [["评估对象","总分","报告日期","报告人","联系人","联系电话","注册证编号/曾用注册证编号","产品名称","型号和规格","产品批号和产品编号","生产日期","有效期至","事件发生日期","发现或获知日期","伤害","伤害表现","器械故障表现","姓名和既往病史","年龄和年龄类型","性别","预期治疗疾病或作用","器械使用日期","使用场所和场所名称","使用过程","合并用药/械情况说明","事件原因分析和事件原因分析描述","初步处置情况","报告时限"]]#line:1199
    except :#line:1200
        pass #line:1201
    try :#line:1202
        OO0O00O00O000OOOO =OO0O00O00O000OOOO [["评估对象","总分","报告类型","报告时限","报告者及患者有关情况","原患疾病","药品信息","不良反应名称","ADR过程描述以及处理情况","关联性评价和ADR分析"]]#line:1203
    except :#line:1204
        pass #line:1205
    OO0O00000OOO0000O =pd .ExcelWriter (str (O000O000O0O0O0O00 )+"最终打分"+".xlsx")#line:1207
    OO0O00O00O000OOOO .to_excel (OO0O00000OOO0000O ,sheet_name ="最终打分")#line:1208
    OO0O00000OOO0000O .close ()#line:1209
    Ttree_Level_2 (OO0O00O00O000OOOO ,0 ,OOOO0OO0OOOOOO000 )#line:1211
def Tpinggu2 (OOO00O0OOOOOOOO0O ):#line:1214
    ""#line:1215
    OOO00O0OOOOOOOO0O ["报告数量小计"]=1 #line:1216
    if ("器械故障表现"in OOO00O0OOOOOOOO0O .columns )and ("modex"not in OOO00O0OOOOOOOO0O .columns ):#line:1219
        OOO00O0OOOOOOOO0O ["专家打分-姓名和既往病史"]=2 #line:1220
        OOO00O0OOOOOOOO0O ["专家打分-报告日期"]=1 #line:1221
        if "专家打分-报告时限情况"not in OOO00O0OOOOOOOO0O .columns :#line:1222
            OOO00O0OOOOOOOO0O ["报告时限"]=OOO00O0OOOOOOOO0O ["报告时限"].astype (float )#line:1223
            OOO00O0OOOOOOOO0O ["专家打分-报告时限"]=0 #line:1224
            OOO00O0OOOOOOOO0O .loc [(OOO00O0OOOOOOOO0O ["伤害"]=="死亡")&(OOO00O0OOOOOOOO0O ["报告时限"]<=7 ),"专家打分-报告时限"]=5 #line:1225
            OOO00O0OOOOOOOO0O .loc [(OOO00O0OOOOOOOO0O ["伤害"]=="严重伤害")&(OOO00O0OOOOOOOO0O ["报告时限"]<=20 ),"专家打分-报告时限"]=5 #line:1226
            OOO00O0OOOOOOOO0O .loc [(OOO00O0OOOOOOOO0O ["伤害"]=="其他")&(OOO00O0OOOOOOOO0O ["报告时限"]<=30 ),"专家打分-报告时限"]=5 #line:1227
    if "专家打分-事件原因分析.1"in OOO00O0OOOOOOOO0O .columns :#line:1231
       OOO00O0OOOOOOOO0O ["专家打分-报告时限"]=10 #line:1232
    OOOOO0OOO00OOOOOO =[]#line:1235
    for OO0OO000O00OO0OOO in OOO00O0OOOOOOOO0O .columns :#line:1236
        if "专家打分-"in OO0OO000O00OO0OOO :#line:1237
            OOOOO0OOO00OOOOOO .append (OO0OO000O00OO0OOO )#line:1238
    OO000OO0O0O0OO0OO =1 #line:1242
    for OO0OO000O00OO0OOO in OOOOO0OOO00OOOOOO :#line:1243
        O00O00000O0O0000O =OOO00O0OOOOOOOO0O .groupby (["质量评估模式"]).aggregate ({OO0OO000O00OO0OOO :"sum"}).reset_index ()#line:1244
        if OO000OO0O0O0OO0OO ==1 :#line:1245
            OO0O0O000O0OO0OOO =O00O00000O0O0000O #line:1246
            OO000OO0O0O0OO0OO =OO000OO0O0O0OO0OO +1 #line:1247
        else :#line:1248
            OO0O0O000O0OO0OOO =pd .merge (OO0O0O000O0OO0OOO ,O00O00000O0O0000O ,on ="质量评估模式",how ="left")#line:1249
    OOOO00000O0000O0O =OOO00O0OOOOOOOO0O .groupby (["质量评估模式"]).aggregate ({"报告数量小计":"sum"}).reset_index ()#line:1251
    OO0O0O000O0OO0OOO =pd .merge (OO0O0O000O0OO0OOO ,OOOO00000O0000O0O ,on ="质量评估模式",how ="left")#line:1252
    for OO0OO000O00OO0OOO in OOOOO0OOO00OOOOOO :#line:1255
        OO0O0O000O0OO0OOO [OO0OO000O00OO0OOO ]=round (OO0O0O000O0OO0OOO [OO0OO000O00OO0OOO ]/OO0O0O000O0OO0OOO ["报告数量小计"],2 )#line:1256
    OO0O0O000O0OO0OOO ["总分"]=round (OO0O0O000O0OO0OOO [OOOOO0OOO00OOOOOO ].sum (axis =1 ),2 )#line:1257
    OO0O0O000O0OO0OOO =OO0O0O000O0OO0OOO .sort_values (by =["总分"],ascending =False ,na_position ="last")#line:1258
    print (OO0O0O000O0OO0OOO )#line:1259
    warnings .filterwarnings ('ignore')#line:1260
    OO0O0O000O0OO0OOO .loc ["平均分(非加权)"]=round (OO0O0O000O0OO0OOO .mean (axis =0 ,numeric_only =True ),2 )#line:1261
    OO0O0O000O0OO0OOO .loc ["标准差(非加权)"]=round (OO0O0O000O0OO0OOO .std (axis =0 ,numeric_only =True ),2 )#line:1262
    OO0O0O000O0OO0OOO =OO0O0O000O0OO0OOO .rename (columns ={"质量评估模式":"评估对象"})#line:1263
    OO0O0O000O0OO0OOO .iloc [-2 ,0 ]="平均分(非加权)"#line:1264
    OO0O0O000O0OO0OOO .iloc [-1 ,0 ]="标准差(非加权)"#line:1265
    return OO0O0O000O0OO0OOO #line:1267
def Ttree_Level_2 (O00O0OOO00O0O000O ,OOOOO0OOOO0000OOO ,OOOO000000O0O0OOO ,*O0O0OO000OOO0OO00 ):#line:1270
    ""#line:1271
    OOOO0O0O0O0000O00 =O00O0OOO00O0O000O .columns .values .tolist ()#line:1273
    OOOOO0OOOO0000OOO =0 #line:1274
    O0O0O0O0O00O0O0O0 =O00O0OOO00O0O000O .loc [:]#line:1275
    OO00OO00O0OOOO0O0 =Toplevel ()#line:1278
    OO00OO00O0OOOO0O0 .title ("报表查看器")#line:1279
    O0OO0000O0O00OO00 =OO00OO00O0OOOO0O0 .winfo_screenwidth ()#line:1280
    O00000OO00O000O0O =OO00OO00O0OOOO0O0 .winfo_screenheight ()#line:1282
    OOO0OO000OOO000O0 =1300 #line:1284
    O000OO0O00O0O0O00 =600 #line:1285
    O0OOOOOO0O0O000OO =(O0OO0000O0O00OO00 -OOO0OO000OOO000O0 )/2 #line:1287
    OOO00O00O0O0OOOO0 =(O00000OO00O000O0O -O000OO0O00O0O0O00 )/2 #line:1288
    OO00OO00O0OOOO0O0 .geometry ("%dx%d+%d+%d"%(OOO0OO000OOO000O0 ,O000OO0O00O0O0O00 ,O0OOOOOO0O0O000OO ,OOO00O00O0O0OOOO0 ))#line:1289
    O00O0OOOO000OOO00 =ttk .Frame (OO00OO00O0OOOO0O0 ,width =1300 ,height =20 )#line:1290
    O00O0OOOO000OOO00 .pack (side =TOP )#line:1291
    OO00O0O00O00O0OOO =O0O0O0O0O00O0O0O0 .values .tolist ()#line:1294
    O0OOOOO000OO0O00O =O0O0O0O0O00O0O0O0 .columns .values .tolist ()#line:1295
    OO0OOO000O00O0OOO =ttk .Treeview (O00O0OOOO000OOO00 ,columns =O0OOOOO000OO0O00O ,show ="headings",height =45 )#line:1296
    for O000OO00O0OO0000O in O0OOOOO000OO0O00O :#line:1298
        OO0OOO000O00O0OOO .heading (O000OO00O0OO0000O ,text =O000OO00O0OO0000O )#line:1299
    for OOOOOOO00000OOO00 in OO00O0O00O00O0OOO :#line:1300
        OO0OOO000O00O0OOO .insert ("","end",values =OOOOOOO00000OOO00 )#line:1301
    for O0OOO0OOOOO0O00O0 in O0OOOOO000OO0O00O :#line:1302
        OO0OOO000O00O0OOO .column (O0OOO0OOOOO0O00O0 ,minwidth =0 ,width =120 ,stretch =NO )#line:1303
    O0O00O0O000O0OO00 =Scrollbar (O00O0OOOO000OOO00 ,orient ="vertical")#line:1305
    O0O00O0O000O0OO00 .pack (side =RIGHT ,fill =Y )#line:1306
    O0O00O0O000O0OO00 .config (command =OO0OOO000O00O0OOO .yview )#line:1307
    OO0OOO000O00O0OOO .config (yscrollcommand =O0O00O0O000O0OO00 .set )#line:1308
    O00OO0000000O0000 =Scrollbar (O00O0OOOO000OOO00 ,orient ="horizontal")#line:1310
    O00OO0000000O0000 .pack (side =BOTTOM ,fill =X )#line:1311
    O00OO0000000O0000 .config (command =OO0OOO000O00O0OOO .xview )#line:1312
    OO0OOO000O00O0OOO .config (yscrollcommand =O0O00O0O000O0OO00 .set )#line:1313
    def O000O0OOOOOO00OO0 (OOO0OO000000OOOOO ,OOOOO0OOOO00O00O0 ,O0O00O0O00OOO00OO ):#line:1315
        for OOO0O0O0O0000O0O0 in OO0OOO000O00O0OOO .selection ():#line:1318
            OO0O00O00O0O0O000 =OO0OOO000O00O0OOO .item (OOO0O0O0O0000O0O0 ,"values")#line:1319
        OOO000OOOOOO0O0O0 =OO0O00O00O0O0O000 [2 :]#line:1321
        O0000OO000000OO0O =O0O00O0O00OOO00OO .iloc [-1 ,:][2 :]#line:1324
        OOO0O0OOOO000OOO0 =O0O00O0O00OOO00OO .columns #line:1325
        OOO0O0OOOO000OOO0 =OOO0O0OOOO000OOO0 [2 :]#line:1326
        Tpo (O0000OO000000OO0O ,OOO000OOOOOO0O0O0 ,OOO0O0OOOO000OOO0 ,"失分","得分",OO0O00O00O0O0O000 [0 ])#line:1328
        return 0 #line:1329
    OO0OOO000O00O0OOO .bind ("<Double-1>",lambda OO000O0000O0O0O0O :O000O0OOOOOO00OO0 (OO000O0000O0O0O0O ,O0OOOOO000OO0O00O ,O0O0O0O0O00O0O0O0 ),)#line:1335
    def O0O000OO00OOOOO00 (O000O00OO0O0OOOO0 ,OOO0OO0OOOOO00OOO ,OO00O0OO000OO00O0 ):#line:1337
        O0OO00O0O00000OO0 =[(O000O00OO0O0OOOO0 .set (OOOOOO0O00OOOO00O ,OOO0OO0OOOOO00OOO ),OOOOOO0O00OOOO00O )for OOOOOO0O00OOOO00O in O000O00OO0O0OOOO0 .get_children ("")]#line:1338
        O0OO00O0O00000OO0 .sort (reverse =OO00O0OO000OO00O0 )#line:1339
        for O00O0OOO000OOOOOO ,(O0000OO0OOO000OOO ,O00O00O000000000O )in enumerate (O0OO00O0O00000OO0 ):#line:1341
            O000O00OO0O0OOOO0 .move (O00O00O000000000O ,"",O00O0OOO000OOOOOO )#line:1342
        O000O00OO0O0OOOO0 .heading (OOO0OO0OOOOO00OOO ,command =lambda :O0O000OO00OOOOO00 (O000O00OO0O0OOOO0 ,OOO0OO0OOOOO00OOO ,not OO00O0OO000OO00O0 ))#line:1345
    for OOO0O0O000O0OOO00 in O0OOOOO000OO0O00O :#line:1347
        OO0OOO000O00O0OOO .heading (OOO0O0O000O0OOO00 ,text =OOO0O0O000O0OOO00 ,command =lambda _col =OOO0O0O000O0OOO00 :O0O000OO00OOOOO00 (OO0OOO000O00O0OOO ,_col ,False ),)#line:1352
    OO0OOO000O00O0OOO .pack ()#line:1354
def Txuanze ():#line:1356
    ""#line:1357
    global ori #line:1358
    O00O0OOO0O0O0OOO0 =pd .read_excel (peizhidir +"0（范例）批量筛选.xls",sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1359
    text .insert (END ,"\n正在执行内部数据规整...\n")#line:1360
    text .insert (END ,O00O0OOO0O0O0OOO0 )#line:1361
    ori ["temppr"]=""#line:1362
    for OOOOO0OOO0O00O000 in O00O0OOO0O0O0OOO0 .columns .tolist ():#line:1363
        ori ["temppr"]=ori ["temppr"]+"----"+ori [OOOOO0OOO0O00O000 ]#line:1364
    OO0OO00OO0OOO0O00 ="测试字段MMMMM"#line:1365
    for OOOOO0OOO0O00O000 in O00O0OOO0O0O0OOO0 .columns .tolist ():#line:1366
        for OOO00OOOOO00OO000 in O00O0OOO0O0O0OOO0 [OOOOO0OOO0O00O000 ].drop_duplicates ():#line:1367
            if OOO00OOOOO00OO000 :#line:1368
                OO0OO00OO0OOO0O00 =OO0OO00OO0OOO0O00 +"|"+str (OOO00OOOOO00OO000 )#line:1369
    ori =ori .loc [ori ["temppr"].str .contains (OO0OO00OO0OOO0O00 ,na =False )].copy ()#line:1370
    del ori ["temppr"]#line:1371
    ori =ori .reset_index (drop =True )#line:1373
    text .insert (END ,"\n内部数据规整完毕。\n")#line:1374
def Tpo (O0O00O0O0O0000O0O ,OOOO00O0O000OOOOO ,O0O0O0O0OOOO0OOO0 ,O0OOO0OOO0OO0000O ,O00OOO0OOO0OOO00O ,OO0000O000O000O0O ):#line:1377
    ""#line:1378
    O0O00O0O0O0000O0O =O0O00O0O0O0000O0O .astype (float )#line:1379
    OOOO00O0O000OOOOO =tuple (float (O0O0OOOO00OO0OO0O )for O0O0OOOO00OO0OO0O in OOOO00O0O000OOOOO )#line:1380
    O00OO00O00O0OOO00 =Toplevel ()#line:1381
    O00OO00O00O0OOO00 .title (OO0000O000O000O0O )#line:1382
    O000OOOOO0OO00O00 =ttk .Frame (O00OO00O00O0OOO00 ,height =20 )#line:1383
    O000OOOOO0OO00O00 .pack (side =TOP )#line:1384
    OO0O0OO00OOOO0O00 =0.2 #line:1386
    OO00OO0O0O00O000O =Figure (figsize =(12 ,6 ),dpi =100 )#line:1387
    OO0O0OO0000OO0O0O =FigureCanvasTkAgg (OO00OO0O0O00O000O ,master =O00OO00O00O0OOO00 )#line:1388
    OO0O0OO0000OO0O0O .draw ()#line:1389
    OO0O0OO0000OO0O0O .get_tk_widget ().pack (expand =1 )#line:1390
    O0O0000O000O0OOOO =OO00OO0O0O00O000O .add_subplot (111 )#line:1391
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1393
    OOO000OOOOOO0OOO0 =NavigationToolbar2Tk (OO0O0OO0000OO0O0O ,O00OO00O00O0OOO00 )#line:1395
    OOO000OOOOOO0OOO0 .update ()#line:1396
    OO0O0OO0000OO0O0O .get_tk_widget ().pack ()#line:1398
    O0000OO0O0OOOO0O0 =range (0 ,len (O0O0O0O0OOOO0OOO0 ),1 )#line:1399
    O0O0000O000O0OOOO .set_xticklabels (O0O0O0O0OOOO0OOO0 ,rotation =-90 ,fontsize =8 )#line:1402
    O0O0000O000O0OOOO .bar (O0000OO0O0OOOO0O0 ,O0O00O0O0O0000O0O ,align ="center",tick_label =O0O0O0O0OOOO0OOO0 ,label =O0OOO0OOO0OO0000O )#line:1406
    O0O0000O000O0OOOO .bar (O0000OO0O0OOOO0O0 ,OOOO00O0O000OOOOO ,align ="center",label =O00OOO0OOO0OOO00O )#line:1407
    O0O0000O000O0OOOO .set_title (OO0000O000O000O0O )#line:1408
    O0O0000O000O0OOOO .set_xlabel ("项")#line:1409
    O0O0000O000O0OOOO .set_ylabel ("数量")#line:1410
    OO00OO0O0O00O000O .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:1413
    OOO00OOOO0O000O00 =O0O0000O000O0OOOO .get_position ()#line:1414
    O0O0000O000O0OOOO .set_position ([OOO00OOOO0O000O00 .x0 ,OOO00OOOO0O000O00 .y0 ,OOO00OOOO0O000O00 .width *0.7 ,OOO00OOOO0O000O00 .height ])#line:1415
    O0O0000O000O0OOOO .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:1416
    OO0O0OO0000OO0O0O .draw ()#line:1418
def helper ():#line:1421
    ""#line:1422
    O00O000O000O00O00 =Toplevel ()#line:1423
    O00O000O000O00O00 .title ("程序使用帮助")#line:1424
    O00O000O000O00O00 .geometry ("700x500")#line:1425
    OOO0O000000O00O00 =Scrollbar (O00O000O000O00O00 )#line:1427
    OO00OOO0O0000OO0O =Text (O00O000O000O00O00 ,height =80 ,width =150 ,bg ="#FFFFFF",font ="微软雅黑")#line:1428
    OOO0O000000O00O00 .pack (side =RIGHT ,fill =Y )#line:1429
    OO00OOO0O0000OO0O .pack ()#line:1430
    OOO0O000000O00O00 .config (command =OO00OOO0O0000OO0O .yview )#line:1431
    OO00OOO0O0000OO0O .config (yscrollcommand =OOO0O000000O00O00 .set )#line:1432
    OO00OOO0O0000OO0O .insert (END ,"\n                                             帮助文件\n\n\n为帮助用户快速熟悉“阅易评”使用方法，现以医疗器械不良事件报告表为例，对使用步骤作以下说明：\n\n第一步：原始数据准备\n用户登录国家医疗器械不良事件监测信息系统（https://maers.adrs.org.cn/），在“个例不良事件管理—报告浏览”页面，选择本次评估的报告范围（时间、报告状态、事发地监测机构等）后进行查询和导出。\n●注意：国家医疗器械不良事件监测信息系统设置每次导出数据上限为5000份报告，如查询发现需导出报告数量超限，需分次导出；如导出数据为压缩包，需先行解压。如原始数据在多个文件夹内，需先行整理到统一文件夹中，方便下一步操作。\n\n第二步：原始数据导入\n用户点击“导入原始数据”按钮，在弹出数据导入框中找到原始数据存储位置，本程序支持导入多个原始数据文件，可在长按键盘“Ctrl”按键的同时分别点击相关文件，选择完毕后点击“打开”按钮，程序会提示“数据读取成功”或“导入文件错误”。\n●注意：基于当前评估工作需要，仅针对使用单位报告进行评估，故导入数据时仅选择“使用单位、经营企业医疗器械不良事件报告”，不支持与“上市许可持有人医疗器械不良事件报告”混选。如提示“导入文件错误，请重试”，请重启程序并重新操作，如仍提示错误可与开发者联系（联系方式见文末）。\n\n第三步：报告抽样分组\n用户点击“随机抽样分组”按钮，在“随机抽样及随机分组”弹窗中：\n1、根据评估目的，在“评估对象”处勾选相应选项，可根据选项对上报单位（医疗机构）、县（区）、地市实施评估。注意：如果您是省级用户，被评估对象是各地市，您要关闭本软件，修改好配置表文件夹“0（范例）质量评估.xls”中的“地市列表”单元表，将本省地市参照范例填好再运行本软件。如果被评估对象不是选择“地市”，则无需该项操作。\n2、根据报告伤害类型依次输入需抽取的比例或报告数量。程序默认此处输入数值小于1（含1）为抽取比例，输入数值大于1为抽取报告数量，用户根据实际情况任选一种方式即可。本程序支持不同伤害类型报告选用不同抽样方式。\n3、根据参与评估专家数量，在“抽样后随机分组数”输入对应数字。\n4、抽样方法有2种，一种是最大覆盖，即对每个评估对象按抽样数量/比例进行单独抽样，如遇到不足则多抽（所以总体实际抽样数量可能会比设置的多一点），每个评估对象都会被抽到；另外一种是总体随机，即按照设定的参数从总体中随机抽取（有可能部分评估对象没有被抽到）。\n用户在确定抽样分组内容全部正确录入后，点击“最大覆盖”或者“总体随机”按钮，根据程序提示选择保存地址。程序将按照专家数量将抽取的报告进行随即分配，生成对应份数的“专家评分表”，专家评分表包含评分项、详细描述、评分、满分、打分标准等。专家评分表自动隐藏报告单位等信息，用户可随机将评分表派发给专家进行评分。\n●注意：为保护数据同时便于专家查看，需对专家评分表进行格式设置，具体操作如下（或者直接使用格式刷一键完成，模板详见配置表-专家模板）：全选表格，右键-设置单元格格式-对齐，勾选自动换行，之后设置好列间距。此外，请勿修改“专家评分表“和“（最终评分需导入）被抽出的所有数据”两类工作文件的文件名。\n\n第四步：评估得分统计\n用户在全部专家完成评分后，将所有专家评分表放置在同一文件夹中，点击“评估得分统计”按钮，全选所有专家评分表和“（最终评分需导入）被抽出的所有数据”这个文件，后点击“打开”，程序将首先进行评分内容校验，对于打分错误报告给与提示并生成错误定位文件，需根据提示修正错误再全部导入。如打分项无误，程序将提示“打分表导入成功，正在统计请耐心等待”，并生成最终的评分结果。\n\n本程序由广东省药品不良反应监测中心和佛山市药品不良反应监测中心共同制作，其他贡献单位包括广州市药品不良反应监测中心、深圳市药物警戒和风险管理研究院等。如有疑问，请联系我们：\n评估标准相关问题：广东省药品不良反应监测中心 张博涵 020-37886057\n程序运行相关问题：佛山市药品不良反应监测中心 蔡权周 0757-82580815 \n\n",)#line:1436
    OO00OOO0O0000OO0O .config (state =DISABLED )#line:1438
def TeasyreadT (O0000OO0OOO0OO000 ):#line:1441
    ""#line:1442
    O0000OO0OOO0OO000 ["#####分隔符#########"]="######################################################################"#line:1445
    O000000000OOOO0OO =O0000OO0OOO0OO000 .stack (dropna =False )#line:1446
    O000000000OOOO0OO =pd .DataFrame (O000000000OOOO0OO ).reset_index ()#line:1447
    O000000000OOOO0OO .columns =["序号","条目","详细描述"]#line:1448
    O000000000OOOO0OO ["逐条查看"]="逐条查看"#line:1449
    return O000000000OOOO0OO #line:1450
def Tget_list (OO0O0OOO0OO0O000O ):#line:1455
    ""#line:1456
    OO0O0OOO0OO0O000O =str (OO0O0OOO0OO0O000O )#line:1457
    OOO00OOOOO0O0O0OO =[]#line:1458
    OOO00OOOOO0O0O0OO .append (OO0O0OOO0OO0O000O )#line:1459
    OOO00OOOOO0O0O0OO =",".join (OOO00OOOOO0O0O0OO )#line:1460
    OOO00OOOOO0O0O0OO =OOO00OOOOO0O0O0OO .split (",")#line:1461
    OOO00OOOOO0O0O0OO =",".join (OOO00OOOOO0O0O0OO )#line:1462
    OOO00OOOOO0O0O0OO =OOO00OOOOO0O0O0OO .split ("，")#line:1463
    OOO0OOOO0O0OO0000 =OOO00OOOOO0O0O0OO [:]#line:1464
    OOO00OOOOO0O0O0OO =list (set (OOO00OOOOO0O0O0OO ))#line:1465
    OOO00OOOOO0O0O0OO .sort (key =OOO0OOOO0O0OO0000 .index )#line:1466
    return OOO00OOOOO0O0O0OO #line:1467
def thread_it (OO0O00OOO0O00O0OO ,*OOOO0O0O00OOOOOO0 ):#line:1470
    ""#line:1471
    OO0O0O00O0000O0O0 =threading .Thread (target =OO0O00OOO0O00O0OO ,args =OOOO0O0O00OOOOOO0 )#line:1473
    OO0O0O00O0000O0O0 .setDaemon (True )#line:1475
    OO0O0O00O0000O0O0 .start ()#line:1477
def showWelcome ():#line:1480
    ""#line:1481
    O0OO000OO00O0O000 =roox .winfo_screenwidth ()#line:1482
    O0OOOO0O00O0OO0O0 =roox .winfo_screenheight ()#line:1484
    roox .overrideredirect (True )#line:1486
    roox .attributes ("-alpha",1 )#line:1487
    O00OOO0OOOO0O000O =(O0OO000OO00O0O000 -475 )/2 #line:1488
    OOOOO0O0O0O000000 =(O0OOOO0O00O0OO0O0 -200 )/2 #line:1489
    roox .geometry ("675x140+%d+%d"%(O00OOO0OOOO0O000O ,OOOOO0O0O0O000000 ))#line:1491
    roox ["bg"]="royalblue"#line:1492
    OOO0O00OOO0000000 =Label (roox ,text ="阅易评",fg ="white",bg ="royalblue",font =("微软雅黑",35 ))#line:1495
    OOO0O00OOO0000000 .place (x =0 ,y =15 ,width =675 ,height =90 )#line:1496
    OOO0O000OO00O0O00 =Label (roox ,text ="                                 广东省药品不良反应监测中心                         V"+version_now ,fg ="white",bg ="cornflowerblue",font =("微软雅黑",15 ),)#line:1503
    OOO0O000OO00O0O00 .place (x =0 ,y =90 ,width =675 ,height =50 )#line:1504
def closeWelcome ():#line:1507
    ""#line:1508
    for OO0OO000O0O0OO0O0 in range (2 ):#line:1509
        root .attributes ("-alpha",0 )#line:1510
        time .sleep (1 )#line:1511
    root .attributes ("-alpha",1 )#line:1512
    roox .destroy ()#line:1513
root =Tk ()#line:1517
root .title ("阅易评 V"+version_now )#line:1518
try :#line:1519
    root .iconphoto (True ,PhotoImage (file =peizhidir +"0（范例）ico.png"))#line:1520
except :#line:1521
    pass #line:1522
sw_root =root .winfo_screenwidth ()#line:1523
sh_root =root .winfo_screenheight ()#line:1525
ww_root =700 #line:1527
wh_root =620 #line:1528
x_root =(sw_root -ww_root )/2 #line:1530
y_root =(sh_root -wh_root )/2 #line:1531
root .geometry ("%dx%d+%d+%d"%(ww_root ,wh_root ,x_root ,y_root ))#line:1532
root .configure (bg ="steelblue")#line:1533
try :#line:1536
    frame0 =ttk .Frame (root ,width =100 ,height =20 )#line:1537
    frame0 .pack (side =LEFT )#line:1538
    B_open_files1 =Button (frame0 ,text ="导入原始数据",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Topentable ,0 ),)#line:1551
    B_open_files1 .pack ()#line:1552
    B_open_files3 =Button (frame0 ,text ="随机抽样分组",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tchouyang ,ori ),)#line:1565
    B_open_files3 .pack ()#line:1566
    B_open_files3 =Button (frame0 ,text ="评估得分统计",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tpinggu ),)#line:1579
    B_open_files3 .pack ()#line:1580
    B_open_files3 =Button (frame0 ,text ="查看帮助文件",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (helper ),)#line:1593
    B_open_files3 .pack ()#line:1594
    B_open_files1 =Button (frame0 ,text ="更改评分标准",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Topentable ,123 ),)#line:1606
    B_open_files1 =Button (frame0 ,text ="内置数据清洗",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Txuanze ),)#line:1620
    if usergroup =="用户组=1":#line:1621
        B_open_files1 .pack ()#line:1622
    B_open_files1 =Button (frame0 ,text ="更改用户分组",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (display_random_number ))#line:1634
    if usergroup =="用户组=0":#line:1635
        B_open_files1 .pack ()#line:1636
except :#line:1638
    pass #line:1639
text =ScrolledText (root ,height =400 ,width =400 ,bg ="#FFFFFF",font ="微软雅黑")#line:1643
text .pack ()#line:1644
text .insert (END ,"\n    欢迎使用“阅易评”，本程序由广东省药品不良反应监测中心联合佛山市药品不良反应监测中心开发，主要功能包括：\n    1、根据报告伤害类型和用户自定义抽样比例对报告表随机抽样；\n    2、根据评估专家数量对抽出报告表随机分组，生成专家评分表；\n    3、根据专家最终评分实现自动汇总统计。\n    本程序供各监测机构免费使用，使用前请先查看帮助文件。\n  \n版本功能更新日志：\n2022年6月1日  支持医疗器械不良事件报告表质量评估(上报部分)。\n2022年10月31日  支持药品不良反应报告表质量评估。  \n2023年4月6日  支持化妆品不良反应报告表质量评估。\n2023年6月9日  支持医疗器械不良事件报告表质量评估(调查评价部分)。\n\n缺陷修正：20230609 修正结果列排序（按评分项目排序）。\n\n注：化妆品质量评估仅支持第一怀疑化妆品。",)#line:1649
text .insert (END ,"\n\n")#line:1650
setting_cfg =read_setting_cfg ()#line:1656
generate_random_file ()#line:1657
setting_cfg =open_setting_cfg ()#line:1658
if setting_cfg ["settingdir"]==0 :#line:1659
    showinfo (title ="提示",message ="未发现默认配置文件夹，请选择一个。如该配置文件夹中并无配置文件，将生成默认配置文件。")#line:1660
    filepathu =filedialog .askdirectory ()#line:1661
    path =get_directory_path (filepathu )#line:1662
    update_setting_cfg ("settingdir",path )#line:1663
setting_cfg =open_setting_cfg ()#line:1664
random_number =int (setting_cfg ["sidori"])#line:1665
input_number =int (str (setting_cfg ["sidfinal"])[0 :6 ])#line:1666
day_end =convert_and_compare_dates (str (setting_cfg ["sidfinal"])[6 :14 ])#line:1667
sid =random_number *2 +183576 #line:1668
if input_number ==sid and day_end =="未过期":#line:1669
    usergroup ="用户组=1"#line:1670
    text .insert (END ,usergroup +"   有效期至：")#line:1671
    text .insert (END ,datetime .strptime (str (int (int (str (setting_cfg ["sidfinal"])[6 :14 ])/4 )),"%Y%m%d"))#line:1672
else :#line:1673
    text .insert (END ,usergroup )#line:1674
text .insert (END ,"\n配置文件路径："+setting_cfg ["settingdir"]+"\n")#line:1675
peizhidir =str (setting_cfg ["settingdir"])+csdir .split ("pinggutools")[0 ][-1 ]#line:1676
roox =Toplevel ()#line:1680
tMain =threading .Thread (target =showWelcome )#line:1681
tMain .start ()#line:1682
t1 =threading .Thread (target =closeWelcome )#line:1683
t1 .start ()#line:1684
root .lift ()#line:1685
root .attributes ("-topmost",True )#line:1686
root .attributes ("-topmost",False )#line:1687
root .mainloop ()#line:1688
