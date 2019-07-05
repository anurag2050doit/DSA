import datetime


class User(object):

    def __init__(self, name, desc=None):
        self.name = name
        self.desc = desc
        self.trips = []
        self.vehicle = None
        self.offering_ride = False

    def add_vehicle(self, vehicle):
        self.vehicle = vehicle

    def add_trip(self, trip):
        self.trips.append(trip)

    def get_all_trip(self):
        return self.trips

    def remove_trip(self, trip):
        if trip in self.trips:
            self.trips.pop(trip)
        else:
            return 'Invalid Trip'

    def __str__(self):
        return self.name


class Vehicle(object):

    def __init__(self, name, model=None, company=None):
        self.name = name
        self.model = model
        self.company = company

    def __str__(self):
        return self.name


class Trip(object):

    def __init__(self, origin, destination, start_time=None, duration=None):
        self.origin = origin
        self.destination = destination
        if not start_time:
            self.start_time = datetime.datetime.now()
        else:
            self.start_time = start_time
        if not duration:
            self.duration = datetime.timedelta(hours=1)
        else:
            self.duration = duration

    def __str__(self):
        return self.origin + ' ' + self.destination


class Ride(object):

    def __init__(self):
        self.users = []

    def add_user(self, name, vehicle, host=False, desc=None):
        vehicle = Vehicle(vehicle['name'], vehicle.get('model'), vehicle.get('company'))
        user = User(name, desc)
        user.add_vehicle(vehicle)
        if host:
            user.offering_ride = True
        self.users.append(user)

    def _get_riders(self):
        return [user for user in self.users if not user.offering_ride]

    def _get_hosts(self):
        return [user for user in self.users if user.offering_ride]

    def _check_user_vehicle(self, user_name, vehicle_name):
        for user in self._get_hosts():
            if user.name == user_name and user.vehicle.name == vehicle_name:
                return user

    def _check_user(self, user_name):
        for user in self._get_riders():
            if user.name == user_name:
                return user

    def _get_user_of_same_route(self, origin, destination):
        valid_users = []
        for user in self._get_hosts():
            for trip in user.trips:
                if trip.origin == origin and trip.destination == destination:
                    valid_users.append(user)
        return valid_users

    @staticmethod
    def _get_user(users, parameter):
        best_user = users[0]
        if parameter == 'shortest':
            best_trip = users[0].trips[0].duration
            for user in users:
                for trip in user.get_all_trip():
                    if trip.duration < best_trip:
                        best_user = user
        elif parameter == 'earliest':
            earliest_time = users[0].trips[0].start_time + users[0].trips[0].duration
            for user in users:
                for trip in user.get_all_trip():
                    total_time = trip.start_time + trip.duration
                    if total_time < earliest_time:
                        best_user = user

        return best_user

    def offer_ride(self, user_name, vehicle_name, origin, destination, start_time=None, duration=None):
        user = self._check_user_vehicle(user_name, vehicle_name)
        if user:
            trip = Trip(origin, destination, start_time, duration)
            user.add_trip(trip)

    def select_ride(self, user_name, origin, destination, parameter='shortest'):
        if self._check_user(user_name):
            users = self._get_user_of_same_route(origin, destination)
            if users:
                user = self._get_user(users, parameter)
                return user
            else:
                return 'Sorry no user is available for this route'


if __name__ == '__main__':
    ride = Ride()
    ride.add_user('anurag', {'name': 'SUV'}, True)
    ride.add_user('rahul', {'name': 'SUV'}, False)
    ride.add_user('aman', {'name': 'SUV'}, True)
    current_time = datetime.datetime.now()
    ride.offer_ride('anurag', 'SUV', 'kanpur', 'lucknow', current_time + datetime.timedelta(hours=3),
                    datetime.timedelta(hours=2))
    ride.offer_ride('aman', 'SUV', 'kanpur', 'lucknow', current_time + datetime.timedelta(hours=1),
                    datetime.timedelta(hours=3))
    print(ride.select_ride('rahul', 'kanpur', 'lucknow'))
    print(ride.select_ride('rahul', 'kanpur', 'lucknow', 'earliest'))
