class allredemption:
    def __init__(self, user,date, bank_card, card_no, full_name,qty, redeemed_pt):
        self.__user = user
        self.__date = date
        self.__bank_card = bank_card
        self.__card_no = card_no
        self.__full_name = full_name
        self.__qty = qty
        self.__redeemed_pt = redeemed_pt

    def get_user(self):
        return self.__user

    def get_date(self):
        return self.__date

    def get_bank_card(self):
        return self.__bank_card

    def get_card_no(self):
        return self.__card_no

    def get_full_name(self):
        return self.__full_name

    def get_qty(self):
        return self.__qty

    def get_redeemed_pt(self):
        return self.__redeemed_pt

    def set_user(self,user):
        self.__user = user
    def set_date(self, date):
        self.__date = date

    def set_bank_card(self, bank_card):
        self.__bank_card = bank_card

    def set_card_no(self, card_no):
        self.__card_no = card_no

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def set_qty(self,qty):
        self.__qty = qty

    def set_redeemed_pt(self,redeemed_pt):
        self.__redeemed_pt = redeemed_pt

