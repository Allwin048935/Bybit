# config.py
API_KEY = 'jcTIZOTsd1OsUOpgER'
API_SECRET = 'IlBRdxegRqhkWFyHWs2K9omWXTuCDyLEx7a6'
SECRET_2 = 'eyJhbGciOiJIUzI1NiJ9.eyJzaWduYWxzX3NvdXJjZV9pZCI6MTAyNTR9.UpdSFm3FpcmR7hcVaBUOzPp5Q6-1gBRlQA21sH0ieHo'
SECRET_1 = 'eyJhbGciOiJIUzI1NiJ9.eyJzaWduYWxzX3NvdXJjZV9pZCI6ODI4MzV9.ccZIwRRxe781qP0Mtlx62NIkmKyUGs155h433uxE-M0'
THREE_COMMAS_WEBHOOK_URL = 'https://api.3commas.io/signal_bots/webhooks'
TELEGRAM_TOKEN = '7426543281:AAHu4Qf_KT6sGBaqUJU5ccFKZroHKrVc9R0'
CHAT_ID = '1385370555'
SELECTED_SYMBOLS = [
"1CATUSDT", "1INCHUSDT", "A8USDT", "AAVEUSDT", "ACEUSDT", "ACHUSDT", "ADAUSDT", "AERGOUSDT", "AEROUSDT", "AEVOUSDT", "AGIUSDT", "AGLDUSDT", "AIOZUSDT", "AIUSDT", "AKROUSDT", "AKTUSDT", "ALEOUSDT", "ALGOUSDT", "ALICEUSDT", "ALPACAUSDT","ALPHAUSDT", "ALTUSDT", "AMBUSDT", "ANKRUSDT", 
"BADGERUSDT", "BAKEUSDT", "BALUSDT", "BANANAUSDT", "BANDUSDT", "BATUSDT", "BBUSDT", "BCHUSDT", "BEAMUSDT", "BELUSDT", "BENDOGUSDT", "BICOUSDT", "BIGTIMEUSDT", "BLASTUSDT", "BLURUSDT", "BLZUSDT", "BNBUSDT", "BNTUSDT", "BNXUSDT", "BOBAUSDT", "BOMEUSDT",
"BONDUSDT", "DARUSDT", "DASHUSDT", "DATAUSDT", "DEGENUSDT", "DENTUSDT", "DEXEUSDT", "DGBUSDT", "DODOUSDT", "DOGEUSDT", "DOGSUSDT", "DOGUSDT", "DOP1USDT", "DOTUSDT", "DRIFTUSDT", "DUSKUSDT", "DYDXUSDT", "DYMUSDT", 
"EDUUSDT", "EGLDUSDT", "ENAUSDT", "ENJUSDT", "HBARUSDT", "HFTUSDT", "HIFIUSDT", "HIGHUSDT", "HNTUSDT", "HOOKUSDT", "HOTUSDT", 
"ICPUSDT", "ICXUSDT", "IDEXUSDT", "IDUSDT", "ILVUSDT", "IMXUSDT", "INJUSDT", "IOSTUSDT", "IOTAUSDT", "IOTXUSDT", "IOUSDT", "JASMYUSDT", "JOEUSDT", "JSTUSDT", "JTOUSDT", 
"MAGICUSDT", "MANAUSDT", "MANEKIUSDT", "MANTAUSDT", "MASAUSDT", "MASKUSDT", "MAVIAUSDT", "MAVUSDT", "MAXUSDT", "MBLUSDT", "MBOXUSDT", "MDTUSDT", "MEMEUSDT", "MERLUSDT", "METISUSDT", "MEWUSDT", "MINAUSDT", "MKRUSDT", "MNTUSDT", "MOBILEUSDT", "MOCAUSDT", 
"PAXGUSDT", "PENDLEUSDT", "PENGUSDT", "PEOPLEUSDT", "PERPUSDT", "PHAUSDT", "PHBUSDT", "PIRATEUSDT", "PIXELUSDT", "PIXFIUSDT", "POLUSDT", "POLYXUSDT", "PONKEUSDT", "POPCATUSDT", "PORTALUSDT", "POWRUSDT", "PRCLUSDT", "PROMUSDT", "PYTHUSDT", "QIUSDT", "QNTUSDT", "QTUMUSDT",
"TAIKOUSDT", "TAOUSDT", "THETAUSDT", "TIAUSDT", "TLMUSDT", "TNSRUSDT", "TOKENUSDT", "TOMIUSDT", "TONUSDT", "TRBUSDT", "TRUUSDT", "TRXUSDT", "TUSDT", "TWTUSDT", "UMAUSDT", "UNFIUSDT", "UNIUSDT", "UXLINKUSDT", "VANRYUSDT", 
"APEUSDT", "API3USDT", "APTUSDT", "ARBUSDT", "ARKMUSDT", "ARKUSDT", "ARPAUSDT", "ARUSDT", "ASTRUSDT", "ATAUSDT", "ATHUSDT", "ATOMUSDT", "AUCTIONUSDT", "AUDIOUSDT", "AVAILUSDT", "AVAXUSDT", "AXLUSDT", "AXSUSDT", "ORDIUSDT", "ORNUSDT", "OSMOUSDT", "OXTUSDT", 
"ENSUSDT", "EOSUSDT", "ETCUSDT", "ETHBTCUSDT", "ETHFIUSDT", "ETHUSDT", "ETHWUSDT", "FDUSDUSDT", "FILUSDT", "FIREUSDT", "FITFIUSDT", "FLMUSDT", "FLOWUSDT", "FLRUSDT", "FLUXUSDT", "FORTHUSDT", "FOXYUSDT", "FTMUSDT", "ZECUSDT", "ZENUSDT", "ZETAUSDT", "ZEUSUSDT", 
"JUPUSDT", "KASUSDT", "KAVAUSDT", "KDAUSDT", "KEYUSDT", "KLAYUSDT", "KNCUSDT", "KSMUSDT", "L3USDT", "LAIUSDT", "LDOUSDT", "LEVERUSDT", "LINAUSDT", "LINKUSDT", "LISTAUSDT", "LITUSDT", "LOOKSUSDT", 
"MONUSDT", "MOTHERUSDT", "MOVRUSDT", "MTLUSDT", "MYRIAUSDT", "MYROUSDT", "NEARUSDT", "NEIROETHUSDT", "NEOUSDT", "NFPUSDT", "NKNUSDT", "NMRUSDT", "NOTUSDT", "NTRNUSDT", "NULSUSDT", "NYANUSDT", "OGNUSDT", "OGUSDT", 				
"QUICKUSDT", "RADUSDT", "MOVRUSDT", "RAYDIUMUSDT", "RDNTUSDT", "REEFUSDT", "RENDERUSDT", "RENUSDT", "REQUSDT", "REZUSDT", "RIFUSDT", "RLCUSDT", "RONUSDT", "ROSEUSDT", "RPLUSDT", "RSRUSDT", "RSS3USDT", "RUNEUSDT", 				
"VELOUSDT", "VETUSDT", "VIDTUSDT", "VOXELUSDT", "VRAUSDT", "VTHOUSDT", "WAVESUSDT", "WAXPUSDT", "WIFUSDT", "WLDUSDT", "WOOUSDT", "WUSDT", "XAIUSDT", "XCHUSDT", "XCNUSDT", "XEMUSDT", "XLMUSDT", 				
"COREUSDT", "COSUSDT", "COTIUSDT", "CROUSDT", "CRVUSDT", "CTCUSDT", "CTKUSDT", "CTSIUSDT", "CVCUSDT", "CVXUSDT", "CYBERUSDT", "SUSHIUSDT", "SWEATUSDT", "SXPUSDT", "SYNUSDT", "SYSUSDT", 						
"FTNUSDT", "FUNUSDT", "FXSUSDT", "GALAUSDT", "GASUSDT", "GFTUSDT", "GLMRUSDT", "GLMUSDT", "GMEUSDT", "GMTUSDT", "GMXUSDT", "ZILUSDT", "ZKFUSDT", "ZKJUSDT", "ZKUSDT", "ZROUSDT", "ZRXUSDT", 					
"LPTUSDT", "LQTYUSDT", "LRCUSDT", "LSKUSDT", "LTCUSDT", "LTOUSDT", "LUNA2USDT", "GNOUSDT", "GODSUSDT", "GRTUSDT", "GTCUSDT", "GUSDT", "STRKUSDT", "STXUSDT", "SUIUSDT", "SUNDOGUSDT", "SUNUSDT", "SUPERUSDT", 
"OMGUSDT", "OMNIUSDT", "OMUSDT", "ONDOUSDT", "ONEUSDT", "ONGUSDT", "ONTUSDT", "OPUSDT", "ORBSUSDT", "ORCAUSDT", "ORDERUSDT",
"RVNUSDT", "SAFEUSDT", "SAGAUSDT", "SANDUSDT", "SCAUSDT", "SCRTUSDT", "SCUSDT", "SEIUSDT", "SFPUSDT", "SHIB1000USDT", "SILLYUSDT", "XMRUSDT", "XNOUSDT", "XRDUSDT", "XRPUSDT", "XTZUSDT", "XVGUSDT", "XVSUSDT", "YFIUSDT", "YGGUSDT", "ZBCNUSDT", 
"BRETTUSDT", "BSVUSDT", "BSWUSDT", "BTCUSDT", "C98USDT", "CAKEUSDT", "CELOUSDT", "CELRUSDT", "CETUSUSDT", "CFXUSDT", "CHESSUSDT", "CHRUSDT", "CHZUSDT", "CKBUSDT", "CLOUDUSDT", "COMBOUSDT", "COMPUSDT", "SKLUSDT", "SLERFUSDT", "SLFUSDT", "SLPUSDT", "SNTUSDT", "SNXUSDT", "SOLUSDT", "SPECUSDT", "SPELLUSDT", "SSVUSDT", "STEEMUSDT", "STGUSDT", "STMXUSDT", "STORJUSDT", "STPTUSDT"
]
  # Add your desired symbols