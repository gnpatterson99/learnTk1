import csv
import os
from .constants import FieldTypes as FT, Dimensions


class CSVModel:
    """CSV file storage"""

    fields = {
        "Radius": {'req': True, 'type': FT.decimal,
                     'min': 1.0, 'max': 100.0, 'inc': 1.0},

        "yPosition": {'req': True, 'type': FT.decimal,
                     'min': 0.0, 'max': 100.0, 'inc': 1.0},

        "xPosition": {'req': True, 'type': FT.decimal,
                     'min': 0.0, 'max': 100.0, 'inc': 1.0},

        "xVelocity": {'req': True, 'type': FT.decimal,
                     'min': -100.0, 'max': 100.0, 'inc': 1.0},

        "yVelocity": {'req': True, 'type': FT.decimal,
                     'min': -100.0, 'max': 100.0, 'inc': 1.0},

        "Color": {'req': False, 'type': FT.string_list,
                 'values': ['Red', 'Orange', 'Yellow', 'Green','Blue', 'Indigo','Violet']},

        # "Velocity": {'req': True, 'type': FT.decimal,
        #              'min': -100.0, 'max': 100.0, 'inc': .01},
        #
        # "Date": {'req': True, 'type': FT.iso_date_string},
        #
        # "Time": {'req': True, 'type': FT.string_list,
        #          'values': ['8:00', '12:00', '16:00', '20:00']},
        #
        # "Technician": {'req': True, 'type':  FT.string},
        #
        # "Lab": {'req': True, 'type': FT.string_list,
        #         'values': ['A', 'B', 'C', 'D', 'E']},
        # "Plot": {'req': True, 'type': FT.string_list,
        #          'values': [str(x) for x in range(1, 21)]},
        #
        # "Seed sample":  {'req': True, 'type': FT.string},
        #
        # "Humidity": {'req': True, 'type': FT.decimal,
        #              'min': 0.5, 'max': 52.0, 'inc': .01},
        # "Light": {'req': True, 'type': FT.decimal,
        #           'min': 0, 'max': 100.0, 'inc': .01},
        # "Temperature": {'req': True, 'type': FT.decimal,
        #                 'min': 4, 'max': 40, 'inc': .01},
        # "Equipment Fault": {'req': False, 'type': FT.boolean},
        # "Plants": {'req': True, 'type': FT.integer,
        #            'min': 0, 'max': 20},
        # "Blossoms": {'req': True, 'type': FT.integer,
        #              'min': 0, 'max': 1000},
        # "Fruit": {'req': True, 'type': FT.integer,
        #           'min': 0, 'max': 1000},
        # "Min Height": {'req': True, 'type': FT.decimal,
        #                'min': 0, 'max': 1000, 'inc': .01},
        # "Max Height": {'req': True, 'type': FT.decimal,
        #                'min': 0, 'max': 1000, 'inc': .01},
        # "Median Height": {'req': True, 'type': FT.decimal,
        #                   'min': 0, 'max': 1000, 'inc': .01},
        # "Notes": {'req': False, 'type': FT.long_string}
    }

    def __init__(self, filename):

        self.filename = filename

    def save_record(self, data):
        """Save a dict of data to the CSV file"""

        newfile = not os.path.exists(self.filename)

        with open(self.filename, 'a') as fh:
            csvwriter = csv.DictWriter(fh, fieldnames=self.fields.keys())
            if newfile:
                csvwriter.writeheader()
            csvwriter.writerow(data)


class Particle(object):

    def __init__(self, position_x, position_y, velocity_x, velocity_y, size, color):
        self.position_x=position_x
        self.position_y=position_y
        self.velocity_x=velocity_x
        self.velocity_y=velocity_y
        self.size=size
        self.color=color

    def set_id(self, particle_id):
        self.particle_id=particle_id

    def get_id(self):
        return self.particle_id

    #def __init__(self,position_x, position_y):
    #    self.__init__(position_x, position_y, 0.0, 0.0, 1, 'default')

    def time_to_wall_collision(self):
        time_y_collision=None
        if self.velocity_y > 0:
            time_y_collision = (Dimensions.wall_y - self.size - self.position_y) / self.velocity_y
        elif self.velocity_y < 0:
            time_y_collision = (self.size - self.position_y) / self.velocity_y
        else:
            time_y_collision = None

        time_x_collision=None
        if self.velocity_x > 0:
            time_x_collision = (Dimensions.wall_x - self.size - self.position_x) / self.velocity_x
        elif self.velocity_x < 0:
            time_x_collision = (self.size - self.position_x) / self.velocity_x
        else:
            time_x_collision = None

        return (time_x_collision, time_y_collision)


    def update_physics(self, delta_t):
        self.position_x=self.position_x + (self.velocity_x * delta_t)
        self.position_y=self.position_y + (self.velocity_y * delta_t)



class ParticleBag(object):
    """ use this to store a collections of particles.
    over time this will be enhanced to keep an ordered list of the
    particles that are closest to collosion so that we can deal with them
    """

    def __init__(self):
        self.particle_array=[]
        self.particle_count=0
        self.print_status()

    def add_particle(self, particle):
        self.particle_array.append(particle)
        self.particle_count+=1
        self.print_status()


    def print_status(self):
        print("Bag contains:", self.particle_count,"particles")


    def updateAllParticles(self, delta_t):
        for p in self.particle_array:
            p.update_physics(delta_t)


    def time_to_wall_collision_list(self):
        result_list = []
        for p in self.particle_array:
            tmp = p.time_to_wall_collision()
            result_list.append(tmp)
        return result_list
