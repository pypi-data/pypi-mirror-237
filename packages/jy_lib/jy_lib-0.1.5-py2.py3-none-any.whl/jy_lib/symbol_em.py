# -*- coding: utf-8 -*-
"""东方财富代码"""
from .exchange import Exchange
from .symbol import (
    SymbolSubType, StockType, FundType, BondType, FuturesType,
    OptionsType, WarrantsType, IndexType, DrType, SpotType, SymbolFlag)
from typing import Dict, Tuple


def get_exchange_from_em(
        f13: int = None, f19: int = None, f111: int = None, f139: int = None, f148: int = None) \
        -> Tuple[Exchange, SymbolSubType, SymbolFlag]:
    """从东方财富市场信息解析交易所及标的品种类型等信息"""
    m: int = f13
    t: int = f19
    s: int = f111
    e: int = f139
    f: int = f148
    exchange: Exchange | None = None
    typ: SymbolSubType | None = None
    flg: SymbolFlag = SymbolFlag()

    if m in {0, 1}:
        if f & 2 ** 2:
            flg.is_st = True
        if f & 2 ** 3:
            flg.is_new = True
        if s & 2 ** 19:
            flg.is_approval = True
        if s & 2 ** 17:
            flg.is_registration = True
        if s & 2 ** 9:
            flg.is_innovation_market = True
        if s & 2 ** 8:
            flg.is_base_market = True
        if s & 2 ** 7:
            flg.is_call_auction = True
        if s & 2 ** 5:
            flg.is_market_making = True
        if s & 3:
            flg.is_pt = True

    if m == 0:
        exchange = Exchange.SZSE
        if t == 5:
            typ = IndexType.INDEX_OTHER
        elif t == 6:
            typ = StockType.STOCK_A
        elif t == 7:
            typ = StockType.STOCK_B
        elif t == 8:
            # [7, 9, 10, 11, 12, 13, 14, 15, 29]
            if e == 7:
                typ = BondType.BOND_OTHER         # 政府债
            elif e == 9:
                typ = BondType.BOND_ENTERPRISE
            elif e == 10:
                typ = BondType.BOND_COMPANY
            elif e == 11:
                typ = BondType.BOND_CONVERTIBLE
            elif e == 12:
                typ = BondType.BOND_EXCHANGEABLE
            elif e == 13:
                typ = BondType.BOND_ABS
            elif e == 14:
                typ = BondType.BOND_BUYBACK
            elif e == 15:
                typ = BondType.BOND_COMPANY       # 私募公司债
            elif e == 29:
                typ = StockType.STOCK_P
        elif t == 10:
            if e == 97:
                typ = FundType.FUND_REITS
        elif t == 80:
            typ = StockType.STOCK_G
        elif t == 81:
            if s & 2048:
                # 北证A股
                exchange = Exchange.BSE
                typ = StockType.STOCK_A
            else:
                exchange = Exchange.NEEQ
                typ = StockType.STOCK_OTHER
    elif m == 1:
        exchange = Exchange.SSE
        # if e == 15:
        #     return exchange, stype  # 新标准券
        # elif e == 34:
        #     return exchange, stype  # 申购
        # elif e == 36:
        #     return exchange, stype  # 配号
        # elif e == 37:
        #     return exchange, stype  # 认购款
        # elif e == 44:
        #     return exchange, stype  # 配债
        # elif e == 48:
        #     return exchange, stype  # 分红代码
        # elif e == 49:
        #     return exchange, stype  # 转托管代码
        if t == 1:
            typ = IndexType.INDEX_OTHER
        elif t == 2:
            typ = StockType.STOCK_A
        elif t == 3:
            typ = StockType.STOCK_B
        elif t == 4:
            # [7, 9, 10, 11, 12, 14, 15, 29, 34, 36, 37, 44, 99]
            if e == 7:
                typ = BondType.BOND_OTHER         # 政府债
            elif e == 9:
                typ = BondType.BOND_ENTERPRISE    # 一般企业债
            elif e == 10:
                typ = BondType.BOND_COMPANY       # 一般公司债
            elif e == 11:
                typ = BondType.BOND_CONVERTIBLE   # 可转债
            elif e == 12:
                typ = BondType.BOND_EXCHANGEABLE
            elif e == 14:
                typ = BondType.BOND_BUYBACK
            elif e == 29:
                typ = StockType.STOCK_P
            elif e == 99:
                pass    # 定向可转债 属于私募债
        elif t == 9:
            # [16, 17, 20, 23, 34, 37, 46, 47, 48, 49, 97]
            if e == 16:
                typ = FundType.FUND_ETF
            elif e == 17:
                typ = FundType.FUND_LOF
            elif e == 20:
                typ = FundType.FUND_BOND
            elif e == 23:
                typ = FundType.FUND_HYBRID
            elif e == 46:
                typ = FundType.FUND_OPEN    # 开放式
            elif e == 47:
                pass
            elif e == 97:
                typ = FundType.FUND_REITS
        elif t == 23:
            typ = StockType.STOCK_K
    elif m == 2:
        exchange = Exchange.CSI
        if t == 24:
            typ = IndexType.INDEX_OTHER
    elif m == 10:
        exchange = Exchange.SSE
        typ = OptionsType.OPTIONS_ETF
        if t == 173:
            flg.is_call = True
        elif t == 174:
            flg.is_put = True
    elif m == 12:
        exchange = Exchange.SZSE
        typ = OptionsType.OPTIONS_ETF
        if t == 178:
            flg.is_call = True
        elif t == 179:
            flg.is_put = True
    elif m == 128:
        exchange = Exchange.HKEX
        if t == 1:
            typ = StockType.STOCK_A   # 港股主板
        elif t == 2:
            typ = StockType.STOCK_A  # 港股主板
        elif t == 3:
            typ = StockType.STOCK_A   # 港股主板
        elif t == 4:
            typ = StockType.STOCK_G   # 港股创业板
        elif t == 5:
            typ = WarrantsType.WARRANTS_CBBC  # 港股牛熊证
        elif t == 6:
            typ = OptionsType.OPTIONS_STOCK   # 港股窝轮
        if s & 64:
            pass    # 人民币交易港股
        if s & 1:
            pass    # ADR
    if m in {124, 125, 305}:
        exchange = Exchange.HKEX
        typ = IndexType.INDEX_OTHER
    elif m == 101:
        exchange = Exchange.COMEX
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 102:
        exchange = Exchange.NYMEX
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 103:
        exchange = Exchange.CBOT
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 104:
        exchange = Exchange.SGX
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 105:
        exchange = Exchange.NASDAQ
        typ = StockType.STOCK_A
    elif m == 106:
        exchange = Exchange.NYSE
        typ = StockType.STOCK_A
    elif m == 107:
        exchange = Exchange.AMEX
        typ = StockType.STOCK_A
    elif m == 108:
        exchange = Exchange.NYBOT
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 109:
        exchange = Exchange.LME
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 110:
        exchange = Exchange.BMD
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 111:
        exchange = Exchange.TOCOM
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 112:
        exchange = Exchange.ICE
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 113:
        exchange = Exchange.SHFE
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 114:
        exchange = Exchange.DCE
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 115:
        exchange = Exchange.ZCE
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 116:
        # t = [0, 1, 2, 3, 4, 5, 6, 7]
        # e = [9, 10, 15]
        exchange = Exchange.HKEX
        if t == 0:
            pass
        elif t == 1:
            # e = [0, 8, 9, 10, 16, 17, 18]
            if e & 0:
                typ = FundType.FUND_ETF
            elif e & 8:
                typ = FundType.FUND_REITS
            elif e & 9:
                typ = FundType.FUND_OTHER
            elif e & 10:
                typ = FundType.FUND_ETF
            elif e & 16:
                typ = FundType.FUND_ETF
            elif e & 17:
                typ = FundType.FUND_BOND
            elif e & 18:
                typ = FundType.FUND_DERIVATIVES
        elif t == 2:
            if e & 4:
                typ = BondType.BOND_OTHER
        elif t == 3:
            # e = [0, 1, 2, 7]
            typ = StockType.STOCK_A
            if e & 2:
                typ = StockType.STOCK_P
        elif t == 4:
            typ = StockType.STOCK_G
        elif t == 5:
            typ = WarrantsType.WARRANTS_CBBC
            if s & 2:
                flg.is_call = True        # 牛证
            if s & 4:
                flg.is_put = True         # 熊证
        elif t == 6:
            typ = OptionsType.OPTIONS_STOCK
            if s & 2:
                flg.is_call = True        # 购
            if s & 4:
                flg.is_put = True         # 沽
        elif t == 7:
            typ = WarrantsType.WARRANTS_INLINE
    elif m == 118:
        exchange = Exchange.SGE
        typ = SpotType.SPOT_COMMODITY
    elif m == 139:
        exchange = Exchange.HKEX
        typ = OptionsType.OPTIONS_FOREX
    elif m == 140:
        exchange = Exchange.DCE
        typ = OptionsType.OPTIONS_COMMODITY
    elif m == 141:
        exchange = Exchange.ZCE
        typ = OptionsType.OPTIONS_COMMODITY
    elif m == 142:
        exchange = Exchange.INE
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 151:
        exchange = Exchange.SHFE
        typ = OptionsType.OPTIONS_COMMODITY
    elif m == 155:
        exchange = Exchange.LSE
        if t == 1:
            typ = StockType.STOCK_OTHER
        elif t == 2:
            typ = StockType.STOCK_P
        elif t == 3:
            typ = FundType.FUND_ETF
    elif m == 156:
        # s = [1, 5, 6, 7, 8]
        exchange = Exchange.LSE
        typ = DrType.DR_GDR
    elif m == 163:
        exchange = Exchange.INE
        typ = OptionsType.OPTIONS_COMMODITY
    elif m == 252:
        exchange = Exchange.SIX
        if t == 1:
            typ = DrType.DR_GDR
    elif m == 220:
        exchange = Exchange.CFFEX
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 221:
        exchange = Exchange.CFFEX
        typ = OptionsType.OPTIONS_INDEX
    elif m == 225:
        exchange = Exchange.GFEX
        typ = FuturesType.FUTURES_COMMODITY
    elif m == 226:
        exchange = Exchange.GFEX
        typ = OptionsType.OPTIONS_COMMODITY
    elif m == 242:
        exchange = Exchange.HKEX
        typ = FuturesType.FUTURES_INDEX
    elif m == 341:
        exchange = Exchange.LSE
        typ = IndexType.INDEX_OTHER

    return exchange, typ, flg


def get_exchange_from_em_record(record: Dict) -> Tuple[Exchange, SymbolSubType, SymbolFlag]:
    return get_exchange_from_em(f13=record['f13'], f19=record['f19'], f111=record['f111'], f148=record['f148'])
