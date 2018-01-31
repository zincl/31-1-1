class dbsitems:
    def __init__(self,item, type, points,image,width,height,full_name):
        self.__item = item
        self.__type = type
        self.__points = points
        self.__image = image
        self.__width = width
        self.__height = height
        self.__full_name = full_name
        self.__maxquantity = 0
        self.__addtocartqty= 0
        self.__count = 0

    def get_item(self):
        return self.__item

    def get_type (self):
        return self.__type

    def get_points(self):
        return self.__points

    def get_maxquantity(self):
        return self.__maxquantity

    def get_image(self):
        return self.__image

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_full_name(self):
        return self.__full_name

    def get_count(self):
        return self.__count

    def set_item(self, item):
        self.__item = item

    def set_type(self, type):
        self.__type = type

    def set_points(self, points):
        self.__points = points

    def set_maxquantity(self, maxquantity):
        self.__maxquantity = maxquantity

    def set_image(self, image):
        self.__image = image

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def set_count(self, count):
        self.__count = count


    def addtocart(self):
            points = self.get_points

    def set_addtocartqty(self, addtocartqty):
        self.__addtocartqty = addtocartqty

    def get_addtocartqty(self):
        return self.__addtocartqty


class checkoutdbsitems(dbsitems):
    def __init__(self,item, type, points,image,width,height,full_name,quantity,totalpoints,position):
        super().__init__(item, type, points,image,width,height,full_name)
        self.__quantity = quantity
        self.__totalpoints = totalpoints
        self.__position = position
    def set_quantity(self,quantity):
        self.__quantity = quantity

    def set_totalpoints(self,totalpoints):
        self.__totalpoints = totalpoints

    def set_position(self,position):
        self.__position = position

    def get_quantity(self):
        return self.__quantity

    def get_totalpoints(self):
        return self.__totalpoints

    def get_position(self):
        return self.__position
 #   def totalitem_pts(self):
  #      return self.__points * self.__quantity
