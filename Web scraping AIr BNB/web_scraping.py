from bs4 import BeautifulSoup
import requests


class WebScraping:
    def __init__(self, url):
        self.url = url
        self.soup = self.get_html()

    def get_html(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, "html.parser")
        return soup

    def get_rooms(self):
        return self.soup.find_all("div", class_="_1e9w8hic")

    def get_subtitle(self, room):
        return room.find("div", class_="mj1p6c8 dir dir-ltr").text

    def get_title(self, room):
        return room.find("span", class_="ts5gl90 tl3qa0j t1nzedvd dir dir-ltr").text

    def get_attrs(self, room):
        attr_room = {}
        details = room.find("div", class_="i1wgresd dir dir-ltr")
        attrs = details.find_all("span", class_="mp2hv9t dir dir-ltr")
        for attr in attrs:
            attr_info = attr.text.split()
            attr_room[f"{attr_info[1][:3]}"] = attr_info[0]
            return attr_room

    def get_price(self, room_html):
        return room_html.find("div", class_="p1qe1cgb dir dir-ltr").find("span", class_="_tyxjp1").text[2:]

    def pick_all_rooms(self):
        for room in self.get_rooms():
            list_of_rooms = []
            room_info = {}

            room_info["Title"] = self.get_title(room)
            room_info["Subtitle"] = self.get_subtitle(room)
            room_info["Price per night (R$) "] = self.get_price(room)
            attrs = self.get_attrs(room)
            room_info["Guests"] = attrs.get ("hós", None )
            room_info["Bedrooms"] = attrs.get("qua", None)
            room_info["Beds"] = attrs.get("cam", None)
            room_info["Bathrooms"] = attrs.get ("ban", None)

            list_of_rooms.append(room_info)

        return list_of_rooms
