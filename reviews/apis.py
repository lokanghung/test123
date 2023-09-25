from flask import Blueprint, request, json, g
from dacite import from_dict
from dacite_config import config
from reviews import dataclasses, datahelper, errors
from results import make_data_result

blueprint = Blueprint("reviews", import_name = "reviews")


@blueprint.route('', methods=["POST"])
def add_review():
    #1. 解析JSON或參數
    x = json.loads(request.data)
    obj = from_dict(dataclasses.AddReview, x, config=config)
    #2. 驗證資料
    #2.1. restaurant_id是否存在
    if datahelper.is_restaurant_id_existed(obj.restaurant_id) == False:
        return json.jsonify(errors.e1001)
    #2.2. rating介於1~5之間
    if obj.rating < 1 or obj.rating > 5:
        return json.jsonify(errors.e1002)
    #2.3. comment<=45個字
    if obj.comment != None and len(obj.comment) > 45:
        return json.jsonify(errors.e1003)

    #3. 建立review
    #3.1. 建立review
    s = datahelper.create_review(obj.restaurant_id, obj.rating, obj.comment)
    #3.2. 提交
    g.cursor().connection.commit()
    #4. 回傳review
    return json.jsonify(make_data_result(s))




# @blueprint.route('', methods=["GET"])
# def get_products():
#     #1. 解析JSON或參數
#     #2. 驗證資料
#     #3. 取得產品
#     s = datahelper.get_products()
#    #4. 回傳產品
#     return json.jsonify(make_data_result(s))

# @blueprint.route('/<product_id>', methods=["GET"])
# def get_product(product_id):
#     #1. 解析JSON或參數
#     #1.1. 解析product_id為int
#     try:
#         product_id = int(product_id)
#     except:
#         pass

#     #2. 驗證資料
#     #2.1. 驗證product_id是否存在
#     if  isinstance(product_id, int) == False or \
#           datahelper.is_product_id_existed(product_id) == False:
#         return json.jsonify(errors.e2001)
#     #3. 取得產品
#     s = datahelper.get_product(product_id)
#    #4. 回傳產品
#     return json.jsonify(make_data_result(s))

# @blueprint.route('/<product_id>', methods=["PUT"])
# def update_product(product_id):
#     #1. 解析JSON或參數
#     #1.1. 解析JSON
#     x = json.loads(request.data)
#     obj = from_dict(dataclasses.UpdateProduct, x, config=config)
#     #1.2. 解析product_id為int
#     try:
#         product_id = int(product_id)
#     except:
#         pass

#     #2. 驗證資料
#     #2.1. 驗證product_id是否存在
#     if  isinstance(product_id, int) == False or \
#           datahelper.is_product_id_existed(product_id) == False:
#         return json.jsonify(errors.e3001) 
#     #2.2. 價格必須大於0
#     if obj.price < 0:
#         return json.jsonify(errors.e3002)
#     #3. 更新產品
#     #3.1. 更新產品
#     s = datahelper.update_product(product_id, obj.name, obj.price)
#     #3.2. 提交
#     g.cursor().connection.commit()
#    #4. 回傳產品
#     return json.jsonify(make_data_result(s))

# @blueprint.route('<product_id>', methods=["DELETE"])
# def delete_product(product_id):
    #1. 解析JSON
    #1.1. 解析product_id為int
    # try:
    #     product_id = int(product_id)
    # except:
    #     pass
    # #2. 驗證資料
    # #2.1. 驗證product_id是否存在
    # if  isinstance(product_id, int) == False or \
    #       datahelper.is_product_id_existed(product_id) == False:
    #     return json.jsonify(errors.e4001) 
    # #3. 刪除資料
    # #3.1. 刪除資料
    # success = datahelper.delete_product(product_id)
    # #3.2. 提交
    # g.cursor().connection.commit()
    # #4. 回傳是否成功刪除
    # return json.jsonify(make_data_result({"success":success}))