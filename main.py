
from random import randint

class TravelAgency:
    __count_tips = 0
    __map_places = ["Istanbul", "Ankara", "Sochi", "Gelendzhik", "Denpasar", "Paris"]
    __degrees_of_comfort = [1, 2, 3, 4, 5]

    def set_tips_count(self, count):
        self.__count_tips = count

    def get_tip(self):
        place = self.__map_places[randint(0, len(self.__map_places) - 1)]
        degree_of_comfort = self.__degrees_of_comfort[randint(0, len(self.__degrees_of_comfort) - 1)]

        return [place, degree_of_comfort]

    def get_tips(self):
        all_tips = []
        for n in (range(self.__count_tips)):
            all_tips.append(self.get_tip())

        return all_tips

class Tourist:
    __tips = []

    def set_tips(self, tips):
        self.__tips = tips

    def get_choice(self):
        best_tip = self.__tips[0]
        for tip in self.__tips:
            if best_tip[1] < tip[1]:
                best_tip = tip
        
        return best_tip


def main():
    travel_agency = TravelAgency()
    tourist = Tourist()

    travel_agency.set_tips_count(10)
    travel_agency_tips = travel_agency.get_tips()

    tourist.set_tips(travel_agency_tips)

    print(tourist.get_choice())

if __name__ == '__main__':
    main()