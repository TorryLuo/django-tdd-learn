from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitor(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()
        # pass

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪丝听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 她注意到网页的标题和头部都包含“To-Do” 这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用激请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Endter a to-do item')
        # 她在一个文本框中输入了“Buv peacock feathers”,伊迪丝的爱好是使用假蝇做饵钓鱼
        inputbox.send_keys('Buy peacock feathers')
        # ＃她按回车键后，页面更新了
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        # ＃待办事项表格中显示了
        # "1: Buy peacock feathers"
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [r.text for r in rows])

        # ＃页面中又显示了一个文本框，可以输人其他的待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        # ＃她输入了
        # “Use peacock feathers to make a flv
        # ＃伊迪丝做事很有条理
        # （使用孔雀羽毛做假蝇）
        # ＃ 页面再次更新，她的清单中显示了这两个待办事项
        inputbox.send_keys('Use peacock feathers to make a flv')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        # ＃伊迪丝想知道这个网站是否会记住她的清单
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('2: Use peacock feathers to make a flv', [r.text for r in rows])


        # ＃她看到网站为她牛成了一个唯一的URL
        # ＃ 而且页面中有一些文字解说这个功能
        # # 她访问那个URL.发现她的待办事项列表还在
        # ＃她很满意，去睡觉了
        # self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main(warnings='ignore')
