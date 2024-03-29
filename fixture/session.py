class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element("name", "username").clear()
        wd.find_element("name", "username").send_keys(username)
        wd.find_element("name", "password").clear()
        wd.find_element("name", "password").send_keys(password)
        wd.find_element("xpath", "//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element("link text", "Logout").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements("link text", "Logout")) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def ensure_logout(self):
        if self.is_logged_in() > 0:
            self.logout()

    def ensure_login(self, username, password):
        if self.is_logged_in() > 0:
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(
            "xpath", "/html/body/table[1]/tbody/tr/td[1]/span[1]"
        ).text
