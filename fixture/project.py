from selenium.webdriver.support.ui import Select


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element('xpath', '//input[@value="Create New Project"]').click()
        self.fill_project_form(project)
        self.open_manage_projects_page()

    def open_manage_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith('/manage_proj_page.php'):
            wd.find_element("link text", "Manage").click()
            wd.find_element('link text', 'Manage Projects').click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_text_field_value('name', project.name)
        self.change_dropdown_field_value('status', project.status)
        self.change_dropdown_field_value('view_state', project.view_status)
        self.change_text_field_value('description', project.description)
        wd.find_element('xpath', '(//input[@value="Add Project"])').click()

    def change_text_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element('name', field_name).click()
            wd.find_element('name', field_name).clear()
            wd.find_element('name', field_name).send_keys(text)

    def change_dropdown_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            Select(wd.find_element('name', field_name)).select_by_visible_text(
                value)

    def delete_project_by_index(self, name):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element('link text', name).click()
        wd.find_element('xpath', '//input[@value="Delete Project"]').click()
        wd.find_element('xpath', '//input[@value="Delete Project"]').click()