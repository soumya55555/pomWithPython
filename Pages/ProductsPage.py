from Test.BaseTest import BaseTest
class ProductPage(BaseTest):
    link_catalog_xpath = "(//a[contains(@href,'#')])[3]"
    link_Products_xpath="//span[text()='Products']"
    text_toVerify_Title_xpath="//h1[contains(text(),'Products')]"
    products_table_rows="//table/tbody/tr"
    products_table_column_productsName= "//table/tbody/tr/td[3]"

    def __init__(self,driver):
        self.driver=driver

    def clickonLinkCatalog(self):
        self.driver.find_element_by_xpath(self.link_catalog_xpath).click()
    def clickonLinkProduct(self):
        self.driver.find_element_by_xpath(self.link_Products_xpath).click()

    def verifyTitle(self):
        element1=self.driver.find_element_by_xpath(self.text_toVerify_Title_xpath)
        if element1.is_displayed():
            print("Product title was verified successfully")
        else:
            print("Product title was not  verified successfully")

    def getAllTheProductsDetails(self):
        num_of_rows=self.driver.find_elements_by_xpath("products_table_rows")
        num_of_cols=self.driver.find_elements_by_xpath("products_table_column_productsName")
        for row in num_of_rows:
            for col in num_of_cols:
                print(col.text)


