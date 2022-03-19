from Implementation import ProductsImplementation, VendorImplementation

if __name__ == '__main__':

    vendor = VendorImplementation.VendorImplementation()
    products = ProductsImplementation.ProductsImplementation()

    vendor.add_vendor('john', 'john07', 'jonnybones')
    vendor.login('john07', 'jonnybones')

    products.add_product("Lenovo Thinkpad", "Laptop", 40, 20000)
    products.add_product("Dell Inspiron", "Laptop", 40, 30000)
    products.add_product("Acer razor", "Laptop", 40, 25000)
    products.add_product("Asus Tinker", "Laptop", 40, 20000)
    products.add_product("Lenovo Gaming", "Laptop", 40, 20000)

    products.search_product_by_name("Lenovo Gaming")

    products.get_all_products()

    vendor.logout()