import logging
from typing import Union

from .model import ShopModel, PartnerShopType

LOGGER = logging.getLogger(__name__)

"""
1、自营
a 有自营标识，店铺名称含企业购
b 有自营标识，店铺名称里含SKU在PCS的品牌，完全一致，店铺名称含旗舰店
c 有自营标识，店铺名称含旗舰店
d 有自营标识，店铺名称不含旗舰店

2、旗舰店
无自营标识，店铺名称里含旗舰店 就是旗舰店

3、专营店
其他都算专营店
    
4、其他
除了京东、天猫、苏宁，其他平台都显示其他
"""


def parse_shop(plat_code: str, shop_name: str, brand_name: str = None) -> Union[ShopModel, None]:
    """
    根据平台编码和店铺名称解析店铺类型
    有效链接返回ShopModel，无效链接返回None
    """
    _shop_type = ""
    # 京东、苏宁逻辑一样
    if plat_code == "jd" or plat_code == "suning":
        if "自营" in shop_name:
            _shop_type = "自营"

        elif "自营" not in shop_name and "旗舰店" in shop_name:
            _shop_type = "旗舰店"

        else:
            _shop_type = "专营店"
    # 天猫
    elif plat_code == "tmall":
        if "旗舰店" in shop_name:
            _shop_type = "旗舰店"
        else:
            _shop_type = "专营店"

    else:
        _shop_type = "其他"

    shop_model = build_model(plat_code=plat_code, shop_name=shop_name, shop_type=_shop_type)
    if shop_model.shop_type_code:
        return shop_model

    return None


def build_model(plat_code: str = None, shop_name: str = None, shop_type: str = None) -> Union[ShopModel, None]:
    shop_type_code = None
    shop_type_name = None
    shop_types = PartnerShopType.to_list()
    for _shop_type in shop_types:
        code = _shop_type.get("id", "")
        name = _shop_type.get("name", "")
        if shop_type == name:
            shop_type_name = name
            shop_type_code = code

    if "自营" in shop_name:
        is_self = "是"
    else:
        is_self = "否"

    shop_model = ShopModel()
    shop_model.plat_code = plat_code
    shop_model.shop_name = shop_name
    shop_model.shop_type_code = shop_type_code
    shop_model.shop_type_name = shop_type_name
    shop_model.is_self = is_self

    return shop_model
