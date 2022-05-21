from flask import jsonify, current_app
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from src.constants.user_const import ID, NAME, OBJECT_ID, PASSWORD, RANK, ROLE
from src.constants.common_const import ERROR, MESSAGE
from src.util.db_util import db


class Auth():
    def __init__(self):
        pass


    def register(self, request):
        try:
            pwd_hash = generate_password_hash(request.form[PASSWORD])
            user = {
                OBJECT_ID: request.form[ID],
                NAME: request.form[NAME],
                RANK: request.form[RANK],
                ROLE: request.form[ROLE],
                PASSWORD: pwd_hash
            }
            db_response = db.users.insert_one(user)
            current_app.logger.info("User created with ID: " + db_response.inserted_id)

            return jsonify ({MESSAGE: "User created with ID: " + str(db_response.inserted_id)}), HTTP_201_CREATED

        except Exception as ex:
            current_app.logger.error(ex)
            return jsonify ({MESSAGE: ERROR + str(ex)}), HTTP_409_CONFLICT


    def login(self, request):
        try:
            id = request.form[ID]
            password = request.form[PASSWORD]

            user = db.users.find_one({OBJECT_ID: id})
            if user:
                if check_password_hash(user[PASSWORD], password):
                    current_app.logger.info("Successful Login! by: " + id + " at " + str(datetime.now()))
                    return jsonify ({
                            MESSAGE: "Login successful",
                            NAME: user[NAME],
                            RANK: user[RANK],
                            ROLE: user[ROLE]
                        }), HTTP_200_OK
                else:
                    current_app.logger.info("Login Failed! Invalid password")
                    return jsonify ({MESSAGE: "Login Failed! Invalid password"}), HTTP_401_UNAUTHORIZED
            else:
                current_app.logger.info("Login Failed! No such user with ID: " + id)
                return jsonify ({MESSAGE: "Login Failed! No such user with ID: " + id}), HTTP_401_UNAUTHORIZED
        
        except Exception as ex:
            current_app.logger.error(ex)
            return jsonify ({MESSAGE: ERROR + str(ex)}), HTTP_400_BAD_REQUEST

    
    def get_all_users(self):
        try:
            all_users = list(db.users.find())
            users = []
            for user in all_users:
                tmp_user = {
                        ID: user[OBJECT_ID],
                        NAME: user[NAME],
                        RANK: user[RANK],
                        ROLE: user[ROLE]
                    }
                users.append(tmp_user)
            current_app.logger.info("Returning " + str(len(users)) + " users")
            return jsonify (users), HTTP_200_OK

        except Exception as ex:
            current_app.logger.error(ex)
            return jsonify ({MESSAGE: ERROR + str(ex)}), HTTP_400_BAD_REQUEST


    def update_rank(self, id, request):
        try:
            db_response = db.users.update_one(
                {OBJECT_ID: id},
                {"$set": {RANK:request.form[RANK]}}
            )

            if db_response.matched_count:
                current_app.logger.info("Rank updated successfully!")
                return jsonify ("Rank updated successfully!"), HTTP_200_OK
            else:
                current_app.logger.info("No such record to update!")
                return jsonify ("No such record to update!"), HTTP_400_BAD_REQUEST

        except Exception as ex:
            current_app.logger.error(ex)
            return jsonify ({MESSAGE: ERROR + str(ex)}), HTTP_400_BAD_REQUEST


    def delete_user(self, id):
        try:
            db_response = db.users.delete_one({OBJECT_ID: id})

            if db_response.deleted_count:
                current_app.logger.info("User deleted successfully!")
                return jsonify ("User deleted successfully!"), HTTP_200_OK
            else:
                current_app.logger.info("No such record to delete!")
                return jsonify ("No such record to delete!"), HTTP_400_BAD_REQUEST

        except Exception as ex:
            current_app.logger.error(ex)
            return jsonify ({MESSAGE: ERROR + str(ex)}), HTTP_400_BAD_REQUEST
