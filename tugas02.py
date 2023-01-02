from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://demoqa.com/webtables'

"""
Karena beberapa kali test, Google ads ini cukup merepotkan.
Kadang bisa kadang tidak jadinya, baik untuk menghapus / mengisi data.
Jadi ada tambahan experimental option untuk menghapus message :
'Chrome is being controlled by automated test software'
"""

opt = Options()
opt.add_experimental_option('excludeSwitches' , ['enable-logging' , 'enable-automation'])

driver = webdriver.Chrome(options=opt)
wait = WebDriverWait(driver,10)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get(url)

# Scroll down -- | Tujuannya agar hasil menghapus / mengisi data keliatan semua.
driver.execute_script('window.scrollTo(0, 80)') 


""" Menghapus record yang sudah ada """


tombolHapus = '//*[@id="delete-record-{}"]'
for jumlahBaris in range(1,4) :
    hapusXpath = tombolHapus.format(jumlahBaris)
    try : 
        # wait.until(EC.element_to_be_clickable((By.XPATH,hapusXpath)))
        driver.find_element(By.XPATH,hapusXpath ).click()
        print(f'Baris ke - {jumlahBaris} sudah dihapus.')
    except :
        print(f'Baris ke - {jumlahBaris} gagal dihapus.')
        pass
print('------------------------------')


""" Menambah record ke tabel """


tombolTambah = '//*[@id="addNewRecordButton"]'
formKosong = '//*[@id="{}"]'
tombolSubmit = '//*[@id="submit"]'
dbProfil = {
    'firstName'  : ['Test' , 'Test' , 'Test'] ,
    'lastName' : ['01' , '02' , '03'] ,
    'userEmail' : ['Test01@email.com' , 'Test02@email.com' , 'Test03@email.com'] , 
    'age' : [25,26,27] , 
    'salary' : [3000000,2500000,2000000] ,
    'department' : ['Marketing' , 'Finance and Accounting' , 'Customer Service' ]
}

for index in range(0,3) :
    driver.find_element(By.XPATH,tombolTambah).click()
    for kolom in dbProfil.keys() :
        kolomXpath = formKosong.format(kolom)
        try :
            # wait.until(EC.presence_of_element_located((By.XPATH,kolomXpath)))
            driver.find_element(By.XPATH ,kolomXpath ).send_keys(dbProfil[kolom][index])
        except :
            print('Terjadi kesalahan dalam memilih Locator')
            pass  
    driver.find_element(By.XPATH,tombolSubmit ).click()
    print(f'Nama {dbProfil["firstName"][index]} telah diinput.')