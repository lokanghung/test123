from results import make_error_result

# #給unregister API使用的error
# e2001 = make_error_result("e2001","此客戶名字不存在")

#給add_review API使用的error
e1001 = make_error_result("e1001","restaurant_id不存在")
e1002 = make_error_result("e1002","rating需介於1~5之間")
e1003 = make_error_result("e1003","comment需<=45個字")
# #給get_product API使用的error
# e2001 = make_error_result("e2001","product_id不存在")

# #給update API使用的error
# e3001 = make_error_result("e3001","product_id不存在")
# e3002 = make_error_result("e3002","price必須大於0")

# #給delete API使用的error
# e4001 = make_error_result("e4001","product_id不存在")