# Shannon-s-Demon
SUMMARY & KEY FINDINGS

A little-known concept called Shannon’s Demon may actually be a vital tool for increasing returns and minimizing risks in investor portfolios over time.

As we’ll show, the mathematical underpinnings of Shannon’s Demon can actually make it possible to generate positive returns at the portfolio level, even when all of the portfolio’s individual holdings are expected to produce zero, or even negative, returns over time.

Given the market environment as of this writing, which is characterized by near-zero bond yields and all-time high U.S. stock valuations, we feel the concepts that we outline below and the rebalancing return premiums that can be generated have the potential to offer investors attractive alternative paths to portfolio returns, all while avoiding incremental portfolio risks.

# How to use
pip install pandas, TA-lib, numpy, ccxt   
if u have trouble in install TA-lib? please follow below setp  
---
wget https://downloads.sourceforge.net/project/ta-lib/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz  
tar -xvf ta-lib-0.4.0-src.tar.gz  
cd ta-lib  
./configure  
make && make install 

when all done   
---
ftx = ccxt.ftx({   
    'enableRateLimit': True,   
    'apiKey': '',   
    'secret': '',   
})

python trading.py
# Liability
I am not your financial adviser, nor is this tool. Use this program as an educational tool, and nothing more. None of the contributors to this project are liable for any losses you may incur. Be wise and always do your own research.

# Trading strategies
Pretend you have 20 cake-perp long position and calculate with latest price as init_amount.
if cake-perp price go down or up, the bot will buy or sell to make the balance equal to init_amount,
as the result the bot will buy the bottom and sell the top.

# Buy me a coffee
Use my ftx Affiliate Link you will get 30% of your fees back.
https://ftx.com/referrals#a=7471063   
Or:   
BTC:   
3BgGZG7ZJwjCWgXFseyHTnAeiHrXX4MS4B   
DOGE:   
DKZA9RUaMhhqdTgm3XjK1y6jcvbwnV5jgD   
USDT:   
TX3tcBnTSSL9cPSoRvhv5bByDBekUByY4U   
