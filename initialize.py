from project.models.constant.authority import AuthorityModel
from project.models.person.user_authority import UserAuthorityModel
from setting.db import db
from project.models.constant.role import RoleModel
from project.models.constant.hierarchy import HierarchyModel
from project.models.constant.command import CommandModel
from project.models.constant.command_collar_mark import CommandCollarMarkModel
from project.models.constant.command_collar_mark_rank import CommandCollarMarkRankModel

from project.models.person.user import UserModel
from passlib.hash import pbkdf2_sha256


class FirstRecords:
    def __init__(self, status):
        pass

    def check():
        hierarchy_data = {"name": "Hierarchy 1", "hierarchical_order": 1}
        is_found = HierarchyModel.query.filter(HierarchyModel.name == hierarchy_data["name"]).first()
        if not is_found:
            hierarchy = HierarchyModel(**hierarchy_data)
            db.session.add(hierarchy)
            db.session.flush()
            db.session.commit()

        command_data = {"name": "Kara Kuvvetleri", "hierarchical_order": 1}
        command_id = 0
        is_found = CommandModel.query.filter(CommandModel.name == command_data["name"]).first()
        if not is_found:
            command = CommandModel(**command_data)
            db.session.add(command)
            db.session.flush()
            db.session.commit()
            command_id = command.id

        command_coolar_mark_data = {"name": "Kurmay", "hierarchical_order": 1, "command_id": command_id}
        command_coolar_mark_id = 0
        is_found = CommandCollarMarkModel.query.filter(
            CommandCollarMarkModel.name == command_coolar_mark_data["name"]).first()
        if not is_found:
            ommand_coolar_mark = CommandCollarMarkModel(**command_coolar_mark_data)
            db.session.add(ommand_coolar_mark)
            db.session.flush()
            db.session.commit()
            command_coolar_mark_id = ommand_coolar_mark.id

        command_coolar_mark_rank_data = {"name": "Subay", "hierarchical_order": 1,
                                         "command_collar_mark_id": command_coolar_mark_id}
        is_found = CommandCollarMarkRankModel.query.filter(
            CommandCollarMarkRankModel.name == command_coolar_mark_rank_data["name"]).first()
        if not is_found:
            command_coolar_mark_rank = CommandCollarMarkRankModel(**command_coolar_mark_rank_data)
            db.session.add(command_coolar_mark_rank)
            db.session.flush()
            db.session.commit()

        authorities = ["TRACK_ANOMALY", "TRACK_CAMERA", "OPERATION_ANOMALY", "OPERATION_CAMERA", "UPSERT_DRAWING",
                       "UPSERT_ROLE"]
        for authority in authorities:
            is_found_role = AuthorityModel.query.filter(AuthorityModel.name == authority).first()
            if not is_found_role:
                authority_data = {
                    "name": authority,
                    "description": authority,
                    "hierarchy_id": 1,
                    "status": 1,
                    "created_by": 1
                }
                new_authority = AuthorityModel(**authority_data)
                db.session.add(new_authority)
                db.session.commit()
        role_id = 1
        roles = ["ROLE_1", "ROLE_2", "ROLE_3"]
        for role in roles:
            is_found_role = RoleModel.query.filter(RoleModel.name == role).first()
            if not is_found_role:
                role_data = {
                    "name": role,
                    "description": role,
                    "status": 1,
                    "created_by": 1
                }
                new_role = RoleModel(**role_data)
                db.session.add(new_role)
                db.session.flush()
                db.session.commit()
                role_id = new_role.id
                print(role_id)

        user_data = {"name": "Admin", "surname": "Admin",
                     "username": "admin", "password": "admin",
                     "role_id": 1,
                     "hierarchy_id": 1,
                     "command_id": 1,
                     "command_collar_mark_id": 1,
                     "command_collar_mark_rank_id": 1
                     }
        is_found = UserModel.query.filter(UserModel.username == user_data["username"]).first()
        if not is_found:
            user_data["password"] = pbkdf2_sha256.hash(user_data["password"])
            user = UserModel(**user_data)
            db.session.add(user)
            db.session.flush()
            db.session.commit()
            user_id = user.id

        user_id = 1
        authorityList = db.session.query(AuthorityModel)
        for auth in authorityList:
            is_found = db.session.query(UserAuthorityModel).filter(
                UserAuthorityModel.user_id == user_id, UserAuthorityModel.authority_id == auth.id).all()
            if not is_found:
                user_auth_data = {"user_id": 1,
                                  "authority_id": auth.id,
                                  "authority_type": "type",
                                  "status": 1,
                                  "created_by": 1
                                  }
                user_auth = UserAuthorityModel(**user_auth_data)
                db.session.add(user_auth)
                db.session.flush()
                db.session.commit()


    def check2():
        pass

    authority_list = [
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "KURMAY"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "PİYADE"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "SÜVARİ"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "TANK"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "TOPÇU"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "HAVA SAVUNMA"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "KARA HAVACILIK"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "İSTİHKAM"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "MUHABERE"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "İSTİHBARAT"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "ULAŞTIRMA"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "İKMAL"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "HARİTA"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "MUHİMMAT"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "BAKIM"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "PERSONEL"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "TABİB"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "ECZACI"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "KİMYAGER"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "DİŞ TABİBİ"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "VETERİNER HEKİM"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "MÜHENDİS"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "HAKİM"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "MALİYE"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "ÖĞRETMEN"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "BANDO"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "SAĞLIK"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "HARİTA TEKNİSYENİ"},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "UÇAK VE HELİKOPTER TEKNİSYENİ"},
    ]
    authority_list_2 = [
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "ORGENERAL", "order": 1, "type": "General", "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "KORGENERAL", "order": 2, "type": "General", "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "TÜMGENERAL", "order": 3, "type": "General", "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "TUĞGENERAL", "order": 4, "type": "General", "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "ALBAY", "order": 5, "type": "Subay", "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "YARBAY", "order": 6, "type": "Subay", "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "BİNBAŞI", "order": 7, "type": "Subay", "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "YÜZBAŞI", "order": 8, "type": "Subay", "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "ÜSTEĞMEN", "order": 9, "type": "Subay", "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "TEĞMEN", "order": 10, "type": "Subay", "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "ASTEĞMEN", "order": 11, "type": "Subay", "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "Astsubay Kıdemli Başçavuş", "order": 12, "type": "Astsubay",
         "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "Astsubay Başçavuş", "order": 13, "type": "Astsubay",
         "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "Astsubay Kıdemli Üstçavuş", "order": 14, "type": "Astsubay",
         "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "Astsubay Üstçavuş", "order": 15, "type": "Astsubay",
         "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "Astsubay Kıdemli Çavuş", "order": 16, "type": "Astsubay",
         "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "Astsubay Çavuş", "order": 17, "type": "Astsubay",
         "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "Yedek Astsubay", "order": 18, "type": "Astsubay",
         "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "Uzman Çavuş", "order": 19, "type": "Uzman Erbaş",
         "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "Uzman Onbaşı", "order": 20, "type": "Uzman Erbaş",
         "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "Çavuş", "order": 21, "type": "", "logo": ""},
        {"komuta": "Kara Kuvvetleri Komutanlığı", "name": "Onbaşı", "order": 22, "type": "", "logo": ""}
    ]
