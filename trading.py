#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
import threading
import time
import sys
import math
import json
import pandas as pd
import talib as ta
import numpy as np
import ccxt 
symbols=['CAKE-PERP']
hodl_num=20
ftx = ccxt.ftx({
    'enableRateLimit': True,
    'apiKey': '',
    'secret': '',
})


def get_balance(symbol):
    global total_coin,total_u
    a=ftx.fetch_balance()
    total_u=a['total']['USD']
    symbol=symbol.split('/')
    total_coin=a[symbol[0]]['total']
    '''for i in a:
        print (i)
        if i==symbol:
            coin_total=i['total']
            print (coin_total)
    total_sol=a['total']['SOL']
    total_srm=a['total']['SRM']
    total_sushi=a['total']['SUSHI']
    total_u=a['total']['USD']'''

def get_ticker(symbol):
    global tickers,bid_price,ask_price,last_price
    tickers=ftx.fetch_ticker(symbol)
    last_price=tickers['last']
    bid_price=tickers['bid']
    ask_price=tickers['ask']

def get_candle(symbol):
    global kline, k_close
    kline=ftx.fetch_ohlcv(symbol=symbol,timeframe='1m')
    k_close=[]
    for i in kline:
        k_close=k_close+[i[4]]
    return k_close

def trader(symbol):
    global now_amount
    open_orders=ftx.fetch_open_orders(symbol)
    if open_orders!=[]:
        #print ('cancel orders')
        ftx.cancel_all_orders(symbol=symbol)
    get_position(symbol)
    get_ticker(symbol)
    now_amount=fsize*last_price
    if symbol=='CAKE-PERP':
        order_size=0.1
        if fsize>-hodl_num and fsize<hodl_num:
            if now_amount<=init_amount-last_price:
                a=ftx.create_order(symbol=symbol, type='limit',side='buy', amount=order_size, price=bid_price)
                time.sleep(88)
            if now_amount>=init_amount+last_price:
                a=ftx.create_order(symbol=symbol, type='limit',side='sell', amount=order_size, price=ask_price)
                time.sleep(88)
    a=  ('init amount:',int(init_amount),' now amount:',int(now_amount),' PNL:',int(realizedPnl), ' Postion:',fsize)
    sys.stdout.flush()    
    sys.stdout.write("\r{0}".format(a))
    #2694.98
    #print (symbol.split('-')[0],' P:',fsize,' now:',last_price,' entry price:',recentAverageOpenPrice,' PNL:',realizedPnl,' TRI:',int(TRI))
    #print ('####'*22)

def get_position(symbol):
    global entryprice,fsize,side,recentAverageOpenPrice,realizedPnl
    a=ftx.fetch_positions()
    #print (a)
    fsize=entryprice=recentAverageOpenPrice=0
    side='null'
    for i in a:
        if i['info']['future']==symbol:
            if i['info']['entryPrice']!=None:
                entryprice=float(i['info']['entryPrice'])
                recentAverageOpenPrice=round(float(i['info']['recentAverageOpenPrice']),3)
                realizedPnl=round(float(i['info']['realizedPnl']),3)
            fsize=float(i['info']['netSize'])
            side=i['info']['side']

def get_trade_history(symbol):
    global trade_history
    a=ftx.fetch_my_trades(symbol)
    order_list=[]
    for i in a:
        order_list=order_list+[i['info']['side']]
    trade_history=order_list[-7:]
 
get_position(symbols[0])
#print (entryprice,fsize,side,recentAverageOpenPrice,realizedPnl)
init_amount=entryprice*fsize*20 #Pretend you have 20 cake-perp long position 
while 1:
    try:
        trader(symbols[0])
    except:
        pass
    time.sleep(8)
