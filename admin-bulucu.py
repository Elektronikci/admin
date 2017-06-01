#!/usr/bin/env python
#-*-coding:utf-8-*-

from os import system
from requests import get, post
from re import findall
from sys import argv
from time import sleep

bold, underline, endcolor = "\033[1m", "\033[4m", "\033[0m"
green, blue, yellow, red = "\033[92m", "\033[94m", "\033[93m", "\033[91m"


admPath = ['admin', 'administrator', 'admin1', 'admin2', 'admin3', 'admin4', 'admin5', 'usuarios', 'usuario', 'administrator', 'moderator', 'webadmin', 'adminarea', 'bb-admin', 'adminLogin', 'admin_area', 'panel-administracion', 'instadmin', 'memberadmin', 'administratorlogin', 'adm', 'admin/account.php', 'admin/index.php', 'admin/login.php', 'admin/admin.php', 'admin/account.php', 'admin_area/admin.php', 'admin_area/login.php', 'siteadmin/login.php', 'siteadmin/index.php', 'siteadmin/login.html', 'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html', 'admin_area/index.php', 'bb-admin/index.php', 'bb-admin/login.php', 'bb-admin/admin.php', 'admin/home.php', 'admin_area/login.html', 'admin_area/index.html', 'admin/controlpanel.php', 'admin.php', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html', 'admin/account.html', 'adminpanel.html', 'webadmin.html', 'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'admin/admin_login.html', 'admin_login.html', 'panel-administracion/login.html', 'admin/cp.php', 'cp.php', 'administrator/index.php', 'administrator/login.php', 'nsw/admin/login.php', 'webadmin/login.php', 'admin/admin_login.php', 'admin_login.php', 'administrator/account.php', 'administrator.php', 'admin_area/admin.html', 'pages/admin/admin-login.php', 'admin/admin-login.php', 'admin-login.php', 'bb-admin/index.html', 'bb-admin/login.html', 'acceso.php', 'bb-admin/admin.html', 'admin/home.html', 'login.php', 'modelsearch/login.php', 'moderator.php', 'moderator/login.php', 'moderator/admin.php', 'account.php', 'pages/admin/admin-login.html', 'admin/admin-login.html', 'admin-login.html', 'controlpanel.php', 'admincontrol.php', 'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html', 'rcjakar/admin/login.php', 'adminarea/index.html', 'adminarea/admin.html', 'webadmin.php', 'webadmin/index.php', 'webadmin/admin.php', 'admin/controlpanel.html', 'admin.html', 'admin/cp.html', 'cp.html', 'adminpanel.php', 'moderator.html', 'administrator/index.html', 'administrator/login.html', 'user.html', 'administrator/account.html', 'administrator.html', 'login.html', 'modelsearch/login.html', 'moderator/login.html', 'adminarea/login.html', 'panel-administracion/index.html', 'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html', 'admincontrol/login.html', 'adm/index.html', 'adm.html', 'moderator/admin.html', 'user.php', 'account.html', 'controlpanel.html', 'admincontrol.html', 'panel-administracion/login.php', 'wp-login.php', 'adminLogin.php', 'admin/adminLogin.php', 'home.php', 'admin.php', 'adminarea/index.php', 'adminarea/admin.php', 'adminarea/login.php', 'panel-administracion/index.php', 'panel-administracion/admin.php', 'modelsearch/index.php', 'modelsearch/admin.php', 'admincontrol/login.php', 'adm/admloginuser.php', 'admloginuser.php', 'admin2.php', 'admin2/login.php', 'admin2/index.php', 'usuarios/login.php', 'adm/index.php', 'adm.php', 'affiliate.php', 'adm_auth.php', 'memberadmin.php', 'administratorlogin.php']


def logo():
    system("clear")
    print "--==["+bold+blue+"nickname"+endcolor+"] [ Elektronikçi / ExitStars"
    print "--==["+bold+yellow+"MyGitHub"+endcolor+"] [ http://github.com/ExitStars"
    print "--==["+bold+green+"software"+endcolor+"] [ apFinder / Admin Page Finder"
    print "-"*50

def apScan(domain):
    def roboScan(domain):
        print bold+yellow+"<< robots.txt Dosyasi Taraniyor >>".center(50)+endcolor
        try:
            payload = get("http://"+domain+"/robots.txt").text
            print bold+green+"[!] Asagida ki Listede, "+endcolor+red+"Disallow:"+bold+green+" yazan kisimlar olasi admin panelleridir.\n\n"+endcolor+payload
        except Exception as e:
            print bold+red+"[!-! Hata]"+endcolor, e

    def listScan(domain):
        print bold+yellow+"<< Liste Dosyasi Taraniyor >>".center(50)+endcolor
        for path in admPath:
            scode = get("http://"+domain+"/"+path).status_code
            if scode == 200:
                print bold+green+"[+] Olasi Admin Panel: "+endcolor+"http://"+domain+"/"+path
            elif scode == 302:
                print bold+blue+"[/] Yonlendirme Sayfasi: "+endcolor+"http://"+domain+"/"+path
            elif scode == 404:
                pass
            else:
                print "[?] ("+str(scode)+") Bilinmeyen Sayfa: "+"http://"+domain+"/"+path

    listScan(domain)
    roboScan(domain)



def main():
    logo()
    if len(argv) != 2:
        print "Hatali Giris"
    else:
        domain = argv[1].replace("http://", "").replace("https://", "").replace("www.", "")
        if domain.endswith("/"): domain = domain[:len(domain)-1]
        print bold+yellow+"Domain: "+endcolor+" "+domain
        sleep(2)
        apScan(domain)

if __name__ == '__main__':
    main()
