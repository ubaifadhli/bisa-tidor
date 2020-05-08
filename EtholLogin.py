import pytest
import time
import json
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

class EtholLogin():
    def startDriver(self):
        self.driver = webdriver.Chrome()
        #self.driver.set_window_size(800, 560)

        self.driver.get("https://ethol.pens.ac.id/")

    def getCredential(self):
        self.username = input("Masukkan username (username@it.student.pens.ac.id) : ")
        self.password = getpass.getpass(prompt='Masukkan password : ')

    def portalLogin(self):
        self.driver.find_element(By.LINK_TEXT, "Login").click()

        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys(self.username + "@it.student.pens.ac.id")

        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys(self.password)

        self.driver.find_element(By.NAME, "submit").click()

    def printCourseList(self):
        self.courseList = ["Bahasa Inggris Untuk Professional 2",
              "Kecerdasan Komputasional",
              "Pemrograman Lanjut",
              "Pengolahan Citra",
              "Workshop Administrasi & Manajemen Jaringan",
              "Workshop Pengembangan Perangkat Lunak",
              "Interaksi Manusia & Komputer",
              "Pemrograman Framework",
              "Praktikum Kecerdasan Komputasional",
              "Praktikum Pengolahan Citra",
              "Praktikum Pemrograman Lanjut"]

        print("")

        for i in range(len(self.courseList)):
            print(str(i + 1) + ". " + self.courseList[i])

    def getChosenCourse(self):
        print("")
        
        self.chosenCourse = int(input("Masukkan pilihan mata kuliah : "))
        self.carouselChosenCourse = int( ( (self.chosenCourse  - 1) / 3 ) + 1)

        
    def loadCourse(self):
        self.wait = WebDriverWait(self.driver, 10)

        self.carouselDotVar = ".VueCarousel-dot:nth-child(" + str(self.carouselChosenCourse) + ")"
        self.carouselSlideVar = ".VueCarousel-slide:nth-child(" + str(self.chosenCourse) + ") .v-btn__content"
        self.confRoomButtonVar = ".primary:nth-child(6)"
        
        self.element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.carouselDotVar)))
        self.driver.find_element(By.CSS_SELECTOR, self.carouselDotVar).click()
        
        self.element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.carouselSlideVar)))
        self.driver.find_element(By.CSS_SELECTOR, self.carouselSlideVar).click()

        time.sleep(3);
        self.element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.confRoomButtonVar)))
        self.driver.find_element(By.CSS_SELECTOR, self.confRoomButtonVar).click()

        #self.driver.find_element(By.CSS_SELECTOR, ".v-btn--block > .v-btn__content").click()

        self.wait = WebDriverWait(self.driver, 60)

        self.element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-bbb-listen")))
        self.driver.find_element(By.CSS_SELECTOR, ".icon-bbb-listen").click()

login = EtholLogin()
login.getCredential()
login.printCourseList()
login.getChosenCourse()
login.startDriver()
login.portalLogin()
login.loadCourse()
