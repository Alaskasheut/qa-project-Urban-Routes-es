import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_solicitude = (By.XPATH, ".//button[@class='button round']")
    tariff = (By.CSS_SELECTOR, "img[alt = 'Comfort']")
    picker_tariff = (By.XPATH,"/html/body/div/div/div[3]/div[3]/div[2]/div[1]/div[5]")
    phone_section = (By.XPATH, ".//div[@class='np-text']")
    input_phone = (By.XPATH, ".//input[@id='phone']")
    next_button_phone = (By.XPATH, ".//button[@class='button full']")
    code_box = (By.CSS_SELECTOR, "[placeholder = 'xxxx']")
    submit_code = (By.XPATH,".//div[@class = 'section active']//button[@class='button full']")
    payment_section = (By.CLASS_NAME,'pp-value')
    plus_card_section = (By.CLASS_NAME,'pp-plus-container')
    card_input = (By.CSS_SELECTOR, "input[placeholder='1234 4321 1408']")
    code_input = (By.CSS_SELECTOR,"input[placeholder = '12']")
    space = (By.CSS_SELECTOR,"div[class='plc']")
    adding_card = (By.XPATH, ".//div[@class='pp-buttons']//button[@class='button full']")
    added_card = (By.CSS_SELECTOR,"label[for='card-1']")
    closing_payment_method = (By.XPATH,".//div[@class='payment-picker open']//button[@class='close-button section-close']")
    message_box = (By.CSS_SELECTOR,"input[placeholder='Traiga un aperitivo']")
    manta_panuelo = (By.CLASS_NAME,'r-sw')
    icecream_counter = (By.XPATH,".//div[@class='r r-type-group']//div[@class='counter-plus']")
    counter_icecream_value = (By.XPATH, ".//div[@class='counter-value']")
    ask_travel = (By.CLASS_NAME,'smart-button-main')
    order_body = (By.CLASS_NAME, 'order-body')
    order_number =(By.CLASS_NAME,'order-number')
    order_looking_time = (By.CLASS_NAME,'order-header-time')
    order_title = (By.CLASS_NAME,'order-header-title')
    def __init__(self, driver):
        self.driver = driver

    def wait(self,element_visibility):
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(element_visibility))

    def scroll_screen(self,position):
        element = self.driver.find_element(position)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def set_from(self, from_address):
        self.wait(self.from_field)
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.wait(self.to_field)
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def ask_taxi(self):
        self.wait(self.taxi_solicitude)
        self.driver.find_element(*self.taxi_solicitude).click()

    def select_tariff(self):
        self.wait(self.tariff)
        self.driver.find_element(*self.tariff).click()

    def click_phone_section(self):
        self.wait(self.phone_section)
        self.driver.find_element(*self.phone_section).click()

    def fill_phone_input(self,phone_input):
        self.wait(self.input_phone)
        self.driver.find_element(*self.input_phone).send_keys(phone_input)

    def click_next_button_phone(self):
        self.wait(self.next_button_phone)
        self.driver.find_element(*self.next_button_phone).click()

    def get_phone(self):
        return self.driver.find_element(*self.input_phone).get_property('value')

    def set_number_phone(self, number_phone):
        self.click_phone_section()
        self.fill_phone_input(number_phone)
        self.click_next_button_phone()
    def set_code_confirmation(self, given_code):
        self.fill_confirmation_code(given_code)
        self.click_submit_code_confirmation()
    def fill_confirmation_code(self, confirmation_code):
        self.wait(self.code_box)
        self.driver.find_element(*self.code_box).send_keys(confirmation_code)

    def click_submit_code_confirmation(self):
        self.driver.find_element(*self.submit_code).click()

    def click_payment_section(self):
        self.driver.find_element(*self.payment_section).click()

    def click_add_card(self):
        self.driver.find_element(*self.plus_card_section).click()

    def fill_number_card_input(self,number_card):
        self.wait(self.card_input)
        self.driver.find_element(*self.card_input).send_keys(number_card)

    def fill_number_code_input(self,code_card):
        self.driver.find_element(*self.code_input).send_keys(code_card)

    def get_confirmation_code(self):
        return self.driver.find_element(*self.code_box).get_property('value')

    def get_number_card(self):
        return self.driver.find_element(*self.card_input).get_property('value')

    def get_code_card(self):
        return self.driver.find_element(*self.code_input).get_property('value')

    def click_space_card(self):
        self.driver.find_element(*self.space).click()

    def click_adding_card(self):
        self.driver.find_element(*self.adding_card).click()

    def select_added_card(self):
        self.driver.find_element(*self.added_card).click()

    def close_payment_methods(self):
        self.driver.find_element(*self.closing_payment_method).click()

    def set_payment_method(self,card_numbers,code_numbers):
        self.click_payment_section()
        self.click_add_card()
        self.fill_number_card_input(card_numbers)
        self.fill_number_code_input(code_numbers)
        self.click_space_card()
        self.click_adding_card()
        self.select_added_card()
        self.close_payment_methods()

    def write_in_message_box(self,letters):
        element = self.driver.find_element(*self.message_box)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element(*self.message_box).send_keys(letters)

    def get_written_message(self):
        return self.driver.find_element(*self.message_box).get_property('value')

    def switch_manta_panuelos(self):
        self.driver.find_element(*self.manta_panuelo).click()

    def click_plus_icecream(self):
        self.driver.find_element(*self.icecream_counter).click()

    def get_number_counter_icecream(self):
        return self.driver.find_element(*self.counter_icecream_value).text

    def click_ask_travel(self):
        self.driver.find_element(*self.ask_travel).click()
        self.wait(self.order_body)

    def get_text_ask_taxi_main_button(self):
        return self.driver.find_element(*self.ask_travel).text

    def is_taxi_order_displayed(self):
        if self.driver.find_element(*self.order_body).is_displayed():
            value = 'True'
        else:
            value = 'False'
        return value

    def is_order_number_displayed(self):
        if self.driver.find_element(*self.order_number).is_displayed():
            value = 'True'
        else:
            value = 'False'
        return value

    def is_order_looking_time_displayed(self):
        if self.driver.find_element(*self.order_looking_time).is_displayed():
            value = 'True'
        else:
            value = 'False'
        return value

    def get_information_travel_header_text(self):
        return self.driver.find_element(*self.order_title).text

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_comfort_tariff_selected(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.ask_taxi()
        routes_page.select_tariff()

    def test_add_number_phone(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.set_number_phone(phone_number)
        phone_registered = routes_page.get_phone()
        code_confirmation = retrieve_phone_code(self.driver)
        routes_page.set_code_confirmation(code_confirmation)
        actual_confirmation_code = routes_page.get_confirmation_code()
        time.sleep(3)
        assert phone_registered == phone_number
        assert code_confirmation == actual_confirmation_code
    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        routes_page.set_payment_method(card_number,card_code)
        actual_number_card = routes_page.get_number_card()
        actual_code_card = routes_page.get_code_card()
        time.sleep(3)
        assert actual_number_card == card_number
        assert actual_code_card == card_code
    def test_write_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        message = data.message_for_driver
        routes_page.write_in_message_box(message)
        written_message = routes_page.get_written_message()
        assert written_message == message
    def test_switch_on_mantas_panuelos(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.switch_manta_panuelos()
    def test_add_2_icecreams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_plus_icecream()
        routes_page.click_plus_icecream()
        counter = routes_page.get_number_counter_icecream()
        assert counter == '2'

    def test_confirm_ask_taxi_modal(self):
        routes_page = UrbanRoutesPage(self.driver)
        button_text = routes_page.get_text_ask_taxi_main_button()
        routes_page.click_ask_travel()
        answer = routes_page.is_taxi_order_displayed()
        assert button_text == 'Pedir un taxi'
        assert answer == 'True'


    def test_travel_information_is_displayed(self):
        routes_page = UrbanRoutesPage(self.driver)
        looking_time = routes_page.is_order_looking_time_displayed()
        time.sleep(40)
        number_car_displayed = routes_page.is_order_number_displayed()
        travel_information = routes_page.get_information_travel_header_text()
        assert looking_time == 'True'
        assert number_car_displayed == 'True'
        assert travel_information != ''

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()