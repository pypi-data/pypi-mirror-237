#!/usr/bin/env python
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
version_now ="0.0.3"#line:57
usergroup ="用户组=0"#line:58
setting_cfg =""#line:59
csdir =str (os .path .abspath (__file__ )).replace (str (__file__ ),"")#line:60
csdir =csdir +csdir .split ("pinggutools")[0 ][-1 ]#line:61
print (csdir )#line:62
def extract_zip_file (OOO00OO000OO0000O ,O0OOO00OO00OOO00O ):#line:70
    import zipfile #line:72
    if O0OOO00OO00OOO00O =="":#line:73
        return 0 #line:74
    with zipfile .ZipFile (OOO00OO000OO0000O ,'r')as O00OOO000O0O0OOO0 :#line:75
        for O0O0O0O000O0O0OOO in O00OOO000O0O0OOO0 .infolist ():#line:76
            O0O0O0O000O0O0OOO .filename =O0O0O0O000O0O0OOO .filename .encode ('cp437').decode ('gbk')#line:78
            O00OOO000O0O0OOO0 .extract (O0O0O0O000O0O0OOO ,O0OOO00OO00OOO00O )#line:79
def get_directory_path (O0000OO0OO00OO0OO ):#line:85
    global csdir #line:87
    if not (os .path .isfile (os .path .join (O0000OO0OO00OO0OO ,'0（范例）质量评估.xls'))):#line:89
        extract_zip_file (csdir +"def.py",O0000OO0OO00OO0OO )#line:94
    if O0000OO0OO00OO0OO =="":#line:96
        quit ()#line:97
    return O0000OO0OO00OO0OO #line:98
def convert_and_compare_dates (O0000O00OO0O0OO0O ):#line:102
    import datetime #line:103
    O0OO0OO0000O00O0O =datetime .datetime .now ()#line:104
    try :#line:106
       OOO0O0OO0OOOO0OO0 =datetime .datetime .strptime (str (int (int (O0000O00OO0O0OO0O )/4 )),"%Y%m%d")#line:107
    except :#line:108
        print ("fail")#line:109
        return "已过期"#line:110
    if OOO0O0OO0OOOO0OO0 >O0OO0OO0000O00O0O :#line:112
        return "未过期"#line:114
    else :#line:115
        return "已过期"#line:116
def read_setting_cfg ():#line:118
    global csdir #line:119
    if os .path .exists (csdir +'setting.cfg'):#line:121
        text .insert (END ,"已完成初始化\n")#line:122
        with open (csdir +'setting.cfg','r')as OO00O0OOO0O0O0OO0 :#line:123
            O0OOOOO0OOO0OO000 =eval (OO00O0OOO0O0O0OO0 .read ())#line:124
    else :#line:125
        OO00000O0O0OOOO00 =csdir +'setting.cfg'#line:127
        with open (OO00000O0O0OOOO00 ,'w')as OO00O0OOO0O0O0OO0 :#line:128
            OO00O0OOO0O0O0OO0 .write ('{"settingdir": 0, "sidori": 0, "sidfinal": "11111180000808"}')#line:129
        text .insert (END ,"未初始化，正在初始化...\n")#line:130
        O0OOOOO0OOO0OO000 =read_setting_cfg ()#line:131
    return O0OOOOO0OOO0OO000 #line:132
def open_setting_cfg ():#line:135
    global csdir #line:136
    with open (csdir +"setting.cfg","r")as OO0OO0OOO00O000O0 :#line:138
        OO000O0OO000O0OOO =eval (OO0OO0OOO00O000O0 .read ())#line:140
    return OO000O0OO000O0OOO #line:141
def update_setting_cfg (O00OOOOOOO00O0000 ,O00O0O00O0OO0OO0O ):#line:143
    global csdir #line:144
    with open (csdir +"setting.cfg","r")as O0000O00000O000O0 :#line:146
        O00OOOOOO00OOOOOO =eval (O0000O00000O000O0 .read ())#line:148
    if O00OOOOOO00OOOOOO [O00OOOOOOO00O0000 ]==0 or O00OOOOOO00OOOOOO [O00OOOOOOO00O0000 ]=="11111180000808":#line:150
        O00OOOOOO00OOOOOO [O00OOOOOOO00O0000 ]=O00O0O00O0OO0OO0O #line:151
        with open (csdir +"setting.cfg","w")as O0000O00000O000O0 :#line:153
            O0000O00000O000O0 .write (str (O00OOOOOO00OOOOOO ))#line:154
def generate_random_file ():#line:157
    O0000O0000O0OOO0O =random .randint (200000 ,299999 )#line:159
    update_setting_cfg ("sidori",O0000O0000O0OOO0O )#line:161
def display_random_number ():#line:163
    global csdir #line:164
    O00OO0O0O00OOOO0O =Toplevel ()#line:165
    O00OO0O0O00OOOO0O .title ("ID")#line:166
    OO00O0O000OO0O0O0 =O00OO0O0O00OOOO0O .winfo_screenwidth ()#line:168
    OO00000O0000OOO00 =O00OO0O0O00OOOO0O .winfo_screenheight ()#line:169
    OO0O0OO00O00O0000 =80 #line:171
    OO000O000OO00O0OO =70 #line:172
    O0000OOO0O0OOO0O0 =(OO00O0O000OO0O0O0 -OO0O0OO00O00O0000 )/2 #line:174
    OO00O000OOOOO0OOO =(OO00000O0000OOO00 -OO000O000OO00O0OO )/2 #line:175
    O00OO0O0O00OOOO0O .geometry ("%dx%d+%d+%d"%(OO0O0OO00O00O0000 ,OO000O000OO00O0OO ,O0000OOO0O0OOO0O0 ,OO00O000OOOOO0OOO ))#line:176
    with open (csdir +"setting.cfg","r")as O0O0O000OO00O0OOO :#line:179
        OO0OOOOOOOOO00000 =eval (O0O0O000OO00O0OOO .read ())#line:181
    OO00O0000OO0O00OO =int (OO0OOOOOOOOO00000 ["sidori"])#line:182
    O00000O000000000O =OO00O0000OO0O00OO *2 +183576 #line:183
    print (O00000O000000000O )#line:185
    O0O000O0OO00O0O00 =ttk .Label (O00OO0O0O00OOOO0O ,text =f"机器码: {OO00O0000OO0O00OO}")#line:187
    O00OO00OOO0O0OOO0 =ttk .Entry (O00OO0O0O00OOOO0O )#line:188
    O0O000O0OO00O0O00 .pack ()#line:191
    O00OO00OOO0O0OOO0 .pack ()#line:192
    ttk .Button (O00OO0O0O00OOOO0O ,text ="验证",command =lambda :check_input (O00OO00OOO0O0OOO0 .get (),O00000O000000000O )).pack ()#line:196
def check_input (OO0000OO00OO0O000 ,OO0O00O0OO00000O0 ):#line:198
    try :#line:202
        O0O00O00O0OOOOOOO =int (str (OO0000OO00OO0O000 )[0 :6 ])#line:203
        OO0OOO0O00000OOO0 =convert_and_compare_dates (str (OO0000OO00OO0O000 )[6 :14 ])#line:204
    except :#line:205
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:206
        return 0 #line:207
    if O0O00O00O0OOOOOOO ==OO0O00O0OO00000O0 and OO0OOO0O00000OOO0 =="未过期":#line:209
        update_setting_cfg ("sidfinal",OO0000OO00OO0O000 )#line:210
        showinfo (title ="提示",message ="注册成功,请重新启动程序。")#line:211
        quit ()#line:212
    else :#line:213
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:214
def update_software (OOO0O0O0000O0000O ):#line:219
    global version_now #line:221
    text .insert (END ,"当前版本为："+version_now +",正在检查更新...(您可以同时执行分析任务)")#line:222
    try :#line:223
        OO00OO00OO0000O00 =requests .get (f"https://pypi.org/pypi/{OOO0O0O0000O0000O}/json",timeout =2 ).json ()["info"]["version"]#line:224
    except :#line:225
        return "...更新失败。"#line:226
    if OO00OO00OO0000O00 >version_now :#line:227
        text .insert (END ,"\n最新版本为："+OO00OO00OO0000O00 +",正在尝试自动更新....")#line:228
        pip .main (['install',OOO0O0O0000O0000O ,'--upgrade'])#line:230
        text .insert (END ,"\n您可以开展工作。")#line:231
        return "...更新成功。"#line:232
def Topentable (OO0OO0000OO0OO0OO ):#line:235
    ""#line:236
    global ori #line:237
    global biaozhun #line:238
    global dishi #line:239
    OO0O0O0O00O00O0OO =[]#line:240
    OO000OOOOOOO0OO00 =[]#line:241
    OO000OO0O0000O000 =1 #line:242
    if OO0OO0000OO0OO0OO ==123 :#line:245
        try :#line:246
            O0O000O00OO0OOOO0 =filedialog .askopenfilename (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:249
            biaozhun =pd .read_excel (O0O000O00OO0OOOO0 ,sheet_name =0 ,header =0 ,index_col =0 ).reset_index ()#line:252
        except :#line:253
            showinfo (title ="提示",message ="配置表文件有误或您没有选择。")#line:254
            return 0 #line:255
        try :#line:256
            dishi =pd .read_excel (O0O000O00OO0OOOO0 ,sheet_name ="地市清单",header =0 ,index_col =0 ).reset_index ()#line:259
        except :#line:260
            showinfo (title ="提示",message ="您选择的配置文件没有地市列表或您没有选择。")#line:261
            return 0 #line:262
        if ("评分项"in biaozhun .columns and "打分标准"in biaozhun .columns and "专家序号"not in biaozhun .columns ):#line:267
            text .insert (END ,"\n您使用自定义的配置表。")#line:268
            text .see (END )#line:269
            showinfo (title ="提示",message ="您将使用自定义的配置表。")#line:270
            return 0 #line:271
        else :#line:272
            showinfo (title ="提示",message ="配置表文件有误，请正确选择。")#line:273
            biaozhun =""#line:274
            return 0 #line:275
    try :#line:278
        if OO0OO0000OO0OO0OO !=1 :#line:279
            OO00OOOOO0O0OO0OO =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:282
        if OO0OO0000OO0OO0OO ==1 :#line:283
            OO00OOOOO0O0OO0OO =filedialog .askopenfilenames (filetypes =[("XLSX",".xlsx"),("XLS",".xls")])#line:286
            for O0OOOOO00O0O00OOO in OO00OOOOO0O0OO0OO :#line:287
                if ("●专家评分表"in O0OOOOO00O0O00OOO )and ("●(最终评分需导入)被抽出的所有数据.xls"not in O0OOOOO00O0O00OOO ):#line:288
                    OO0O0O0O00O00O0OO .append (O0OOOOO00O0O00OOO )#line:289
                elif "●(最终评分需导入)被抽出的所有数据.xls"in O0OOOOO00O0O00OOO :#line:290
                    OO000OOOOOOO0OO00 .append (O0OOOOO00O0O00OOO )#line:291
                    OO0OO0OOOO0O0O0O0 =O0OOOOO00O0O00OOO .replace ("●(最终评分需导入)被抽出的所有数据","分数错误信息")#line:292
                    OO000OO0O0000O000 =0 #line:293
            if OO000OO0O0000O000 ==1 :#line:294
                showinfo (title ="提示",message ="请一并导入以下文件：●(最终评分需导入)被抽出的所有数据.xls")#line:296
                return 0 #line:297
            OO00OOOOO0O0OO0OO =OO0O0O0O00O00O0OO #line:298
        O00OO0OO000O00000 =[pd .read_excel (OOO0O00OO000O0O0O ,header =0 ,sheet_name =0 )for OOO0O00OO000O0O0O in OO00OOOOO0O0OO0OO ]#line:301
        ori =pd .concat (O00OO0OO000O00000 ,ignore_index =True ).drop_duplicates ().reset_index (drop =True )#line:302
        if "报告编码"in ori .columns or "报告表编码"in ori .columns :#line:304
            ori =ori .fillna ("-未填写-")#line:305
        if "报告类型-新的"in ori .columns :#line:308
            biaozhun =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="药品",header =0 ,index_col =0 ).reset_index ()#line:311
            ori ["报告编码"]=ori ["报告表编码"]#line:312
            text .insert (END ,"检测到导入的文件为药品报告，正在进行兼容性数据规整，请稍后...")#line:313
            ori =ori .rename (columns ={"医院名称":"单位名称"})#line:314
            ori =ori .rename (columns ={"报告地区名称":"使用单位、经营企业所属监测机构"})#line:315
            ori =ori .rename (columns ={"报告类型-严重程度":"伤害"})#line:316
            ori ["伤害"]=ori ["伤害"].str .replace ("一般","其他",regex =False )#line:317
            ori ["伤害"]=ori ["伤害"].str .replace ("严重","严重伤害",regex =False )#line:318
            ori .loc [(ori ["不良反应结果"]=="死亡"),"伤害"]="死亡"#line:319
            ori ["上报单位所属地区"]=ori ["使用单位、经营企业所属监测机构"]#line:320
            try :#line:321
                ori ["报告编码"]=ori ["唯一标识"]#line:322
            except :#line:323
                pass #line:324
            ori ["药品信息"]=""#line:328
            OO0O0O0O0O000O00O =0 #line:329
            OOOOO0O000OOO0OOO =len (ori ["报告编码"].drop_duplicates ())#line:330
            for O00O0OOOO000OOO0O in ori ["报告编码"].drop_duplicates ():#line:331
                OO0O0O0O0O000O00O =OO0O0O0O0O000O00O +1 #line:332
                O0OO0O0OOO0OOO000 =round (OO0O0O0O0O000O00O /OOOOO0O000OOO0OOO ,2 )#line:333
                try :#line:334
                    change_schedule (OO0O0O0O0O000O00O ,OOOOO0O000OOO0OOO )#line:335
                except :#line:336
                    if O0OO0O0OOO0OOO000 in [0.10 ,0.20 ,0.30 ,0.40 ,0.50 ,0.60 ,0.70 ,0.80 ,0.90 ,0.99 ]:#line:337
                        text .insert (END ,O0OO0O0OOO0OOO000 )#line:338
                        text .insert (END ,"...")#line:339
                OOO00OO000O0OO000 =ori [(ori ["报告编码"]==O00O0OOOO000OOO0O )].sort_values (by =["药品序号"]).reset_index ()#line:341
                for OO0OO0O0000OOOO00 ,OO0O0OO00O00O0O0O in OOO00OO000O0OO000 .iterrows ():#line:342
                    ori .loc [(ori ["报告编码"]==OO0O0OO00O00O0O0O ["报告编码"]),"药品信息"]=ori ["药品信息"]+"●药品序号："+str (OO0O0OO00O00O0O0O ["药品序号"])+" 性质："+str (OO0O0OO00O00O0O0O ["怀疑/并用"])+"\n批准文号:"+str (OO0O0OO00O00O0O0O ["批准文号"])+"\n商品名称："+str (OO0O0OO00O00O0O0O ["商品名称"])+"\n通用名称："+str (OO0O0OO00O00O0O0O ["通用名称"])+"\n剂型："+str (OO0O0OO00O00O0O0O ["剂型"])+"\n生产厂家："+str (OO0O0OO00O00O0O0O ["生产厂家"])+"\n生产批号："+str (OO0O0OO00O00O0O0O ["生产批号"])+"\n用量："+str (OO0O0OO00O00O0O0O ["用量"])+str (OO0O0OO00O00O0O0O ["用量单位"])+"，"+str (OO0O0OO00O00O0O0O ["用法-日"])+"日"+str (OO0O0OO00O00O0O0O ["用法-次"])+"次\n给药途径:"+str (OO0O0OO00O00O0O0O ["给药途径"])+"\n用药开始时间："+str (OO0O0OO00O00O0O0O ["用药开始时间"])+"\n用药终止时间："+str (OO0O0OO00O00O0O0O ["用药终止时间"])+"\n用药原因："+str (OO0O0OO00O00O0O0O ["用药原因"])+"\n"#line:343
            ori =ori .drop_duplicates ("报告编码")#line:344
        if "皮损部位"in ori .columns :#line:351
            biaozhun =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="化妆品",header =0 ,index_col =0 ).reset_index ()#line:354
            ori ["报告编码"]=ori ["报告表编号"]#line:355
            text .insert (END ,"检测到导入的文件为化妆品报告，正在进行兼容性数据规整，请稍后...")#line:356
            ori ["报告地区名称"]=ori ["报告单位名称"].astype (str )#line:358
            ori ["单位名称"]=ori ["报告单位名称"].astype (str )#line:360
            ori ["伤害"]=ori ["报告类型"].astype (str )#line:361
            ori ["伤害"]=ori ["伤害"].str .replace ("一般","其他",regex =False )#line:362
            ori ["伤害"]=ori ["伤害"].str .replace ("严重","严重伤害",regex =False )#line:363
            ori ["上报单位所属地区"]=ori ["报告地区名称"]#line:365
            try :#line:366
                ori ["报告编码"]=ori ["唯一标识"]#line:367
            except :#line:368
                pass #line:369
            text .insert (END ,"\n正在开展化妆品注册单位规整...")#line:370
            O00OO00OOO00O0000 =pd .read_excel (peizhidir +"0（范例）注册单位.xlsx",sheet_name ="机构列表",header =0 ,index_col =0 ,).reset_index ()#line:371
            for OO0OO0O0000OOOO00 ,OO0O0OO00O00O0O0O in O00OO00OOO00O0000 .iterrows ():#line:373
                ori .loc [(ori ["单位名称"]==OO0O0OO00O00O0O0O ["中文全称"]),"监测机构"]=OO0O0OO00O00O0O0O ["归属地区"]#line:374
                ori .loc [(ori ["单位名称"]==OO0O0OO00O00O0O0O ["中文全称"]),"市级监测机构"]=OO0O0OO00O00O0O0O ["地市"]#line:375
            ori ["监测机构"]=ori ["监测机构"].fillna ("未规整")#line:376
            ori ["市级监测机构"]=ori ["市级监测机构"].fillna ("未规整")#line:377
        try :#line:380
                text .insert (END ,"\n开展报告单位和监测机构名称规整...")#line:381
                OOOOOOOO00O0O000O =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="报告单位",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:382
                O00OO00OOO00O0000 =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="监测机构",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:383
                OOO000O0O000OO000 =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="地市清单",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:384
                for OO0OO0O0000OOOO00 ,OO0O0OO00O00O0O0O in OOOOOOOO00O0O000O .iterrows ():#line:385
                        ori .loc [(ori ["单位名称"]==OO0O0OO00O00O0O0O ["曾用名1"]),"单位名称"]=OO0O0OO00O00O0O0O ["单位名称"]#line:386
                        ori .loc [(ori ["单位名称"]==OO0O0OO00O00O0O0O ["曾用名2"]),"单位名称"]=OO0O0OO00O00O0O0O ["单位名称"]#line:387
                        ori .loc [(ori ["单位名称"]==OO0O0OO00O00O0O0O ["曾用名3"]),"单位名称"]=OO0O0OO00O00O0O0O ["单位名称"]#line:388
                        ori .loc [(ori ["单位名称"]==OO0O0OO00O00O0O0O ["曾用名4"]),"单位名称"]=OO0O0OO00O00O0O0O ["单位名称"]#line:389
                        ori .loc [(ori ["单位名称"]==OO0O0OO00O00O0O0O ["曾用名5"]),"单位名称"]=OO0O0OO00O00O0O0O ["单位名称"]#line:390
                        ori .loc [(ori ["单位名称"]==OO0O0OO00O00O0O0O ["单位名称"]),"使用单位、经营企业所属监测机构"]=OO0O0OO00O00O0O0O ["监测机构"]#line:393
                for OO0OO0O0000OOOO00 ,OO0O0OO00O00O0O0O in O00OO00OOO00O0000 .iterrows ():#line:395
                        ori .loc [(ori ["使用单位、经营企业所属监测机构"]==OO0O0OO00O00O0O0O ["曾用名1"]),"使用单位、经营企业所属监测机构"]=OO0O0OO00O00O0O0O ["监测机构"]#line:396
                        ori .loc [(ori ["使用单位、经营企业所属监测机构"]==OO0O0OO00O00O0O0O ["曾用名2"]),"使用单位、经营企业所属监测机构"]=OO0O0OO00O00O0O0O ["监测机构"]#line:397
                        ori .loc [(ori ["使用单位、经营企业所属监测机构"]==OO0O0OO00O00O0O0O ["曾用名3"]),"使用单位、经营企业所属监测机构"]=OO0O0OO00O00O0O0O ["监测机构"]#line:398
                for O0O0OO0000O0O0O0O in OOO000O0O000OO000 ["地市列表"]:#line:400
                        ori .loc [(ori ["上报单位所属地区"].str .contains (O0O0OO0000O0O0O0O ,na =False )),"市级监测机构"]=O0O0OO0000O0O0O0O #line:401
                ori .loc [(ori ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构"]="佛山"#line:402
        except :#line:404
                text .insert (END ,"\n报告单位和监测机构名称规整失败.")#line:405
    except :#line:407
        showinfo (title ="提示",message ="导入文件错误,请重试。")#line:408
        return 0 #line:409
    try :#line:412
        ori =ori .loc [:,~ori .columns .str .contains ("Unnamed")]#line:413
    except :#line:414
        pass #line:415
    try :#line:416
        ori ["报告编码"]=ori ["报告编码"].astype (str )#line:417
    except :#line:418
        pass #line:419
    ori =ori .sample (frac =1 ).copy ()#line:422
    ori .reset_index (inplace =True )#line:423
    text .insert (END ,"\n数据读取成功，行数："+str (len (ori )))#line:424
    text .see (END )#line:425
    if OO0OO0000OO0OO0OO ==0 :#line:428
        if "报告编码"not in ori .columns :#line:429
            showinfo (title ="提示信息",message ="\n在校验过程中，发现您导入的并非原始报告数据，请重新导入。")#line:430
        else :#line:431
            showinfo (title ="提示信息",message ="\n数据读取成功。")#line:432
        return 0 #line:433
    O0O0OOOOO0OOO0O0O =ori .copy ()#line:436
    OOO00O00OO00OOO00 ={}#line:437
    O0O0O0OOO0O00O000 =0 #line:438
    if "专家序号"not in O0O0OOOOO0OOO0O0O .columns :#line:439
        showinfo (title ="提示信息",message ="您导入的并非专家评分文件，请重新导入。")#line:440
        return 0 #line:441
    for OO0OO0O0000OOOO00 ,OO0O0OO00O00O0O0O in O0O0OOOOO0OOO0O0O .iterrows ():#line:442
        OO00000000O000O00 ="专家打分-"+str (OO0O0OO00O00O0O0O ["条目"])#line:443
        try :#line:444
            float (OO0O0OO00O00O0O0O ["评分"])#line:445
            float (OO0O0OO00O00O0O0O ["满分"])#line:446
        except :#line:447
            showinfo (title ="错误提示",message ="因专家评分或满分值输入的不是数字，导致了程序中止，请修正："+"专家序号："+str (int (OO0O0OO00O00O0O0O ["专家序号"]))+"，报告序号："+str (int (OO0O0OO00O00O0O0O ["序号"]))+OO0O0OO00O00O0O0O ["条目"],)#line:456
            ori =0 #line:457
        if float (OO0O0OO00O00O0O0O ["评分"])>float (OO0O0OO00O00O0O0O ["满分"])or float (OO0O0OO00O00O0O0O ["评分"])<0 :#line:458
            OOO00O00OO00OOO00 [str (OO0OO0O0000OOOO00 )]=("专家序号："+str (int (OO0O0OO00O00O0O0O ["专家序号"]))+"；  报告序号："+str (int (OO0O0OO00O00O0O0O ["序号"]))+OO0O0OO00O00O0O0O ["条目"])#line:465
            O0O0O0OOO0O00O000 =1 #line:466
    if O0O0O0OOO0O00O000 ==1 :#line:468
        OO0OOOO0O00O00O0O =pd .DataFrame (list (OOO00O00OO00OOO00 .items ()),columns =["错误编号","错误信息"])#line:469
        del OO0OOOO0O00O00O0O ["错误编号"]#line:470
        OOOO00O00O0OOO000 =OO0OO0OOOO0O0O0O0 #line:471
        OO0OOOO0O00O00O0O =OO0OOOO0O00O00O0O .sort_values (by =["错误信息"],ascending =True ,na_position ="last")#line:472
        O0O00OO00OOOOO0O0 =pd .ExcelWriter (OOOO00O00O0OOO000 )#line:473
        OO0OOOO0O00O00O0O .to_excel (O0O00OO00OOOOO0O0 ,sheet_name ="字典数据")#line:474
        O0O00OO00OOOOO0O0 .close ()#line:475
        showinfo (title ="警告",message ="经检查，部分专家的打分存在错误。请您修正错误的打分文件再重新导入全部的专家打分文件。详见:分数错误信息.xls",)#line:479
        text .insert (END ,"\n经检查，部分专家的打分存在错误。详见:分数错误信息.xls。请您修正错误的打分文件再重新导入全部的专家打分文件。")#line:480
        text .insert (END ,"\n以下是错误信息概况：\n")#line:481
        text .insert (END ,OO0OOOO0O00O00O0O )#line:482
        text .see (END )#line:483
        return 0 #line:484
    if OO0OO0000OO0OO0OO ==1 :#line:487
        return ori ,OO000OOOOOOO0OO00 #line:488
def Tchouyang (O0OO00O00O0O0000O ):#line:491
    ""#line:492
    try :#line:494
        if O0OO00O00O0O0000O ==0 :#line:495
            showinfo (title ="提示",message ="您尚未导入原始数据。")#line:496
            return 0 #line:497
    except :#line:498
        pass #line:499
    if "详细描述"in O0OO00O00O0O0000O .columns :#line:500
        showinfo (title ="提示",message ="目前工作文件为专家评分文件，请导入原始数据进行抽样。")#line:501
        return 0 #line:502
    OOO0OO0O0OO00OOO0 =Toplevel ()#line:505
    OOO0OO0O0OO00OOO0 .title ("随机抽样及随机分组")#line:506
    OO0OOOO00O0OO0O0O =OOO0OO0O0OO00OOO0 .winfo_screenwidth ()#line:507
    OO0OOOOO0OO000000 =OOO0OO0O0OO00OOO0 .winfo_screenheight ()#line:509
    O0OO0000000OOOO00 =300 #line:511
    OOOO00OOOOO00OOO0 =220 #line:512
    O00000OOOO00OO0OO =(OO0OOOO00O0OO0O0O -O0OO0000000OOOO00 )/1.7 #line:514
    O00OO000O000O000O =(OO0OOOOO0OO000000 -OOOO00OOOOO00OOO0 )/2 #line:515
    OOO0OO0O0OO00OOO0 .geometry ("%dx%d+%d+%d"%(O0OO0000000OOOO00 ,OOOO00OOOOO00OOO0 ,O00000OOOO00OO0OO ,O00OO000O000O000O ))#line:516
    OO0O0OOO0OO00OOO0 =Label (OOO0OO0O0OO00OOO0 ,text ="评估对象：")#line:518
    OO0O0OOO0OO00OOO0 .grid (row =1 ,column =0 ,sticky ="w")#line:519
    O0O0OOO0000OO0O00 =StringVar ()#line:520
    OOO0000000000OOOO =ttk .Combobox (OOO0OO0O0OO00OOO0 ,width =25 ,height =10 ,state ="readonly",textvariable =O0O0OOO0000OO0O00 )#line:523
    OOO0000000000OOOO ["values"]=["上报单位","县区","地市","省级审核人","上市许可持有人"]#line:524
    OOO0000000000OOOO .current (0 )#line:525
    OOO0000000000OOOO .grid (row =2 ,column =0 )#line:526
    O00O0O00O0OO00O00 =Label (OOO0OO0O0OO00OOO0 ,text ="-----------------------------------------")#line:528
    O00O0O00O0OO00O00 .grid (row =3 ,column =0 ,sticky ="w")#line:529
    OO0OOO0O00O00000O =Label (OOO0OO0O0OO00OOO0 ,text ="死亡报告抽样数量（>1)或比例(<=1)：")#line:531
    OO0OOO0O00O00000O .grid (row =4 ,column =0 ,sticky ="w")#line:532
    O0O0O0OO0O0O0O000 =Entry (OOO0OO0O0OO00OOO0 ,width =10 )#line:533
    O0O0O0OO0O0O0O000 .grid (row =4 ,column =1 ,sticky ="w")#line:534
    OOOO000O00O0O00OO =Label (OOO0OO0O0OO00OOO0 ,text ="严重报告抽样数量（>1)或比例(<=1)：")#line:536
    OOOO000O00O0O00OO .grid (row =6 ,column =0 ,sticky ="w")#line:537
    O00000O000OOOO00O =Entry (OOO0OO0O0OO00OOO0 ,width =10 )#line:538
    O00000O000OOOO00O .grid (row =6 ,column =1 ,sticky ="w")#line:539
    OOOO00OO0OOO0O00O =Label (OOO0OO0O0OO00OOO0 ,text ="一般报告抽样数量（>1)或比例(<=1)：")#line:541
    OOOO00OO0OOO0O00O .grid (row =8 ,column =0 ,sticky ="w")#line:542
    OOO0OO00OO0O00OO0 =Entry (OOO0OO0O0OO00OOO0 ,width =10 )#line:543
    OOO0OO00OO0O00OO0 .grid (row =8 ,column =1 ,sticky ="w")#line:544
    O00O0O00O0OO00O00 =Label (OOO0OO0O0OO00OOO0 ,text ="-----------------------------------------")#line:546
    O00O0O00O0OO00O00 .grid (row =9 ,column =0 ,sticky ="w")#line:547
    O0OO0000O0OO0O000 =Label (OOO0OO0O0OO00OOO0 ,text ="抽样后随机分组数（专家数量）：")#line:549
    OOO0O0000OO000000 =Entry (OOO0OO0O0OO00OOO0 ,width =10 )#line:550
    O0OO0000O0OO0O000 .grid (row =10 ,column =0 ,sticky ="w")#line:551
    OOO0O0000OO000000 .grid (row =10 ,column =1 ,sticky ="w")#line:552
    OOO00O000OO0OO0OO =Button (OOO0OO0O0OO00OOO0 ,text ="最大覆盖",width =12 ,command =lambda :thread_it (Tdoing0 ,O0OO00O00O0O0000O ,OOO0OO00OO0O00OO0 .get (),O00000O000OOOO00O .get (),O0O0O0OO0O0O0O000 .get (),OOO0O0000OO000000 .get (),OOO0000000000OOOO .get (),"最大覆盖",1 ,),)#line:569
    OOO00O000OO0OO0OO .grid (row =13 ,column =1 ,sticky ="w")#line:570
    OOO0000OO0OOOO0OO =Button (OOO0OO0O0OO00OOO0 ,text ="总体随机",width =12 ,command =lambda :thread_it (Tdoing0 ,O0OO00O00O0O0000O ,OOO0OO00OO0O00OO0 .get (),O00000O000OOOO00O .get (),O0O0O0OO0O0O0O000 .get (),OOO0O0000OO000000 .get (),OOO0000000000OOOO .get (),"总体随机",1 ))#line:571
    OOO0000OO0OOOO0OO .grid (row =13 ,column =0 ,sticky ='w')#line:572
def Tdoing0 (O000O000O0O00O000 ,O0000000OOOO00O0O ,O0000OO0OOO0O00O0 ,OO0O0OOOO0OO0000O ,OO00OO0O0OOOOO0OO ,O00O00OOO0O0OOOO0 ,OO0O000O000OOOOOO ,OO0O00000O0O000OO ):#line:578
    ""#line:579
    global dishi #line:580
    global biaozhun #line:581
    if (O0000000OOOO00O0O ==""or O0000OO0OOO0O00O0 ==""or OO0O0OOOO0OO0000O ==""or OO00OO0O0OOOOO0OO ==""or O00O00OOO0O0OOOO0 ==""or OO0O000O000OOOOOO ==""):#line:591
        showinfo (title ="提示信息",message ="参数设置不完整。")#line:592
        return 0 #line:593
    if O00O00OOO0O0OOOO0 =="上报单位":#line:594
        O00O00OOO0O0OOOO0 ="单位名称"#line:595
    if O00O00OOO0O0OOOO0 =="县区":#line:596
        O00O00OOO0O0OOOO0 ="使用单位、经营企业所属监测机构"#line:597
    if O00O00OOO0O0OOOO0 =="地市":#line:598
        O00O00OOO0O0OOOO0 ="市级监测机构"#line:599
    if O00O00OOO0O0OOOO0 =="省级审核人":#line:600
        O00O00OOO0O0OOOO0 ="审核人.1"#line:601
        O000O000O0O00O000 ["modex"]=1 #line:602
        O000O000O0O00O000 ["审核人.1"]=O000O000O0O00O000 ["审核人.1"].fillna ("未填写")#line:603
    if O00O00OOO0O0OOOO0 =="上市许可持有人":#line:604
        O00O00OOO0O0OOOO0 ="上市许可持有人名称"#line:605
        O000O000O0O00O000 ["modex"]=1 #line:606
        O000O000O0O00O000 ["上市许可持有人名称"]=O000O000O0O00O000 ["上市许可持有人名称"].fillna ("未填写")#line:607
    if OO0O00000O0O000OO ==1 :#line:609
        if len (biaozhun )==0 :#line:610
            OO00OOOO00OO0O000 =peizhidir +"0（范例）质量评估.xls"#line:611
            try :#line:612
                if "modex"in O000O000O0O00O000 .columns :#line:613
                    OOO000000OOOOO00O =pd .read_excel (OO00OOOO00OO0O000 ,sheet_name ="器械持有人",header =0 ,index_col =0 ).reset_index ()#line:614
                else :#line:615
                    OOO000000OOOOO00O =pd .read_excel (OO00OOOO00OO0O000 ,sheet_name =0 ,header =0 ,index_col =0 ).reset_index ()#line:616
                text .insert (END ,"\n您使用配置表文件夹中的“0（范例）质量评估.xls“作为评分标准。")#line:617
                text .see (END )#line:618
            except :#line:621
                OOO000000OOOOO00O =pd .DataFrame ({"评分项":{0 :"识别代码",1 :"报告人",2 :"联系人",3 :"联系电话",4 :"注册证编号/曾用注册证编号",5 :"产品名称",6 :"型号和规格",7 :"产品批号和产品编号",8 :"生产日期",9 :"有效期至",10 :"事件发生日期",11 :"发现或获知日期",12 :"伤害",13 :"伤害表现",14 :"器械故障表现",15 :"年龄和年龄类型",16 :"性别",17 :"预期治疗疾病或作用",18 :"器械使用日期",19 :"使用场所和场所名称",20 :"使用过程",21 :"合并用药/械情况说明",22 :"事件原因分析和事件原因分析描述",23 :"初步处置情况",},"打分标准":{0 :"",1 :"填写人名或XX科室，得1分",2 :"填写报告填报人员姓名或XX科X医生，得1分",3 :"填写报告填报人员移动电话或所在科室固定电话，得1分",4 :"可利用国家局数据库检索，注册证号与产品名称及事件描述相匹配的，得8分",5 :"可利用国家局数据库检索，注册证号与产品名称及事件描述相匹配的，得4分",6 :"规格和型号任填其一，且内容正确，得4分",7 :"产品批号和编号任填其一，且内容正确，,得4分。\n注意：（1）如果该器械使用年限久远，或在院外用械，批号或编号无法查询追溯的，报告表“使用过程”中给予说明的，得4分；（2）出现YZB格式、YY格式、GB格式等产品标准格式，或“XX生产许XX”等许可证号，得0分；（3）出现和注册证号一样的数字，得0分。",8 :"确保“生产日期”和“有效期至”逻辑正确，“有效期至”晚于“生产日期”，且两者时间间隔应为整月或整年，得2分。",9 :"确保生产日期和有效期逻辑正确。\n注意：如果该器械是使用年限久远的（2014年之前生产产品），或在院外用械，生产日期和有效期无法查询追溯的，并在报告表“使用过程”中给予说明的，该项得4分",10 :"指发生医疗器械不良事件的日期，应与使用过程描述一致，如仅知道事件发生年份，填写当年的1月1日；如仅知道年份和月份，填写当月的第1日；如年月日均未知，填写事件获知日期，并在“使用过程”给予说明。填写正确得2分。\n注意：“事件发生日期”早于“器械使用日期”的，得0分。",11 :"指报告单位发现或知悉该不良事件的日期，填写正确得5分。\n注意：“发现或获知日期”早于“事件发生日期”的，或者早于使用日期的，得0分。",12 :"分为“死亡”、“严重伤害”“其他”，判断正确，得8分。",13 :"描述准确且简明，或者勾选的术语贴切的，得6分；描述较为准确且简明，或选择术语较为贴切，或描述准确但不够简洁，得3分；描述冗长、填成器械故障表现的，得0分。\n注意：对于“严重伤害”事件，需写明实际导致的严重伤害，填写不恰当的或填写“无”的，得0分。伤害表现描述与使用过程中关于伤害的描述不一致的，得0分。对于“其他”未对患者造成伤害的，该项可填“无”或未填写，默认得6分。",14 :"描述准确而简明，或者勾选的术语贴切的，得6分；描述较为准确，或选择术语较为贴切，或描述准确但不够简洁，得3分；描述冗长、填成伤害表现的，得0分。故障表现与使用过程中关于器械故障的描述不一致的，得0分。\n注意：对于不存在器械故障但仍然对患者造成了伤害的，在伤害表现处填写了对应伤害，该项填“无”，默认得6分。",15 :"医疗器械若未用于患者或者未造成患者伤害的，患者信息非必填项，默认得1分。",16 :"医疗器械若未用于患者或者未造成患者伤害的，患者信息非必填项，默认得1分。",17 :"指涉及医疗器械的用途或适用范围，如治疗类医疗器械的预期治疗疾病，检验检查类、辅助治疗类医疗器械的预期作用等。填写完整准确，得4分；未填写、填写不完整或填写错误，得0分。",18 :"需与使用过程描述的日期一致，若器械使用日期和不良事件发生日期不是同一天，填成“不良事件发生日期”的，得0分；填成“有源设备启用日期”的，得0分。如仅知道事件使用年份，填写当年的1月1日；如仅知道年份和月份，填写当月的第1日；如年月日均未知，填写事件获知日期，并在“使用过程”给予说明。",19 :"使用场所为“医疗机构”的，场所名称可以为空，默认得2分；使用场所为“家庭”或“其他”，但勾选为医疗机构的，得0分；如使用场所为“其他”，没有填写实际使用场所或填写错误的，得0分。",20 :"按照以下四个要素进行评分：\n（1）具体操作使用情况（5分）\n详细描述具体操作人员资质、操作使用过程等信息，对于体外诊断医疗器械应填写患者诊疗信息（如疾病情况、用药情况）、样品检测过程与结果等信息。该要素描述准确完整的，得5分；较完整准确的，得2.5分；要素缺失的，得0分。\n（2）不良事件情况（5分）\n详细描述使用过程中出现的非预期结果等信息，对于体外诊断医疗器械应填写发现的异常检测情况，该要素描述完整准确的，得5分；较完整准确的，得2.5分；要素缺失的，得0分。\n（3）对受害者的影响（4分）\n详细描述该事件（可能）对患者造成的伤害，（可能）对临床诊疗造成的影响。有实际伤害的事件，需写明对受害者的伤害情况，包括必要的体征（如体温、脉搏、血压、皮损程度、失血情况等）和相关检查结果（如血小板检查结果）；对于可能造成严重伤害的事件，需写明可能对患者或其他人员造成的伤害。该要素描述完整准确的，得4分；较完整准确的，得2分；要素缺失的，得0分。\n（4）采取的治疗措施及结果（4分）\n有实际伤害的情况，须写明对伤者采取的治疗措施（包括用药、用械、或手术治疗等，及采取各个治疗的时间），以及采取治疗措施后的转归情况。该要素描述完整准确得4分，较完整准确得2分，描述过于笼统简单，如描述为“对症治疗”、“报告医生”、“转院”等，或者要素缺失的，得0分；无实际伤害的，该要素默认得4分。",21 :"有合并用药/械情况但没有填写此项的，得0分；填写不完整的，得2分；评估认为该不良事件过程中不存在合并用药/械情况的，该项不填写可得4分。\n如：输液泵泵速不准，合并用药/械情况应写明输注的药液、并用的输液器信息等。",22 :"原因分析不正确，如对于产品原因（包括说明书等）、操作原因 、患者自身原因 、无法确定的勾选与原因分析的描述的内容不匹配的，得0分，例如勾选了产品原因，但描述中说明该事件可能是未按照说明书要求进行操作导致（操作原因）；原因分析正确，但原因分析描述填成使用过程或者处置方式的，得2分。",23 :"包含产品的初步处置措施和对患者的救治措施等，填写完整得2分，部分完整得1分，填写过于简单得0分。",},"满分分值":{0 :0 ,1 :1 ,2 :1 ,3 :1 ,4 :8 ,5 :4 ,6 :4 ,7 :4 ,8 :2 ,9 :2 ,10 :2 ,11 :5 ,12 :8 ,13 :6 ,14 :6 ,15 :1 ,16 :1 ,17 :4 ,18 :2 ,19 :2 ,20 :18 ,21 :4 ,22 :4 ,23 :2 ,},})#line:703
                text .insert (END ,"\n您使用软件内置的评分标准。")#line:704
                text .see (END )#line:705
            try :#line:707
                dishi =pd .read_excel (OO00OOOO00OO0O000 ,sheet_name ="地市清单",header =0 ,index_col =0 ).reset_index ()#line:710
                text .insert (END ,"\n找到地市清单，将规整地市名称。")#line:711
                for OOO0O0O000000O00O in dishi ["地市列表"]:#line:712
                    O000O000O0O00O000 .loc [(O000O000O0O00O000 ["上报单位所属地区"].str .contains (OOO0O0O000000O00O ,na =False )),"市级监测机构",]=OOO0O0O000000O00O #line:716
                    O000O000O0O00O000 .loc [(O000O000O0O00O000 ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构",]="佛山"#line:720
                    O000O000O0O00O000 .loc [(O000O000O0O00O000 ["市级监测机构"].str .contains ("北海",na =False )),"市级监测机构",]="北海"#line:727
                    O000O000O0O00O000 .loc [(O000O000O0O00O000 ["联系地址"].str .contains ("北海市",na =False )),"市级监测机构",]="北海"#line:731
                text .see (END )#line:732
            except :#line:733
                text .insert (END ,"\n未找到地市清单或清单有误，不对地市名称进行规整，未维护产品的报表的地市名称将以“未填写”的形式展现。")#line:734
                text .see (END )#line:735
        else :#line:736
            OOO000000OOOOO00O =biaozhun .copy ()#line:737
            if len (dishi )!=0 :#line:738
                try :#line:739
                    text .insert (END ,"\n找到自定义的地市清单，将规整地市名称。")#line:740
                    for OOO0O0O000000O00O in dishi ["地市列表"]:#line:741
                        O000O000O0O00O000 .loc [(O000O000O0O00O000 ["使用单位、经营企业所属监测机构"].str .contains (OOO0O0O000000O00O ,na =False )),"市级监测机构",]=OOO0O0O000000O00O #line:745
                    O000O000O0O00O000 .loc [(O000O000O0O00O000 ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构",]="佛山"#line:749
                    text .see (END )#line:750
                except TRD :#line:751
                    text .insert (END ,"\n导入的自定义配置表中，未找到地市清单或清单有误，不对地市名称进行规整，未维护产品的报表的地市名称将以“未填写”的形式展现。",)#line:755
                    text .see (END )#line:756
            text .insert (END ,"\n您使用了自己导入的配置表作为评分标准。")#line:757
            text .see (END )#line:758
    text .insert (END ,"\n正在抽样，请稍候...已完成30%")#line:759
    O000O000O0O00O000 =O000O000O0O00O000 .reset_index (drop =True )#line:760
    O000O000O0O00O000 ["质量评估模式"]=O000O000O0O00O000 [O00O00OOO0O0OOOO0 ]#line:763
    O000O000O0O00O000 ["报告时限"]=""#line:764
    O000O000O0O00O000 ["报告时限情况"]="超时报告"#line:765
    O000O000O0O00O000 ["识别代码"]=range (0 ,len (O000O000O0O00O000 ))#line:766
    try :#line:767
        O000O000O0O00O000 ["报告时限"]=pd .to_datetime (O000O000O0O00O000 ["报告日期"])-pd .to_datetime (O000O000O0O00O000 ["发现或获知日期"])#line:770
        O000O000O0O00O000 ["报告时限"]=O000O000O0O00O000 ["报告时限"].dt .days #line:771
        O000O000O0O00O000 .loc [(O000O000O0O00O000 ["伤害"]=="死亡")&(O000O000O0O00O000 ["报告时限"]<=7 ),"报告时限情况"]="死亡未超时，报告时限："+O000O000O0O00O000 ["报告时限"].astype (str )#line:774
        O000O000O0O00O000 .loc [(O000O000O0O00O000 ["伤害"]=="严重伤害")&(O000O000O0O00O000 ["报告时限"]<=20 ),"报告时限情况"]="严重伤害未超时，报告时限："+O000O000O0O00O000 ["报告时限"].astype (str )#line:777
        O000O000O0O00O000 .loc [(O000O000O0O00O000 ["伤害"]=="其他")&(O000O000O0O00O000 ["报告时限"]<=30 ),"报告时限情况"]="其他未超时，报告时限："+O000O000O0O00O000 ["报告时限"].astype (str )#line:780
        O000O000O0O00O000 .loc [(O000O000O0O00O000 ["报告时限情况"]=="超时报告"),"报告时限情况"]="！疑似超时报告，报告时限："+O000O000O0O00O000 ["报告时限"].astype (str )#line:783
        O000O000O0O00O000 ["型号和规格"]=("型号："+O000O000O0O00O000 ["型号"].astype (str )+"   \n规格："+O000O000O0O00O000 ["规格"].astype (str ))#line:786
        O000O000O0O00O000 ["产品批号和产品编号"]=("产品批号："+O000O000O0O00O000 ["产品批号"].astype (str )+"   \n产品编号："+O000O000O0O00O000 ["产品编号"].astype (str ))#line:792
        O000O000O0O00O000 ["使用场所和场所名称"]=("使用场所："+O000O000O0O00O000 ["使用场所"].astype (str )+"   \n场所名称："+O000O000O0O00O000 ["场所名称"].astype (str ))#line:798
        O000O000O0O00O000 ["年龄和年龄类型"]=("年龄："+O000O000O0O00O000 ["年龄"].astype (str )+"   \n年龄类型："+O000O000O0O00O000 ["年龄类型"].astype (str ))#line:804
        O000O000O0O00O000 ["事件原因分析和事件原因分析描述"]=("事件原因分析："+O000O000O0O00O000 ["事件原因分析"].astype (str )+"   \n事件原因分析描述："+O000O000O0O00O000 ["事件原因分析描述"].astype (str ))#line:810
        O000O000O0O00O000 ["是否开展了调查及调查情况"]=("是否开展了调查："+O000O000O0O00O000 ["是否开展了调查"].astype (str )+"   \n调查情况："+O000O000O0O00O000 ["调查情况"].astype (str ))#line:819
        O000O000O0O00O000 ["控制措施情况"]=("是否已采取控制措施："+O000O000O0O00O000 ["是否已采取控制措施"].astype (str )+"   \n具体控制措施："+O000O000O0O00O000 ["具体控制措施"].astype (str )+"   \n未采取控制措施原因："+O000O000O0O00O000 ["未采取控制措施原因"].astype (str ))#line:828
        O000O000O0O00O000 ["是否为错报误报报告及错报误报说明"]=("是否为错报误报报告："+O000O000O0O00O000 ["是否为错报误报报告"].astype (str )+"   \n错报误报说明："+O000O000O0O00O000 ["错报误报说明"].astype (str ))#line:835
        O000O000O0O00O000 ["是否合并报告及合并报告编码"]=("是否合并报告："+O000O000O0O00O000 ["是否合并报告"].astype (str )+"   \n合并报告编码："+O000O000O0O00O000 ["合并报告编码"].astype (str ))#line:842
    except :#line:843
        pass #line:844
    if "报告类型-新的"in O000O000O0O00O000 .columns :#line:845
        O000O000O0O00O000 ["报告时限"]=pd .to_datetime (O000O000O0O00O000 ["报告日期"].astype (str ))-pd .to_datetime (O000O000O0O00O000 ["不良反应发生时间"].astype (str ))#line:847
        O000O000O0O00O000 ["报告类型"]=O000O000O0O00O000 ["报告类型-新的"].astype (str )+O000O000O0O00O000 ["伤害"].astype (str )+"    "+O000O000O0O00O000 ["严重药品不良反应"].astype (str )#line:848
        O000O000O0O00O000 ["报告类型"]=O000O000O0O00O000 ["报告类型"].str .replace ("-未填写-","",regex =False )#line:849
        O000O000O0O00O000 ["报告类型"]=O000O000O0O00O000 ["报告类型"].str .replace ("其他","一般",regex =False )#line:850
        O000O000O0O00O000 ["报告类型"]=O000O000O0O00O000 ["报告类型"].str .replace ("严重伤害","严重",regex =False )#line:851
        O000O000O0O00O000 ["关联性评价和ADR分析"]="停药减药后反应是否减轻或消失："+O000O000O0O00O000 ["停药减药后反应是否减轻或消失"].astype (str )+"\n再次使用可疑药是否出现同样反应："+O000O000O0O00O000 ["再次使用可疑药是否出现同样反应"].astype (str )+"\n报告人评价："+O000O000O0O00O000 ["报告人评价"].astype (str )#line:852
        O000O000O0O00O000 ["ADR过程描述以及处理情况"]="不良反应发生时间："+O000O000O0O00O000 ["不良反应发生时间"].astype (str )+"\n不良反应过程描述："+O000O000O0O00O000 ["不良反应过程描述"].astype (str )+"\n不良反应结果:"+O000O000O0O00O000 ["不良反应结果"].astype (str )+"\n对原患疾病影响:"+O000O000O0O00O000 ["对原患疾病影响"].astype (str )+"\n后遗症表现："+O000O000O0O00O000 ["后遗症表现"].astype (str )+"\n死亡时间:"+O000O000O0O00O000 ["死亡时间"].astype (str )+"\n直接死因:"+O000O000O0O00O000 ["直接死因"].astype (str )#line:853
        O000O000O0O00O000 ["报告者及患者有关情况"]="患者姓名："+O000O000O0O00O000 ["患者姓名"].astype (str )+"\n性别："+O000O000O0O00O000 ["性别"].astype (str )+"\n出生日期:"+O000O000O0O00O000 ["出生日期"].astype (str )+"\n年龄:"+O000O000O0O00O000 ["年龄"].astype (str )+O000O000O0O00O000 ["年龄单位"].astype (str )+"\n民族："+O000O000O0O00O000 ["民族"].astype (str )+"\n体重:"+O000O000O0O00O000 ["体重"].astype (str )+"\n原患疾病:"+O000O000O0O00O000 ["原患疾病"].astype (str )+"\n病历号/门诊号:"+O000O000O0O00O000 ["病历号/门诊号"].astype (str )+"\n既往药品不良反应/事件:"+O000O000O0O00O000 ["既往药品不良反应/事件"].astype (str )+"\n家族药品不良反应/事件:"+O000O000O0O00O000 ["家族药品不良反应/事件"].astype (str )#line:854
    OOO0OO0000O0OOO00 =filedialog .askdirectory ()#!!!!!!!#line:858
    O00OOOO0O0OO0O00O =1 #line:861
    for OO0OO0O0OOOOOOOO0 in O000O000O0O00O000 ["伤害"].drop_duplicates ():#line:862
        if OO0OO0O0OOOOOOOO0 =="其他":#line:863
            OOO00OO0O00O000OO =1 #line:864
            OOOO000O0O00O0OO0 =O000O000O0O00O000 [(O000O000O0O00O000 ["伤害"]=="其他")]#line:865
            OOOOOOO00OOO0O0OO =Tdoing (OOOO000O0O00O0OO0 ,O0000000OOOO00O0O ,OO00OO0O0OOOOO0OO ,O00O00OOO0O0OOOO0 ,OO0O000O000OOOOOO ,OO0O00000O0O000OO )#line:866
            if O00OOOO0O0OO0O00O ==1 :#line:867
                O0O00O00OOO0000O0 =OOOOOOO00OOO0O0OO [0 ]#line:868
                O00OOOO0O0OO0O00O =O00OOOO0O0OO0O00O +1 #line:869
            else :#line:870
                O0O00O00OOO0000O0 =pd .concat ([O0O00O00OOO0000O0 ,OOOOOOO00OOO0O0OO [0 ]],axis =0 )#line:871
        if OO0OO0O0OOOOOOOO0 =="严重伤害":#line:873
            O0O00O00O0O000O0O =1 #line:874
            OOOOOO0OO00OOOOO0 =O000O000O0O00O000 [(O000O000O0O00O000 ["伤害"]=="严重伤害")]#line:875
            OO00O0O000O000000 =Tdoing (OOOOOO0OO00OOOOO0 ,O0000OO0OOO0O00O0 ,OO00OO0O0OOOOO0OO ,O00O00OOO0O0OOOO0 ,OO0O000O000OOOOOO ,OO0O00000O0O000OO )#line:876
            if O00OOOO0O0OO0O00O ==1 :#line:877
                O0O00O00OOO0000O0 =OO00O0O000O000000 [0 ]#line:878
                O00OOOO0O0OO0O00O =O00OOOO0O0OO0O00O +1 #line:879
            else :#line:880
                O0O00O00OOO0000O0 =pd .concat ([O0O00O00OOO0000O0 ,OO00O0O000O000000 [0 ]],axis =0 )#line:881
        if OO0OO0O0OOOOOOOO0 =="死亡":#line:883
            OO0OO000OOOO00O00 =1 #line:884
            OO0OO00O000OO0OOO =O000O000O0O00O000 [(O000O000O0O00O000 ["伤害"]=="死亡")]#line:885
            O000OO0O00OO0OO0O =Tdoing (OO0OO00O000OO0OOO ,OO0O0OOOO0OO0000O ,OO00OO0O0OOOOO0OO ,O00O00OOO0O0OOOO0 ,OO0O000O000OOOOOO ,OO0O00000O0O000OO )#line:886
            if O00OOOO0O0OO0O00O ==1 :#line:887
                O0O00O00OOO0000O0 =O000OO0O00OO0OO0O [0 ]#line:888
                O00OOOO0O0OO0O00O =O00OOOO0O0OO0O00O +1 #line:889
            else :#line:890
                O0O00O00OOO0000O0 =pd .concat ([O0O00O00OOO0000O0 ,O000OO0O00OO0OO0O [0 ]],axis =0 )#line:891
    text .insert (END ,"\n正在抽样，请稍候...已完成50%")#line:895
    O0OOO00OO0O000O0O =pd .ExcelWriter (str (OOO0OO0000O0OOO00 )+"/●(最终评分需导入)被抽出的所有数据"+".xlsx")#line:896
    O0O00O00OOO0000O0 .to_excel (O0OOO00OO0O000O0O ,sheet_name ="被抽出的所有数据")#line:897
    O0OOO00OO0O000O0O .close ()#line:898
    if OO0O00000O0O000OO ==1 :#line:901
        OO0OO0OO0OO0O00OO =O000O000O0O00O000 .copy ()#line:902
        OO0OO0OO0OO0O00OO ["原始数量"]=1 #line:903
        OO00000OOOOO0OOO0 =O0O00O00OOO0000O0 .copy ()#line:904
        OO00000OOOOO0OOO0 ["抽取数量"]=1 #line:905
        OOO000OO0OO0OOOOO =OO0OO0OO0OO0O00OO .groupby ([O00O00OOO0O0OOOO0 ]).aggregate ({"原始数量":"count"})#line:908
        OOO000OO0OO0OOOOO =OOO000OO0OO0OOOOO .sort_values (by =["原始数量"],ascending =False ,na_position ="last")#line:911
        OOO000OO0OO0OOOOO =OOO000OO0OO0OOOOO .reset_index ()#line:912
        O0O0OOOO0O000O00O =pd .pivot_table (OO00000OOOOO0OOO0 ,values =["抽取数量"],index =O00O00OOO0O0OOOO0 ,columns ="伤害",aggfunc ={"抽取数量":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:923
        O0O0OOOO0O000O00O .columns =O0O0OOOO0O000O00O .columns .droplevel (0 )#line:924
        O0O0OOOO0O000O00O =O0O0OOOO0O000O00O .sort_values (by =["All"],ascending =[False ],na_position ="last")#line:927
        O0O0OOOO0O000O00O =O0O0OOOO0O000O00O .reset_index ()#line:928
        O0O0OOOO0O000O00O =O0O0OOOO0O000O00O .rename (columns ={"All":"抽取总数量"})#line:929
        try :#line:930
            O0O0OOOO0O000O00O =O0O0OOOO0O000O00O .rename (columns ={"一般":"抽取数量(一般)"})#line:931
        except :#line:932
            pass #line:933
        try :#line:934
            O0O0OOOO0O000O00O =O0O0OOOO0O000O00O .rename (columns ={"严重伤害":"抽取数量(严重)"})#line:935
        except :#line:936
            pass #line:937
        try :#line:938
            O0O0OOOO0O000O00O =O0O0OOOO0O000O00O .rename (columns ={"死亡":"抽取数量-死亡"})#line:939
        except :#line:940
            pass #line:941
        OO0OO000O000O0O00 =pd .merge (OOO000OO0OO0OOOOO ,O0O0OOOO0O000O00O ,on =[O00O00OOO0O0OOOO0 ],how ="left")#line:942
        OO0OO000O000O0O00 ["抽取比例"]=round (OO0OO000O000O0O00 ["抽取总数量"]/OO0OO000O000O0O00 ["原始数量"],2 )#line:943
        OOOO0OO00OO000000 =pd .ExcelWriter (str (OOO0OO0000O0OOO00 )+"/抽样情况分布"+".xlsx")#line:944
        OO0OO000O000O0O00 .to_excel (OOOO0OO00OO000000 ,sheet_name ="抽样情况分布")#line:945
        OOOO0OO00OO000000 .close ()#line:946
    O0O00O00OOO0000O0 =O0O00O00OOO0000O0 [OOO000000OOOOO00O ["评分项"].tolist ()]#line:952
    OO00O0O00OO0O0OO0 =int (OO00OO0O0OOOOO0OO )#line:954
    text .insert (END ,"\n正在抽样，请稍候...已完成70%")#line:956
    for OO0OO0O0OOOOOOOO0 in range (OO00O0O00OO0O0OO0 ):#line:957
        if OO0OO0O0OOOOOOOO0 ==0 :#line:958
            OO00OO0O0O0000OOO =O0O00O00OOO0000O0 [(O0O00O00OOO0000O0 ["伤害"]=="其他")].sample (frac =1 /(OO00O0O00OO0O0OO0 -OO0OO0O0OOOOOOOO0 ),replace =False )#line:962
            OO00OOO00OOOOOO00 =O0O00O00OOO0000O0 [(O0O00O00OOO0000O0 ["伤害"]=="严重伤害")].sample (frac =1 /(OO00O0O00OO0O0OO0 -OO0OO0O0OOOOOOOO0 ),replace =False )#line:965
            O0O0O00O00OOO0OOO =O0O00O00OOO0000O0 [(O0O00O00OOO0000O0 ["伤害"]=="死亡")].sample (frac =1 /(OO00O0O00OO0O0OO0 -OO0OO0O0OOOOOOOO0 ),replace =False )#line:968
            O000OOOO0O0OO0OOO =pd .concat ([OO00OO0O0O0000OOO ,OO00OOO00OOOOOO00 ,O0O0O00O00OOO0OOO ],axis =0 )#line:970
        else :#line:972
            O0O00O00OOO0000O0 =pd .concat ([O0O00O00OOO0000O0 ,O000OOOO0O0OO0OOO ],axis =0 )#line:973
            O0O00O00OOO0000O0 .drop_duplicates (subset =["识别代码"],keep =False ,inplace =True )#line:974
            OO00OO0O0O0000OOO =O0O00O00OOO0000O0 [(O0O00O00OOO0000O0 ["伤害"]=="其他")].sample (frac =1 /(OO00O0O00OO0O0OO0 -OO0OO0O0OOOOOOOO0 ),replace =False )#line:977
            OO00OOO00OOOOOO00 =O0O00O00OOO0000O0 [(O0O00O00OOO0000O0 ["伤害"]=="严重伤害")].sample (frac =1 /(OO00O0O00OO0O0OO0 -OO0OO0O0OOOOOOOO0 ),replace =False )#line:980
            O0O0O00O00OOO0OOO =O0O00O00OOO0000O0 [(O0O00O00OOO0000O0 ["伤害"]=="死亡")].sample (frac =1 /(OO00O0O00OO0O0OO0 -OO0OO0O0OOOOOOOO0 ),replace =False )#line:983
            O000OOOO0O0OO0OOO =pd .concat ([OO00OO0O0O0000OOO ,OO00OOO00OOOOOO00 ,O0O0O00O00OOO0OOO ],axis =0 )#line:984
        try :#line:985
            O000OOOO0O0OO0OOO ["报告编码"]=O000OOOO0O0OO0OOO ["报告编码"].astype (str )#line:986
        except :#line:987
            pass #line:988
        OOOO0O0OOOO000O0O =str (OOO0OO0000O0OOO00 )+"/"+str (OO0OO0O0OOOOOOOO0 +1 )+".xlsx"#line:989
        if OO0O00000O0O000OO ==1 :#line:992
            O000O0OOO0OOOOOO0 =TeasyreadT (O000OOOO0O0OO0OOO .copy ())#line:993
            del O000O0OOO0OOOOOO0 ["逐条查看"]#line:994
            O000O0OOO0OOOOOO0 ["评分"]=""#line:995
            if len (O000O0OOO0OOOOOO0 )>0 :#line:996
                for O00O0O0OO0000OO0O ,O0OO0OOOO0OOO0OO0 in OOO000000OOOOO00O .iterrows ():#line:997
                    O000O0OOO0OOOOOO0 .loc [(O000O0OOO0OOOOOO0 ["条目"]==O0OO0OOOO0OOO0OO0 ["评分项"]),"满分"]=O0OO0OOOO0OOO0OO0 ["满分分值"]#line:998
                    O000O0OOO0OOOOOO0 .loc [(O000O0OOO0OOOOOO0 ["条目"]==O0OO0OOOO0OOO0OO0 ["评分项"]),"打分标准"]=O0OO0OOOO0OOO0OO0 ["打分标准"]#line:1001
            O000O0OOO0OOOOOO0 ["专家序号"]=OO0OO0O0OOOOOOOO0 +1 #line:1003
            O000O00O0O00OOOO0 =str (OOO0OO0000O0OOO00 )+"/"+"●专家评分表"+str (OO0OO0O0OOOOOOOO0 +1 )+".xlsx"#line:1004
            OOOOO00O000OO0O0O =pd .ExcelWriter (O000O00O0O00OOOO0 )#line:1005
            O000O0OOO0OOOOOO0 .to_excel (OOOOO00O000OO0O0O ,sheet_name ="字典数据")#line:1006
            OOOOO00O000OO0O0O .close ()#line:1007
    text .insert (END ,"\n正在抽样，请稍候...已完成100%")#line:1010
    showinfo (title ="提示信息",message ="抽样和分组成功，请查看以下文件夹："+str (OOO0OO0000O0OOO00 ))#line:1011
    text .insert (END ,"\n抽样和分组成功，请查看以下文件夹："+str (OOO0OO0000O0OOO00 ))#line:1012
    text .insert (END ,"\n抽样概况:\n")#line:1013
    text .insert (END ,OO0OO000O000O0O00 [[O00O00OOO0O0OOOO0 ,"原始数量","抽取总数量"]])#line:1014
    text .see (END )#line:1015
def Tdoing (O00O00OO0O0000000 ,O00OOOOOOO000O00O ,OOOOOO00O0O0O000O ,O000OO000000OOOO0 ,O0OOOO00OO0OO0OOO ,O0000OO00O0OO0O0O ):#line:1018
    ""#line:1019
    def O0O00O000000OO0O0 (O00000OO0O0O00O00 ,O0OOO00000000OO00 ,OO0O000OOOOO0OOOO ):#line:1021
        if float (O0OOO00000000OO00 )>1 :#line:1022
            try :#line:1023
                OO00000000O00O00O =O00000OO0O0O00O00 .sample (int (O0OOO00000000OO00 ),replace =False )#line:1024
            except ValueError :#line:1026
                OO00000000O00O00O =O00000OO0O0O00O00 #line:1028
        else :#line:1029
            OO00000000O00O00O =O00000OO0O0O00O00 .sample (frac =float (O0OOO00000000OO00 ),replace =False )#line:1030
            if len (O00000OO0O0O00O00 )*float (O0OOO00000000OO00 )>len (OO00000000O00O00O )and OO0O000OOOOO0OOOO =="最大覆盖":#line:1032
                OOOO00O0O000OOOOO =pd .concat ([O00000OO0O0O00O00 ,OO00000000O00O00O ],axis =0 )#line:1033
                OOOO00O0O000OOOOO .drop_duplicates (subset =["识别代码"],keep =False ,inplace =True )#line:1034
                O0OOO00OO00OO0OO0 =OOOO00O0O000OOOOO .sample (1 ,replace =False )#line:1035
                OO00000000O00O00O =pd .concat ([OO00000000O00O00O ,O0OOO00OO00OO0OO0 ],axis =0 )#line:1036
        return OO00000000O00O00O #line:1037
    if O0OOOO00OO0OO0OOO =="总体随机":#line:1040
        OOO00O0OOOO000OOO =O0O00O000000OO0O0 (O00O00OO0O0000000 ,O00OOOOOOO000O00O ,O0OOOO00OO0OO0OOO )#line:1041
    else :#line:1043
        OO0000OOO0OOOOO0O =1 #line:1044
        for OOOOO00OO00O00OO0 in O00O00OO0O0000000 [O000OO000000OOOO0 ].drop_duplicates ():#line:1045
            O0000OO000O0OOOO0 =O00O00OO0O0000000 [(O00O00OO0O0000000 [O000OO000000OOOO0 ]==OOOOO00OO00O00OO0 )].copy ()#line:1046
            if OO0000OOO0OOOOO0O ==1 :#line:1047
                OOO00O0OOOO000OOO =O0O00O000000OO0O0 (O0000OO000O0OOOO0 ,O00OOOOOOO000O00O ,O0OOOO00OO0OO0OOO )#line:1048
                OO0000OOO0OOOOO0O =OO0000OOO0OOOOO0O +1 #line:1049
            else :#line:1050
                OOOO0O00O0O00000O =O0O00O000000OO0O0 (O0000OO000O0OOOO0 ,O00OOOOOOO000O00O ,O0OOOO00OO0OO0OOO )#line:1051
                OOO00O0OOOO000OOO =pd .concat ([OOO00O0OOOO000OOO ,OOOO0O00O0O00000O ])#line:1052
    OOO00O0OOOO000OOO =OOO00O0OOOO000OOO .drop_duplicates ()#line:1053
    return OOO00O0OOOO000OOO ,1 #line:1054
def Tpinggu ():#line:1057
    ""#line:1058
    OO0000000O00OOOO0 =Topentable (1 )#line:1059
    OOOO000O00OOOOOO0 =OO0000000O00OOOO0 [0 ]#line:1060
    OO0O000O0O0O0O0O0 =OO0000000O00OOOO0 [1 ]#line:1061
    try :#line:1064
        OO0OOOO0O0O0O0O0O =[pd .read_excel (O0O00O0OOOOOO0O0O ,header =0 ,sheet_name =0 )for O0O00O0OOOOOO0O0O in OO0O000O0O0O0O0O0 ]#line:1068
        OOO00O0OOOOO0OO0O =pd .concat (OO0OOOO0O0O0O0O0O ,ignore_index =True ).drop_duplicates ()#line:1069
        try :#line:1070
            OOO00O0OOOOO0OO0O =OOO00O0OOOOO0OO0O .loc [:,~OOO00O0OOOOO0OO0O .columns .str .contains ("^Unnamed")]#line:1071
        except :#line:1072
            pass #line:1073
    except :#line:1074
        showinfo (title ="提示信息",message ="载入文件出错，任务终止。")#line:1075
        return 0 #line:1076
    try :#line:1079
        OOOO000O00OOOOOO0 =OOOO000O00OOOOOO0 .reset_index ()#line:1080
    except :#line:1081
        showinfo (title ="提示信息",message ="专家评分文件存在错误，程序中止。")#line:1082
        return 0 #line:1083
    OOO00O0OOOOO0OO0O ["质量评估专用表"]=""#line:1085
    text .insert (END ,"\n打分表导入成功，正在统计，请耐心等待...")#line:1088
    text .insert (END ,"\n正在计算总分，请稍候，已完成20%")#line:1089
    text .see (END )#line:1090
    O0O0000OO0O00OOOO =OOOO000O00OOOOOO0 [["序号","条目","详细描述","评分","满分","打分标准","专家序号"]].copy ()#line:1093
    O000O00O0O00O0000 =OOO00O0OOOOO0OO0O [["质量评估模式","识别代码"]].copy ()#line:1094
    O0O0000OO0O00OOOO .reset_index (inplace =True )#line:1095
    O000O00O0O00O0000 .reset_index (inplace =True )#line:1096
    O000O00O0O00O0000 =O000O00O0O00O0000 .rename (columns ={"识别代码":"序号"})#line:1097
    O0O0000OO0O00OOOO =pd .merge (O0O0000OO0O00OOOO ,O000O00O0O00O0000 ,on =["序号"])#line:1098
    O0O0000OO0O00OOOO =O0O0000OO0O00OOOO .sort_values (by =["序号","条目"],ascending =True ,na_position ="last")#line:1099
    O0O0000OO0O00OOOO =O0O0000OO0O00OOOO [["质量评估模式","序号","条目","详细描述","评分","满分","打分标准","专家序号"]]#line:1100
    for OO0OOO0O0O0000O00 ,O0OOOOO0OO0000000 in OOOO000O00OOOOOO0 .iterrows ():#line:1102
        OO00OO0OOOO0OOOOO ="专家打分-"+str (O0OOOOO0OO0000000 ["条目"])#line:1103
        OOO00O0OOOOO0OO0O .loc [(OOO00O0OOOOO0OO0O ["识别代码"]==O0OOOOO0OO0000000 ["序号"]),OO00OO0OOOO0OOOOO ]=O0OOOOO0OO0000000 ["评分"]#line:1104
    del OOO00O0OOOOO0OO0O ["专家打分-识别代码"]#line:1105
    del OOO00O0OOOOO0OO0O ["专家打分-#####分隔符#########"]#line:1106
    try :#line:1107
        OOO00O0OOOOO0OO0O =OOO00O0OOOOO0OO0O .loc [:,~OOO00O0OOOOO0OO0O .columns .str .contains ("^Unnamed")]#line:1108
    except :#line:1109
        pass #line:1110
    text .insert (END ,"\n正在计算总分，请稍候，已完成60%")#line:1111
    text .see (END )#line:1112
    O00O000OOOOO00000 =OO0O000O0O0O0O0O0 [0 ]#line:1115
    try :#line:1116
        O0000OO00OO00OOOO =str (O00O000OOOOO00000 ).replace ("●(最终评分需导入)被抽出的所有数据.xls","")#line:1117
    except :#line:1118
        O0000OO00OO00OOOO =str (O00O000OOOOO00000 )#line:1119
    O0O00OO00O000OOO0 =pd .ExcelWriter (str (O0000OO00OO00OOOO )+"各评估对象打分核对文件"+".xlsx")#line:1127
    O0O0000OO0O00OOOO .to_excel (O0O00OO00O000OOO0 ,sheet_name ="原始打分")#line:1128
    O0O00OO00O000OOO0 .close ()#line:1129
    O000000O0OOOO0O00 =Tpinggu2 (OOO00O0OOOOO0OO0O )#line:1133
    text .insert (END ,"\n正在计算总分，请稍候，已完成100%")#line:1135
    text .see (END )#line:1136
    showinfo (title ="提示信息",message ="打分计算成功，请查看文件："+str (O0000OO00OO00OOOO )+"最终打分"+".xlsx")#line:1137
    text .insert (END ,"\n打分计算成功，请查看文件："+str (O00O000OOOOO00000 )+"最终打分"+".xls\n")#line:1138
    O000000O0OOOO0O00 .reset_index (inplace =True )#line:1139
    text .insert (END ,"\n以下是结果概况：\n")#line:1140
    text .insert (END ,O000000O0OOOO0O00 [["评估对象","总分"]])#line:1141
    text .see (END )#line:1142
    O0O00O000000O0OOO =["评估对象","总分"]#line:1146
    for OOOOO0O0OO0OO000O in O000000O0OOOO0O00 .columns :#line:1147
        if "专家打分"in OOOOO0O0OO0OO000O :#line:1148
            O0O00O000000O0OOO .append (OOOOO0O0OO0OO000O )#line:1149
    O000O0OO00O0OOO00 =O000000O0OOOO0O00 [O0O00O000000O0OOO ]#line:1150
    OOOOO0O000OOOO0OO =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name =0 ,header =0 ,index_col =0 ).reset_index ()#line:1154
    if "专家打分-不良反应名称"in O0O00O000000O0OOO :#line:1156
        OOOOO0O000OOOO0OO =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="药品",header =0 ,index_col =0 ).reset_index ()#line:1157
    if "专家打分-化妆品名称"in O0O00O000000O0OOO :#line:1159
        OOOOO0O000OOOO0OO =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="化妆品",header =0 ,index_col =0 ).reset_index ()#line:1160
    if "专家打分-是否需要开展产品风险评价"in O0O00O000000O0OOO :#line:1161
        OOOOO0O000OOOO0OO =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="器械持有人",header =0 ,index_col =0 ).reset_index ()#line:1162
    for OO0OOO0O0O0000O00 ,O0OOOOO0OO0000000 in OOOOO0O000OOOO0OO .iterrows ():#line:1163
        O0OO0O0OOO00OOO0O ="专家打分-"+str (O0OOOOO0OO0000000 ["评分项"])#line:1164
        try :#line:1165
            warnings .filterwarnings ('ignore')#line:1166
            O000O0OO00O0OOO00 .loc [-1 ,O0OO0O0OOO00OOO0O ]=O0OOOOO0OO0000000 ["满分分值"]#line:1167
        except :#line:1168
            pass #line:1169
    del O000O0OO00O0OOO00 ["专家打分-识别代码"]#line:1170
    O000O0OO00O0OOO00 .iloc [-1 ,0 ]="满分分值"#line:1171
    O000O0OO00O0OOO00 .loc [-1 ,"总分"]=100 #line:1172
    if "专家打分-事件原因分析.1"not in O0O00O000000O0OOO :#line:1174
        O000O0OO00O0OOO00 .loc [-1 ,"专家打分-报告时限"]=5 #line:1175
    if "专家打分-事件原因分析.1"in O0O00O000000O0OOO :#line:1177
        O000O0OO00O0OOO00 .loc [-1 ,"专家打分-报告时限"]=10 #line:1178
    O000O0OO00O0OOO00 .columns =O000O0OO00O0OOO00 .columns .str .replace ("专家打分-","",regex =False )#line:1181
    if ("专家打分-器械故障表现"in O0O00O000000O0OOO )and ("modex"not in OOO00O0OOOOO0OO0O .columns ):#line:1183
        O000O0OO00O0OOO00 .loc [-1 ,"姓名和既往病史"]=2 #line:1184
        O000O0OO00O0OOO00 .loc [-1 ,"报告日期"]=1 #line:1185
    else :#line:1186
        del O000O0OO00O0OOO00 ["伤害"]#line:1187
    if "专家打分-化妆品名称"in O0O00O000000O0OOO :#line:1189
        del O000O0OO00O0OOO00 ["报告时限"]#line:1190
    try :#line:1193
        O000O0OO00O0OOO00 =O000O0OO00O0OOO00 [["评估对象","总分","伤害.1","是否开展了调查及调查情况","关联性评价","事件原因分析.1","是否需要开展产品风险评价","控制措施情况","是否为错报误报报告及错报误报说明","是否合并报告及合并报告编码","报告时限"]]#line:1194
    except :#line:1195
        pass #line:1196
    try :#line:1197
        O000O0OO00O0OOO00 =O000O0OO00O0OOO00 [["评估对象","总分","报告日期","报告人","联系人","联系电话","注册证编号/曾用注册证编号","产品名称","型号和规格","产品批号和产品编号","生产日期","有效期至","事件发生日期","发现或获知日期","伤害","伤害表现","器械故障表现","姓名和既往病史","年龄和年龄类型","性别","预期治疗疾病或作用","器械使用日期","使用场所和场所名称","使用过程","合并用药/械情况说明","事件原因分析和事件原因分析描述","初步处置情况","报告时限"]]#line:1198
    except :#line:1199
        pass #line:1200
    try :#line:1201
        O000O0OO00O0OOO00 =O000O0OO00O0OOO00 [["评估对象","总分","报告类型","报告时限","报告者及患者有关情况","原患疾病","药品信息","不良反应名称","ADR过程描述以及处理情况","关联性评价和ADR分析"]]#line:1202
    except :#line:1203
        pass #line:1204
    O00OOO000000000O0 =pd .ExcelWriter (str (O0000OO00OO00OOOO )+"最终打分"+".xlsx")#line:1206
    O000O0OO00O0OOO00 .to_excel (O00OOO000000000O0 ,sheet_name ="最终打分")#line:1207
    O00OOO000000000O0 .close ()#line:1208
    Ttree_Level_2 (O000O0OO00O0OOO00 ,0 ,O000000O0OOOO0O00 )#line:1210
def Tpinggu2 (OO000O00O0OO0O00O ):#line:1213
    ""#line:1214
    OO000O00O0OO0O00O ["报告数量小计"]=1 #line:1215
    if ("器械故障表现"in OO000O00O0OO0O00O .columns )and ("modex"not in OO000O00O0OO0O00O .columns ):#line:1218
        OO000O00O0OO0O00O ["专家打分-姓名和既往病史"]=2 #line:1219
        OO000O00O0OO0O00O ["专家打分-报告日期"]=1 #line:1220
        if "专家打分-报告时限情况"not in OO000O00O0OO0O00O .columns :#line:1221
            OO000O00O0OO0O00O ["报告时限"]=OO000O00O0OO0O00O ["报告时限"].astype (float )#line:1222
            OO000O00O0OO0O00O ["专家打分-报告时限"]=0 #line:1223
            OO000O00O0OO0O00O .loc [(OO000O00O0OO0O00O ["伤害"]=="死亡")&(OO000O00O0OO0O00O ["报告时限"]<=7 ),"专家打分-报告时限"]=5 #line:1224
            OO000O00O0OO0O00O .loc [(OO000O00O0OO0O00O ["伤害"]=="严重伤害")&(OO000O00O0OO0O00O ["报告时限"]<=20 ),"专家打分-报告时限"]=5 #line:1225
            OO000O00O0OO0O00O .loc [(OO000O00O0OO0O00O ["伤害"]=="其他")&(OO000O00O0OO0O00O ["报告时限"]<=30 ),"专家打分-报告时限"]=5 #line:1226
    if "专家打分-事件原因分析.1"in OO000O00O0OO0O00O .columns :#line:1230
       OO000O00O0OO0O00O ["专家打分-报告时限"]=10 #line:1231
    O000O00O0OOOO0O00 =[]#line:1234
    for OOO0O0OO000O00OOO in OO000O00O0OO0O00O .columns :#line:1235
        if "专家打分-"in OOO0O0OO000O00OOO :#line:1236
            O000O00O0OOOO0O00 .append (OOO0O0OO000O00OOO )#line:1237
    OOO000OO00OOO0000 =1 #line:1241
    for OOO0O0OO000O00OOO in O000O00O0OOOO0O00 :#line:1242
        O0OOO000O0O00OOOO =OO000O00O0OO0O00O .groupby (["质量评估模式"]).aggregate ({OOO0O0OO000O00OOO :"sum"}).reset_index ()#line:1243
        if OOO000OO00OOO0000 ==1 :#line:1244
            OO0O0OO0O000OOO0O =O0OOO000O0O00OOOO #line:1245
            OOO000OO00OOO0000 =OOO000OO00OOO0000 +1 #line:1246
        else :#line:1247
            OO0O0OO0O000OOO0O =pd .merge (OO0O0OO0O000OOO0O ,O0OOO000O0O00OOOO ,on ="质量评估模式",how ="left")#line:1248
    O00000OOOOOOO0000 =OO000O00O0OO0O00O .groupby (["质量评估模式"]).aggregate ({"报告数量小计":"sum"}).reset_index ()#line:1250
    OO0O0OO0O000OOO0O =pd .merge (OO0O0OO0O000OOO0O ,O00000OOOOOOO0000 ,on ="质量评估模式",how ="left")#line:1251
    for OOO0O0OO000O00OOO in O000O00O0OOOO0O00 :#line:1254
        OO0O0OO0O000OOO0O [OOO0O0OO000O00OOO ]=round (OO0O0OO0O000OOO0O [OOO0O0OO000O00OOO ]/OO0O0OO0O000OOO0O ["报告数量小计"],2 )#line:1255
    OO0O0OO0O000OOO0O ["总分"]=round (OO0O0OO0O000OOO0O [O000O00O0OOOO0O00 ].sum (axis =1 ),2 )#line:1256
    OO0O0OO0O000OOO0O =OO0O0OO0O000OOO0O .sort_values (by =["总分"],ascending =False ,na_position ="last")#line:1257
    warnings .filterwarnings ('ignore')#line:1258
    OO0O0OO0O000OOO0O .loc ["平均分(非加权)"]=round (OO0O0OO0O000OOO0O .mean (axis =0 ),2 )#line:1259
    OO0O0OO0O000OOO0O .loc ["标准差(非加权)"]=round (OO0O0OO0O000OOO0O .std (axis =0 ),2 )#line:1260
    OO0O0OO0O000OOO0O =OO0O0OO0O000OOO0O .rename (columns ={"质量评估模式":"评估对象"})#line:1261
    OO0O0OO0O000OOO0O .iloc [-2 ,0 ]="平均分(非加权)"#line:1262
    OO0O0OO0O000OOO0O .iloc [-1 ,0 ]="标准差(非加权)"#line:1263
    return OO0O0OO0O000OOO0O #line:1265
def Ttree_Level_2 (O00O0O00OOO0OO000 ,O0000O0000OOOO00O ,OOOOOO0000OOOOO0O ,*OO00O0OOOO00OOO00 ):#line:1268
    ""#line:1269
    OO00OO00O00OO0O0O =O00O0O00OOO0OO000 .columns .values .tolist ()#line:1271
    O0000O0000OOOO00O =0 #line:1272
    O0000OOO00000OOOO =O00O0O00OOO0OO000 .loc [:]#line:1273
    OO0O0000000OO0O0O =Toplevel ()#line:1276
    OO0O0000000OO0O0O .title ("报表查看器")#line:1277
    O0O00000O00OOOO00 =OO0O0000000OO0O0O .winfo_screenwidth ()#line:1278
    OOOOOO00OO000000O =OO0O0000000OO0O0O .winfo_screenheight ()#line:1280
    O0000O00OO00OO00O =1300 #line:1282
    O0O000O000O0O00O0 =600 #line:1283
    OO00O0OO0OO000OOO =(O0O00000O00OOOO00 -O0000O00OO00OO00O )/2 #line:1285
    O000O0OO0000OO0O0 =(OOOOOO00OO000000O -O0O000O000O0O00O0 )/2 #line:1286
    OO0O0000000OO0O0O .geometry ("%dx%d+%d+%d"%(O0000O00OO00OO00O ,O0O000O000O0O00O0 ,OO00O0OO0OO000OOO ,O000O0OO0000OO0O0 ))#line:1287
    O000OO000O0000O0O =ttk .Frame (OO0O0000000OO0O0O ,width =1300 ,height =20 )#line:1288
    O000OO000O0000O0O .pack (side =TOP )#line:1289
    OOO0OO0OOO0O000O0 =O0000OOO00000OOOO .values .tolist ()#line:1292
    O0O00O0O00O00000O =O0000OOO00000OOOO .columns .values .tolist ()#line:1293
    O0O000O0000O0OO0O =ttk .Treeview (O000OO000O0000O0O ,columns =O0O00O0O00O00000O ,show ="headings",height =45 )#line:1294
    for O0OO0O0O0000O0OOO in O0O00O0O00O00000O :#line:1296
        O0O000O0000O0OO0O .heading (O0OO0O0O0000O0OOO ,text =O0OO0O0O0000O0OOO )#line:1297
    for O00000OOOOO00OOO0 in OOO0OO0OOO0O000O0 :#line:1298
        O0O000O0000O0OO0O .insert ("","end",values =O00000OOOOO00OOO0 )#line:1299
    for O00OO0OO0O000OOO0 in O0O00O0O00O00000O :#line:1300
        O0O000O0000O0OO0O .column (O00OO0OO0O000OOO0 ,minwidth =0 ,width =120 ,stretch =NO )#line:1301
    OOOO00O0000OO00O0 =Scrollbar (O000OO000O0000O0O ,orient ="vertical")#line:1303
    OOOO00O0000OO00O0 .pack (side =RIGHT ,fill =Y )#line:1304
    OOOO00O0000OO00O0 .config (command =O0O000O0000O0OO0O .yview )#line:1305
    O0O000O0000O0OO0O .config (yscrollcommand =OOOO00O0000OO00O0 .set )#line:1306
    O0O0OO0000OOOO000 =Scrollbar (O000OO000O0000O0O ,orient ="horizontal")#line:1308
    O0O0OO0000OOOO000 .pack (side =BOTTOM ,fill =X )#line:1309
    O0O0OO0000OOOO000 .config (command =O0O000O0000O0OO0O .xview )#line:1310
    O0O000O0000O0OO0O .config (yscrollcommand =OOOO00O0000OO00O0 .set )#line:1311
    def O0O00O000OOO0OO00 (OO00O00O00O000O00 ,OOOOOO0O000OOOOO0 ,OOO0OO0OO00OOOOO0 ):#line:1313
        for O0O0O00OO0O00O0O0 in O0O000O0000O0OO0O .selection ():#line:1316
            OO0OO000O0O0000O0 =O0O000O0000O0OO0O .item (O0O0O00OO0O00O0O0 ,"values")#line:1317
        O0OOO00O0OOO0OOOO =OO0OO000O0O0000O0 [2 :]#line:1319
        OOOOO00O0OOOO0O00 =OOO0OO0OO00OOOOO0 .iloc [-1 ,:][2 :]#line:1322
        OO00000O00OO0O00O =OOO0OO0OO00OOOOO0 .columns #line:1323
        OO00000O00OO0O00O =OO00000O00OO0O00O [2 :]#line:1324
        Tpo (OOOOO00O0OOOO0O00 ,O0OOO00O0OOO0OOOO ,OO00000O00OO0O00O ,"失分","得分",OO0OO000O0O0000O0 [0 ])#line:1326
        return 0 #line:1327
    O0O000O0000O0OO0O .bind ("<Double-1>",lambda OO0OOOO000OO00000 :O0O00O000OOO0OO00 (OO0OOOO000OO00000 ,O0O00O0O00O00000O ,O0000OOO00000OOOO ),)#line:1333
    def O0O0OO00OOOO0O0O0 (O0O000O0O0O0O000O ,OOOO0O0OOOO00OO0O ,O0OOOOO0O00O0O0O0 ):#line:1335
        O000OOO00OO0OO00O =[(O0O000O0O0O0O000O .set (OO0OOOO0000O00000 ,OOOO0O0OOOO00OO0O ),OO0OOOO0000O00000 )for OO0OOOO0000O00000 in O0O000O0O0O0O000O .get_children ("")]#line:1336
        O000OOO00OO0OO00O .sort (reverse =O0OOOOO0O00O0O0O0 )#line:1337
        for O0O00OOO0OOO0OO0O ,(OOOO0OOO000O0OO0O ,OOO00000000OO0O00 )in enumerate (O000OOO00OO0OO00O ):#line:1339
            O0O000O0O0O0O000O .move (OOO00000000OO0O00 ,"",O0O00OOO0OOO0OO0O )#line:1340
        O0O000O0O0O0O000O .heading (OOOO0O0OOOO00OO0O ,command =lambda :O0O0OO00OOOO0O0O0 (O0O000O0O0O0O000O ,OOOO0O0OOOO00OO0O ,not O0OOOOO0O00O0O0O0 ))#line:1343
    for O0O0O00O00O0OOOO0 in O0O00O0O00O00000O :#line:1345
        O0O000O0000O0OO0O .heading (O0O0O00O00O0OOOO0 ,text =O0O0O00O00O0OOOO0 ,command =lambda _col =O0O0O00O00O0OOOO0 :O0O0OO00OOOO0O0O0 (O0O000O0000O0OO0O ,_col ,False ),)#line:1350
    O0O000O0000O0OO0O .pack ()#line:1352
def Txuanze ():#line:1354
    ""#line:1355
    global ori #line:1356
    O00000O0O0O00O000 =pd .read_excel (peizhidir +"0（范例）批量筛选.xls",sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1357
    text .insert (END ,"\n正在执行内部数据规整...\n")#line:1358
    text .insert (END ,O00000O0O0O00O000 )#line:1359
    ori ["temppr"]=""#line:1360
    for OO0OO0000OO00O0OO in O00000O0O0O00O000 .columns .tolist ():#line:1361
        ori ["temppr"]=ori ["temppr"]+"----"+ori [OO0OO0000OO00O0OO ]#line:1362
    OOO0000OOOOO00O0O ="测试字段MMMMM"#line:1363
    for OO0OO0000OO00O0OO in O00000O0O0O00O000 .columns .tolist ():#line:1364
        for OOOO0O0OOO00O0O00 in O00000O0O0O00O000 [OO0OO0000OO00O0OO ].drop_duplicates ():#line:1365
            if OOOO0O0OOO00O0O00 :#line:1366
                OOO0000OOOOO00O0O =OOO0000OOOOO00O0O +"|"+str (OOOO0O0OOO00O0O00 )#line:1367
    ori =ori .loc [ori ["temppr"].str .contains (OOO0000OOOOO00O0O ,na =False )].copy ()#line:1368
    del ori ["temppr"]#line:1369
    ori =ori .reset_index (drop =True )#line:1371
    text .insert (END ,"\n内部数据规整完毕。\n")#line:1372
def Tpo (O0OOOO0O0OOO0O0OO ,O0O0O000000O00O0O ,O0OOOOOO0O0O0000O ,O0OO0OOOO000OO000 ,OO0OO0O0000OOOOO0 ,O0OO0OOOO00000OOO ):#line:1375
    ""#line:1376
    O0OOOO0O0OOO0O0OO =O0OOOO0O0OOO0O0OO .astype (float )#line:1377
    O0O0O000000O00O0O =tuple (float (O00OOOOO0OO0OOOOO )for O00OOOOO0OO0OOOOO in O0O0O000000O00O0O )#line:1378
    O0000OOOO0O000O00 =Toplevel ()#line:1379
    O0000OOOO0O000O00 .title (O0OO0OOOO00000OOO )#line:1380
    O0O0OO0000OO0OOO0 =ttk .Frame (O0000OOOO0O000O00 ,height =20 )#line:1381
    O0O0OO0000OO0OOO0 .pack (side =TOP )#line:1382
    O00O0000O00O0O0O0 =0.2 #line:1384
    OO0OO00OOO000O0O0 =Figure (figsize =(12 ,6 ),dpi =100 )#line:1385
    O00O0O00OOO00O00O =FigureCanvasTkAgg (OO0OO00OOO000O0O0 ,master =O0000OOOO0O000O00 )#line:1386
    O00O0O00OOO00O00O .draw ()#line:1387
    O00O0O00OOO00O00O .get_tk_widget ().pack (expand =1 )#line:1388
    O0OO000OO0OO00O0O =OO0OO00OOO000O0O0 .add_subplot (111 )#line:1389
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1391
    O0O00O000OO0000OO =NavigationToolbar2Tk (O00O0O00OOO00O00O ,O0000OOOO0O000O00 )#line:1393
    O0O00O000OO0000OO .update ()#line:1394
    O00O0O00OOO00O00O .get_tk_widget ().pack ()#line:1396
    OOO0OOOOOOO000000 =range (0 ,len (O0OOOOOO0O0O0000O ),1 )#line:1397
    O0OO000OO0OO00O0O .set_xticklabels (O0OOOOOO0O0O0000O ,rotation =-90 ,fontsize =8 )#line:1400
    O0OO000OO0OO00O0O .bar (OOO0OOOOOOO000000 ,O0OOOO0O0OOO0O0OO ,align ="center",tick_label =O0OOOOOO0O0O0000O ,label =O0OO0OOOO000OO000 )#line:1404
    O0OO000OO0OO00O0O .bar (OOO0OOOOOOO000000 ,O0O0O000000O00O0O ,align ="center",label =OO0OO0O0000OOOOO0 )#line:1405
    O0OO000OO0OO00O0O .set_title (O0OO0OOOO00000OOO )#line:1406
    O0OO000OO0OO00O0O .set_xlabel ("项")#line:1407
    O0OO000OO0OO00O0O .set_ylabel ("数量")#line:1408
    OO0OO00OOO000O0O0 .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:1411
    OO00000OOO00O0O00 =O0OO000OO0OO00O0O .get_position ()#line:1412
    O0OO000OO0OO00O0O .set_position ([OO00000OOO00O0O00 .x0 ,OO00000OOO00O0O00 .y0 ,OO00000OOO00O0O00 .width *0.7 ,OO00000OOO00O0O00 .height ])#line:1413
    O0OO000OO0OO00O0O .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:1414
    O00O0O00OOO00O00O .draw ()#line:1416
def helper ():#line:1419
    ""#line:1420
    OO00O0OOO0O0OOOOO =Toplevel ()#line:1421
    OO00O0OOO0O0OOOOO .title ("程序使用帮助")#line:1422
    OO00O0OOO0O0OOOOO .geometry ("700x500")#line:1423
    OOO000OO0000O0000 =Scrollbar (OO00O0OOO0O0OOOOO )#line:1425
    O0000OO0O0OOO0O00 =Text (OO00O0OOO0O0OOOOO ,height =80 ,width =150 ,bg ="#FFFFFF",font ="微软雅黑")#line:1426
    OOO000OO0000O0000 .pack (side =RIGHT ,fill =Y )#line:1427
    O0000OO0O0OOO0O00 .pack ()#line:1428
    OOO000OO0000O0000 .config (command =O0000OO0O0OOO0O00 .yview )#line:1429
    O0000OO0O0OOO0O00 .config (yscrollcommand =OOO000OO0000O0000 .set )#line:1430
    O0000OO0O0OOO0O00 .insert (END ,"\n                                             帮助文件\n\n\n为帮助用户快速熟悉“阅易评”使用方法，现以医疗器械不良事件报告表为例，对使用步骤作以下说明：\n\n第一步：原始数据准备\n用户登录国家医疗器械不良事件监测信息系统（https://maers.adrs.org.cn/），在“个例不良事件管理—报告浏览”页面，选择本次评估的报告范围（时间、报告状态、事发地监测机构等）后进行查询和导出。\n●注意：国家医疗器械不良事件监测信息系统设置每次导出数据上限为5000份报告，如查询发现需导出报告数量超限，需分次导出；如导出数据为压缩包，需先行解压。如原始数据在多个文件夹内，需先行整理到统一文件夹中，方便下一步操作。\n\n第二步：原始数据导入\n用户点击“导入原始数据”按钮，在弹出数据导入框中找到原始数据存储位置，本程序支持导入多个原始数据文件，可在长按键盘“Ctrl”按键的同时分别点击相关文件，选择完毕后点击“打开”按钮，程序会提示“数据读取成功”或“导入文件错误”。\n●注意：基于当前评估工作需要，仅针对使用单位报告进行评估，故导入数据时仅选择“使用单位、经营企业医疗器械不良事件报告”，不支持与“上市许可持有人医疗器械不良事件报告”混选。如提示“导入文件错误，请重试”，请重启程序并重新操作，如仍提示错误可与开发者联系（联系方式见文末）。\n\n第三步：报告抽样分组\n用户点击“随机抽样分组”按钮，在“随机抽样及随机分组”弹窗中：\n1、根据评估目的，在“评估对象”处勾选相应选项，可根据选项对上报单位（医疗机构）、县（区）、地市实施评估。注意：如果您是省级用户，被评估对象是各地市，您要关闭本软件，修改好配置表文件夹“0（范例）质量评估.xls”中的“地市列表”单元表，将本省地市参照范例填好再运行本软件。如果被评估对象不是选择“地市”，则无需该项操作。\n2、根据报告伤害类型依次输入需抽取的比例或报告数量。程序默认此处输入数值小于1（含1）为抽取比例，输入数值大于1为抽取报告数量，用户根据实际情况任选一种方式即可。本程序支持不同伤害类型报告选用不同抽样方式。\n3、根据参与评估专家数量，在“抽样后随机分组数”输入对应数字。\n4、抽样方法有2种，一种是最大覆盖，即对每个评估对象按抽样数量/比例进行单独抽样，如遇到不足则多抽（所以总体实际抽样数量可能会比设置的多一点），每个评估对象都会被抽到；另外一种是总体随机，即按照设定的参数从总体中随机抽取（有可能部分评估对象没有被抽到）。\n用户在确定抽样分组内容全部正确录入后，点击“最大覆盖”或者“总体随机”按钮，根据程序提示选择保存地址。程序将按照专家数量将抽取的报告进行随即分配，生成对应份数的“专家评分表”，专家评分表包含评分项、详细描述、评分、满分、打分标准等。专家评分表自动隐藏报告单位等信息，用户可随机将评分表派发给专家进行评分。\n●注意：为保护数据同时便于专家查看，需对专家评分表进行格式设置，具体操作如下（或者直接使用格式刷一键完成，模板详见配置表-专家模板）：全选表格，右键-设置单元格格式-对齐，勾选自动换行，之后设置好列间距。此外，请勿修改“专家评分表“和“（最终评分需导入）被抽出的所有数据”两类工作文件的文件名。\n\n第四步：评估得分统计\n用户在全部专家完成评分后，将所有专家评分表放置在同一文件夹中，点击“评估得分统计”按钮，全选所有专家评分表和“（最终评分需导入）被抽出的所有数据”这个文件，后点击“打开”，程序将首先进行评分内容校验，对于打分错误报告给与提示并生成错误定位文件，需根据提示修正错误再全部导入。如打分项无误，程序将提示“打分表导入成功，正在统计请耐心等待”，并生成最终的评分结果。\n\n本程序由广东省药品不良反应监测中心和佛山市药品不良反应监测中心共同制作，其他贡献单位包括广州市药品不良反应监测中心、深圳市药物警戒和风险管理研究院等。如有疑问，请联系我们：\n评估标准相关问题：广东省药品不良反应监测中心 张博涵 020-37886057\n程序运行相关问题：佛山市药品不良反应监测中心 蔡权周 0757-82580815 \n\n",)#line:1434
    O0000OO0O0OOO0O00 .config (state =DISABLED )#line:1436
def TeasyreadT (OO00OOOO00OOOO000 ):#line:1439
    ""#line:1440
    OO00OOOO00OOOO000 ["#####分隔符#########"]="######################################################################"#line:1443
    OO000OO000OO0OO00 =OO00OOOO00OOOO000 .stack (dropna =False )#line:1444
    OO000OO000OO0OO00 =pd .DataFrame (OO000OO000OO0OO00 ).reset_index ()#line:1445
    OO000OO000OO0OO00 .columns =["序号","条目","详细描述"]#line:1446
    OO000OO000OO0OO00 ["逐条查看"]="逐条查看"#line:1447
    return OO000OO000OO0OO00 #line:1448
def Tget_list (OO0OOO0O0OO0000OO ):#line:1453
    ""#line:1454
    OO0OOO0O0OO0000OO =str (OO0OOO0O0OO0000OO )#line:1455
    O000OO0000OO000OO =[]#line:1456
    O000OO0000OO000OO .append (OO0OOO0O0OO0000OO )#line:1457
    O000OO0000OO000OO =",".join (O000OO0000OO000OO )#line:1458
    O000OO0000OO000OO =O000OO0000OO000OO .split (",")#line:1459
    O000OO0000OO000OO =",".join (O000OO0000OO000OO )#line:1460
    O000OO0000OO000OO =O000OO0000OO000OO .split ("，")#line:1461
    OOO0OOOO0OOO0000O =O000OO0000OO000OO [:]#line:1462
    O000OO0000OO000OO =list (set (O000OO0000OO000OO ))#line:1463
    O000OO0000OO000OO .sort (key =OOO0OOOO0OOO0000O .index )#line:1464
    return O000OO0000OO000OO #line:1465
def thread_it (O0OOOO0O0OOOO00OO ,*O00000OO0O0O0O000 ):#line:1468
    ""#line:1469
    OO0OO00O00000000O =threading .Thread (target =O0OOOO0O0OOOO00OO ,args =O00000OO0O0O0O000 )#line:1471
    OO0OO00O00000000O .setDaemon (True )#line:1473
    OO0OO00O00000000O .start ()#line:1475
def showWelcome ():#line:1478
    ""#line:1479
    OO0OOO0O0O0O0OO00 =roox .winfo_screenwidth ()#line:1480
    O0OO0000OOO0O0OO0 =roox .winfo_screenheight ()#line:1482
    roox .overrideredirect (True )#line:1484
    roox .attributes ("-alpha",1 )#line:1485
    O0O00OO00O000OO00 =(OO0OOO0O0O0O0OO00 -475 )/2 #line:1486
    OOOOO0OO000O0OO00 =(O0OO0000OOO0O0OO0 -200 )/2 #line:1487
    roox .geometry ("675x140+%d+%d"%(O0O00OO00O000OO00 ,OOOOO0OO000O0OO00 ))#line:1489
    roox ["bg"]="royalblue"#line:1490
    OO000O000O0O00000 =Label (roox ,text ="阅易评",fg ="white",bg ="royalblue",font =("微软雅黑",35 ))#line:1493
    OO000O000O0O00000 .place (x =0 ,y =15 ,width =675 ,height =90 )#line:1494
    O00O00000O0OO000O =Label (roox ,text ="                                 广东省药品不良反应监测中心                         V"+version_now ,fg ="white",bg ="cornflowerblue",font =("微软雅黑",15 ),)#line:1501
    O00O00000O0OO000O .place (x =0 ,y =90 ,width =675 ,height =50 )#line:1502
def closeWelcome ():#line:1505
    ""#line:1506
    for O00OOO000OO0O0OO0 in range (2 ):#line:1507
        root .attributes ("-alpha",0 )#line:1508
        time .sleep (1 )#line:1509
    root .attributes ("-alpha",1 )#line:1510
    roox .destroy ()#line:1511
root =Tk ()#line:1515
root .title ("阅易评 V"+version_now )#line:1516
try :#line:1517
    root .iconphoto (True ,PhotoImage (file =peizhidir +"0（范例）ico.png"))#line:1518
except :#line:1519
    pass #line:1520
sw_root =root .winfo_screenwidth ()#line:1521
sh_root =root .winfo_screenheight ()#line:1523
ww_root =700 #line:1525
wh_root =620 #line:1526
x_root =(sw_root -ww_root )/2 #line:1528
y_root =(sh_root -wh_root )/2 #line:1529
root .geometry ("%dx%d+%d+%d"%(ww_root ,wh_root ,x_root ,y_root ))#line:1530
root .configure (bg ="steelblue")#line:1531
try :#line:1534
    frame0 =ttk .Frame (root ,width =100 ,height =20 )#line:1535
    frame0 .pack (side =LEFT )#line:1536
    B_open_files1 =Button (frame0 ,text ="导入原始数据",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Topentable ,0 ),)#line:1549
    B_open_files1 .pack ()#line:1550
    B_open_files3 =Button (frame0 ,text ="随机抽样分组",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tchouyang ,ori ),)#line:1563
    B_open_files3 .pack ()#line:1564
    B_open_files3 =Button (frame0 ,text ="评估得分统计",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tpinggu ),)#line:1577
    B_open_files3 .pack ()#line:1578
    B_open_files3 =Button (frame0 ,text ="查看帮助文件",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (helper ),)#line:1591
    B_open_files3 .pack ()#line:1592
    B_open_files1 =Button (frame0 ,text ="更改评分标准",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Topentable ,123 ),)#line:1604
    B_open_files1 =Button (frame0 ,text ="内置数据清洗",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Txuanze ),)#line:1618
    if usergroup =="用户组=1":#line:1619
        B_open_files1 .pack ()#line:1620
    B_open_files1 =Button (frame0 ,text ="更改用户分组",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (display_random_number ))#line:1632
    if usergroup =="用户组=0":#line:1633
        B_open_files1 .pack ()#line:1634
except :#line:1636
    pass #line:1637
text =ScrolledText (root ,height =400 ,width =400 ,bg ="#FFFFFF",font ="微软雅黑")#line:1641
text .pack ()#line:1642
text .insert (END ,"\n    欢迎使用“阅易评”，本程序由广东省药品不良反应监测中心联合佛山市药品不良反应监测中心开发，主要功能包括：\n    1、根据报告伤害类型和用户自定义抽样比例对报告表随机抽样；\n    2、根据评估专家数量对抽出报告表随机分组，生成专家评分表；\n    3、根据专家最终评分实现自动汇总统计。\n    本程序供各监测机构免费使用，使用前请先查看帮助文件。\n  \n版本功能更新日志：\n2022年6月1日  支持医疗器械不良事件报告表质量评估(上报部分)。\n2022年10月31日  支持药品不良反应报告表质量评估。  \n2023年4月6日  支持化妆品不良反应报告表质量评估。\n2023年6月9日  支持医疗器械不良事件报告表质量评估(调查评价部分)。\n\n缺陷修正：20230609 修正结果列排序（按评分项目排序）。\n\n注：化妆品质量评估仅支持第一怀疑化妆品。",)#line:1647
text .insert (END ,"\n\n")#line:1648
setting_cfg =read_setting_cfg ()#line:1654
generate_random_file ()#line:1655
setting_cfg =open_setting_cfg ()#line:1656
if setting_cfg ["settingdir"]==0 :#line:1657
    showinfo (title ="提示",message ="未发现默认配置文件夹，请选择一个。如该配置文件夹中并无配置文件，将生成默认配置文件。")#line:1658
    filepathu =filedialog .askdirectory ()#line:1659
    path =get_directory_path (filepathu )#line:1660
    update_setting_cfg ("settingdir",path )#line:1661
setting_cfg =open_setting_cfg ()#line:1662
random_number =int (setting_cfg ["sidori"])#line:1663
input_number =int (str (setting_cfg ["sidfinal"])[0 :6 ])#line:1664
day_end =convert_and_compare_dates (str (setting_cfg ["sidfinal"])[6 :14 ])#line:1665
sid =random_number *2 +183576 #line:1666
if input_number ==sid and day_end =="未过期":#line:1667
    usergroup ="用户组=1"#line:1668
    text .insert (END ,usergroup +"   有效期至：")#line:1669
    text .insert (END ,datetime .strptime (str (int (int (str (setting_cfg ["sidfinal"])[6 :14 ])/4 )),"%Y%m%d"))#line:1670
else :#line:1671
    text .insert (END ,usergroup )#line:1672
text .insert (END ,"\n配置文件路径："+setting_cfg ["settingdir"]+"\n")#line:1673
peizhidir =str (setting_cfg ["settingdir"])+csdir .split ("pinggutools")[0 ][-1 ]#line:1674
aaass =update_software ("pinggutools")#line:1675
text .insert (END ,aaass )#line:1676
roox =Toplevel ()#line:1679
tMain =threading .Thread (target =showWelcome )#line:1680
tMain .start ()#line:1681
t1 =threading .Thread (target =closeWelcome )#line:1682
t1 .start ()#line:1683
root .lift ()#line:1684
root .attributes ("-topmost",True )#line:1685
root .attributes ("-topmost",False )#line:1686
root .mainloop ()#line:1687
