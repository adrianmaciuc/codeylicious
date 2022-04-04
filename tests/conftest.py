import os

class Config:
    DRIVER_PATH = os.getcwd() + "\\resources"
    SS_FOLDER = os.getcwd() + "\\resources\\screenshots"
    BROWSER_TYPE = "Chrome"
    USERNAME = "user@phptravels.com"
    USERNAME_ADMIN = "admin@phptravels.com"
    PASSWORD = "demouser"
    PASSWORD_ADMIN = "demoadmin"
    REDIRECT_AFTER_LOGIN_PAGE = "https://www.phptravels.net/account/dashboard"

class Config2:
    DRIVER_PATH = os.getcwd() + "\\resources"
    BROWSER_TYPE = "Edge"
    USERNAME = "user@phptravels.com"
    PASSWORD = "demouser"
    REDIRECT_AFTER_LOGIN_PAGE = "https://www.phptravels.net/account/dashboard"