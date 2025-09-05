class userData():
    def __init__(self, user_id:int, name:str, email_id:str, email_verified:bool, profile_icon:str):
        self.name = name
        self.email_id = email_id
        self.email_verified = email_verified
        self.profile_icon = profile_icon

    def get_data(self):
        return {
            "name": self.name,
            "email_id": self.email_id,
            "email_verified": self.email_verified,
            "profile_icon": self.profile_icon
        }