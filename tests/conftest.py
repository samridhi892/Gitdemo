import pytest
from selenium import webdriver

diver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="expecting chrome or edge"
    )


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise TypeError("Error")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    # return driver

    request.cls.driver = driver
    yield driver
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
