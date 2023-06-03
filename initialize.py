from db import db
from models import UserModel
from passlib.hash import pbkdf2_sha256




class FirstRecords():
    
    def role_register():
        user = {"name":"Admin"}
        is_found =  UserModel.query.filter(UserModel.username == user["username"]).first()
        if not is_found:
            user = UserModel(**user
            )
            db.session.add(user)
            db.session.commit()
            print('created user ok.')  


    def chechjk():
        user = {"name":"Ceyhun", "surname":"Tekkaya", "registration_number":"123456", "phone":"3123121212", "phone_extension_line":"0101", "mail":"ceyhun@genixo.ai", "code":"007", "username":"admin", "password":"123", "create_at":1685791783117, "update_at":None, 
                "delete_at":None, "active":True, "create_by":None, "update_by":None, "delete_by":None, "last_login":None, "last_login_ip":None, 
                "role_id":0, "hierarchy_id":0, "command_id":0, "command_collar_mark_id":0, "command_collar_mark_rank_id":0}
        is_found =  UserModel.query.filter(UserModel.username == user["username"]).first()
        if not is_found:
            user = UserModel(**user
            )
            db.session.add(user)
            db.session.commit()
            print('created user ok.')  


    

    def check():
        x=5
        #role_register()


    authority_list = [
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"KURMAY" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"PİYADE" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"SÜVARİ" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"TANK" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"TOPÇU" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"HAVA SAVUNMA" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"KARA HAVACILIK" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"İSTİHKAM" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"MUHABERE" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"İSTİHBARAT" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"ULAŞTIRMA" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"İKMAL" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"HARİTA" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"MUHİMMAT" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"BAKIM" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"PERSONEL" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"TABİB" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"ECZACI" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"KİMYAGER" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"DİŞ TABİBİ" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"VETERİNER HEKİM" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"MÜHENDİS" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"HAKİM" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"MALİYE" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"ÖĞRETMEN" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"BANDO" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"SAĞLIK" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"HARİTA TEKNİSYENİ" },
        {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"UÇAK VE HELİKOPTER TEKNİSYENİ" },
    ]
    authority_list_2 = [
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"ORGENERAL", "order":1, "type":"General", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"KORGENERAL", "order":2, "type":"General", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"TÜMGENERAL", "order":3, "type":"General", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"TUĞGENERAL", "order":4, "type":"General", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"ALBAY", "order":5, "type":"Subay", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"YARBAY", "order":6, "type":"Subay", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"BİNBAŞI", "order":7, "type":"Subay", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"YÜZBAŞI", "order":8, "type":"Subay", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"ÜSTEĞMEN", "order":9, "type":"Subay", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"TEĞMEN", "order":10, "type":"Subay", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"ASTEĞMEN", "order":11, "type":"Subay", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"Astsubay Kıdemli Başçavuş", "order":12, "type":"Astsubay", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"Astsubay Başçavuş", "order":13, "type":"Astsubay", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"Astsubay Kıdemli Üstçavuş", "order":14, "type":"Astsubay", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"Astsubay Üstçavuş", "order":15, "type":"Astsubay", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"Astsubay Kıdemli Çavuş", "order":16, "type":"Astsubay", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"Astsubay Çavuş", "order":17, "type":"Astsubay", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"Yedek Astsubay", "order":18, "type":"Astsubay", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"Uzman Çavuş", "order":19, "type":"Uzman Erbaş", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"Uzman Onbaşı", "order":20, "type":"Uzman Erbaş", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"Çavuş", "order":21, "type":"", "logo":""},
            {"komuta":"Kara Kuvvetleri Komutanlığı", "name":"Onbaşı", "order":22, "type":"", "logo":""}
        ]