from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SEARCH_BUTTON = (By.NAME, "submit_search")
    SLIDER = (By.ID, "homeslider")
    TOP_CONTENT = (By.ID, "htmlcontent_top")
    HOME_CONTENT = (By.ID, "htmlcontent_home")
    CART_REMOVE = (By.CLASS_NAME, 'remove_link')
    SEARCH_BAR = (By.ID, 'search_query_top')
    CONTACT_US = (By.ID, 'contact-link')


class TopMenuLocators(object):
    WOMEN = (By.ID, "Women")
    DRESSES = (By.ID, "Dresses")
    T_SHIRTS = (By.ID, "T-shirts")


class Catalog(object):
    TOPS = (By.ID, "layered_category_4")
    DRESSES = (By.ID, "layered_category_8")
    SIZE_S = (By.ID, "layered_id_attribute_group_1")
    SIZE_M = (By.ID, "layered_id_attribute_group_2")
    SIZE_L = (By.ID, "layered_id_attribute_group_3")
    BEIGE = (By.ID, "layered_id_attribute_group_7")
    WHITE = (By.ID, "layered_id_attribute_group_8")
    BLACK = (By.ID, "layered_id_attribute_group_11")
    ORANGE = (By.ID, "layered_id_attribute_group_13")
    BLUE = (By.ID, "layered_id_attribute_group_14")
    GREEN = (By.ID, "layered_id_attribute_group_15")
    YELLOW = (By.ID, "layered_id_attribute_group_16")
    PINK = (By.ID, "layered_id_attribute_group_24")
    CASUAL = (By.ID, "layered_id_feature_11")
    DRESSY = (By.ID, "layered_id_feature_16")
    GIRLY = (By.ID, "layered_id_feature_13")
    STOCK = (By.ID, "layered_quantity_1")
    MANUFACTURER = (By.ID, "layered_manufacturer_1")
    NEW = (By.ID, "layered_condition_new")
    PRICE_RANGE = (By.ID, "layered_price_slider")


class SearchResultsLocators(object):
    SORT = (By.ID, "selectProductSort")
    GRID_VIEW = (By.ID, 'grid')
    LIST_VIEW = (By.ID, 'list')
    ADD_TO_CART = (By.CLASS_NAME, 'button ajax_add_to_cart_button btn btn-default')


class ShoppingCartLocators(object):
    REMOVE = (By.CLASS_NAME, 'cart_quantity_delete')


class CartPopupLocators(object):
    PROCEED = (By.CLASS_NAME, "btn btn-default button button-medium")
    CONTINUE = (By.CLASS_NAME, "continue btn btn-default button exclusive-medium")


class ContactLocators(object):
    SUBJECT = (By.ID, 'id_contact')
    ERROR = (By.CLASS_NAME, 'alert alert-danger')
    EMAIL = (By.ID, 'email')
    ATTACH_FILE = (By.ID, 'fileUpload')
    MESSAGE = (By.ID, 'message')
    SEND = (By.ID, 'submitMessage')


