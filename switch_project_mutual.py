import os
import base64
import pandas as pd
import datetime as dt
from binance import Client
from time import sleep
import math
from datetime import datetime
import numpy as np
import termcolor
import random
import json
import jsonpickle
from json import JSONEncoder
import pprint
from collections import Counter
from contextlib import suppress

# login
key = 
secret = 
client = Client(key,secret)

# onedrive link
def create_onedrive_directdownload(onedrive_link):
    data_bytes64 = base64.b64encode(bytes(onedrive_link, 'utf-8'))
    data_bytes64_String = data_bytes64.decode('utf-8').replace('/', '_').replace('+', '-').rstrip("=")
    resultUrl = f"https://api.onedrive.com/v1.0/shares/u!{data_bytes64_String}/root/content"
    return resultUrl

# filter dataframe to all pairs of trusted list
def filter_it(dataframe, trusts):
    df_trusts = dataframe[dataframe['symbol'].isin(trusts)]
    #df[df['A'].isin(lis)]
    return df_trusts
# binance
list_of_pairs = ['ETHBTC', 'LTCBTC', 'BNBBTC', 'NEOBTC', 'QTUMETH', 'EOSETH', 'SNTETH', 'BNTETH', 'BCCBTC', 'GASBTC', 'BNBETH','BTCUSDT', 'ETHUSDT', 'HSRBTC', 'OAXETH', 'DNTETH', 'MCOETH', 'ICNETH', 'MCOBTC', 'WTCBTC', 'WTCETH', 'LRCBTC', 'LRCETH', 'QTUMBTC', 'YOYOBTC', 'OMGBTC', 'OMGETH', 'ZRXBTC', 'ZRXETH', 'STRATBTC', 'STRATETH', 'SNGLSBTC', 'SNGLSETH', 'BQXBTC', 'BQXETH', 'KNCBTC', 'KNCETH', 'FUNBTC', 'FUNETH', 'SNMBTC', 'SNMETH', 'NEOETH', 'IOTABTC', 'IOTAETH', 'LINKBTC', 'LINKETH', 'XVGBTC', 'XVGETH', 'SALTBTC', 'SALTETH', 'MDABTC', 'MDAETH', 'MTLBTC', 'MTLETH', 'SUBBTC', 'SUBETH', 'EOSBTC', 'SNTBTC', 'ETCETH', 'ETCBTC', 'MTHBTC', 'MTHETH', 'ENGBTC', 'ENGETH', 'DNTBTC', 'ZECBTC', 'ZECETH', 'BNTBTC', 'ASTBTC', 'ASTETH', 'DASHBTC', 'DASHETH', 'OAXBTC', 'ICNBTC', 'BTGBTC', 'BTGETH', 'EVXBTC', 'EVXETH', 'REQBTC', 'REQETH', 'VIBBTC', 'VIBETH', 'HSRETH', 'TRXBTC', 'TRXETH', 'POWRBTC', 'POWRETH', 'ARKBTC', 'ARKETH', 'YOYOETH', 'XRPBTC', 'XRPETH', 'MODBTC', 'MODETH', 'ENJBTC', 'ENJETH', 'STORJBTC', 'STORJETH', 'BNBUSDT', 'VENBNB', 'YOYOBNB', 'POWRBNB', 'VENBTC', 'VENETH', 'KMDBTC', 'KMDETH', 'NULSBNB', 'RCNBTC', 'RCNETH', 'RCNBNB', 'NULSBTC', 'NULSETH', 'RDNBTC', 'RDNETH', 'RDNBNB', 'XMRBTC', 'XMRETH', 'DLTBNB', 'WTCBNB', 'DLTBTC', 'DLTETH', 'AMBBTC', 'AMBETH', 'AMBBNB', 'BCCETH', 'BCCUSDT', 'BCCBNB', 'BATBTC', 'BATETH', 'BATBNB', 'BCPTBTC', 'BCPTETH', 'BCPTBNB', 'ARNBTC', 'ARNETH', 'GVTBTC', 'GVTETH', 'CDTBTC', 'CDTETH', 'GXSBTC', 'GXSETH', 'NEOUSDT', 'NEOBNB', 'POEBTC', 'POEETH', 'QSPBTC', 'QSPETH', 'QSPBNB', 'BTSBTC', 'BTSETH', 'BTSBNB', 'XZCBTC', 'XZCETH', 'XZCBNB', 'LSKBTC', 'LSKETH', 'LSKBNB', 'TNTBTC', 'TNTETH', 'FUELBTC', 'FUELETH', 'MANABTC', 'MANAETH', 'BCDBTC', 'BCDETH', 'DGDBTC', 'DGDETH', 'IOTABNB', 'ADXBTC', 'ADXETH', 'ADXBNB', 'ADABTC', 'ADAETH', 'PPTBTC', 'PPTETH', 'CMTBTC', 'CMTETH', 'CMTBNB', 'XLMBTC', 'XLMETH', 'XLMBNB', 'CNDBTC', 'CNDETH', 'CNDBNB', 'LENDBTC', 'LENDETH', 'WABIBTC', 'WABIETH', 'WABIBNB', 'LTCETH', 'LTCUSDT', 'LTCBNB', 'TNBBTC', 'TNBETH', 'WAVESBTC', 'WAVESETH', 'WAVESBNB', 'GTOBTC', 'GTOETH', 'GTOBNB', 'ICXBTC', 'ICXETH', 'ICXBNB', 'OSTBTC', 'OSTETH', 'OSTBNB', 'ELFBTC', 'ELFETH', 'AIONBTC', 'AIONETH', 'AIONBNB', 'NEBLBTC', 'NEBLBNB', 'BRDBTC', 'BRDETH', 'BRDBNB', 'MCOBNB', 'EDOBTC', 'EDOETH', 'WINGSBTC', 'WINGSETH', 'NAVBTC', 'NAVETH', 'NAVBNB', 'LUNBTC', 'LUNETH', 'TRIGBTC', 'TRIGETH', 'TRIGBNB', 'APPCBTC', 'APPCETH', 'APPCBNB', 'VIBEBTC', 'VIBEETH', 'RLCBTC', 'RLCETH', 'RLCBNB', 'INSBTC', 'INSETH', 'PIVXBTC', 'PIVXBNB', 'IOSTBTC', 'IOSTETH', 'CHATBTC', 'CHATETH', 'STEEMBTC', 'STEEMETH', 'STEEMBNB', 'NANOBTC', 'NANOETH', 'NANOBNB', 'VIABTC', 'VIAETH', 'VIABNB', 'BLZBTC', 'BLZETH', 'BLZBNB', 'AEBTC', 'AEETH', 'AEBNB', 'RPXBTC', 'RPXETH', 'RPXBNB', 'NCASHBTC', 'NCASHETH', 'NCASHBNB', 'POABTC', 'POAETH', 'POABNB', 'ZILBTC', 'ZILETH', 'ZILBNB', 'ONTBTC', 'ONTETH', 'ONTBNB', 'STORMBTC', 'STORMETH', 'STORMBNB', 'QTUMBNB', 'QTUMUSDT', 'XEMBTC', 'XEMETH', 'XEMBNB', 'WANBTC', 'WANETH', 'WANBNB', 'WPRBTC', 'WPRETH', 'QLCBTC', 'QLCETH', 'SYSBTC', 'SYSETH', 'SYSBNB', 'QLCBNB', 'GRSBTC', 'GRSETH', 'ADAUSDT', 'ADABNB', 'CLOAKBTC', 'CLOAKETH', 'GNTBTC', 'GNTETH', 'GNTBNB', 'LOOMBTC', 'LOOMETH', 'LOOMBNB', 'XRPUSDT', 'BCNBTC', 'BCNETH', 'BCNBNB', 'REPBTC', 'REPBNB', 'BTCTUSD', 'TUSDBTC', 'ETHTUSD', 'TUSDETH', 'TUSDBNB', 'ZENBTC', 'ZENETH', 'ZENBNB', 'SKYBTC', 'SKYETH', 'SKYBNB', 'EOSUSDT', 'EOSBNB', 'CVCBTC', 'CVCETH', 'CVCBNB', 'THETABTC', 'THETAETH', 'THETABNB', 'XRPBNB', 'TUSDUSDT', 'IOTAUSDT', 'XLMUSDT', 'IOTXBTC', 'IOTXETH', 'QKCBTC', 'QKCETH', 'AGIBTC', 'AGIETH', 'AGIBNB', 'NXSBTC', 'NXSETH', 'NXSBNB', 'ENJBNB', 'DATABTC', 'DATAETH', 'ONTUSDT', 'TRXBNB', 'TRXUSDT', 'ETCUSDT', 'ETCBNB', 'ICXUSDT', 'SCBTC', 'SCETH', 'NPXSBTC', 'NPXSETH', 'VENUSDT', 'KEYBTC', 'KEYETH', 'NASBTC', 'NASETH', 'NASBNB', 'MFTBTC', 'MFTETH', 'MFTBNB', 'DENTBTC', 'DENTETH', 'ARDRBTC', 'ARDRETH', 'ARDRBNB', 'NULSUSDT', 'HOTBTC', 'HOTETH', 'VETBTC', 'VETETH', 'VETUSDT', 'VETBNB', 'DOCKBTC', 'DOCKETH', 'POLYBTC', 'POLYBNB', 'PHXBTC', 'PHXETH', 'PHXBNB', 'HCBTC', 'HCETH', 'GOBTC', 'GOBNB', 'PAXBTC', 'PAXBNB', 'PAXUSDT', 'PAXETH', 'RVNBTC', 'DCRBTC', 'DCRBNB', 'USDCBNB', 'MITHBTC', 'MITHBNB', 'BCHABCBTC', 'BCHSVBTC', 'BCHABCUSDT', 'BCHSVUSDT', 'BNBPAX', 'BTCPAX', 'ETHPAX', 'XRPPAX', 'EOSPAX', 'XLMPAX', 'RENBTC', 'RENBNB', 'BNBTUSD', 'XRPTUSD', 'EOSTUSD', 'XLMTUSD', 'BNBUSDC', 'BTCUSDC', 'ETHUSDC', 'XRPUSDC', 'EOSUSDC', 'XLMUSDC', 'USDCUSDT', 'ADATUSD', 'TRXTUSD', 'NEOTUSD', 'TRXXRP', 'XZCXRP', 'PAXTUSD', 'USDCTUSD', 'USDCPAX', 'LINKUSDT', 'LINKTUSD', 'LINKPAX', 'LINKUSDC', 'WAVESUSDT', 'WAVESTUSD', 'WAVESPAX', 'WAVESUSDC', 'BCHABCTUSD', 'BCHABCPAX', 'BCHABCUSDC', 'BCHSVTUSD', 'BCHSVPAX', 'BCHSVUSDC', 'LTCTUSD', 'LTCPAX', 'LTCUSDC', 'TRXPAX', 'TRXUSDC', 'BTTBTC', 'BTTBNB', 'BTTUSDT', 'BNBUSDS', 'BTCUSDS', 'USDSUSDT', 'USDSPAX', 'USDSTUSD', 'USDSUSDC', 'BTTPAX', 'BTTTUSD', 'BTTUSDC', 'ONGBNB', 'ONGBTC', 'ONGUSDT', 'HOTBNB', 'HOTUSDT', 'ZILUSDT', 'ZRXBNB', 'ZRXUSDT', 'FETBNB', 'FETBTC', 'FETUSDT', 'BATUSDT', 'XMRBNB', 'XMRUSDT', 'ZECBNB', 'ZECUSDT', 'ZECPAX', 'ZECTUSD', 'ZECUSDC', 'IOSTUSDT', 'CELRBNB', 'CELRBTC', 'CELRUSDT', 'ADAPAX', 'ADAUSDC', 'NEOPAX', 'NEOUSDC', 'DASHBNB', 'DASHUSDT', 'NANOUSDT', 'OMGBNB', 'OMGUSDT', 'THETAUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICBNB', 'MATICBTC', 'MATICUSDT', 'ATOMBNB', 'ATOMBTC', 'ATOMUSDT', 'ATOMUSDC', 'ATOMPAX', 'ATOMTUSD', 'ETCUSDC', 'ETCPAX', 'ETCTUSD', 'BATUSDC', 'BATPAX', 'BATTUSD', 'PHBBNB', 'PHBBTC', 'PHBUSDC', 'PHBTUSD', 'PHBPAX', 'TFUELBNB', 'TFUELBTC', 'TFUELUSDT', 'TFUELUSDC', 'TFUELTUSD', 'TFUELPAX', 'ONEBNB', 'ONEBTC', 'ONEUSDT', 'ONETUSD', 'ONEPAX', 'ONEUSDC', 'FTMBNB', 'FTMBTC', 'FTMUSDT', 'FTMTUSD', 'FTMPAX', 'FTMUSDC', 'BTCBBTC', 'BCPTTUSD', 'BCPTPAX', 'BCPTUSDC', 'ALGOBNB', 'ALGOBTC', 'ALGOUSDT', 'ALGOTUSD', 'ALGOPAX', 'ALGOUSDC', 'USDSBUSDT', 'USDSBUSDS', 'GTOUSDT', 'GTOPAX', 'GTOTUSD', 'GTOUSDC', 'ERDBNB', 'ERDBTC', 'ERDUSDT', 'ERDPAX', 'ERDUSDC', 'DOGEBNB', 'DOGEBTC', 'DOGEUSDT', 'DOGEPAX', 'DOGEUSDC', 'DUSKBNB', 'DUSKBTC', 'DUSKUSDT', 'DUSKUSDC', 'DUSKPAX', 'BGBPUSDC', 'ANKRBNB', 'ANKRBTC', 'ANKRUSDT', 'ANKRTUSD', 'ANKRPAX', 'ANKRUSDC', 'ONTPAX', 'ONTUSDC', 'WINBNB', 'WINBTC', 'WINUSDT', 'WINUSDC', 'COSBNB', 'COSBTC', 'COSUSDT', 'TUSDBTUSD', 'NPXSUSDT', 'NPXSUSDC', 'COCOSBNB', 'COCOSBTC', 'COCOSUSDT', 'MTLUSDT', 'TOMOBNB', 'TOMOBTC', 'TOMOUSDT', 'TOMOUSDC', 'PERLBNB', 'PERLBTC', 'PERLUSDC', 'PERLUSDT', 'DENTUSDT', 'MFTUSDT', 'KEYUSDT', 'STORMUSDT', 'DOCKUSDT', 'WANUSDT', 'FUNUSDT', 'CVCUSDT', 'BTTTRX', 'WINTRX', 'CHZBNB', 'CHZBTC', 'CHZUSDT', 'BANDBNB', 'BANDBTC', 'BANDUSDT', 'BNBBUSD', 'BTCBUSD', 'BUSDUSDT', 'BEAMBNB', 'BEAMBTC', 'BEAMUSDT', 'XTZBNB', 'XTZBTC', 'XTZUSDT', 'RENUSDT', 'RVNUSDT', 'HCUSDT', 'HBARBNB', 'HBARBTC', 'HBARUSDT', 'NKNBNB', 'NKNBTC', 'NKNUSDT', 'XRPBUSD', 'ETHBUSD', 'BCHABCBUSD', 'LTCBUSD', 'LINKBUSD', 'ETCBUSD', 'STXBNB', 'STXBTC', 'STXUSDT', 'KAVABNB', 'KAVABTC', 'KAVAUSDT', 'BUSDNGN', 'BNBNGN', 'BTCNGN', 'ARPABNB', 'ARPABTC', 'ARPAUSDT', 'TRXBUSD', 'EOSBUSD', 'IOTXUSDT', 'RLCUSDT', 'MCOUSDT', 'XLMBUSD', 'ADABUSD', 'CTXCBNB', 'CTXCBTC', 'CTXCUSDT', 'BCHBNB', 'BCHBTC', 'BCHUSDT', 'BCHUSDC', 'BCHTUSD', 'BCHPAX', 'BCHBUSD', 'BTCRUB', 'ETHRUB', 'XRPRUB', 'BNBRUB', 'TROYBNB', 'TROYBTC', 'TROYUSDT', 'BUSDRUB', 'QTUMBUSD', 'VETBUSD', 'VITEBNB', 'VITEBTC', 'VITEUSDT', 'FTTBNB', 'FTTBTC', 'FTTUSDT', 'BTCTRY', 'BNBTRY', 'BUSDTRY', 'ETHTRY', 'XRPTRY', 'USDTTRY', 'USDTRUB', 'BTCEUR', 'ETHEUR', 'BNBEUR', 'XRPEUR', 'EURBUSD', 'EURUSDT', 'OGNBNB', 'OGNBTC', 'OGNUSDT', 'DREPBNB', 'DREPBTC', 'DREPUSDT', 'BULLUSDT', 'BULLBUSD', 'BEARUSDT', 'BEARBUSD', 'ETHBULLUSDT', 'ETHBULLBUSD', 'ETHBEARUSDT', 'ETHBEARBUSD', 'TCTBNB', 'TCTBTC', 'TCTUSDT', 'WRXBNB', 'WRXBTC', 'WRXUSDT', 'ICXBUSD', 'BTSUSDT', 'BTSBUSD', 'LSKUSDT', 'BNTUSDT', 'BNTBUSD', 'LTOBNB', 'LTOBTC', 'LTOUSDT', 'ATOMBUSD', 'DASHBUSD', 'NEOBUSD', 'WAVESBUSD', 'XTZBUSD', 'EOSBULLUSDT', 'EOSBULLBUSD', 'EOSBEARUSDT', 'EOSBEARBUSD', 'XRPBULLUSDT', 'XRPBULLBUSD', 'XRPBEARUSDT', 'XRPBEARBUSD', 'BATBUSD', 'ENJBUSD', 'NANOBUSD', 'ONTBUSD', 'RVNBUSD', 'STRATBUSD', 'STRATBNB', 'STRATUSDT', 'AIONBUSD', 'AIONUSDT', 'MBLBNB', 'MBLBTC', 'MBLUSDT', 'COTIBNB', 'COTIBTC', 'COTIUSDT', 'ALGOBUSD', 'BTTBUSD', 'TOMOBUSD', 'XMRBUSD', 'ZECBUSD', 'BNBBULLUSDT', 'BNBBULLBUSD', 'BNBBEARUSDT', 'BNBBEARBUSD', 'STPTBNB', 'STPTBTC', 'STPTUSDT', 'BTCZAR', 'ETHZAR', 'BNBZAR', 'USDTZAR', 'BUSDZAR', 'BTCBKRW', 'ETHBKRW', 'BNBBKRW', 'WTCUSDT', 'DATABUSD', 'DATAUSDT', 'XZCUSDT', 'SOLBNB', 'SOLBTC', 'SOLUSDT', 'SOLBUSD', 'BTCIDRT', 'BNBIDRT', 'USDTIDRT', 'BUSDIDRT', 'CTSIBTC', 'CTSIUSDT', 'CTSIBNB', 'CTSIBUSD', 'HIVEBNB', 'HIVEBTC', 'HIVEUSDT', 'CHRBNB', 'CHRBTC', 'CHRUSDT', 'BTCUPUSDT', 'BTCDOWNUSDT', 'GXSUSDT', 'ARDRUSDT', 'ERDBUSD', 'LENDUSDT', 'HBARBUSD', 'MATICBUSD', 'WRXBUSD', 'ZILBUSD', 'MDTBNB', 'MDTBTC', 'MDTUSDT', 'STMXBTC', 'STMXETH', 'STMXUSDT', 'KNCBUSD', 'KNCUSDT', 'REPBUSD', 'REPUSDT', 'LRCBUSD', 'LRCUSDT', 'IQBNB', 'IQBUSD', 'PNTBTC', 'PNTUSDT', 'BTCGBP', 'ETHGBP', 'XRPGBP', 'BNBGBP', 'GBPBUSD', 'DGBBTC', 'DGBBUSD', 'BTCUAH', 'USDTUAH', 'COMPBTC', 'COMPBNB', 'COMPBUSD', 'COMPUSDT', 'BTCBIDR', 'ETHBIDR', 'BNBBIDR', 'BUSDBIDR', 'USDTBIDR', 'BKRWUSDT', 'BKRWBUSD', 'SCUSDT', 'ZENUSDT', 'SXPBTC', 'SXPBNB', 'SXPBUSD', 'SNXBTC', 'SNXBNB', 'SNXBUSD', 'SNXUSDT', 'ETHUPUSDT', 'ETHDOWNUSDT', 'ADAUPUSDT', 'ADADOWNUSDT', 'LINKUPUSDT', 'LINKDOWNUSDT', 'VTHOBNB', 'VTHOBUSD', 'VTHOUSDT', 'DCRBUSD', 'DGBUSDT', 'GBPUSDT', 'STORJBUSD', 'SXPUSDT', 'IRISBNB', 'IRISBTC', 'IRISBUSD', 'MKRBNB', 'MKRBTC', 'MKRUSDT', 'MKRBUSD', 'DAIBNB', 'DAIBTC', 'DAIUSDT', 'DAIBUSD', 'RUNEBNB', 'RUNEBTC', 'RUNEBUSD', 'MANABUSD', 'DOGEBUSD', 'LENDBUSD', 'ZRXBUSD', 'DCRUSDT', 'STORJUSDT', 'XRPBKRW', 'ADABKRW', 'BTCAUD', 'ETHAUD', 'AUDBUSD', 'FIOBNB', 'FIOBTC', 'FIOBUSD', 'BNBUPUSDT', 'BNBDOWNUSDT', 'XTZUPUSDT', 'XTZDOWNUSDT', 'AVABNB', 'AVABTC', 'AVABUSD', 'USDTBKRW', 'BUSDBKRW', 'IOTABUSD', 'MANAUSDT', 'XRPAUD', 'BNBAUD', 'AUDUSDT', 'BALBNB', 'BALBTC', 'BALBUSD', 'YFIBNB', 'YFIBTC', 'YFIBUSD', 'YFIUSDT', 'BLZBUSD', 'KMDBUSD', 'BALUSDT', 'BLZUSDT', 'IRISUSDT', 'KMDUSDT', 'BTCDAI', 'ETHDAI', 'BNBDAI', 'USDTDAI', 'BUSDDAI', 'JSTBNB', 'JSTBTC', 'JSTBUSD', 'JSTUSDT', 'SRMBNB', 'SRMBTC', 'SRMBUSD', 'SRMUSDT', 'ANTBNB', 'ANTBTC', 'ANTBUSD', 'ANTUSDT', 'CRVBNB', 'CRVBTC', 'CRVBUSD', 'CRVUSDT', 'SANDBNB', 'SANDBTC', 'SANDUSDT', 'SANDBUSD', 'OCEANBNB', 'OCEANBTC', 'OCEANBUSD', 'OCEANUSDT', 'NMRBTC', 'NMRBUSD', 'NMRUSDT', 'DOTBNB', 'DOTBTC', 'DOTBUSD', 'DOTUSDT', 'LUNABNB', 'LUNABTC', 'LUNABUSD', 'LUNAUSDT', 'IDEXBTC', 'IDEXBUSD', 'RSRBNB', 'RSRBTC', 'RSRBUSD', 'RSRUSDT', 'PAXGBNB', 'PAXGBTC', 'PAXGBUSD', 'PAXGUSDT', 'WNXMBNB', 'WNXMBTC', 'WNXMBUSD', 'WNXMUSDT', 'TRBBNB', 'TRBBTC', 'TRBBUSD', 'TRBUSDT', 'ETHNGN', 'DOTBIDR', 'LINKAUD', 'SXPAUD', 'BZRXBNB', 'BZRXBTC', 'BZRXBUSD', 'BZRXUSDT', 'WBTCBTC', 'WBTCETH', 'SUSHIBNB', 'SUSHIBTC', 'SUSHIBUSD', 'SUSHIUSDT', 'YFIIBNB', 'YFIIBTC', 'YFIIBUSD', 'YFIIUSDT', 'KSMBNB', 'KSMBTC', 'KSMBUSD', 'KSMUSDT', 'EGLDBNB', 'EGLDBTC', 'EGLDBUSD', 'EGLDUSDT', 'DIABNB', 'DIABTC', 'DIABUSD', 'DIAUSDT', 'RUNEUSDT', 'FIOUSDT', 'UMABTC', 'UMAUSDT', 'EOSUPUSDT', 'EOSDOWNUSDT', 'TRXUPUSDT', 'TRXDOWNUSDT', 'XRPUPUSDT', 'XRPDOWNUSDT', 'DOTUPUSDT', 'DOTDOWNUSDT', 'SRMBIDR', 'ONEBIDR', 'LINKTRY', 'USDTNGN', 'BELBNB', 'BELBTC', 'BELBUSD', 'BELUSDT', 'WINGBNB', 'WINGBTC', 'SWRVBNB', 'SWRVBUSD', 'WINGBUSD', 'WINGUSDT', 'LTCUPUSDT', 'LTCDOWNUSDT', 'LENDBKRW', 'SXPEUR', 'CREAMBNB', 'CREAMBUSD', 'UNIBNB', 'UNIBTC', 'UNIBUSD', 'UNIUSDT', 'NBSBTC', 'NBSUSDT', 'OXTBTC', 'OXTUSDT', 'SUNBTC', 'SUNUSDT', 'AVAXBNB', 'AVAXBTC', 'AVAXBUSD', 'AVAXUSDT', 'HNTBTC', 'HNTUSDT', 'BAKEBNB', 'BURGERBNB', 'SXPBIDR', 'LINKBKRW', 'FLMBNB', 'FLMBTC', 'FLMBUSD', 'FLMUSDT', 'SCRTBTC', 'SCRTETH', 'CAKEBNB', 'CAKEBUSD', 'SPARTABNB', 'UNIUPUSDT', 'UNIDOWNUSDT', 'ORNBTC', 'ORNUSDT', 'TRXNGN', 'SXPTRY', 'UTKBTC', 'UTKUSDT', 'XVSBNB', 'XVSBTC', 'XVSBUSD', 'XVSUSDT', 'ALPHABNB', 'ALPHABTC', 'ALPHABUSD', 'ALPHAUSDT', 'VIDTBTC', 'VIDTBUSD', 'AAVEBNB', 'BTCBRL', 'USDTBRL', 'AAVEBTC', 'AAVEETH', 'AAVEBUSD', 'AAVEUSDT', 'AAVEBKRW', 'NEARBNB', 'NEARBTC', 'NEARBUSD', 'NEARUSDT', 'SXPUPUSDT', 'SXPDOWNUSDT', 'DOTBKRW', 'SXPGBP', 'FILBNB', 'FILBTC', 'FILBUSD', 'FILUSDT', 'FILUPUSDT', 'FILDOWNUSDT', 'YFIUPUSDT', 'YFIDOWNUSDT', 'INJBNB', 'INJBTC', 'INJBUSD', 'INJUSDT', 'AERGOBTC', 'AERGOBUSD', 'LINKEUR', 'ONEBUSD', 'EASYETH', 'AUDIOBTC', 'AUDIOBUSD', 'AUDIOUSDT', 'CTKBNB', 'CTKBTC', 'CTKBUSD', 'CTKUSDT', 'BCHUPUSDT', 'BCHDOWNUSDT', 'BOTBTC', 'BOTBUSD', 'ETHBRL', 'DOTEUR', 'AKROBTC', 'AKROUSDT', 'KP3RBNB', 'KP3RBUSD', 'AXSBNB', 'AXSBTC', 'AXSBUSD', 'AXSUSDT', 'HARDBNB', 'HARDBTC', 'HARDBUSD', 'HARDUSDT', 'BNBBRL', 'LTCEUR', 'RENBTCBTC', 'RENBTCETH', 'DNTBUSD', 'DNTUSDT', 'SLPETH', 'ADAEUR', 'LTCNGN', 'CVPETH', 'CVPBUSD', 'STRAXBTC', 'STRAXETH', 'STRAXBUSD', 'STRAXUSDT', 'FORBTC', 'FORBUSD', 'UNFIBNB', 'UNFIBTC', 'UNFIBUSD', 'UNFIUSDT', 'FRONTETH', 'FRONTBUSD', 'BCHABUSD', 'ROSEBTC', 'ROSEBUSD', 'ROSEUSDT', 'AVAXTRY', 'BUSDBRL', 'AVAUSDT', 'SYSBUSD', 'XEMUSDT', 'HEGICETH', 'HEGICBUSD', 'AAVEUPUSDT', 'AAVEDOWNUSDT', 'PROMBNB', 'PROMBUSD', 'XRPBRL', 'XRPNGN', 'SKLBTC', 'SKLBUSD', 'SKLUSDT', 'BCHEUR', 'YFIEUR', 'ZILBIDR', 'SUSDBTC', 'SUSDETH', 'SUSDUSDT', 'COVERETH', 'COVERBUSD', 'GLMBTC', 'GLMETH', 'GHSTETH', 'GHSTBUSD', 'SUSHIUPUSDT', 'SUSHIDOWNUSDT', 'XLMUPUSDT', 'XLMDOWNUSDT', 'LINKBRL', 'LINKNGN', 'LTCRUB', 'TRXTRY', 'XLMEUR', 'DFETH', 'DFBUSD', 'GRTBTC', 'GRTETH', 'GRTUSDT', 'JUVBTC', 'JUVBUSD', 'JUVUSDT', 'PSGBTC', 'PSGBUSD', 'PSGUSDT', 'BUSDBVND', 'USDTBVND', '1INCHBTC', '1INCHUSDT', 'REEFBTC', 'REEFUSDT', 'OGBTC', 'OGUSDT', 'ATMBTC', 'ATMUSDT', 'ASRBTC', 'ASRUSDT', 'CELOBTC', 'CELOUSDT', 'RIFBTC', 'RIFUSDT', 'CHZTRY', 'XLMTRY', 'LINKGBP', 'GRTEUR', 'BTCSTBTC', 'BTCSTBUSD', 'BTCSTUSDT', 'TRUBTC', 'TRUBUSD', 'TRUUSDT', 'DEXEETH', 'DEXEBUSD', 'EOSEUR', 'LTCBRL', 'USDCBUSD', 'TUSDBUSD', 'PAXBUSD', 'CKBBTC', 'CKBBUSD', 'CKBUSDT', 'TWTBTC', 'TWTBUSD', 'TWTUSDT', 'FIROBTC', 'FIROETH', 'FIROUSDT', 'BETHETH', 'DOGEEUR', 'DOGETRY', 'DOGEAUD', 'DOGEBRL', 'DOTNGN', 'PROSETH', 'LITBTC', 'LITBUSD', 'LITUSDT', 'BTCVAI', 'BUSDVAI', 'SFPBTC', 'SFPBUSD', 'SFPUSDT', 'DOGEGBP', 'DOTTRY', 'FXSBTC', 'FXSBUSD', 'DODOBTC', 'DODOBUSD', 'DODOUSDT', 'FRONTBTC', 'EASYBTC', 'CAKEBTC', 'CAKEUSDT', 'BAKEBUSD', 'UFTETH', 'UFTBUSD', '1INCHBUSD', 'BANDBUSD', 'GRTBUSD', 'IOSTBUSD', 'OMGBUSD', 'REEFBUSD', 'ACMBTC', 'ACMBUSD', 'ACMUSDT', 'AUCTIONBTC', 'AUCTIONBUSD', 'PHABTC', 'PHABUSD', 'DOTGBP', 'ADATRY', 'ADABRL', 'ADAGBP', 'TVKBTC', 'TVKBUSD', 'BADGERBTC', 'BADGERBUSD', 'BADGERUSDT', 'FISBTC', 'FISBUSD', 'FISUSDT', 'DOTBRL', 'ADAAUD', 'HOTTRY', 'EGLDEUR', 'OMBTC', 'OMBUSD', 'OMUSDT', 'PONDBTC', 'PONDBUSD', 'PONDUSDT', 'DEGOBTC', 'DEGOBUSD', 'DEGOUSDT', 'AVAXEUR', 'BTTTRY', 'CHZBRL', 'UNIEUR', 'ALICEBTC', 'ALICEBUSD', 'ALICEUSDT', 'CHZBUSD', 'CHZEUR', 'CHZGBP', 'BIFIBNB', 'BIFIBUSD', 'LINABTC', 'LINABUSD', 'LINAUSDT', 'ADARUB', 'ENJBRL', 'ENJEUR', 'MATICEUR', 'NEOTRY', 'PERPBTC', 'PERPBUSD', 'PERPUSDT', 'RAMPBTC', 'RAMPBUSD', 'RAMPUSDT', 'SUPERBTC', 'SUPERBUSD', 'SUPERUSDT', 'CFXBTC', 'CFXBUSD', 'CFXUSDT', 'ENJGBP', 'EOSTRY', 'LTCGBP', 'LUNAEUR', 'RVNTRY', 'THETAEUR', 'XVGBUSD', 'EPSBTC', 'EPSBUSD', 'EPSUSDT', 'AUTOBTC', 'AUTOBUSD', 'AUTOUSDT', 'TKOBTC', 'TKOBIDR', 'TKOBUSD', 'TKOUSDT', 'PUNDIXETH', 'PUNDIXUSDT', 'BTTBRL', 'BTTEUR', 'HOTEUR', 'WINEUR', 'TLMBTC', 'TLMBUSD', 'TLMUSDT', '1INCHUPUSDT', '1INCHDOWNUSDT', 'BTGBUSD', 'BTGUSDT', 'HOTBUSD', 'BNBUAH', 'ONTTRY', 'VETEUR', 'VETGBP', 'WINBRL', 'MIRBTC', 'MIRBUSD', 'MIRUSDT', 'BARBTC', 'BARBUSD', 'BARUSDT', 'FORTHBTC', 'FORTHBUSD', 'FORTHUSDT', 'CAKEGBP', 'DOGERUB', 'HOTBRL', 'WRXEUR', 'EZBTC', 'EZETH', 'BAKEUSDT', 'BURGERBUSD', 'BURGERUSDT', 'SLPBUSD', 'SLPUSDT', 'TRXAUD', 'TRXEUR', 'VETTRY', 'SHIBUSDT', 'SHIBBUSD', 'ICPBTC', 'ICPBNB', 'ICPBUSD', 'ICPUSDT', 'BTCGYEN', 'USDTGYEN', 'SHIBEUR', 'SHIBRUB', 'ETCEUR', 'ETCBRL', 'DOGEBIDR', 'ARBTC', 'ARBNB', 'ARBUSD', 'ARUSDT', 'POLSBTC', 'POLSBNB', 'POLSBUSD', 'POLSUSDT', 'MDXBTC', 'MDXBNB', 'MDXBUSD', 'MDXUSDT', 'MASKBNB', 'MASKBUSD', 'MASKUSDT', 'LPTBTC', 'LPTBNB', 'LPTBUSD', 'LPTUSDT', 'ETHUAH', 'MATICBRL', 'SOLEUR', 'SHIBBRL', 'AGIXBTC', 'ICPEUR', 'MATICGBP', 'SHIBTRY', 'MATICBIDR', 'MATICRUB', 'NUBTC', 'NUBNB', 'NUBUSD', 'NUUSDT', 'XVGUSDT', 'RLCBUSD', 'CELRBUSD', 'ATMBUSD', 'ZENBUSD', 'FTMBUSD', 'THETABUSD', 'WINBUSD', 'KAVABUSD', 'XEMBUSD', 'ATABTC', 'ATABNB', 'ATABUSD', 'ATAUSDT', 'GTCBTC', 'GTCBNB', 'GTCBUSD', 'GTCUSDT', 'TORNBTC', 'TORNBNB', 'TORNBUSD', 'TORNUSDT', 'MATICTRY', 'ETCGBP', 'SOLGBP', 'BAKEBTC', 'COTIBUSD', 'KEEPBTC', 'KEEPBNB', 'KEEPBUSD', 'KEEPUSDT', 'SOLTRY', 'RUNEGBP', 'SOLBRL', 'SCBUSD', 'CHRBUSD', 'STMXBUSD', 'HNTBUSD', 'FTTBUSD', 'DOCKBUSD', 'ADABIDR', 'ERNBNB', 'ERNBUSD', 'ERNUSDT', 'KLAYBTC', 'KLAYBNB', 'KLAYBUSD', 'KLAYUSDT', 'RUNEEUR', 'MATICAUD', 'DOTRUB', 'UTKBUSD', 'IOTXBUSD', 'PHAUSDT', 'SOLRUB', 'RUNEAUD', 'BUSDUAH', 'BONDBTC', 'BONDBNB', 'BONDBUSD', 'BONDUSDT', 'MLNBTC', 'MLNBNB', 'MLNBUSD', 'MLNUSDT', 'GRTTRY', 'CAKEBRL', 'ICPRUB', 'DOTAUD', 'AAVEBRL', 'EOSAUD', 'DEXEUSDT', 'LTOBUSD', 'ADXBUSD', 'QUICKBTC', 'QUICKBNB', 'QUICKBUSD', 'C98USDT', 'C98BUSD', 'C98BNB', 'C98BTC', 'CLVBTC', 'CLVBNB', 'CLVBUSD', 'CLVUSDT', 'QNTBTC', 'QNTBNB', 'QNTBUSD', 'QNTUSDT', 'FLOWBTC', 'FLOWBNB', 'FLOWBUSD', 'FLOWUSDT', 'XECBUSD', 'AXSBRL', 'AXSAUD', 'TVKUSDT', 'MINABTC', 'MINABNB', 'MINABUSD', 'MINAUSDT', 'RAYBNB', 'RAYBUSD', 'RAYUSDT', 'FARMBTC', 'FARMBNB', 'FARMBUSD', 'FARMUSDT', 'ALPACABTC', 'ALPACABNB', 'ALPACABUSD', 'ALPACAUSDT', 'TLMTRY', 'QUICKUSDT', 'ORNBUSD', 'MBOXBTC', 'MBOXBNB', 'MBOXBUSD', 'MBOXUSDT', 'VGXBTC', 'VGXETH', 'FORUSDT', 'REQUSDT', 'GHSTUSDT', 'TRURUB', 'FISBRL', 'WAXPUSDT', 'WAXPBUSD', 'WAXPBNB', 'WAXPBTC', 'TRIBEBTC', 'TRIBEBNB', 'TRIBEBUSD', 'TRIBEUSDT', 'GNOUSDT', 'GNOBUSD', 'GNOBNB', 'GNOBTC', 'ARPATRY', 'PROMBTC', 'MTLBUSD', 'OGNBUSD', 'XECUSDT', 'C98BRL', 'SOLAUD', 'XRPBIDR', 'POLYBUSD', 'ELFUSDT', 'DYDXUSDT', 'DYDXBUSD', 'DYDXBNB', 'DYDXBTC', 'ELFBUSD', 'POLYUSDT', 'IDEXUSDT', 'VIDTUSDT', 'SOLBIDR', 'AXSBIDR', 'BTCUSDP', 'ETHUSDP', 'BNBUSDP', 'USDPBUSD', 'USDPUSDT', 'GALAUSDT', 'GALABUSD', 'GALABNB', 'GALABTC', 'FTMBIDR', 'ALGOBIDR', 'CAKEAUD', 'KSMAUD', 'WAVESRUB', 'SUNBUSD', 'ILVUSDT', 'ILVBUSD', 'ILVBNB', 'ILVBTC', 'RENBUSD', 'YGGUSDT', 'YGGBUSD', 'YGGBNB', 'YGGBTC', 'STXBUSD', 'SYSUSDT', 'DFUSDT', 'SOLUSDC', 'ARPARUB', 'LTCUAH', 'FETBUSD', 'ARPABUSD', 'LSKBUSD', 'AVAXBIDR', 'ALICEBIDR', 'FIDAUSDT', 'FIDABUSD', 'FIDABNB', 'FIDABTC', 'DENTBUSD', 'FRONTUSDT', 'CVPUSDT', 'AGLDBTC', 'AGLDBNB', 'AGLDBUSD', 'AGLDUSDT', 'RADBTC', 'RADBNB', 'RADBUSD', 'RADUSDT', 'UNIAUD', 'HIVEBUSD', 'STPTBUSD', 'BETABTC', 'BETABNB', 'BETABUSD', 'BETAUSDT', 'SHIBAUD', 'RAREBTC', 'RAREBNB', 'RAREBUSD', 'RAREUSDT', 'AVAXBRL', 'AVAXAUD', 'LUNAAUD', 'TROYBUSD', 'AXSETH', 'FTMETH', 'SOLETH', 'SSVBTC', 'SSVETH', 'LAZIOTRY', 'LAZIOEUR', 'LAZIOBTC', 'LAZIOUSDT', 'CHESSBTC', 'CHESSBNB', 'CHESSBUSD', 'CHESSUSDT', 'FTMAUD', 'FTMBRL', 'SCRTBUSD', 'ADXUSDT', 'AUCTIONUSDT', 'CELOBUSD', 'FTMRUB', 'NUAUD', 'NURUB', 'REEFTRY', 'REEFBIDR', 'SHIBDOGE', 'DARUSDT', 'DARBUSD', 'DARBNB', 'DARBTC', 'BNXBTC', 'BNXBNB', 'BNXBUSD', 'BNXUSDT', 'RGTUSDT', 'RGTBTC', 'RGTBUSD', 'RGTBNB', 'LAZIOBUSD', 'OXTBUSD', 'MANATRY', 'ALGORUB', 'SHIBUAH', 'LUNABIDR', 'AUDUSDC', 'MOVRBTC', 'MOVRBNB', 'MOVRBUSD', 'MOVRUSDT', 'CITYBTC', 'CITYBNB', 'CITYBUSD', 'CITYUSDT', 'ENSBTC', 'ENSBNB', 'ENSBUSD', 'ENSUSDT', 'SANDETH', 'DOTETH', 'MATICETH', 'ANKRBUSD', 'SANDTRY', 'MANABRL', 'KP3RUSDT', 'QIUSDT', 'QIBUSD', 'QIBNB', 'QIBTC', 'PORTOBTC', 'PORTOUSDT', 'PORTOTRY', 'PORTOEUR', 'POWRUSDT', 'POWRBUSD', 'AVAXETH', 'SLPTRY', 'FISTRY', 'LRCTRY', 'CHRETH', 'FISBIDR', 'VGXUSDT', 'GALAETH', 'JASMYUSDT', 'JASMYBUSD', 'JASMYBNB', 'JASMYBTC', 'AMPBTC', 'AMPBNB', 'AMPBUSD', 'AMPUSDT', 'PLABTC', 'PLABNB', 'PLABUSD', 'PLAUSDT', 'PYRBTC', 'PYRBUSD', 'PYRUSDT', 'RNDRBTC', 'RNDRUSDT', 'RNDRBUSD', 'ALCXBTC', 'ALCXBUSD', 'ALCXUSDT', 'SANTOSBTC', 'SANTOSUSDT', 'SANTOSBRL', 'SANTOSTRY', 'MCBTC', 'MCBUSD', 'MCUSDT', 'BELTRY', 'COCOSBUSD', 'DENTTRY', 'ENJTRY', 'NEORUB', 'SANDAUD', 'SLPBIDR', 'ANYBTC', 'ANYBUSD', 'ANYUSDT', 'BICOBTC', 'BICOBUSD', 'BICOUSDT', 'FLUXBTC', 'FLUXBUSD', 'FLUXUSDT', 'ALICETRY', 'FXSUSDT', 'GALABRL', 'GALATRY', 'LUNATRY', 'REQBUSD', 'SANDBRL', 'MANABIDR', 'SANDBIDR', 'VOXELBTC', 'VOXELBNB', 'VOXELBUSD', 'VOXELUSDT', 'COSBUSD', 'CTXCBUSD', 'FTMTRY', 'MANABNB', 'MINATRY', 'XTZTRY', 'HIGHBTC', 'HIGHBUSD', 'HIGHUSDT', 'CVXBTC', 'CVXBUSD', 'CVXUSDT', 'PEOPLEBTC', 'PEOPLEBUSD', 'PEOPLEUSDT', 'OOKIBUSD', 'OOKIUSDT', 'COCOSTRY', 'GXSBNB', 'LINKBNB', 'LUNAETH', 'MDTBUSD', 'NULSBUSD', 'SPELLBTC', 'SPELLUSDT', 'SPELLBUSD', 'USTBTC', 'USTBUSD', 'USTUSDT', 'JOEBTC', 'JOEBUSD', 'JOEUSDT', 'ATOMETH', 'DUSKBUSD', 'EGLDETH', 'ICPETH', 'LUNABRL', 'LUNAUST', 'NEARETH', 'ROSEBNB', 'VOXELETH', 'ALICEBNB', 'ATOMTRY', 'ETHUST', 'GALAAUD', 'LRCBNB', 'ONEETH', 'OOKIBNB', 'ACHBTC', 'ACHBUSD', 'ACHUSDT', 'IMXBTC', 'IMXBUSD', 'IMXUSDT', 'GLMRBTC', 'GLMRBUSD', 'GLMRUSDT', 'ATOMBIDR', 'DYDXETH', 'FARMETH', 'FORBNB', 'ICPTRY', 'JASMYETH', 'LINABNB', 'OOKIETH', 'ROSEETH', 'UMABUSD', 'UNIETH', 'XTZETH', 'LOKABTC', 'LOKABNB', 'LOKABUSD', 'LOKAUSDT', 'ATOMBRL', 'BNBUST', 'CRVETH', 'HIGHBNB', 'NEARRUB', 'ROSETRY', 'SCRTUSDT', 'API3BTC', 'API3BUSD', 'API3USDT', 'BTTCUSDT', 'BTTCUSDC', 'BTTCTRY', 'ACABTC', 'ACABUSD', 'ACAUSDT', 'ANCBTC', 'ANCBUSD', 'ANCUSDT', 'BDOTDOT', 'XNOBTC', 'XNOETH', 'XNOBUSD', 'XNOUSDT', 'COSTRY', 'KAVAETH', 'MCBNB', 'ONETRY', 'WOOBTC', 'WOOBNB', 'WOOBUSD', 'WOOUSDT', 'CELRETH', 'PEOPLEBNB', 'SLPBNB', 'SPELLBNB', 'SPELLTRY', 'TFUELBUSD', 'AXSTRY', 'DARTRY', 'NEARTRY', 'IDEXBNB', 'ALPINEEUR', 'ALPINETRY', 'ALPINEUSDT', 'ALPINEBTC', 'TUSDT', 'TBUSD', 'API3BNB', 'BETAETH', 'INJTRY', 'TLMBNB', 'ASTRBUSD', 'ASTRUSDT', 'API3TRY', 'GLMRBNB', 'MBOXTRY', 'NBTBIDR', 'NBTUSDT', 'GMTBTC', 'GMTBNB', 'GMTBUSD', 'GMTUSDT', 'ANCBNB', 'ATOMEUR', 'GALAEUR', 'KSMETH', 'UMATRY', 'KDABTC', 'KDABUSD', 'KDAUSDT', 'APEUSDT', 'APEBUSD', 'APEBTC', 'ALPINEBUSD', 'LUNAGBP', 'NEAREUR', 'TWTTRY', 'WAVESEUR', 'APEEUR', 'APEGBP', 'APETRY', 'BSWUSDT', 'BSWBUSD', 'BSWBNB', 'APEBNB', 'GMTBRL', 'GMTETH', 'JASMYTRY', 'SANTOSBUSD', 'APEAUD', 'BIFIUSDT', 'GMTEUR', 'IMXBNB', 'RUNEETH', 'AVAXGBP', 'MULTIBTC', 'MULTIBUSD', 'MULTIUSDT', 'APEETH', 'BSWETH', 'FILTRY', 'FTMEUR', 'GMTGBP', 'ZILTRY', 'GMTTRY', 'WAVESTRY', 'BTCUST', 'ASTRBTC', 'ASTRETH', 'BSWTRY', 'FTTETH', 'FUNBNB', 'PORTOBUSD', 'STEEMUSDT', 'ZILEUR', 'APEBRL', 'AUDIOTRY', 'BTTCBUSD', 'GMTAUD', 'MBLBUSD', 'MOBUSDT', 'MOBBUSD', 'MOBBTC', 'NEXOUSDT', 'NEXOBUSD', 'NEXOBTC', 'REIUSDT', 'REIBNB', 'REIETH', 'GALUSDT', 'GALBUSD', 'GALBNB', 'GALBTC', 'JASMYEUR', 'KNCBNB', 'SHIBGBP', 'GALEUR', 'GALTRY', 'LDOBUSD', 'LDOUSDT', 'LDOBTC', 'ENSTRY', 'DAREUR', 'DARETH', 'ALGOETH', 'ALGOTRY', 'GALETH', 'EPXUSDT', 'EPXBUSD', 'RUNETRY', 'GALBRL', 'STEEMBUSD', 'CVCBUSD', 'REIBUSD', 'DREPBUSD', 'AKROBUSD', 'PUNDIXBUSD', 'LUNCBUSD', 'USTCBUSD', 'OPBTC', 'OPBUSD', 'OPUSDT', 'OGBUSD', 'KEYBUSD', 'ASRBUSD']
trust_symbols = ['IOTA', 'BTC', 'DOT', 'ETH', 'ADA', 'BNB', 'MINA', 'UNI', 'LINK', 'AAVE', 'SAND', 'MANA', 'MATIC', 'FIL', 'FTM', 'SOL',
                 'THETA', 'AXS', 'MKR', 'MIOTA', 'ALGO', 'ATOM', 'ENJ', 'KSM', 'NEXO', 'ZIL', 'AVAX', 'XTZ', 'KAVA', 'APE', 'CELO',
                 'KDA', '1INCH', 'CAKE', 'FTT']

dataframe = pd.DataFrame(client.get_ticker())
dataframe["lastPrice"] = pd.to_numeric(dataframe["lastPrice"], downcast="float")
dataframe["bidPrice"] = pd.to_numeric(dataframe["bidPrice"], downcast="float")
dataframe["askPrice"] = pd.to_numeric(dataframe["askPrice"], downcast="float")
possible_df = pd.DataFrame()
for sample in range(0, len(trust_symbols)):
    symbol = trust_symbols[sample]
    # print(symbol)
    trusts_pairs_1 = [(symbol + s) for s in trust_symbols if s is not symbol]
    trusts_pairs_2 = [(s + symbol) for s in trust_symbols if s is not symbol]
    trusted_pairs = trusts_pairs_1 + trusts_pairs_2
    possible_trades = filter_it(dataframe, trusted_pairs)
    possible_df = possible_df.append(possible_trades, ignore_index=True)
possible_df = possible_df.drop_duplicates()
possibles = possible_df['symbol'].tolist()


# get data market
def get_data_market(symbol):
    #starttime = '1 week ago UTC'  # to start for 1 week ago
    starttime = '1 week ago UTC'
    interval = '1h'
    df_new = get_hourly_dataframe(symbol, starttime, interval)
    #df_new['date'] = pd.to_datetime(df_new['date'],unit='ms')
    # calculate 5 moving average using Pandas
    df_new['5sma'] = df_new['close'].rolling(5).mean()
    # calculate 15 moving average using Pandas
    df_new['15sma'] = df_new['close'].rolling(15).mean()
    # Calculate signal column
    df_new['Signal'] = np.where(df_new['5sma'] > df_new['15sma'], 1, 0)  # NaN is not a number
    # Calculate position column with diff
    df_new['Position'] = df_new['Signal'].diff()
    df_new['Buy'] = np.where(df_new['Position'] == 1, df_new['close'], np.NaN)
    df_new['Sell'] = np.where(df_new['Position'] == -1, df_new['close'], np.NaN)
    #read
    df_new['date'] = pd.to_datetime(df_new['date'], unit='ms')
    return df_new

def get_hourly_dataframe(symbol, starttime, interval):
    ''''valid intervals-1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
    request historical candle (or klines) data using timestamp from above interval
    either every min, hr, day or month
    starttime = '30 minutes ago UTC' for last 30 mins time
    e.g. client.get_historical_klines(symbol='ETHUSDTUSDT', '1m', starttime)
    starttime = '1 Dec, 2017', '1 Jan, 2018'  for last month of 2017
    e.g. client.get_historical_klines(symbol='BTCUSDT', '1m', "1 Dec, 2017", # "1 Jan, 2018")'''
    print(symbol)
    bars = client.get_historical_klines(symbol, interval, starttime)

    # Keep only first 5 columns, "date" "open" "high" "low" "close"
    for line in bars:
        del line[5:]
    #  2 dimensional tabular data
    df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])
    return df

# returns whether to buy quote symbol
def get_last_signal(df_now):
    # indexes
    signals = df_now['Position'].tolist()
    # get last signal at the moment
    buy_indices = []
    sell_indices = []
    for i in range(len(signals)):
        if signals[i] == 1:
            buy_indices.append(i)
    for i in range(len(signals)):
        if signals[i] == -1:
            sell_indices.append(i)
    if len(buy_indices) > 0:
        last_buy = max(buy_indices)
    else:
        last_buy = 1
    if len(sell_indices) > 0:
        last_sell = max(sell_indices)
    else:
        last_sell = 2

    if last_buy > last_sell:
        buy_quote = False
    if last_buy < last_sell:
        buy_quote = True
    return buy_quote

# Xmin back trend % (last x minutes) as df (positive first)
def get_trend_of_x_min(x, list_of_pairs):
    ## build indicator yourself
    new_frame = pd.DataFrame()
    for sample in list_of_pairs:
        dict = {}
        dict['pair'] = sample
        #print(sample)
        klines = client.get_historical_klines(sample, Client.KLINE_INTERVAL_1MINUTE, "10 minutes ago UTC")
        for line in klines:
            del line[5:]
        #  2 dimensional tabular data
        df = pd.DataFrame(klines, columns=['date', 'open', 'high', 'low', 'close'])
        df['date'] = pd.to_datetime(df['date'], unit='ms')
        df_last_xmin = df[10-x:]
        if len(df_last_xmin) > x-1:
            # minute 1
            then = float(df_last_xmin['close'].tolist()[:1][0])
            # minute x
            now = float(df_last_xmin['close'].tolist()[x-1:][0])
            # trend
            trend = ((1 - then / now) * 100)
            dict['trend'] = trend
            new_frame = new_frame.append(dict, ignore_index=True)
            new_frame = new_frame.sort_values(by=['trend'], ascending=False)
    new_frame = new_frame.reset_index()
    return new_frame

# trend 10min
def get_trend_of_x_min10(list_of_pairs):
    ## build indicator yourself
    new_frame = pd.DataFrame()
    for sample in list_of_pairs:
        dict = {}
        dict['pair'] = sample
        #print(sample)
        klines = client.get_historical_klines(sample, Client.KLINE_INTERVAL_1MINUTE, "10 minutes ago UTC")
        for line in klines:
            del line[5:]
        #  2 dimensional tabular data
        df = pd.DataFrame(klines, columns=['date', 'open', 'high', 'low', 'close'])
        df['date'] = pd.to_datetime(df['date'], unit='ms')
        if len(df) == 10:
            # minute 1
            then = float(df['close'].tolist()[:1][0])
            # minute x
            now = float(df['close'].tolist()[10-1:][0])
            # trend
            trend = ((1 - then / now) * 100)
            dict['trend'] = trend
            new_frame = new_frame.append(dict, ignore_index=True)
            new_frame = new_frame.sort_values(by=['trend'], ascending=False)
    new_frame = new_frame.reset_index()
    return new_frame

# trend 30min
def get_trend_of_x_min30(list_of_pairs):
    ## build indicator yourself
    new_frame = pd.DataFrame()
    for sample in list_of_pairs:
        dict = {}
        dict['pair'] = sample
        #print(sample)
        klines = client.get_historical_klines(sample, Client.KLINE_INTERVAL_5MINUTE, "30 minutes ago UTC")
        for line in klines:
            del line[5:]
        #  2 dimensional tabular data
        df = pd.DataFrame(klines, columns=['date', 'open', 'high', 'low', 'close'])
        df['date'] = pd.to_datetime(df['date'], unit='ms')
        if len(df) == 6:
            # minute 1
            then = float(df['close'].tolist()[:1][0])
            # minute x
            now = float(df['close'].tolist()[6-1:][0])
            # trend
            trend = ((1 - then / now) * 100)
            dict['trend'] = trend
            new_frame = new_frame.append(dict, ignore_index=True)
            new_frame = new_frame.sort_values(by=['trend'], ascending=False)
    new_frame = new_frame.reset_index()
    return new_frame

# trend 60min
def get_trend_of_x_min60(list_of_pairs):
    ## build indicator yourself
    new_frame = pd.DataFrame()
    for sample in list_of_pairs:
        dict = {}
        dict['pair'] = sample
        #print(sample)
        klines = client.get_historical_klines(sample, Client.KLINE_INTERVAL_5MINUTE, "1 hours ago UTC")
        for line in klines:
            del line[5:]
        #  2 dimensional tabular data
        df = pd.DataFrame(klines, columns=['date', 'open', 'high', 'low', 'close'])
        df['date'] = pd.to_datetime(df['date'], unit='ms')
        if len(df) == 12:
            # minute 1
            then = float(df['close'].tolist()[:1][0])
            # minute x
            now = float(df['close'].tolist()[12-1:][0])
            # trend
            trend = ((1 - then / now) * 100)
            dict['trend'] = trend
            new_frame = new_frame.append(dict, ignore_index=True)
            new_frame = new_frame.sort_values(by=['trend'], ascending=False)
    new_frame = new_frame.reset_index()
    return new_frame

# trend 2h
def get_trend_of_x_min2h(list_of_pairs):
    ## build indicator yourself
    new_frame = pd.DataFrame()
    for sample in list_of_pairs:
        dict = {}
        dict['pair'] = sample
        #print(sample)
        klines = client.get_historical_klines(sample, Client.KLINE_INTERVAL_5MINUTE, "2 hours ago UTC")
        for line in klines:
            del line[5:]
        #  2 dimensional tabular data
        df = pd.DataFrame(klines, columns=['date', 'open', 'high', 'low', 'close'])
        df['date'] = pd.to_datetime(df['date'], unit='ms')
        if len(df) == 24:
            # minute 1
            then = float(df['close'].tolist()[:1][0])
            # minute x
            now = float(df['close'].tolist()[24-1:][0])
            # trend
            trend = ((1 - then / now) * 100)
            dict['trend'] = trend
            new_frame = new_frame.append(dict, ignore_index=True)
            new_frame = new_frame.sort_values(by=['trend'], ascending=False)
    new_frame = new_frame.reset_index()
    return new_frame

# get max prices of last 3h
def get_max_last3(list_of_pairs):
    ## build indicator yourself
    new_frame = pd.DataFrame()
    for sample in list_of_pairs:
        dict = {}
        dict['pair'] = sample
        #print(sample)
        # 12 h back
        klines = client.get_historical_klines(sample, Client.KLINE_INTERVAL_5MINUTE, "3h hours ago UTC")
        for line in klines:
            del line[5:]
        #  2 dimensional tabular data
        df = pd.DataFrame(klines, columns=['date', 'open', 'high', 'low', 'close'])
        df['date'] = pd.to_datetime(df['date'], unit='ms')
        # now
        klines2 = client.get_historical_klines(sample, Client.KLINE_INTERVAL_1MINUTE, "2 minutes ago UTC")
        for line in klines2:
            del line[5:]
        #  2 dimensional tabular data
        df2 = pd.DataFrame(klines2, columns=['date', 'open', 'high', 'low', 'close'])
        df2['date'] = pd.to_datetime(df2['date'], unit='ms')
        if len(df) == 36 and len(df2) == 2:
            # max
            close_values = df['close'].tolist()
            close_values = [float(x) for x in close_values]
            index_max = np.argmax(np.asarray(close_values))
            max = close_values[index_max]
            now = float(df2['close'][1])
            dict['max'] = max
            dict['now'] = now
            dict['relation to max 3'] = 100*(1-(max/now-1))
            new_frame = new_frame.append(dict, ignore_index=True)
            new_frame = new_frame.sort_values(by=['max'], ascending=False)
    new_frame = new_frame.reset_index()
    return new_frame

# get max prices of last 12h
def get_max_last12(list_of_pairs):
    ## build indicator yourself
    new_frame = pd.DataFrame()
    for sample in list_of_pairs:
        dict = {}
        dict['pair'] = sample
        #print(sample)
        # 12 h back
        klines = client.get_historical_klines(sample, Client.KLINE_INTERVAL_3MINUTE, "12 hours ago UTC")
        for line in klines:
            del line[5:]
        #  2 dimensional tabular data
        df = pd.DataFrame(klines, columns=['date', 'open', 'high', 'low', 'close'])
        df['date'] = pd.to_datetime(df['date'], unit='ms')
        # now
        klines2 = client.get_historical_klines(sample, Client.KLINE_INTERVAL_1MINUTE, "2 minutes ago UTC")
        for line in klines2:
            del line[5:]
        #  2 dimensional tabular data
        df2 = pd.DataFrame(klines2, columns=['date', 'open', 'high', 'low', 'close'])
        df2['date'] = pd.to_datetime(df2['date'], unit='ms')
        if len(df) == 240 and len(df2) == 2:
            # max
            close_values = df['close'].tolist()
            close_values = [float(x) for x in close_values]
            index_max = np.argmax(np.asarray(close_values))
            max = close_values[index_max]
            now = float(df2['close'][1])
            dict['max'] = max
            dict['now'] = now
            dict['relation to max 12'] = 100*(1-(max/now-1))
            new_frame = new_frame.append(dict, ignore_index=True)
            new_frame = new_frame.sort_values(by=['max'], ascending=False)
    new_frame = new_frame.reset_index()
    return new_frame

# get max prices of last 36h
def get_max_last36(list_of_pairs):
    ## build indicator yourself
    new_frame = pd.DataFrame()
    for sample in list_of_pairs:
        dict = {}
        dict['pair'] = sample
        #print(sample)
        # 12 h back
        klines = client.get_historical_klines(sample, Client.KLINE_INTERVAL_30MINUTE, "3 days ago UTC")
        for line in klines:
            del line[5:]
        #  2 dimensional tabular data
        df = pd.DataFrame(klines, columns=['date', 'open', 'high', 'low', 'close'])
        df['date'] = pd.to_datetime(df['date'], unit='ms')
        # now
        klines2 = client.get_historical_klines(sample, Client.KLINE_INTERVAL_1MINUTE, "2 minutes ago UTC")
        for line in klines2:
            del line[5:]
        #  2 dimensional tabular data
        df2 = pd.DataFrame(klines2, columns=['date', 'open', 'high', 'low', 'close'])
        df2['date'] = pd.to_datetime(df2['date'], unit='ms')
        if len(df) == 144 and len(df2) == 2:
            # max
            close_values = df['close'].tolist()
            close_values = [float(x) for x in close_values]
            index_max = np.argmax(np.asarray(close_values))
            max = close_values[index_max]
            now = float(df2['close'][1])
            dict['max'] = max
            dict['now'] = now
            dict['relation to max 36'] = 100*(1-(max/now-1))
            new_frame = new_frame.append(dict, ignore_index=True)
            new_frame = new_frame.sort_values(by=['max'], ascending=False)
    new_frame = new_frame.reset_index()
    return new_frame

# get max prices of last 20 days
def get_max_last20d(list_of_pairs):
    ## build indicator yourself
    new_frame = pd.DataFrame()
    for sample in list_of_pairs:
        dict = {}
        dict['pair'] = sample
        #print(sample)
        # 20 d back
        klines = client.get_historical_klines(sample, Client.KLINE_INTERVAL_30MINUTE, "20 days ago UTC")
        for line in klines:
            del line[5:]
        #  2 dimensional tabular data
        df = pd.DataFrame(klines, columns=['date', 'open', 'high', 'low', 'close'])
        df['date'] = pd.to_datetime(df['date'], unit='ms')
        # now
        klines2 = client.get_historical_klines(sample, Client.KLINE_INTERVAL_1MINUTE, "2 minutes ago UTC")
        for line in klines2:
            del line[5:]
        #  2 dimensional tabular data
        df2 = pd.DataFrame(klines2, columns=['date', 'open', 'high', 'low', 'close'])
        df2['date'] = pd.to_datetime(df2['date'], unit='ms')
        if len(df) == 960 and len(df2) == 2:
            # max
            close_values = df['close'].tolist()
            close_values = [float(x) for x in close_values]
            index_max = np.argmax(np.asarray(close_values))
            max = close_values[index_max]
            now = float(df2['close'][1])
            dict['max'] = max
            dict['now'] = now
            dict['relation to max 20 days'] = 100*(1-(max/now-1))
            new_frame = new_frame.append(dict, ignore_index=True)
            new_frame = new_frame.sort_values(by=['max'], ascending=False)
    new_frame = new_frame.reset_index()
    d20_infos = new_frame['relation to max 20 days'].to_list()
    return new_frame, d20_infos

######################
######################

# get the left symbol of a pair (quote symbol has to be 3 letters)
def get_left_symbol(pair):
    if 'BUSD' in pair[1:]:
        quote_symbol = pair[len(pair) - 4:]
    elif 'USDT' in pair[1:]:
        quote_symbol = pair[len(pair) - 4:]
    elif 'USDC' in pair[1:]:
        quote_symbol = pair[len(pair) - 4:]
    elif 'DOGE' in pair[1:]:
        quote_symbol = pair[len(pair) - 4:]
    else:
        quote_symbol = pair[len(pair)-3:]
    left_symbol = pair.replace(quote_symbol, '')
    return left_symbol

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

# get last TRADE (amount (of left_symbol), price and datetime)
def get_last_trade(pair):
    list = []
    amount = np.array(list)
    quote_amount = np.array(list)
    prices = np.array(list)
    trades = client.get_my_trades(symbol=pair)#, recvWindow=150)
    if len(trades) > 0:
        orderId = trades[len(trades)-1]['orderId']
        time = trades[len(trades) - 1]['time'] / 1000
        readable = dt.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S.%f')
        isBuyer = trades[len(trades) - 1]['isBuyer']
        comission = float(trades[len(trades)-1]['commission'])
        for sample in range(0, len(trades)):
            if trades[sample]['orderId'] == orderId:
                # store split amount
                split_amount_qty = np.array(float(trades[sample]['qty']))
                amount = np.append(amount, [split_amount_qty])
                # store split amount quote qty
                split_amount_quote_qty = np.array(float(trades[sample]['quoteQty']))
                quote_amount = np.append(quote_amount, [split_amount_quote_qty])
                # store split prices
                split_price = np.array(float(trades[sample]['price']))
                prices = np.append(prices, [split_price])
                #old# mean_price = float(np.mean(prices))
            tot_amount = float(np.sum(amount))-comission
            tot_amount_quote = float(np.sum(quote_amount))
            # calculate weihted mean price, accourding to amounts per split trade
            combined_pricesXamounts = 0
        for element in range(0, len(amount)):
            #print(element)
            #print(prices[element])
            priceXamount = amount[element] * prices[element]
            combined_pricesXamounts = combined_pricesXamounts + priceXamount
        weigted_price = combined_pricesXamounts/tot_amount
        return tot_amount, weigted_price, readable, isBuyer, tot_amount_quote, orderId, time
    else:
        readable = 'none'
        tot_amount = 'none'
        price = 'none'
        isBuyer = 'none'
        tot_amount_quote = 'none'
        orderId = 'none'
        time = 0
        #print('amount=', amount, ', price=', price, ", time=", readable[0:16])
        return tot_amount, price, readable, isBuyer, tot_amount_quote, orderId, time

# get last TRADE (amount (of left_symbol), price and datetime)
def get_trade_before_last_trade(pair):
    list = []
    amount = np.array(list)
    quote_amount = np.array(list)
    prices = np.array(list)
    trades = client.get_my_trades(symbol=pair)
    if len(trades) > 0:
        # store all order ID as uniqates in list
        od_id_list = []
        for ade in range (0, len(trades)):
            #print(trades[ade]['orderId'])
            id = str(trades[ade]['orderId'])
            if id not in od_id_list:
                od_id_list.append(id)
        # define last trade before last trade
        lastlast = od_id_list[len(od_id_list)-2]
        orderId = int(lastlast)
        #time = trades[len(trades) - 1]['time'] / 1000
        #readable = dt.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S.%f')
        for sample in range(0, len(trades)):
            if trades[sample]['orderId'] == orderId:
                # store split amount
                split_amount_qty = np.array(float(trades[sample]['qty']))
                amount = np.append(amount, [split_amount_qty])
                # store split amount quote qty
                split_amount_quote_qty = np.array(float(trades[sample]['quoteQty']))
                quote_amount = np.append(quote_amount, [split_amount_quote_qty])
                # store split prices
                split_price = np.array(float(trades[sample]['price']))
                prices = np.append(prices, [split_price])
                mean_price = float(np.mean(prices))
                readable = 0
            tot_amount = float(np.sum(amount))
            tot_amount_quote = float(np.sum(quote_amount))
        return tot_amount, mean_price, tot_amount_quote, orderId
    else:
        readable = 'none'
        tot_amount = 'none'
        mean_price = 'none'
        isBuyer = 'none'
        tot_amount_quote = 'none'
        orderId = 'none'
        time = 0
        #print('amount=', amount, ', price=', price, ", time=", readable[0:16])
        return tot_amount, mean_price, tot_amount_quote, orderId

def get_precision(pair):
    info = client.get_symbol_info(pair)
    precision = info['filters'][2]['stepSize']
    position_precision = precision.index('1') - 1
    if position_precision > -1:
        int_precision = position_precision
    else:
        int_precision = 0
    return int_precision

def get_quote_precision(pair):
    info = client.get_symbol_info(pair)
    precision = info['quotePrecision']
    return precision

# print list of the possible trades for each trusted symbol
def get_possible_trades(trust_symbols):
    dataframe = pd.DataFrame(client.get_ticker())
    dataframe["lastPrice"] = pd.to_numeric(dataframe["lastPrice"], downcast="float")
    dataframe["bidPrice"] = pd.to_numeric(dataframe["bidPrice"], downcast="float")
    dataframe["askPrice"] = pd.to_numeric(dataframe["askPrice"], downcast="float")
    possible_df = pd.DataFrame()
    for sample in range(0, len(trust_symbols)):
        symbol = trust_symbols[sample]
        #print(symbol)
        trusts_pairs_1 = [(symbol + s) for s in trust_symbols if s is not symbol]
        trusts_pairs_2 = [(s + symbol) for s in trust_symbols if s is not symbol]
        trusted_pairs = trusts_pairs_1 + trusts_pairs_2
        possible_trades = filter_it(dataframe, trusted_pairs)
        possible_df = possible_df.append(possible_trades, ignore_index=True)
    possible_df = possible_df.drop_duplicates()
    #print(possible_df)
    return possible_df

# get new dataframe of last trade infos
def df_last_trade_info(dataframe):
    pairs = dataframe['symbol'].tolist()
    print(len(pairs), 'possible pairs')
    print(len(trust_symbols), 'possible assets')
    print(str(len(trust_symbols)*max_ships_per_asset+len(n12_ships_assets)*12), 'max possible ships sailing')
    new_frame= pd.DataFrame()
    ## READ json file and include empty array for history
    read_file = open("top_json_mutual_file.json", "r")
    dict_read = json.load(read_file)
    for sample in range(0, len(pairs)):
        pair = pairs[sample]
        # get all active pairs as string
        active_pairs = [get_pair_from_ID(c) for c in dict_read.keys()]
        if pair in active_pairs:
            #print(pair)
            # get all entries from this pair
            active_ships = [c for c in dict_read.keys() if pair in c]
            # for all active ships of pair form dict pandas df for calculation
            for element in active_ships:
                dict = {}
                dict['pair'] = pair
                dict['pairID'] = element
                if 'isBuyer' in dict_read[element]:
                    dict['isBuyer'] = dict_read[element]['isBuyer']
                if 'status' in dict_read[element]:
                    if dict_read[element]['status'] == 'ship':
                        dict['last_trade_amount'] = dict_read[element]['qty']
                        dict['last_trade_price'] = dict_read[element]['ship_price']
                    if dict_read[element]['status'] == 'working':
                        #last_trade = get_last_trade(pair)
                        dict['last_trade_price'] = dict_read[element]['last_switch_price_JSON']
                        #dict['last_trade_amount'] = last_trade[0]
        # else:
        #     last_trade = get_last_trade(pair)
        #     #dict['last_trade_time'] = last_trade[2]
        #     dict['last_trade_price'] = last_trade[1]
        #     dict['last_trade_amount'] = last_trade[0]
        #     dict['isBuyer'] = last_trade[3]
                new_frame = new_frame.append(dict, ignore_index=True)
    read_file.close()
    return new_frame

# define trading sell
def trade_sell(pair, amount, x_coin, reset_market_pair):
    print(termcolor.colored(pair, "green"))
    print('place: amount=', amount, 'SELL')
    if x_coin not in pair:
        order = client.create_order(symbol=pair, side='SELL', type='MARKET', quantity=amount)
        print(termcolor.colored('success sell', "green"))
    else:
        amount = round_down(amount, get_precision(pair))
        order = client.create_order(symbol=pair, side='SELL', type='MARKET', quantity=amount)

# define trading buy (nextPair only for starting ships)
def trade_buy(pairID, pair, amount, x_coin):
    print('place: amount=', amount, 'BUY')
    if x_coin not in pair:
        print(termcolor.colored(pair, "green"))
        order = client.create_order(symbol=pair, side='BUY', type='MARKET', quantity=amount)
        print(termcolor.colored('buy', "cyan"))
    else:
        print(termcolor.colored(pair, "cyan"))
        order = client.create_order(symbol=pair, side='BUY', type='MARKET', quoteOrderQty=amount)
        # store startPair
        # read_file = open("top_json_mutual_file.json", "r")
        # dict_read = json.load(read_file)
        # dict_read[nextPair]['profits_arr'] = new_array
    if x_coin not in pair:
        read_file = open("top_json_mutual_file.json", "r")
        dict_read = json.load(read_file)
        last_trade = get_last_trade(pair)
        quote_amount_after = last_trade[4]
        qty_bought = last_trade[0]
        ####dict_read[pairID]['last_right_amount'] = quote_amount_after
        # store bought amount
        dict_read[pairID]['qty'] = qty_bought
        if dict_read[pairID]['status'] == 'ship':############################## check
            # before
            amount_before = dict_read[pairID]["start_switch_qty"]
            profit = (100-100/amount_before*quote_amount_after)
            # store profit values
            # array = dict_read['stats']['profits_arr']
            # array = jsonpickle.decode(array)
            # new_array = np.append(array, profit)
            # new_array = jsonpickle.encode(new_array)
            # dict_read['stats']['profits_arr'] = new_array
            dict_read[pairID]['last_profit'] = profit
            #store_profits of this ship
            array_sw_pro = dict_read[pairID]['switch_pro']
            array_sw_pro = jsonpickle.decode(array_sw_pro)
            new_sw_pro = np.append(array_sw_pro, profit)
            new_sw_pro = jsonpickle.encode(new_sw_pro)
            dict_read[pairID]['switch_pro'] = new_sw_pro
            print('switches: ', jsonpickle.decode(dict_read[pairID]['switch_pro']))
            print('profit =', round(profit, 3), '%')
        write_new_file = open("top_json_mutual_file.json", "w")
        json.dump(dict_read, write_new_file, indent=4)
        write_new_file.close()

# get dataframes (last BUY) with old and new prices and calculate price change from last trade
def build_dataframes_buyer(trust_symbols, split_loop):
    ### get markte data
    data = get_possible_trades(trust_symbols)
    data = data.reset_index()
    print('calculating buyers... # ', split_loop)
    ### get json data and combine with market data
    trades = df_last_trade_info(data)
    trades = trades.reset_index()

    # split buyer df
    if split_loop == 0:
        splitting = 10
        start = 0
        if len(trades) < splitting:
            splitting = len(trades)
    if split_loop == 1:
        splitting = 20
        start = 10
        if len(trades) < splitting:
            splitting = len(trades)
    if split_loop == 2:
        splitting = 30
        start = 20
        if len(trades) < splitting:
            splitting = len(trades)
    if split_loop == 3:
        splitting = 40
        start = 30
        if len(trades) < splitting:
            splitting = len(trades)
    if split_loop == 4:
        splitting = 50
        start = 40
        if len(trades) < splitting:
            splitting = len(trades)
    if split_loop == 5:
        splitting = 60
        start = 50
        if len(trades) < splitting:
            splitting = len(trades)
    if split_loop == 6:
        splitting = 70
        start = 60
        if len(trades) < splitting:
            splitting = len(trades)
    if split_loop == 7:
        splitting = 80
        start = 70
        if len(trades) < splitting:
            splitting = len(trades)
    if split_loop == 8:
        splitting = 90
        start = 80
        if len(trades) < splitting:
            splitting = len(trades)
    if split_loop == 9:
        splitting = 100
        start = 90
        if len(trades) < splitting:
            splitting = len(trades)
    if split_loop == 10:
        splitting = 110
        start = 100
        if len(trades) < splitting:
            splitting = len(trades)
    if split_loop == 11:
        splitting = 120
        start = 110
        if len(trades) < splitting:
            splitting = len(trades)
    # fusion
    if splitting > start:
        for sample in range(start, splitting):
            pairID = trades.loc[[sample]].pairID.values[0]
            pair = trades.loc[[sample]].pair.values[0]
            bid_price = float(data[data.symbol.str.contains(pair)].bidPrice.values[0])
            ask_price = float(data[data.symbol.str.contains(pair)].askPrice.values[0])
            trades.loc[sample, 'bidPrice'] = bid_price
            trades.loc[sample, 'askPrice'] = ask_price
        # split data into Buyer (True or False)
        buyer = pd.DataFrame(trades[trades['isBuyer'] == True])# last trade was a buy
        buyer['changePercent_lastTrade'] = -((1 - buyer['bidPrice'] / buyer['last_trade_price']) * 100)
        buyer = buyer.reset_index()
        buyer = pd.DataFrame(buyer[buyer['askPrice']> 0])

        ### RETURN tuple with several dataframes
        return buyer#, seller

# get dataframes (last BUY) with old and new prices and calculate price change from last trade
def return_nr_of_ships(trust_symbols):
    ### get markte data
    data = get_possible_trades(trust_symbols)
    data = data.reset_index()
    print('calculating buyers...')
    ### get json data and combine with market data
    trades = df_last_trade_info(data)
    trades = trades.reset_index()

    # count number of Buyer ships
    # analysis = trades['isBuyer'].value_counts(ascending=True)
    # nr_buyers = analysis[1]
    # nr_sellers = analysis[0]
    nr = len(trades)

    ### RETURN
    print('# SHIPS total: ', nr)
    return nr

# get dataframes (last SELL) with old and new prices and calculate price change from last trade
def build_dataframes_seller(trust_symbols):
    data = get_possible_trades(trust_symbols)
    data = data.reset_index()
    print('calculating sellers...')
    trades = df_last_trade_info(data)
    trades = trades.reset_index()
    #data['last_trade_amount'] = trades['last_trade_amount']
    #data['last_trade_price'] = trades['last_trade_price']
    # fusion
    for sample in range(0, len(trades)):
        pairID = trades.loc[[sample]].pairID.values[0]
        pair = trades.loc[[sample]].pair.values[0]
        bid_price = float(data[data.symbol.str.contains(pair)].bidPrice.values[0])
        ask_price = float(data[data.symbol.str.contains(pair)].askPrice.values[0])
        trades.loc[sample, 'bidPrice'] = bid_price
        trades.loc[sample, 'askPrice'] = ask_price

    #data['last_trade_time'] = trades['last_trade_time']
    # data['isBuyer'] = trades['isBuyer']
    # data['pair'] = trades['pair']
    # data['pairID'] = trades['pairID']
    # drop entries
    #data = data[data.last_trade_time != 'none']

    # split data into Buyer (True or False)
    #buyer = pd.DataFrame(trades[trades['isBuyer'] == True])# last trade was a buy
    #buyer['changePercent_lastTrade'] = -((1 - buyer['bidPrice'] / buyer['last_trade_price']) * 100)
    #buyer = buyer.reset_index()
    #print(len(buyer), 'buyers len')
    seller = pd.DataFrame(trades[trades['isBuyer'] == False])# last trade was a sell
    seller['changePercent_lastTrade'] = -((1 - seller['askPrice'] / seller['last_trade_price']) * 100)
    seller = seller.reset_index()
    #print(len(seller), 'sellers len')
    return seller

# check dataframes and trade with conditions (profit = % to trade)
def check_and_trade(profit, x_coin, frame, top_up, d20_infos, splits, nr_of_ships):
    #new_frame_buyers = pd.DataFrame()
    new_frame_sellers = pd.DataFrame()
    # buyers
    for split in range(0, splits+1):
        new_frame_buyers = pd.DataFrame()
        data = build_dataframes_buyer(trust_symbols, split)
        buyer = data
        #print(len(buyer))
        # for all splited df buyers do check and trade
        if buyer is not None:
            if len(buyer) > 0:
                indexes_buyers = buyer.index.values.tolist()
                dataframe = pd.DataFrame(client.get_ticker())
                for sample in range(indexes_buyers[0], indexes_buyers[len(indexes_buyers)-1]+1):
                    #id_list = np.load('id_list.npy')
                    isBuyer = True
                    dict = {}
                    pair = buyer.loc[[sample]].pair.values[0]
                    pairID = buyer.loc[[sample]].pairID.values[0]
                    print(pairID)
                    #sleep(0.5)
                    dict['pair'] = pairID
                    #dict['pairID'] = pair
                    #amount = buyer.loc[[sample]].last_trade_amount.values[0]# amount of symbol on the left side
                    changePercent_lastTrade = float(buyer.loc[[sample]].changePercent_lastTrade.values[0])
                    lastTrade_price = buyer.loc[[sample]].last_trade_price.values[0]
                    #dict['oldPrice'] = lastTrade_price
                    #time = str(buyer.loc[[sample]].last_trade_time.values[0])[0:16]
                    #dict['time'] = time
                    # def current changePercent
                    change = float(round(changePercent_lastTrade, 3))
                    read_file = open("top_json_mutual_file.json", "r")
                    dict_read = json.load(read_file)
                    amount = dict_read[pairID]['qty']
                    investment = dict_read[pairID]['quote_qty']
                    #dict_read[pairID]['amount_left'] = amount
                    dict['# change'] = change
                    if 'switch_pro' in dict_read[pairID].keys():
                        dict['# sw'] = int(len(jsonpickle.decode(dict_read[pairID]['switch_pro'])))
                    # if 'go_to_sea_time' in dict_read[pairID].keys():
                    #     dict['go_to_sea'] = dict_read[pairID]['go_to_sea_time'][5:16]
                    # aim quote quantity
                    aim_q_quantity = dict_read[pairID]["quote_qty"]
                    #print('aim: ', aim_q_quantity)
                    # if 'trend2' in dict_read[pairID].keys() and 'trend30' in dict_read[pairID].keys():
                    #     dict['trend2'] = dict_read[pairID]["trend2"]
                    #     dict['trend30'] = dict_read[pairID]["trend30"]
                    ## READ json file and include empty array for history
                    # last_trade_pair = get_last_trade(pair)
                    # last_trade_timestamp = last_trade_pair[6]
                    # 1 if array history has entries: read
                    # fresh_counter = 999
                    # if pairID in dict_read.keys():
                    #     if "switch_fresh" in dict_read[pairID].keys():
                    #         switch_fresh = dict_read[pairID]["switch_fresh"]
                    #         if dict_read[pairID]["status"] == 'working':
                    #             fresh_counter = dict_read[pairID]["loop_after_switch"]
                    #         # if "loop_after_switch" in dict_read[pairID].keys():
                    #         #     fresh_counter = dict_read[pairID]["loop_after_switch"]
                    #         # else:
                    #         #     fresh_counter = 999
                    #     else:
                    #         switch_fresh = False
                    # else:
                    #     switch_fresh = False
                    #     fresh_counter = 99
                    #dict['fresh'] = switch_fresh
                    ### change percent SWITCHER ###
                    if pairID in dict_read.keys():
                        if 'changePercent' in dict_read[pairID].keys():
                            if len(jsonpickle.decode(dict_read[pairID]['changePercent'])) > 0:
                                former_changes = dict_read[pairID]["changePercent"]
                                former_changes = jsonpickle.decode(former_changes)
                                former_changes = former_changes[~np.isnan(former_changes)]
                                max_percentChange = np.max(former_changes)
                                last_trade_timestamp = 1654326940
                                last_direction = changePercent_lastTrade - former_changes[len(former_changes)-1]
                                if len(former_changes) > 1:
                                    before_last_direction = former_changes[len(former_changes)-1] - former_changes[len(former_changes)-2]
                                    dict_read[pairID]["before_last_direction"] = before_last_direction
                                dict_read[pairID]["last_direction"] = last_direction
                                # define last 10 change percent values and check if equal
                                if len(former_changes) > 10:
                                    lst_last_10 = former_changes[len(former_changes)-10:].tolist()
                                else:
                                    lst_last_10 = [1, 2]
                            if len(jsonpickle.decode(dict_read[pairID]['changePercent'])) == 0:
                                max_percentChange = changePercent_lastTrade
                                lst_last_10 = [1, 2]
                            # if "loop_after_switch" in dict_read[pairID].keys():
                            #     dict['loop_a_switch'] = dict_read[pairID]["loop_after_switch"]
                            # if "last_direction" in dict_read[pairID].keys():
                            #     dict['last_direction'] = dict_read[pairID]["last_direction"]
                        write_new_file = open("top_json_mutual_file.json", "w")
                        json.dump(dict_read, write_new_file, indent=4)
                        write_new_file.close()
                    # 2 if array history is empty create new one
                    else:
                        max_percentChange = changePercent_lastTrade
                        list = []
                        array_history = np.array(list)
                        array_history = jsonpickle.encode(array_history)
                        dict_read.update({pair: {'changePercent': array_history}})
                        write_new_file = open("top_json_mutual_file.json", "w")
                        json.dump(dict_read, write_new_file, indent=4)
                        write_new_file.close()
                    dict['maxChange'] = round(max_percentChange, 3)

                    ### define reset_pair and aiming trade (greater than top_up)
                    reset_pair = get_left_symbol(pair) + x_coin
                    # define reset _price (BID)
                    bid_price = float(dataframe[dataframe.symbol.str.contains(reset_pair)].bidPrice.values[0])
                    possible_reset_quote_amount = bid_price * amount
                    p_reset = float(100/aim_q_quantity*possible_reset_quote_amount)
                    p_reset_str = str(round(p_reset,2))
                    dict['p_reset'] = p_reset_str + ' %'
                    ### change percent P_RESET ###
                    if pairID in dict_read.keys():
                        if 'arr_p_resets' in dict_read[pairID].keys():
                            if len(jsonpickle.decode(dict_read[pairID]['arr_p_resets'])) > 0:
                                former_p_resets = dict_read[pairID]["arr_p_resets"]
                                former_p_resets = jsonpickle.decode(former_p_resets)
                                former_p_resets = former_p_resets[~np.isnan(former_p_resets)]
                                max_p_resets = np.max(former_p_resets)
                                last_trade_timestamp = 1654326940
                                last_direction_p_reset = (p_reset-100) - former_p_resets[len(former_p_resets)-1]
                            if len(jsonpickle.decode(dict_read[pairID]['arr_p_resets'])) == 0:
                                max_p_resets = (p_reset-100)
                            write_new_file = open("top_json_mutual_file.json", "w")
                            json.dump(dict_read, write_new_file, indent=4)
                            write_new_file.close()
                        else:
                            # 2 if array history is empty create new one
                            max_p_resets = (p_reset - 100)
                            list = []
                            array_history = np.array(list)
                            array_history = jsonpickle.encode(array_history)
                            dict_read[pairID]['arr_p_resets'] = array_history
                            write_new_file = open("top_json_mutual_file.json", "w")
                            json.dump(dict_read, write_new_file, indent=4)
                            write_new_file.close()
                    #
                    # if 'loop_after_switch' not in dict_read[pairID].keys():
                    #     dict_read[pairID]['loop_after_switch'] = 0
                    #     write_new_file = open("top_json_mutual_file.json", "w")
                    #     json.dump(dict_read, write_new_file, indent=4)
                    #     write_new_file.close()
                            # if "loop_after_switch" in dict_read[pairID].keys():
                            #     dict['loop_a_switch'] = dict_read[pairID]["loop_after_switch"]
                        #print('stores p_reset value max: ', max_p_resets)
                    p_reset_max_str = str(round(max_p_resets+100,2))
                    #dict['p_reset_max'] = p_reset_max_str + ' %'
                    #print('p_reset value max: ', max_p_resets)
                    #print('possible: (has to bigger than aim included)', possible_reset_quote_amount)
                    #print('aim included: ', aim_q_quantity*1.0017)
                    if 'last_direction' in dict_read[pairID].keys():
                        last_direction = dict_read[pairID]['last_direction']
                    else:
                        last_direction = 0
                    if 'before_last_direction' in dict_read[pairID].keys():
                        before_last_direction = dict_read[pairID]['before_last_direction']
                    else:
                        before_last_direction = 0

                    ## calculate win of switch to get factor for reset aim amount
                    if 'status' in dict_read[pairID].keys():
                        if dict_read[pairID]['status'] == 'working':
                            #reset_condition = dict_read[pairID]['last_profit'] - 0.225
                            p_array = dict_read[pairID]['switch_pro']
                            p_array = jsonpickle.decode(p_array)
                            sum_of_profits = np.sum(p_array)
                            mean_of_profits = np.mean(p_array)
                            #1#reset_condition = (100 + 0.3 - sum_of_profits) / 100
                            #2#reset_condition = (100 - mean_of_profits/2.5)/100
                            if sum_of_profits > 2:
                                x = 0.4
                            elif sum_of_profits > 1.25:
                                x = 0.2
                            else:
                                x = 0.075
                            reset_condition = (100 - x) / 100
                            # print('reset_condition:', reset_condition)
                            # print('aim included: ', aim_q_quantity * reset_condition)
                            # print(-frame, '-frame')
                            # print(changePercent_lastTrade, 'changelast')
                            # if check_reset == True:
                    if 'last_profit' in dict_read[pairID].keys():
                        last_profit = dict_read[pairID]['last_profit']
                    else:
                        last_profit = 0

                    ### INSTANT RESET WHEN P_RESET IS BIGGER THAN 100.6 AND BIGGER THAN CHANGE and of last change values are equal and bigger than 0.7
                    if p_reset > 102 and (p_reset-100) > changePercent_lastTrade or ((p_reset-100) + last_profit) > changePercent_lastTrade and ((p_reset-100) + last_profit) > 1:
                        print('last_profit= ', last_profit)
                        do_reset = True
                    else:
                        do_reset = False
            ######### SWITCH BUYERS
                    # --> SELL if :
                    # 1: (max_percentChange - (current) change) is bigger than fallback parameter
                    # 2: current change is bigger than profit
                    # 3: balance is not reset
                    # 4: switch_fresh == False
                    ### define fallback_2
                    if changePercent_lastTrade > 1:
                        fallback = fallback_2
                    else:
                        fallback = fallback_1
                    if changePercent_lastTrade > 1.75:
                        instant_trade = True
                    else:
                        instant_trade = False
                    if instant_trade == True or before_last_direction <= 0 and last_direction < 0 and (max_percentChange - changePercent_lastTrade) > fallback and changePercent_lastTrade > profit and \
                            dict_read[pairID]["status"] != 'depot' and last_trade_timestamp > 1654326938 or ckeckList(lst_last_10) == True and changePercent_lastTrade > 0.7:
                        print('max_Change =', round(max_percentChange, 3), 'current change =', round(changePercent_lastTrade, 3))
                        print()
                        # read from json topping
                        read_file = open("top_json_mutual_file.json", "r")
                        dict_read = json.load(read_file)
                        if 'last_right_amount' in dict_read[pairID].keys():
                            last_right_amount = dict_read[pairID]['last_right_amount']
                        # if 'status' in dict_read[pairID].keys():
                        #     print('STATUS = ', dict_read[pairID]['status'])
                        #     # if working (trade amount plus topping)
                        #     if dict_read[pairID]['status'] == 'working':
                        #         q_qty_before = last_trade_pair[4]
                        #         qty = dict_read[pairID]["qty"]
                        # else:
                        #     qty = 0
                        # read_file.close()
                        # trade
                        print('before_last_dir: ', before_last_direction)
                        new_amount = round_down(amount, get_precision(pair))# + qty
                        trade_sell(pair, new_amount, x_coin, "")
                        # clean json changePercent history
                        read_file = open("top_json_mutual_file.json", "r")
                        dict_read = json.load(read_file)
                        #dict_read['stats']['switches'] = dict_read['stats']['switches'] + 1
                        list = []
                        array_history = np.array(list)
                        array_history = jsonpickle.encode(array_history)
                        dict_read[pairID]['changePercent'] = array_history
                        #dict_read[pairID]["qty"] = 0
                        #dict_read[pairID]["ship_price"] = 0
                        dict_read[pairID]["isBuyer"] = False
                        dict_read[pairID]["switch_fresh"] = True
                        dict_read[pairID]["loop_after_switch"] = 0
                        last_trade = get_last_trade(pair)
                        last_price = last_trade[1]
                        dict_read[pairID]['last_switch_price_JSON'] = last_price
                        if dict_read[pairID]['status'] == 'working' and 'last_right_amount' in dict_read[pairID].keys():
                            last_trade_now = get_last_trade(pair)
                            q_qty_after = last_trade_now[4]
                            profit = -(100-100/last_right_amount*q_qty_after)
                            print('profit=', profit)
                            # store profit values
                            #array = dict_read['stats']['profits_arr']
                            #array = jsonpickle.decode(array)
                            #new_array = np.append(array, profit)
                            #new_array = jsonpickle.encode(new_array)
                            dict_read[pairID]['last_profit'] = profit
                            dict_read[pairID]['last_right_amount'] = q_qty_after
                            #dict_read['stats']['profits_arr'] = new_array
                            # store_profits of this ship
                            array_sw_pro = dict_read[pairID]['switch_pro']
                            array_sw_pro = jsonpickle.decode(array_sw_pro)
                            new_sw_pro = np.append(array_sw_pro, profit)
                            new_sw_pro = jsonpickle.encode(new_sw_pro)
                            dict_read[pairID]['switch_pro'] = new_sw_pro
                            print('switches: ', jsonpickle.decode(dict_read[pairID]['switch_pro']))
                            # store last right amount
                            dict_read[pairID]['last_right_amount'] = q_qty_after
                        dict_read[pairID]["status"] = 'working'
                        #########################################################################
                        ###STORE SWITCH EXCEL SELL
                        #########################################################################
                        # get last trade info
                        #info = get_last_trade(reset_pair)
                        # open excel
                        if 'last_right_amount' in dict_read[pairID].keys():
                            df = pd.read_excel('switch_stats.xlsx', index_col=0)
                            # create new entry for json
                            timestamp = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
                            pairID = pairID
                            quote_amount = last_trade[4]
                            left_amount = last_trade[0]
                            stays_on_left = 100 * (dict_read[pairID]['qty'] / left_amount - 1)
                            print(stays_on_left)
                            amount_invested_x_coin = dict_read[pairID]['quote_qty']
                            type = 'SELL'
                            #ship_price = dict_read[pairID]['ship_price']
                            switch_price = last_trade[1]
                            profit = (100 * (quote_amount / last_right_amount - 1)) + stays_on_left
                            win = amount_invested_x_coin*(profit/100)
                            switch_data = {'timestamp': timestamp,
                                          'pairID': pairID,
                                          'quote_amount': quote_amount,
                                          'left_amount': left_amount,
                                          'switch_price': switch_price,
                                          'last_right_amount': last_right_amount,
                                          'profit_%': profit,
                                           'win': win,
                                          'type' : type}
                            # add new entry to df
                            df2 = df.append(switch_data, ignore_index=True)
                            df2 = df2.sort_values(by=['timestamp'], ascending=False)
                            # store
                            with suppress(Exception):
                                # your code
                                df2.to_excel('switch_stats.xlsx')
                                df2.to_excel(r"XXX\switch_stats.xlsx")
                            #########################################################################
                        # write new file with same name
                        write_new_file = open("top_json_mutual_file.json", "w")
                        json.dump(dict_read, write_new_file, indent=4)
                        write_new_file.close()
                        # top up
                        #top_store(pair, x_coin, isBuyer, top_up)
            ######### RESET WORKINGS
                    # --> ResetSELL if:
                    # 1 current change is smaller than -(frame)
                    # 2 amount is not reset already
                    # 3--> right after switch dont reset(...)
                    elif changePercent_lastTrade < -(stopp_loss) and p_reset > 99.75 and last_direction_p_reset < 0 or dict_read[pairID]['loop_after_switch'] not in phase_a_switch and last_direction < 0 and changePercent_lastTrade < -(4*frame) and dict_read[pairID]["status"] == 'working' and possible_reset_quote_amount >= aim_q_quantity*reset_condition and last_trade_timestamp > 1654326938:
                        # read from json topping
                        # read_file = open("top_json_mutual_file.json", "r")
                        # dict_read = json.load(read_file)
                        # # if 'status' in dict_read[pairID].keys():
                        # #     print('STATUS = ', dict_read[pairID]['status'])
                        # #     # if working (trade amount plus topping)
                        # #     if dict_read[pairID]['status'] == 'working':
                        # #         qty = dict_read[pairID]["qty"]
                        # # else:
                        # #     qty = 0
                        # read_file.close()
                        ###### TRADE
                        new_amount = amount# + qty
                        #id_list = np.append(id_list, pair)
                        reset_asset_if(pairID, pair, x_coin, isBuyer, new_amount, d20_infos)
                        #dict['z_reset_?'] = 'X'
                        #np.save("id_list", id_list)
                        # calculate reset cost
                        #read_file = open("top_json_mutual_file.json", "r")
                        #dict_read = json.load(read_file)
                        #investment = dict_read[pairID]['quote_qty']
                        reset_quote_amount_end = get_last_trade(reset_pair)[4]
                        loss = -(100-100/investment*reset_quote_amount_end)
                        print('loss=', loss)
                        # store profit values Excel RESET stats


                        # store profit values
                        #array = dict_read['stats']['losses_arr']
                        #array = jsonpickle.decode(array)
                        #new_array = np.append(array, loss)
                        #new_array = jsonpickle.encode(new_array)
                        #dict_read['stats']['losses_arr'] = new_array
                        #write_new_file = open("top_json_mutual_file.json", "w")
                        #json.dump(dict_read, write_new_file, indent=4)
                        #write_new_file.close()
            ######### RESET SHIPS
                    # elif last_direction < 0 and changePercent_lastTrade < -(frame) and dict_read[pairID]["status"] == 'ship' and p_reset > 100.15 and last_trade_timestamp > 1654326938:
                    #     # read from json topping
                    #     read_file = open("top_json_mutual_file.json", "r")
                    #     dict_read = json.load(read_file)
                    #     if 'status' in dict_read[pairID].keys():
                    #         print('STATUS = ', dict_read[pairID]['status'])
                    #         # if working (trade amount plus topping)
                    #         if dict_read[pairID]['status'] == 'working':
                    #             qty = dict_read[pairID]["qty"]
                    #     else:
                    #         qty = 0
                    #     read_file.close()
                    #     # trade
                    #     new_amount = round_down(amount, get_precision(pair))  # + qty
                    #     #id_list = np.append(id_list, pair)
                    #     reset_asset_if(pair, x_coin, isBuyer, new_amount)
                    #     #dict['z_reset_?'] = 'X'
                    #     #np.save("id_list", id_list)
                    #
                    #     ### calculate and store loss
                    #     read_file = open("top_json_mutual_file.json", "r")
                    #     dict_read = json.load(read_file)
                    #     invest = dict_read[pairID]['quote_qty']
                    #     after_reset = get_last_trade(reset_pair)[4]
                    #     loss = -(100-100/invest*after_reset)
                    #     print('loss=', loss)
                    #     # store profit values
                    #     array = dict_read['stats']['losses_arr']
                    #     array = jsonpickle.decode(array)
                    #     new_array = np.append(array, loss)
                    #     new_array = jsonpickle.encode(new_array)
                    #     dict_read['stats']['losses_arr'] = new_array
                    #     write_new_file = open("top_json_mutual_file.json", "w")
                    #     json.dump(dict_read, write_new_file, indent=4)
                    #     write_new_file.close()
            ######### RESET DROPS #########
                    elif do_reset == True or p_reset < 40 or p_reset > 101.75 or changePercent_lastTrade < -(3*frame) and (p_reset-100) > 0.475 and max_p_resets - (p_reset-100) > (fallback_1):# or changePercent_lastTrade < -0.9 and 99.5 < p_reset:
                        # trade
                        print('Drops...')
                        print('do_reset == ', do_reset)

                        new_amount = amount# + qty
                        #id_list = np.append(id_list, pair)
                        reset_asset_if(pairID, pair, x_coin, isBuyer, new_amount, d20_infos)
                        # calculate reset cost
                        # read_file = open("top_json_mutual_file.json", "r")
                        # dict_read = json.load(read_file)
                        #investment = dict_read[pairID]['quote_qty']
                        reset_quote_amount_end = get_last_trade(reset_pair)[4]
                        loss = -(100-100/investment*reset_quote_amount_end)
                        print('loss=', loss)
                        # store profit values
                        # array = dict_read['stats']['losses_arr']
                        # array = jsonpickle.decode(array)
                        # new_array = np.append(array, loss)
                        # new_array = jsonpickle.encode(new_array)
                        # dict_read['stats']['losses_arr'] = new_array
                        # if dict_read[pairID]['status'] == 'working':
                        #     print('switches: ', jsonpickle.decode(dict_read[pairID]['switch_pro']))
                        # write_new_file = open("top_json_mutual_file.json", "w")
                        # json.dump(dict_read, write_new_file, indent=4)
                        # write_new_file.close()
            ###and changePercent_lastTrade < -(frame)
            ######### HOLD
                    else:
                        ## STORE CURRENT CHANGE PERCENT SWITCH TO ARRAY
                        read_file = open("top_json_mutual_file.json", "r")
                        dict_read = json.load(read_file)
                        old_history = jsonpickle.decode(dict_read[pairID]['changePercent'])
                        # append value to array
                        new_history = np.append(old_history, changePercent_lastTrade)
                        new_history = jsonpickle.encode(new_history)
                        dict_read[pairID]['changePercent'] = new_history
                        ## STORE CURRENT CHANGE PERCENT P_RESET TO ARRAY
                        old_history = jsonpickle.decode(dict_read[pairID]['arr_p_resets'])
                        # append value to array
                        #print(p_reset, 'hold')
                        new_history = np.append(old_history, p_reset-100)
                        new_history = jsonpickle.encode(new_history)
                        dict_read[pairID]['arr_p_resets'] = new_history
                        dict_read[pairID]["switch_fresh"] = False
                        if dict_read[pairID]["status"] == 'working':
                            if "loop_after_switch" in dict_read[pairID].keys():
                                dict_read[pairID]["loop_after_switch"] = dict_read[pairID]["loop_after_switch"] +1
                                #dict['loop_a_switch'] = dict_read[pairID]["loop_after_switch"]
                        # write new file with same name
                        write_new_file = open("top_json_mutual_file.json", "w")
                        json.dump(dict_read, write_new_file, indent=4)
                        write_new_file.close()
                    new_frame_buyers = new_frame_buyers.append(dict, ignore_index=True)
                if len(new_frame_buyers) > 0:
                    new_frame_buyers = new_frame_buyers.sort_values(by=['# change'], ascending=False)
                print('last move buy: (sell if positive), ', len(buyer), 'entries')
                buyers_len = len(buyer)
                #sellers_len = len(seller)
                #sum_BSlen = int(buyers_len+sellers_len)
                print(50 * '-')
                date_string = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
                print(date_string)
                print(50 * '-')
                print(new_frame_buyers)
                print()
                sleep(1.5)
        # check df sellers
        # print('last move sell: (buy if negative)', len(seller), 'entries')
        # print(50*'-')

    sleep(5)

    # sellers
    data = build_dataframes_seller(trust_symbols)
    seller = data
    dataframe = pd.DataFrame(client.get_ticker())
    for sample in range(0, len(seller)):
        isBuyer = False
        dict = {}
        pair = seller.loc[[sample]].pair.values[0]
        pairID = seller.loc[[sample]].pairID.values[0]
        print(pairID)
        #sleep(0.5)
        dict['pair'] = pairID
        #amount = seller.loc[[sample]].last_trade_amount.values[0]# amount of symbol on the left side
        changePercent_lastTrade = float(seller.loc[[sample]].changePercent_lastTrade.values[0])
        lastTrade_price = seller.loc[[sample]].last_trade_price.values[0]
        #dict['oldPrice'] = lastTrade_price
        #time = seller.loc[[sample]].last_trade_time.values[0][0:16]
        #dict['time'] = time
        change = float(round(changePercent_lastTrade, 3))
        read_file = open("top_json_mutual_file.json", "r")
        dict_read = json.load(read_file)
        #amount = dict_read[pairID]['qty']
        if 'start_left_qty' in dict_read[pairID].keys():
            amount = dict_read[pairID]['start_left_qty']
        else:
            amount = dict_read[pairID]['qty']
        investment = dict_read[pairID]['quote_qty']
        #dict_read[pairID]['amount_left'] = amount
        dict['# change'] = change
        if 'switch_pro' in dict_read[pairID].keys():
            dict['# sw'] = int(len(jsonpickle.decode(dict_read[pairID]['switch_pro'])))
        # if 'go_to_sea_time' in dict_read[pairID].keys():
        #     dict['go_to_sea'] = dict_read[pairID]['go_to_sea_time'][5:16]
        # aim quote quantity
        aim_q_quantity = dict_read[pairID]["quote_qty"]
        #print('aim: ', aim_q_quantity)
        # if 'trend2' in dict_read[pairID].keys() and 'trend30' in dict_read[pairID].keys():
        #     dict['trend2'] = dict_read[pairID]["trend2"]
        #     dict['trend30'] = dict_read[pairID]["trend30"]
        ## READ json file
        # last_trade_pair = get_last_trade(pair)
        # last_trade_timestamp = last_trade_pair[6]
        # 1 if array history has entries: read
        fresh_counter = 999
        # if pairID in dict_read.keys():
        #     if "switch_fresh" in dict_read[pairID].keys():
        #         switch_fresh = dict_read[pairID]["switch_fresh"]
        #         if dict_read[pairID]["status"] == 'working':
        #             fresh_counter = dict_read[pairID]["loop_after_switch"]
                # if "loop_after_switch" in dict_read[pairID].keys():
                #     fresh_counter = dict_read[pairID]["loop_after_switch"]
                # else:
                #     fresh_counter = 999
            # else:
            #     switch_fresh = False
        # else:
        #     switch_fresh = False
        #     fresh_counter = 99
        #dict['fresh'] = switch_fresh
        ### change percent SWITCHER ###
        if pairID in dict_read.keys():
            if 'changePercent' in dict_read[pairID].keys():
                if len(jsonpickle.decode(dict_read[pairID]['changePercent'])) > 0:
                    former_changes = dict_read[pairID]["changePercent"]
                    former_changes = jsonpickle.decode(former_changes)
                    former_changes = former_changes[~np.isnan(former_changes)]
                    max_percentChange = np.min(former_changes)
                    last_trade_timestamp = 1654326940
                    last_direction = changePercent_lastTrade - former_changes[len(former_changes)-1]
                    dict_read[pairID]["last_direction"] = last_direction
                    if len(former_changes) > 1:
                        before_last_direction = former_changes[len(former_changes)-1] - former_changes[len(former_changes)-2]
                        dict_read[pairID]["before_last_direction"] = before_last_direction
                    # define last 10 change percent values and check if equal
                    if len(former_changes) > 10:
                        lst_last_10 = former_changes[len(former_changes)-10:].tolist()
                    else:
                        lst_last_10 = [1, 2]
                if len(jsonpickle.decode(dict_read[pairID]['changePercent'])) == 0:
                    max_percentChange = changePercent_lastTrade
                    lst_last_10 = [1, 2]
                # if "loop_after_switch" in dict_read[pairID].keys():
                #     dict['loop_a_switch'] = dict_read[pairID]["loop_after_switch"]
                # if "last_direction" in dict_read[pairID].keys():
                #     dict['last_direction'] = dict_read[pairID]["last_direction"]
            write_new_file = open("top_json_mutual_file.json", "w")
            json.dump(dict_read, write_new_file, indent=4)
            write_new_file.close()
        # 2 if array history is empty create new one
        else:
            max_percentChange = changePercent_lastTrade
            list = []
            array_history = np.array(list)
            array_history = jsonpickle.encode(array_history)
            dict_read.update({pair: {'changePercent': array_history}})
            # write new file with same name
            write_new_file = open("top_json_mutual_file.json", "w")
            json.dump(dict_read, write_new_file, indent=4)
            write_new_file.close()
        dict['maxChange'] = round(max_percentChange, 3)

        ### define reset_pair and aiming trade (greater than top_up)
        # WE HAVE
        if dict_read[pairID]["ship_price"] > 0:
            now_amount = dict_read[pairID]["qty"]*dict_read[pairID]["ship_price"]
        else:
            now_amount = last_trade_pair[4]

        right = pair.replace(get_left_symbol(pair), '')
        reset_pair = right + x_coin
        # define reset _price (BID)
        bid_price = float(dataframe[dataframe.symbol.str.contains(reset_pair)].bidPrice.values[0])
        possible_reset_quote_amount = bid_price * now_amount
        p_reset = float(100/aim_q_quantity*possible_reset_quote_amount)
        p_reset_str = str(round(p_reset,2))
        dict['p_reset'] = p_reset_str + ' %'
        ### change percent P_RESET ###
        if pairID in dict_read.keys():
            if 'arr_p_resets' in dict_read[pairID].keys():
                if len(jsonpickle.decode(dict_read[pairID]['arr_p_resets'])) > 0:
                    former_p_resets = dict_read[pairID]["arr_p_resets"]
                    former_p_resets = jsonpickle.decode(former_p_resets)
                    former_p_resets = former_p_resets[~np.isnan(former_p_resets)]
                    max_p_resets = np.max(former_p_resets)
                    last_trade_timestamp = 1654326940
                    last_direction_p_reset = (p_reset-100) - former_p_resets[len(former_p_resets)-1]
                if len(jsonpickle.decode(dict_read[pairID]['arr_p_resets'])) == 0:
                    max_p_resets = (p_reset-100)
                write_new_file = open("top_json_mutual_file.json", "w")
                json.dump(dict_read, write_new_file, indent=4)
                write_new_file.close()
            else:
                # 2 if array history is empty create new one
                max_p_resets = (p_reset - 100)
                list = []
                array_history = np.array(list)
                array_history = jsonpickle.encode(array_history)
                dict_read[pairID]['arr_p_resets'] = array_history
                write_new_file = open("top_json_mutual_file.json", "w")
                json.dump(dict_read, write_new_file, indent=4)
                write_new_file.close()


        #print('stores p_reset value max: ', max_p_resets)
        p_reset_max_str = str(round(max_p_resets+100,2))
        #dict['p_reset_max'] = p_reset_max_str + ' %'
        # if 'loop_after_switch' not in dict_read[pairID].keys():
        #     dict_read[pairID]['loop_after_switch'] = 0
        #     write_new_file = open("top_json_mutual_file.json", "w")
        #     json.dump(dict_read, write_new_file, indent=4)
        #     write_new_file.close()
        # print('possible: (has to bigger than aim included)', possible_reset_quote_amount)
        # print('aim included: ', aim_q_quantity*1.0017)
        ###
        if 'last_direction' in dict_read[pairID].keys():
            last_direction = dict_read[pairID]['last_direction']
        else:
            last_direction = 0
        if 'before_last_direction' in dict_read[pairID].keys():
            before_last_direction = dict_read[pairID]['before_last_direction']
        else:
            before_last_direction = 0
        ## calculate win of switch to get factor for reset aim amount
        if 'status' in dict_read[pairID].keys():
            if dict_read[pairID]['status'] == 'working':
                #reset_condition = dict_read[pairID]['last_profit'] - 0.225
                p_array = dict_read[pairID]['switch_pro']
                p_array = jsonpickle.decode(p_array)
                sum_of_profits = np.sum(p_array)
                mean_of_profits = np.mean(p_array)
                #1#reset_condition = (100 + 0.3 - sum_of_profits) / 100
                #2#reset_condition = (100 - mean_of_profits/2.5)/100
                if sum_of_profits > 2:
                    x = 0.4
                elif sum_of_profits > 1.25:
                    x = 0.2
                else:
                    x = 0.075
                reset_condition = (100 - x) / 100
                # print('reset_condition:', reset_condition)
                # print('aim included: ', aim_q_quantity * reset_condition)
                # print(-frame, '-frame')
                # print(changePercent_lastTrade, 'changelast')
        ### INSTANT RESET WHEN P_RESET IS BIGGER THAN 100.6 AND BIGGER THAN CHANGE and of last change values are equal and smaller than -0.7
        if p_reset > 101.75 and -(p_reset-100) < changePercent_lastTrade:
            do_reset = True
        else:
            do_reset = False

######### SWITCH SELLERS
        # --> BUY if :
        # 1: -(max_percentChange - (current) change) is bigger than fallback parameter
        # 2: current change is smaller than -(profit)
        # 3: balance is not reset
        # 4: switch_fresh == False
        ### define fallback_2
        if changePercent_lastTrade < -1.2:
            fallback = fallback_2
        else:
            fallback = fallback_1
        # print('pair', 'amount', 'fresh_counter', 'switch_fresh', 'changePercent_lastTrade', 'frame', 'check_reset')
        # print(pair, amount, fresh_counter, switch_fresh, changePercent_lastTrade, frame, check_reset)
        if changePercent_lastTrade < -1.2:
            instant_trade = True
        else:
            instant_trade = False
        if instant_trade == True or before_last_direction >= 0 and last_direction > 0 and -(max_percentChange - changePercent_lastTrade) > fallback \
                and changePercent_lastTrade < -(switch1) and dict_read[pairID]["status"] != 'depot' and last_trade_timestamp > 1654326938 or ckeckList(lst_last_10) == True and changePercent_lastTrade < -0.7:
            print('max_Change =', round(max_percentChange, 3), 'current change =', round(changePercent_lastTrade, 3))
            print()
            # buy if profit is there
            # read from json topping
            read_file = open("top_json_mutual_file.json", "r")
            dict_read = json.load(read_file)
            if 'status' in dict_read[pairID].keys():
                print('STATUS = ', dict_read[pairID]['status'])
                # if working (trade amount plus topping)
                if dict_read[pairID]['status'] == 'working':
                    if 'last_right_amount' in dict_read[pairID].keys():
                        last_right_amount = dict_read[pairID]['last_right_amount']
            #         qty = dict_read[pairID]["qty"]
            # else:
            #     qty = 0
            read_file.close()
            #### ####
            if dict_read[pairID]['status'] == 'ship':
                last_right_amount = dict_read[pairID]['start_switch_qty']
            elif dict_read[pairID]['status'] == 'working':
                last_right_amount = dict_read[pairID]['last_right_amount']
            #### ####
            # trade
            print('before_last_dir: ', before_last_direction)
            new_amount = round_down(amount, get_precision(pair))# + qty
            trade_buy(pairID, pair, new_amount, x_coin)
            # clean json changePercent history
            read_file = open("top_json_mutual_file.json", "r")
            dict_read = json.load(read_file)
            #dict_read['stats']['switches'] = dict_read['stats']['switches'] + 1
            list = []
            array_history = np.array(list)
            array_history = jsonpickle.encode(array_history)
            dict_read[pairID]['changePercent'] = array_history
            #dict_read[pairID]["qty"] = 0
            #dict_read[pairID]["ship_price"] = 0
            dict_read[pairID]["isBuyer"] = True
            dict_read[pairID]["switch_fresh"] = True
            dict_read[pairID]["loop_after_switch"] = 0
            last_trade = get_last_trade(pair)
            last_price = last_trade[1]
            dict_read[pairID]['last_switch_price_JSON'] = last_price
            if dict_read[pairID]['status'] == 'working' and 'last_right_amount' in dict_read[pairID].keys():
                last_trade_now = get_last_trade(pair)
                q_qty_after = last_trade_now[4]
                profit = (100-100/last_right_amount*q_qty_after)
                print('profit=', profit)
                dict_read[pairID]['last_profit'] = profit
                # store profit values
                # array = dict_read['stats']['profits_arr']
                # array = jsonpickle.decode(array)
                # new_array = np.append(array, profit)
                # new_array = jsonpickle.encode(new_array)
                # dict_read['stats']['profits_arr'] = new_array
                # store_profits of this ship
                array_sw_pro = dict_read[pairID]['switch_pro']
                array_sw_pro = jsonpickle.decode(array_sw_pro)
                new_sw_pro = np.append(array_sw_pro, profit)
                new_sw_pro = jsonpickle.encode(new_sw_pro)
                dict_read[pairID]['switch_pro'] = new_sw_pro
                print('switches: ', jsonpickle.decode(dict_read[pairID]['switch_pro']))
                # store last right amount
                dict_read[pairID]['last_right_amount'] = q_qty_after
            dict_read[pairID]["status"] = 'working'
            dict_read[pairID]["last_right_amount"] = last_trade[4]
            #########################################################################
            ###STORE SWITCH EXCEL BUY
            #########################################################################
            # get last trade info
            #info = get_last_trade(reset_pair)
            # open excel
            df = pd.read_excel('switch_stats.xlsx', index_col=0)
            # create new entry for json
            timestamp = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
            pairID = pairID
            amount_invested_x_coin = dict_read[pairID]['quote_qty']
            quote_amount = last_trade[4]
            left_amount = last_trade[0]
            type = 'BUY'
            #ship_price = dict_read[pairID]['ship_price']
            switch_price = last_trade[1]
            profit = -(100 * (quote_amount / last_right_amount - 1))
            win = amount_invested_x_coin * (profit / 100)
            switch_data = {'timestamp': timestamp,
                          'pairID': pairID,
                          'quote_amount': quote_amount,
                          'left_amount': left_amount,
                          'switch_price': switch_price,
                          'last_right_amount': last_right_amount,
                          'profit_%': profit,
                           'win': win,
                          'type' : type}
            # add new entry to df
            df2 = df.append(switch_data, ignore_index=True)
            df2 = df2.sort_values(by=['timestamp'], ascending=False)
            # store
            with suppress(Exception):
                # your code
                df2.to_excel('switch_stats.xlsx')
                df2.to_excel(r"XXX\switch_stats.xlsx")
            #########################################################################
            # write new file with same name
            write_new_file = open("top_json_mutual_file.json", "w")
            json.dump(dict_read, write_new_file, indent=4)
            write_new_file.close()
            # top up
            #top_store(pair, x_coin, isBuyer, top_up)
######### RESET WORKINGS
        # --> ResetSELL if:
        # 1 current change is greater than frame
        # 2 amount is not reset already
        # 3--> right after switch dont reset(...)    dict_read[pairID]["status"] == 'working' and
        # 4 wait till 7 loops to reset working ship
        elif changePercent_lastTrade > stopp_loss and p_reset > 99.75 and last_direction_p_reset < 0 or dict_read[pairID]['loop_after_switch'] not in phase_a_switch and last_direction > 0 and changePercent_lastTrade > 4*frame and dict_read[pairID]["status"] == 'working' and possible_reset_quote_amount >= aim_q_quantity*reset_condition and last_trade_timestamp > 1654326938:
            # read from json topping
            # read_file = open("top_json_mutual_file.json", "r")
            # dict_read = json.load(read_file)
            # if 'status' in dict_read[pairID].keys():
            #     print('STATUS = ', dict_read[pairID]['status'])
            #     # if working (trade amount plus topping)
            #     if dict_read[pairID]['status'] == 'working':
            #         qty = dict_read[pairID]["qty"]
            # else:
            #     qty = 0
            # read_file.close()
            # trade
            new_amount = amount# + qty
            #id_list = np.append(id_list, pair)
            reset_asset_if(pairID, pair, x_coin, isBuyer, new_amount, d20_infos)
            #dict['z_reset_?'] = 'X'
            #np.save("id_list", id_list)
            # calculate reset cost
            # read_file = open("top_json_mutual_file.json", "r")
            # dict_read = json.load(read_file)
            #investment = dict_read[pairID]['quote_qty']
            reset_quote_amount_end = get_last_trade(reset_pair)[4]
            loss = -(100-100/investment*reset_quote_amount_end)
            print('loss=', loss)
            # store profit values
            # array = dict_read['stats']['losses_arr']
            # array = jsonpickle.decode(array)
            # new_array = np.append(array, loss)
            # new_array = jsonpickle.encode(new_array)
            # dict_read['stats']['losses_arr'] = new_array
            # write_new_file = open("top_json_mutual_file.json", "w")
            # json.dump(dict_read, write_new_file, indent=4)
            # write_new_file.close()
######### RESET DROPS #########
        elif do_reset == True or p_reset < 40 or p_reset > 101.75 or changePercent_lastTrade > 3*frame and (p_reset-100) > 0.475 and max_p_resets - (p_reset-100) > (fallback_1):# or changePercent_lastTrade > 0.9 and 99.5 < p_reset:
            print('Drops...')
            print('do_reset == ', do_reset)
            # trade
            new_amount = amount  # + qty
            # id_list = np.append(id_list, pair)
            reset_asset_if(pairID, pair, x_coin, isBuyer, new_amount, d20_infos)
            # calculate reset cost
            # read_file = open("top_json_mutual_file.json", "r")
            # dict_read = json.load(read_file)
            #investment = dict_read[pairID]['quote_qty']
            reset_quote_amount_end = get_last_trade(reset_pair)[4]
            loss = -(100 - 100 / investment * reset_quote_amount_end)
            print('loss=', loss)
            # store profit values
            # array = dict_read['stats']['losses_arr']
            # array = jsonpickle.decode(array)
            # new_array = np.append(array, loss)
            # new_array = jsonpickle.encode(new_array)
            # dict_read['stats']['losses_arr'] = new_array
            # # if dict_read[pairID]['status'] == 'working':
            # #     print('switches: ', jsonpickle.decode(dict_read[pairID]['switch_pro']))
            # write_new_file = open("top_json_mutual_file.json", "w")
            # json.dump(dict_read, write_new_file, indent=4)
            # write_new_file.close()
######### RESET SHIPS
        # elif last_direction > 0 and changePercent_lastTrade > frame and dict_read[pairID]["status"] == 'ship' and p_reset > 100.15 and last_trade_timestamp > 1654326938:
        #     # read from json topping
        #     read_file = open("top_json_mutual_file.json", "r")
        #     dict_read = json.load(read_file)
        #     if 'status' in dict_read[pairID].keys():
        #         print('STATUS = ', dict_read[pairID]['status'])
        #         # if working (trade amount plus topping)
        #         if dict_read[pairID]['status'] == 'working':
        #             qty = dict_read[pairID]["qty"]
        #     else:
        #         qty = 0
        #     read_file.close()
        #     # trade
        #     new_amount = round_down(amount, get_precision(pair))# + qty
        #     #id_list = np.append(id_list, pair)
        #     reset_asset_if(pair, x_coin, isBuyer, new_amount)
        #     #dict['z_reset_?'] = 'X'
        #     #np.save("id_list", id_list)
        #
        #     ### calculate and store loss
        #     read_file = open("top_json_mutual_file.json", "r")
        #     dict_read = json.load(read_file)
        #     invest = dict_read[pairID]['quote_qty']
        #     after_reset = get_last_trade(reset_pair)[4]
        #     loss = -(100-100/invest*after_reset)
        #     print('loss=', loss)
        #     # store profit values
        #     array = dict_read['stats']['losses_arr']
        #     array = jsonpickle.decode(array)
        #     new_array = np.append(array, loss)
        #     new_array = jsonpickle.encode(new_array)
        #     dict_read['stats']['losses_arr'] = new_array
        #     write_new_file = open("top_json_mutual_file.json", "w")
        #     json.dump(dict_read, write_new_file, indent=4)
        #     write_new_file.close()

        ###
######### HOLD
        else:
            ## STORE CURRENT CHANGE PERCENT TO ARRAY
            read_file = open("top_json_mutual_file.json", "r")
            dict_read = json.load(read_file)
            old_history = jsonpickle.decode(dict_read[pairID]['changePercent'])
            # append value to array
            new_history = np.append(old_history, changePercent_lastTrade)
            new_history = jsonpickle.encode(new_history)
            dict_read[pairID]['changePercent'] = new_history
            ## STORE CURRENT CHANGE PERCENT P_RESET TO ARRAY
            old_history = jsonpickle.decode(dict_read[pairID]['arr_p_resets'])
            # append value to array
            new_history = np.append(old_history, p_reset-100)
            new_history = jsonpickle.encode(new_history)
            dict_read[pairID]['arr_p_resets'] = new_history
            dict_read[pairID]["switch_fresh"] = False
            if dict_read[pairID]["status"] == 'working':
                if "loop_after_switch" in dict_read[pairID].keys():
                    dict_read[pairID]["loop_after_switch"] = dict_read[pairID]["loop_after_switch"] +1
                    #dict['loop_a_switch'] = dict_read[pairID]["loop_after_switch"]
            # write new file with same name
            write_new_file = open("top_json_mutual_file.json", "w")
            json.dump(dict_read, write_new_file, indent=4)
            write_new_file.close()
        new_frame_sellers = new_frame_sellers.append(dict, ignore_index=True)
    if len(new_frame_sellers) > 0:
        new_frame_sellers = new_frame_sellers.sort_values(by=['# change'], ascending=True)
    print('last move sell: (buy if negative)', len(seller), 'entries')
    print(50 * '-')
    date_string = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
    print(date_string)
    print(50 * '-')
    print(new_frame_sellers)
    #np.save("id_list", id_list)
    print()
    #print(id_list)
    # x_coin balance
    x_coin_balance = client.get_asset_balance(x_coin)
    #print(x_coin_balance, '')
    print(termcolor.colored(x_coin_balance, "magenta"))
    balance = float(x_coin_balance['free'])
    print()
    sellers_len = len(seller)
    print('ships sailing: ', nr_of_ships, '/', str(nr_of_ships + int(round_down(balance/top_up, 0))))
    #print('max ships sailing:', str(int(round_down(2200/top_up, 0))))

# reset to x_coin
def reset_asset_if(pairID, pair, x_coin, isBuyer, new_amount, d20_info):
    #export_dict = {}
    read_file = open("top_json_mutual_file.json", "r")
    dict_read = json.load(read_file)
    #last_trade = get_last_trade(pair)
    #tot_amount = last_trade[0]
    #mean_price = last_trade[1]
    #time = last_trade[2]
    tot_amount_quote = dict_read[pairID]['start_switch_qty']
    #export_dict['start_switch_qty'] = tot_amount_quote
    print(termcolor.colored(pair, "red"))
    #dataframe = pd.DataFrame(client.get_ticker())
    if 'switch_pro' in dict_read[pairID].keys():
        print('switches: ', jsonpickle.decode(dict_read[pairID]['switch_pro']))
    if "isBuyer" in dict_read[pairID]:
        isBuyer = dict_read[pairID]["isBuyer"]
    read_file.close()
    # create trading pair and make the move
    # buyers
    if isBuyer == True:
        reset_pair = get_left_symbol(pair) + x_coin
        # check overall cycle
        #change_percent = get_x_coin_deal_changePercent(pair, reset_pair, x_coin, id_restart, tot_amount, dataframe)
        #print('change to escape is: ', change_percent, '%')
        #new_amount = round_down(new_amount, get_precision(reset_pair))
        read_file = open("top_json_mutual_file.json", "r")
        dict_read = json.load(read_file)
        new_amount = dict_read[pairID]['qty']
        #export_dict['qty'] = new_amount
        trade_sell(reset_pair, new_amount, x_coin, pair)
        # dict_read['stats']['resets'] = dict_read['stats']['resets'] + 1
        #write_new_file = open("top_json_mutual_file.json", "w")
        #json.dump(dict_read, write_new_file, indent=4)
        read_file.close()
        #write_new_file.close()
        print(termcolor.colored('*** reset sell ***', "red"))
        traded = True
        ### TODO from x_coin to pair inkl. store the ID in id-Restart
        ### from pair switch
    # sellers
    elif isBuyer == False:
        # get x_coin pair
        left = get_left_symbol(pair)
        quote = pair.replace(left, '')
        reset_pair = quote + x_coin

        # ### CHECK list of d20 max
        # if 'BTC' in reset_pair:
        #     d20max = d20_info[0]
        # elif 'ETH' in reset_pair:
        #     d20max = d20_info[0]
        # elif 'USDT' in reset_pair:
        #     d20max = d20_info[0]
        # print('d20max = ', d20max)
        ### IF d20max is high enough --> RESET
        #if d20max > min_seller_reset:

        #read_file = open("top_json_mutual_file.json", "r")
        #dict_read = json.load(read_file)
        # if dict_read[pairID]["status"] == 'ship':
        #     tot_amount_quote = round_down(new_amount * dict_read[pairID]["ship_price"], get_precision(reset_pair))
        # if dict_read[pairID]["status"] == 'working':
        #     tot_amount_quote = round_down(tot_amount_quote, get_precision(reset_pair))
        tot_amount_quote = round_down(tot_amount_quote, get_precision(reset_pair))
        trade_sell(reset_pair, tot_amount_quote, x_coin, pair)
        # dict_read['stats']['resets'] = dict_read['stats']['resets'] + 1
        # write_new_file = open("top_json_mutual_file.json", "w")
        # json.dump(dict_read, write_new_file, indent=4)
        # write_new_file.close()
        #read_file.close()
        print(termcolor.colored('*** reset sell ***', "red"))
        traded = True
        # else:
        #     traded = False
        #     print(termcolor.colored('not TRADED!', "cyan"))
    #########################################################################
    ###STORE RESET EXCEL
    #########################################################################
    if traded == True:
        # get last trade info
        info = get_last_trade(reset_pair)
        # open json
        read_file = open("top_json_mutual_file.json", "r")
        dict_read = json.load(read_file)
        # open excel
        df = pd.read_excel('reset_stats.xlsx', index_col=0)
        # create new entry for json
        timestamp = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
        pairID = pairID
        reset_amount = info[4]
        amount_sold = info[0]
        #stays_on_left = 100 * (dict_read[pairID]['qty'] / amount_sold - 1)
        amount_invested = dict_read[pairID]['quote_qty']
        ship_price = dict_read[pairID]['ship_price']
        reset_price = info[1]
        ship_type = dict_read[pairID]['status']
        # add percent profit, if ship is reset on the left side
        if isBuyer == True:
            adding_profit = dict_read[pairID]['last_profit']
            print(isBuyer, 'adding_profit', adding_profit)
        else:
            adding_profit = 0
            print(isBuyer, 'adding_profit', adding_profit)
        profit = 100 * (reset_amount / amount_invested - 1) + adding_profit# + stays_on_left
        win = profit/100*amount_invested
        reset_data = {'timestamp': timestamp,
                      'pairID': pairID,
                      'reset_amount': reset_amount,
                      'amount_sold': amount_sold,
                      'amount_invested': amount_invested,
                      'ship_price': ship_price,
                      'reset_price': reset_price,
                      'profit_%': profit,
                        'win': win,
                      'ship_type': ship_type}
        # add new entry to df
        df2 = df.append(reset_data, ignore_index=True)
        df2 = df2.sort_values(by=['timestamp'], ascending=False)
        # store
        read_file.close()
        with suppress(Exception):
            # your code
            df2.to_excel('reset_stats.xlsx')
            df2.to_excel(r"XXX\reset_stats.xlsx")
        #########################################################################
    # mod json after reset
    read_file = open("top_json_mutual_file.json", "r")
    dict_read = json.load(read_file)
    # delete entry in dict
    del dict_read[pairID]
    # write new file with same name
    write_new_file = open("top_json_mutual_file.json", "w")
    json.dump(dict_read, write_new_file, indent=4)
    write_new_file.close()

# start into sea (add if start on id list later)
def go_to_sea(trust_symbols, x_coin, possibles, top_up, monitor):
    # check own balance
    x_coin_balance = float(client.get_asset_balance(x_coin)['free'])
    x_coin_balance_str = str(round(x_coin_balance, 0))
    balance = str('current balance ' + x_coin_balance_str + ' ' + x_coin)
    print(termcolor.colored(balance, "magenta"))
    if x_coin_balance > top_up:
        # 1 build list with pairs with status 'ship' and 'working' = inside_pairs
        read_file = open("top_json_mutual_file.json", "r")
        dict_read = json.load(read_file)
        inside_pairs = []
        for sample in dict_read:
            if sample != 'stats':
                #print(sample)
                #print(dict_read[sample].items())
                for item in dict_read[sample].items():
                    #print(item[0])
                    if item[0] == 'status':
                        #print(sample, item[1])
                        if item[1] == 'ship' or item[1] == 'working':
                            inside_pairs.append(sample)
        read_file.close()

    ### if depot higher than depot, check markets
        main1 = 'BTC' + x_coin
        main2 = 'ETH' + x_coin
        main3 = 'BNB' + x_coin
        main_pairs = [main1, main2, main3]
        base_trends10 = get_trend_of_x_min10(main_pairs)
        if len(base_trends10) == 3:
            BTCUSDT_trend10 = base_trends10[base_trends10.pair.str.contains(main1)]['trend'].values[0]
            ETHUSDT_trend10 = base_trends10[base_trends10.pair.str.contains(main2)]['trend'].values[0]
            BNBUSDT_trend10 = base_trends10[base_trends10.pair.str.contains(main3)]['trend'].values[0]
            #DOGEUSDT_trend10 = base_trends10[base_trends10.pair.str.contains('DOGEUSDT')]['trend'].values[0]
            # read_file = open("top_json_mutual_file.json", "r")
            # dict_read = json.load(read_file)
            # dict_read['stats']["BTCUSDT_trend10"] = BTCUSDT_trend10
            # dict_read['stats']["ETHUSDT_trend10"] = ETHUSDT_trend10
            # dict_read['stats']["BNBUSDT_trend10"] = BNBUSDT_trend10
            # #dict_read['stats']["DOGEUSDT_trend10"] = DOGEUSDT_trend10
            # write_new_file = open("top_json_mutual_file.json", "w")
            # json.dump(dict_read, write_new_file, indent=4)
            # write_new_file.close()
        print(termcolor.colored('basic trends: last 10 min ', "cyan"))
        print(base_trends10)
        print()
    ### # check for basic trend (30min), only trade when higher than sail
        base_trends30 = get_trend_of_x_min30(main_pairs)
        if len(base_trends30) == 3:
            BTCUSDT_trend30 = base_trends30[base_trends30.pair.str.contains(main1)]['trend'].values[0]
            ETHUSDT_trend30 = base_trends30[base_trends30.pair.str.contains(main2)]['trend'].values[0]
            BNBUSDT_trend30 = base_trends30[base_trends30.pair.str.contains(main3)]['trend'].values[0]
            #DOGEUSDT_trend30 = base_trends30[base_trends30.pair.str.contains('DOGEUSDT')]['trend'].values[0]
            # read_file = open("top_json_mutual_file.json", "r")
            # dict_read = json.load(read_file)
            # dict_read['stats']["BTCUSDT_trend30"] = BTCUSDT_trend30
            # dict_read['stats']["ETHUSDT_trend30"] = ETHUSDT_trend30
            # dict_read['stats']["BNBUSDT_trend30"] = BNBUSDT_trend30
            # #dict_read['stats']["DOGEUSDT_trend30"] = DOGEUSDT_trend30
            # write_new_file = open("top_json_mutual_file.json", "w")
            # json.dump(dict_read, write_new_file, indent=4)
            # write_new_file.close()
        print(termcolor.colored('basic trends: last 30 min ', "cyan"))
        print(base_trends30)
        print()
    ### # check for long trend (60min), only trade when higher than sail
        base_trends60 = get_trend_of_x_min60(main_pairs)
        if len(base_trends60) == 3:
            BTCUSDT_trend60 = base_trends60[base_trends60.pair.str.contains(main1)]['trend'].values[0]
            ETHUSDT_trend60 = base_trends60[base_trends60.pair.str.contains(main2)]['trend'].values[0]
            BNBUSDT_trend60 = base_trends60[base_trends60.pair.str.contains(main3)]['trend'].values[0]
            #DOGEUSDT_trend90 = base_trends90[base_trends90.pair.str.contains('DOGEUSDT')]['trend'].values[0]
            # read_file = open("top_json_mutual_file.json", "r")
            # dict_read = json.load(read_file)
            # dict_read['stats']["BTCUSDT_trend90"] = BTCUSDT_trend60
            # dict_read['stats']["ETHUSDT_trend90"] = ETHUSDT_trend60
            # dict_read['stats']["BNBUSDT_trend90"] = BNBUSDT_trend60
            # #dict_read['stats']["DOGEUSDT_trend90"] = DOGEUSDT_trend90
            # write_new_file = open("top_json_mutual_file.json", "w")
            # json.dump(dict_read, write_new_file, indent=4)
            # write_new_file.close()
        print(termcolor.colored('long trends: last 60 min ', "cyan"))
        print(base_trends60)
        print()
    ### # check for long trend (3h), only trade when higher than sail
        base_trends2h = get_trend_of_x_min2h(main_pairs)
        if len(base_trends2h) == 3:
            BTCUSDT_trend3h = base_trends2h[base_trends2h.pair.str.contains(main1)]['trend'].values[0]
            ETHUSDT_trend3h = base_trends2h[base_trends2h.pair.str.contains(main2)]['trend'].values[0]
            BNBUSDT_trend3h = base_trends2h[base_trends2h.pair.str.contains(main3)]['trend'].values[0]
        print(termcolor.colored('long trends: last 2h ', "cyan"))
        print(base_trends2h)
        print()
        ### PRICE COMPARED TO MAX VALUES OF CURRENT PERIOD ### 3 HOURS
        # df_max_last3 = get_max_last3(['BTCUSDT', 'ETHUSDT', 'BNBUSDT'])  # , 'DOGEUSDT'])
        # print(str(100*(1 - diff_tomax3)), '%')
        # print(termcolor.colored('current price has to be under ... % of 3h max', "cyan"))
        # print(df_max_last3)
        # if len(df_max_last3) == 3:
        #     BTCUSDT_max3 = df_max_last3[df_max_last3.pair.str.contains('BTCUSDT')]['max'].values[0]
        #     BTCUSDT_now = df_max_last3[df_max_last3.pair.str.contains('BTCUSDT')]['now'].values[0]
        #     BTCUSDT_rel_3 = df_max_last3[df_max_last3.pair.str.contains('BTCUSDT')]['relation to max 3'].values[0]
        #     ETHUSDT_max3 = df_max_last3[df_max_last3.pair.str.contains('ETHUSDT')]['max'].values[0]
        #     ETHUSDT_now = df_max_last3[df_max_last3.pair.str.contains('ETHUSDT')]['now'].values[0]
        #     ETHUSDT_rel_3 = df_max_last3[df_max_last3.pair.str.contains('ETHUSDT')]['relation to max 3'].values[0]
        #     BNBUSDT_max3 = df_max_last3[df_max_last3.pair.str.contains('BNBUSDT')]['max'].values[0]
        #     BNBUSDT_now = df_max_last3[df_max_last3.pair.str.contains('BNBUSDT')]['now'].values[0]
        #     BNBUSDT_rel_3 = df_max_last3[df_max_last3.pair.str.contains('BNBUSDT')]['relation to max 3'].values[0]

        ### PRICE COMPARED TO MAX VALUES OF CURRENT PERIOD ### 12 HOURS
        df_max_last12 = get_max_last12(main_pairs)
        #print(str(diff_tomax12), '%')
        print(termcolor.colored('relation to 12h max', "cyan"))
        print(df_max_last12)
        if len(df_max_last12) == 3:
            BTCUSDT_max12 = df_max_last12[df_max_last12.pair.str.contains(main1)]['max'].values[0]
            BTCUSDT_now = df_max_last12[df_max_last12.pair.str.contains(main1)]['now'].values[0]
            BTCUSDT_rel_12 = df_max_last12[df_max_last12.pair.str.contains(main1)]['relation to max 12'].values[0]
            ETHUSDT_max12 = df_max_last12[df_max_last12.pair.str.contains(main2)]['max'].values[0]
            ETHUSDT_now = df_max_last12[df_max_last12.pair.str.contains(main2)]['now'].values[0]
            ETHUSDT_rel_12 = df_max_last12[df_max_last12.pair.str.contains(main2)]['relation to max 12'].values[0]
            BNBUSDT_max12 = df_max_last12[df_max_last12.pair.str.contains(main3)]['max'].values[0]
            BNBUSDT_now = df_max_last12[df_max_last12.pair.str.contains(main3)]['now'].values[0]
            BNBUSDT_rel_12 = df_max_last12[df_max_last12.pair.str.contains(main3)]['relation to max 12'].values[0]

        ### PRICE COMPARED TO MAX VALUES OF CURRENT PERIOD ### 36 HOURS
        df_max_last36 = get_max_last36(main_pairs)
        #print(str(diff_tomax36), '%')
        print(termcolor.colored('relation to 36h max', "cyan"))
        print(df_max_last36)
        if len(df_max_last36) == 3:
            BTCUSDT_max36 = df_max_last36[df_max_last36.pair.str.contains(main1)]['max'].values[0]
            BTCUSDT_now = df_max_last36[df_max_last36.pair.str.contains(main1)]['now'].values[0]
            BTCUSDT_rel_36 = df_max_last36[df_max_last36.pair.str.contains(main1)]['relation to max 36'].values[0]
            ETHUSDT_max36 = df_max_last36[df_max_last36.pair.str.contains(main2)]['max'].values[0]
            ETHUSDT_now = df_max_last36[df_max_last36.pair.str.contains(main2)]['now'].values[0]
            ETHUSDT_rel_36 = df_max_last36[df_max_last36.pair.str.contains(main2)]['relation to max 36'].values[0]
            BNBUSDT_max36 = df_max_last36[df_max_last36.pair.str.contains(main3)]['max'].values[0]
            BNBUSDT_now = df_max_last36[df_max_last36.pair.str.contains(main3)]['now'].values[0]
            BNBUSDT_rel_36 = df_max_last36[df_max_last36.pair.str.contains(main3)]['relation to max 36'].values[0]

        ### PRICE COMPARED TO MAX VALUES OF CURRENT PERIOD ### 20 days
        df_max_last20d_request = get_max_last20d(main_pairs)
        df_max_last20d = df_max_last20d_request[0]
        list_max_last20d_info = df_max_last20d_request[1]
        print(str(diff_tomax20d), '%')
        print(termcolor.colored('current price has to be under ... % of 20 days max', "cyan"))
        print(df_max_last20d)
        if len(df_max_last20d) == 3:
            BTCUSDT_max20d = df_max_last20d[df_max_last20d.pair.str.contains(main1)]['max'].values[0]
            BTCUSDT_now = df_max_last20d[df_max_last20d.pair.str.contains(main1)]['now'].values[0]
            BTCUSDT_rel_20d = df_max_last20d[df_max_last20d.pair.str.contains(main1)]['relation to max 20 days'].values[0]
            ETHUSDT_max20d = df_max_last20d[df_max_last20d.pair.str.contains(main2)]['max'].values[0]
            ETHUSDT_now = df_max_last20d[df_max_last20d.pair.str.contains(main2)]['now'].values[0]
            ETHUSDT_rel_20d = df_max_last20d[df_max_last20d.pair.str.contains(main2)]['relation to max 20 days'].values[0]
            BNBUSDT_max20d = df_max_last20d[df_max_last20d.pair.str.contains(main3)]['max'].values[0]
            BNBUSDT_now = df_max_last20d[df_max_last20d.pair.str.contains(main3)]['now'].values[0]
            BNBUSDT_rel_20d = df_max_last20d[df_max_last20d.pair.str.contains(main3)]['relation to max 20 days'].values[0]
            depot_BTC = define_depot_setting(BTCUSDT_rel_20d, 'BTC', top_up, total_balance, x_coin)
            depot_ETH = define_depot_setting(ETHUSDT_rel_20d, 'ETH', top_up, total_balance, x_coin)
            depot_BNB = define_depot_setting(BNBUSDT_rel_20d, 'BNB', top_up, total_balance, x_coin)

        ### get possible market by filtering from sail factors and maxlast 12 ---> TRUE = Tradable
        # x_coin_balance = float(client.get_asset_balance(x_coin)['free'])
        # x_coin_balance_str = str(round(x_coin_balance, 0))
        # balance = str('current balance ' + x_coin_balance_str + ' ' + x_coin)
        # print(termcolor.colored(balance, "magenta"))
        if len(base_trends10) == 3 and len(base_trends30) == 3 and len(base_trends60) == 3 and len(base_trends2h) == 3 and len(df_max_last20d) == 3:# and len(df_max_last12) == 3:
            # start with BTC conditions
            if p_10_bottom < BTCUSDT_trend10 < p_10_upper and p_30_bottom < BTCUSDT_trend30 < p_30_upper  and p_60_bottom < BTCUSDT_trend60 < p_60_upper and p_3h_bottom < BTCUSDT_trend3h < p_3h_upper and \
                    BTCUSDT_now < BTCUSDT_max20d * (diff_tomax20d/100)\
                    and x_coin_balance > depot_BTC:# and BTCUSDT_now < BTCUSDT_max3 - (BTCUSDT_max3 * diff_tomax3) and BTCUSDT_rel_3 > BTCUSDT_rel_12:# this means that max12 has to be bigger than max3
                start = True
            else:
                start = False
            # start with ETH conditions
            if p_10_bottom < ETHUSDT_trend10 < p_10_upper and p_30_bottom < ETHUSDT_trend30 < p_30_upper  and p_60_bottom < ETHUSDT_trend60 < p_60_upper and p_3h_bottom < ETHUSDT_trend3h < p_3h_upper and \
                    ETHUSDT_now < ETHUSDT_max20d * (diff_tomax20d/100)\
                    and x_coin_balance > depot_ETH:# and ETHUSDT_now < ETHUSDT_max3 - (ETHUSDT_max3 * diff_tomax3) and ETHUSDT_rel_3 > ETHUSDT_rel_12:
                start2 = True
            else:
                start2 = False
            # start with BNB conditions
            if p_10_bottom < BNBUSDT_trend10 < p_10_upper and p_30_bottom < BNBUSDT_trend30 < p_30_upper and p_60_bottom < BNBUSDT_trend60 < p_60_upper and p_3h_bottom < BNBUSDT_trend3h < p_3h_upper and \
                    BNBUSDT_now < BNBUSDT_max20d * (diff_tomax20d/100)\
                    and x_coin_balance > depot_BNB:# and BNBUSDT_now < BNBUSDT_max3 - (BNBUSDT_max3 * diff_tomax3) and BNBUSDT_rel_3 > BNBUSDT_rel_12:
                start3 = True
            else:
                start3 = False

            # 2 filter inside_pairs with all possible pairs from trust
            result1 = [x for x in possibles if x not in inside_pairs]
            result1 = [x for x in result1 if x != 'stats']

            ### PRICE MOVEMENTS ###
            # filter for relevant markets
            ## 1 market is possible
            # BTCis tradeable
            if start == True and start2 == False and start3 == False:
                result = [x for x in result1 if 'BTC' in x]
            # ETHis tradeable
            elif start2 == True and start == False and start3 == False:
                result = [x for x in result1 if 'ETH' in x]
            # BNBis tradeable
            elif start3 == True and start == False and start2 == False:
                result = [x for x in result1 if 'BNB' in x]

            ## 2 markets are possible
            # BTC and ETH is tradeable
            elif start == True and start2 == True:
                result = [x for x in result1 if 'BTC' in x or 'ETH' in x]
            # BTC and BNB is tradeable
            elif start == True and start3 == True:
                result = [x for x in result1 if 'BTC' in x or 'BNB' in x]
            # ETH and BNB is tradeable
            elif start2 == True and start3 == True:
                result = [x for x in result1 if 'ETH' in x or 'BNB' in x]

            ## All 3 are tradeable
            elif start == True and start2 == True and start3 == True:
                result = [x for x in result1 if 'BTC' in x or 'ETH' in x or 'BNB' in x]
            else:
                result = []

            if len(result) == 0:
                print('possible trades: ', result)

            ### choose pair if tradeable market is there --> not to many ships yet ###
            if len(result) > 0:
                # filter for only below 2 ships assets
                too_many = []
                for sample in result:
                    number = get_nr_of_ships_per_asset(dict_read, sample)
                    #print (sample, number)
                    if number > 1:
                        too_many.append(sample)
                # filter from results
                result = [x for x in result if x not in too_many]
                print('possible trades: (before d20 check)', result)

                if len(result) > 0:
            # 3 define  pair to sail (market data indicator)
                    print('choosing new pair, if positive last 5min move is > ', enter_wave, '...')
                    ### test for 20d max
                    # go from nextPair to Reset Pair
                    resets_result = []
                    for nextpair in result:
                        reset_pair = get_left_symbol(nextpair) + x_coin
                        #print(reset_pair)
                        resets_result.append(reset_pair)
                        # remove duplicates
                        res = []
                        for i in resets_result:
                            if i not in res:
                                res.append(i)

                    ### PRICE COMPARED TO MAX VALUES OF CURRENT PERIOD ### 20 days
                    df_max_last20d_next_pair = get_max_last20d(res)[0]
                    print(str(d20_reset_pair_upper), 'till', str(d20_reset_pair_bottom), '%')
                    print(termcolor.colored('current price has to be under ... % of 20 days max of reset pair', "cyan"))
                    print(df_max_last20d_next_pair)
                    ### drop the ones higher d20_reset_pair
                    rslt_df = df_max_last20d_next_pair[(df_max_last20d_next_pair['relation to max 20 days'].values < d20_reset_pair_upper)]
                    rslt_df = rslt_df[(rslt_df['relation to max 20 days'].values > d20_reset_pair_bottom)]
                    rslt = rslt_df['pair'].values.tolist()
                    # cut to left pair only __ resetpairs
                    res2 = []
                    for i in res:
                        res2.append(i[:len(i) - len_xcoin])

                    # get left pairs of possible next pair
                    best_result = []
                    for possible in result:
                        left = get_left_symbol(possible)
                        #print(left, possible)
                        if left in res2:
                            best_result.append(possible)
                    print('possible trades: (after d20 check)', best_result)

                    # list_max_last20d_info = df_max_last20d_request[1]
                    # print(str(diff_tomax20d), '%')
                    # print(termcolor.colored('current price has to be under ... % of 20 days max', "cyan"))
                    # print(df_max_last20d)
                    # if len(df_max_last20d) == 3:
                    #     BTCUSDT_max20d = df_max_last20d[df_max_last20d.pair.str.contains(main1)]['max'].values[0]
                    #     BTCUSDT_now = df_max_last20d[df_max_last20d.pair.str.contains(main1)]['now'].values[0]
                    #     BTCUSDT_rel_20d = df_max_last20d[df_max_last20d.pair.str.contains(main1)]['relation to max 20 days'].values[
                    #         0]
                    #     ETHUSDT_max20d = df_max_last20d[df_max_last20d.pair.str.contains(main2)]['max'].values[0]
                    #     ETHUSDT_now = df_max_last20d[df_max_last20d.pair.str.contains(main2)]['now'].values[0]
                    #     ETHUSDT_rel_20d = df_max_last20d[df_max_last20d.pair.str.contains(main2)]['relation to max 20 days'].values[
                    #         0]
                    #     BNBUSDT_max20d = df_max_last20d[df_max_last20d.pair.str.contains(main3)]['max'].values[0]
                    #     BNBUSDT_now = df_max_last20d[df_max_last20d.pair.str.contains(main3)]['now'].values[0]
                    #     BNBUSDT_rel_20d = df_max_last20d[df_max_last20d.pair.str.contains(main3)]['relation to max 20 days'].values[
                    #         0]
                    #     depot_BTC = define_depot_setting(BTCUSDT_rel_20d, 'BTC', top_up, total_balance, x_coin)
                    #     depot_ETH = define_depot_setting(ETHUSDT_rel_20d, 'ETH', top_up, total_balance, x_coin)
                    #     depot_BNB = define_depot_setting(BNBUSDT_rel_20d, 'BNB', top_up, total_balance, x_coin)



                    # 30min
                    #df30 = get_trend_of_x_min30(result)
                    # 2min
                    df = get_trend_of_x_min(monitor, best_result)
                    top_positive_trend_pair = df['pair'][0]
                    top_negative_trend_pair = df['pair'][len(df)-1]
                    top_positive_trend = df['trend'][0]
                    top_negative_trend = df['trend'][len(df)-1]
                    # go to max trend
                    #if top_positive_trend > -(top_negative_trend):
                    print('positive trend: ', top_positive_trend)
                    trend_X = top_positive_trend
                    trend2 = top_positive_trend
                    # buy left side
                    # nextPair = top_positive_trend_pair
                    # aim = get_left_symbol(nextPair)
                    # startPair = aim + x_coin
                    #buy right side
                    nextPair = top_positive_trend_pair
                    left = get_left_symbol(nextPair)
                    aim = nextPair.replace(left, '')
                    startPair = aim + x_coin
                    # else:
                    #     print('negative trend: ', top_negative_trend)
                    #     trend_X = -(top_negative_trend)
                    #     trend2 = top_negative_trend
                    #     nextPair = top_negative_trend_pair
                    #     # # buy left side
                    #     # nextPair = top_negative_trend_pair
                    #     # aim = get_left_symbol(nextPair)
                    #     # startPair = aim + x_coin
                    #     # # buy right side
                    #     left = get_left_symbol(nextPair)
                    #     aim = nextPair.replace(left, '')
                    #     startPair = aim + x_coin
                    print(nextPair)
                    if 'BNB' in nextPair[2:]:
                        limit_share = 25
                    else:
                        limit_share = 87.5
                    ships_per_asset = get_nr_of_ships_per_asset(dict_read, nextPair)
                    print('currently there are ', str(ships_per_asset), ' ships with ', get_left_symbol(nextPair))
                    ships_per_quote_request = get_share_of_ships_per_quote(dict_read, nextPair, limit_share)
                    ships_per_quote = str(ships_per_quote_request[1])
                    print('currently there are ', str(ships_per_quote), ' ships with ', nextPair[len(nextPair)-3:], 'tradeable= ', ships_per_quote_request[0])
                    print(nextPair[len(nextPair)-3:], '-share: ', ships_per_quote_request[2], ' %')
                    print('limit share = ', limit_share, ' %')
                    # trade if trend is higher then 0.3 in one ditection
                    if trend_X > enter_wave and ships_per_quote_request[0] == True:
        ########################TRADE###
                        dataframe = pd.DataFrame(client.get_ticker())
                        print(termcolor.colored('nextPair:' + nextPair, "cyan"))
                        print('startPair:', startPair)
                        pairID = ''
                        trade_buy(pairID, startPair, top_up, x_coin)
                        # read_file = open("top_json_mutual_file.json", "r")
                        # dict_read = json.load(read_file)
                        # dict_read['stats']['new_ships'] = dict_read['stats']['new_ships']+1
                        # write_new_file = open("top_json_mutual_file.json", "w")
                        # json.dump(dict_read, write_new_file, indent=4)
                        # write_new_file.close()
                        # clean from id_list
                        #index = np.where(id_list == nextPair)
                        #print(index)
                        #id_list = np.delete(id_list, index)
                        #print(id_list)
                        #np.save("id_list", id_list)
                # 6 define the correct quantity for the storage (always left side)
                        last_trade = get_last_trade(startPair)
                        left = get_left_symbol(nextPair)
                        if left in startPair:
                            quantity = last_trade[0]
                            quote_quantity = last_trade[4]
                            ship_price = float(dataframe[dataframe.symbol.str.contains(nextPair)].lastPrice.values[0])
                            isBuyer_new = True
                        else:
                            quantity = round_down(last_trade[0] / float(dataframe[dataframe.symbol.str.contains(nextPair)].askPrice.values[0]), get_precision(nextPair))
                            quote_quantity = last_trade[4]
                            start_switch_qty = last_trade[0]
                            ship_price = float(dataframe[dataframe.symbol.str.contains(nextPair)].askPrice.values[0])
                            isBuyer_new = False
                # 7 mod json
                        read_file = open("top_json_mutual_file.json", "r")
                        dict_read = json.load(read_file)
                        list = []
                        array_history = np.array(list)
                        array_history = jsonpickle.encode(array_history)
                        # modify
                        # note quote quantity
                        date_string = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
                        nextPairID = nextPair + date_string
                        dict_read.update({nextPairID: {'go_to_sea_time': date_string,
                                                       'qty': quantity,
                                                        'start_left_qty': quantity,
                                                       'quote_qty': quote_quantity,
                                                       'start_switch_qty': start_switch_qty,
                                                       'ship_price': ship_price,
                                                     'isBuyer': isBuyer_new,
                                                       'status': 'ship',
                                                       'changePercent': array_history,
                                                       'last_direction': 0,
                                                       'before_last_direction': 0,
                                                       'startPair': startPair,
                                                       'trend2': trend2,
                                                       'switch_pro': array_history,
                                                       'loop_after_switch': 0}})

                            #if len(info_nextPair_past) > 0:
                                #dict_read[nextPair]["trend30"] = info_nextPair_past.trend.values[0]
                                #dict_read[nextPair]["trend2"] = trend2
                            # else:
                            #     #dict_read[nextPair]["trend30"] = 0
                            #     dict_read[nextPair]["trend2"] = 0
                        # else:
                        #     dict_read.update({nextPair: {'qty': quantity,'quote_qty': quote_quantity, 'ship_price': ship_price, 'isBuyer': isBuyer_new,
                        #                                  'status': 'ship', 'changePercent': array_history, 'loop_after_switch': 0}})
                        # # write new file with same name
                        write_new_file = open("top_json_mutual_file.json", "w")
                        json.dump(dict_read, write_new_file, indent=4)
                        write_new_file.close()
                        print(termcolor.colored('success buy SHIP goes to sea', "cyan"))

                    # return list with BTC ETH BNB 20d info
                    if len(df_max_last20d) == 3:
                        return list_max_last20d_info

# get_current_nr_of_ships_per_asset, insert next pair
def get_nr_of_ships_per_asset(json, pair):
    asset_aim = get_left_symbol(pair)
    # create list with all pairs
    all_asssets = []
    for key in json:
        if key != 'stats':
            all_asssets.append(get_left_symbol(get_pair_from_ID(key)))
    # count elements per pair
    c = Counter(all_asssets)
    # open for pair parameter
    if asset_aim in c.keys():
        if asset_aim in n12_ships_assets:
            current_ships = c[asset_aim]-10
        else:
            current_ships =  c[asset_aim]
    else:
        current_ships = 0
    return current_ships

# RETURN TRUE, if ships per quote are less than limit_share; nr of ships with asset BTC, ETH and BNB have to be smaller than 65 % = limit_share!!!
def get_share_of_ships_per_quote(json, pair, limit_share):
    quote = pair[len(pair)-3:]
    # create list with all pairs
    all_asssets = []
    for key in json:
        if key != 'stats':
            all_asssets.append(get_pair_from_ID(key)[len(get_pair_from_ID(key))-3:])
    total_ships = len(all_asssets)
    # count elements per pair
    c = Counter(all_asssets)
    # open for pair parameter
    if quote in c.keys():
            current_ships =  c[quote]
    else:
        current_ships = 0
    # define True for ships less than limit_share
    if current_ships < limit_share/100 * total_ships:
        share = True
    else:
        share = False
    share_value = round(100/total_ships*current_ships, 2)
    return share, current_ships, share_value

# check if all elements are equal
def ckeckList(lst):
    ele = lst[0]
    chk = True
    # Comparing each element with first item
    for item in lst:
        if ele != item:
            chk = False
            break;
    # if (chk == True):
    #     print("Equal")
    # else:
    #     print("Not equal")
    return chk

# run
def run(trust_symbols, profit, x_coin, frame, top_up, monitor, d20_infos):
    # nr_of buyers
    nr_of_ships = return_nr_of_ships(trust_symbols)
    if nr_of_ships > 10:
        splits = int(round_down((nr_of_ships-1)/10, 0))
    else:
        splits = 0
    check_and_trade(profit, x_coin, frame, top_up, d20_infos, splits, nr_of_ships)
    print()

# summary of profits RIGHT SIDE json file
def get_right_profit_amounts(x_coin):
    dataframe = pd.DataFrame(client.get_ticker())
    dataframe["lastPrice"] = pd.to_numeric(dataframe["lastPrice"], downcast="float")
    list = []
    BTC = np.array(list)
    ETH = np.array(list)
    BNB = np.array(list)
    read_file = open("top_json_mutual_file.json", "r")
    dict_read = json.load(read_file)
    for key in dict_read:
        pair = key
        if 'quote_qty' in dict_read[pair]:
            usdt_at_start = dict_read[pair]['quote_qty']
            if 'start_switch_qty' in dict_read[pair] and dict_read[pair]['isBuyer'] == False and dict_read[pair]['status'] != 'depot':# and 'BNBBTC' not in pair:
                first_amount = dict_read[pair]['start_switch_qty']
                startPair = dict_read[pair]['startPair']
                #print(pair)
                # print('usdt:', usdt_at_start)
                #print('first_amount:', first_amount)
                # print('startPair:', startPair)
                if startPair == 'BTCUSDT':
                    BTC = np.append(BTC, first_amount)
                if startPair == 'ETHUSDT':
                    ETH = np.append(ETH, first_amount)
                if startPair == 'BNBUSDT':
                    BNB = np.append(BNB, first_amount)
            elif 'qty' in dict_read[pair] and dict_read[pair]['isBuyer'] == True and dict_read[pair]['status'] != 'depot':
                first_amount = dict_read[pair]['qty']
                pairname = get_pair_from_ID(pair)
                if pairname == 'BNBBTC':
                    BNB = np.append(BNB, first_amount)
                if pairname == 'BNBETH':
                    BNB = np.append(BNB, first_amount)
                if pairname == 'ETHBTC':
                    ETH = np.append(ETH, first_amount)

    current_sum_BTC = round_down(float(np.sum(BTC)), 5)
    current_sum_ETH = round_down(float(np.sum(ETH)), 3)
    current_sum_BNB = round_down(float(np.sum(BNB)), 3)
    main1 = 'BTC' + x_coin
    main2 = 'ETH' + x_coin
    main3 = 'BNB' + x_coin
    print('must_have_BTC:', current_sum_BTC)
    print('balance BTC: ', float(client.get_asset_balance('BTC')['free']))
    BTC_profit = round_down(float(client.get_asset_balance('BTC')['free']) - current_sum_BTC, get_precision(main1))
    USDT_pro_BTC = round_down(BTC_profit * float(dataframe[dataframe.symbol.str.contains(main1)].lastPrice.values[0]), 2)
    print('profit BTC=', BTC_profit, '=== ')
    print(termcolor.colored(USDT_pro_BTC, "green"))
    print(x_coin)
    print()
    print('must_have_ETH:', current_sum_ETH)
    print('balance ETH: ', float(client.get_asset_balance('ETH')['free']))
    ETH_profit = round_down(float(client.get_asset_balance('ETH')['free']) - current_sum_ETH, get_precision(main2))
    USDT_pro_ETH = round_down(ETH_profit * float(dataframe[dataframe.symbol.str.contains(main2)].lastPrice.values[0]), 2)
    print('profit ETH=', ETH_profit, '=== ')
    print(termcolor.colored(USDT_pro_ETH, "green"))
    print(x_coin)
    print()
    print('must_have_BNB:', current_sum_BNB)
    print('balance BNB ', float(client.get_asset_balance('BNB')['free']))
    BNB_profit = round_down(float(client.get_asset_balance('BNB')['free']) - current_sum_BNB, get_precision(main3))
    USDT_pro_BNB = round_down(BNB_profit * float(dataframe[dataframe.symbol.str.contains(main3)].lastPrice.values[0]), 2)
    print('profit BNB=', BNB_profit, '=== ')
    print(termcolor.colored(USDT_pro_BNB, "green"))
    print(x_coin)
    print()
    total = str(round(USDT_pro_BNB+USDT_pro_ETH+USDT_pro_BTC, 2))
    total = str('Total: ' + total + x_coin)
    print(termcolor.colored(total, "green"))

# get pair from pairID
def get_pair_from_ID(name):
    cut1 = name[:len(name)-19]
    return cut1

# CONTROL OF RISK PER RELATIVE PRICE get depot settings dependent on current max20day parameter
def define_depot_setting(rel_20d, pair, top_up, total_balance, x_coin):
    new_depot = (total_balance / 1.48) + ((rel_20d-100) * top_up * (2.6))
    print(str(round(rel_20d, 2)), '%     ', str(round(new_depot, 2)), x_coin, ' for', pair)
    return new_depot

# exe
p_10_upper = 0.5
p_10_bottom = -0.75
p_30_upper = 0.75
p_30_bottom = -0.75
p_60_upper = 2
p_60_bottom = -0.5
# it is 2h not 3h
p_3h_upper = 8
p_3h_bottom = -0.2
# enter
monitor = 5#mins for comare of movement for enter wave value
enter_wave = 0.0750# only positive trend at the moment (last 5 min)
diff_tomax12 = 100.1#% current price must be smaller than 98.5% of last 12h max
diff_tomax36 = 100.1#% current price must be smaller than 99.5% of last 32h max
diff_tomax20d = 99.75#% current price must be smaller than 96% of last 20 d max
# switches
profit = 0.75
switch1 = 0.6
fallback_1 = 0.025# has to be greater than 0
fallback_2 = 0.050# has to be greater than 0
frame = 0.175# in this frame, no resets are possible
stopp_loss = 4# % change for change switches value if 99% of top up is given
max_ships_per_asset = 2
#limit_share = 80#% max share of ships per quote (BTC, ETH, BNB)
n12_ships_assets = ['NEXO', 'BNB', 'ETH', 'BTC']
x_coin = 'USDT'
d20_reset_pair_upper = 94# %
d20_reset_pair_bottom = 65# %
total_balance = 9000
phase_a_switch = list(range(0, 6))
min_seller_reset = 95#%
top_up = 100
len_xcoin = 4
counter = 0
max_loops = total_balance
print('profit=', profit)
print('fallback_1=', fallback_1)
print('fallback_2=', fallback_2)
print('frame=', frame)
print('x_coin=', x_coin)
print('top_up=', top_up, x_coin)
print('phase_a_switch=', phase_a_switch)
while counter < max_loops:
    counter = 1 + counter
    path = (r"XXX")
    os.chdir(path)
    folder = os.listdir(path)
    #id_list = np.load('id_list.npy')
    read_file = open("top_json_mutual_file.json", "r")
    dict_read = json.load(read_file)
    date_string = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
    dict_read['stats']['last_log'] = date_string
    write_new_file = open("top_json_mutual_file.json", "w")
    json.dump(dict_read, write_new_file, indent=4)
    write_new_file.close()
    # investment managing
    phases = [100, 97.5, 95, 92.5, 90, 85, 80, 75]
    for percent in phases:
        define_depot_setting(percent, 'pair', top_up, total_balance, x_coin)
    d20_infos = go_to_sea(trust_symbols, x_coin, possibles, top_up, monitor)
    for sample in range(0, 4):
        run(trust_symbols, profit, x_coin, frame, top_up, monitor, d20_infos)
        print('loop', sample)
        sleep(3)

    # look at profits from switches
    get_right_profit_amounts(x_coin)
    ### ### ###
    # sync excels, i case it wasnt yet
    ### ### ###
    ## RESETS STATS
    dt_original_R = int(os.path.getmtime('XXX.xlsx'))
    dt_cloud_R = int(os.path.getmtime(r"XXX"))
    # sync if there is a diff in closetime
    if dt_original_R - dt_cloud_R > 1:
        dfR = pd.read_excel('XXX.xlsx', index_col=0)
        with suppress(Exception):
            dfR.to_excel(r"XXX")
    ## SWITCH STATS
    dt_original_S = int(os.path.getmtime('XXX'))
    dt_cloud_S = int(os.path.getmtime(r"XXX"))
    # sync if there is a diff in closetime
    if dt_original_S - dt_cloud_S > 1:
        dfS = pd.read_excel('XXX', index_col=0)
        with suppress(Exception):
            dfS.to_excel(r"XXX.xlsx")

    sleep(20)



