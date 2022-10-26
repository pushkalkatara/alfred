import os
from collections import OrderedDict

########################################################################################################################
# General Settings

DEBUG = True
EVAL = False
ET_ROOT = os.environ['ET_ROOT']
ET_DATA = os.environ['ET_DATA']
ET_LOGS = os.environ['ET_LOGS']

RECORD_VIDEO_IMAGES = True
RECORD_SMOOTHING_FACTOR = 1
DATA_SAVE_PATH = "dataset/new_trajectories"

OPEN_LOOP = True
FULL_OBSERVABLE_STATE = True

########################################################################################################################
# Generation Ablations

MAX_NUM_OF_OBJ_INSTANCES = 3     # when randomly initializing the scene, create duplicate instance up to this number
PICKUP_REPEAT_MAX = 4            # how many of the target pickup object to generate in [1, MAX] (randomly chosen)
RECEPTACLE_SPARSE_POINTS = 50    # increment for how many points to leave free for sparsely populated receptacles
RECEPTACLE_EMPTY_POINTS = 200    # increment for how many points to leave free for empty receptacles

MIN_VISIBLE_RATIO = 0.0011       # minimum area ratio (with respect to image size) of visible object
PLANNER_MAX_STEPS = 100          # if the generated plan is more than these steps, discard the traj
MAX_EPISODE_LENGTH = 1000        # maximum number of API steps allowed per trajectory

FORCED_SAMPLING = False          # set True for debugging instead of proper sampling
PRUNE_UNREACHABLE_POINTS = True  # prune navigation points that were deemed unreachable by the proprocessing script

########################################################################################################################
# Goals

GOALS = ["pick_and_place_simple",
         "pick_two_obj_and_place",
         "look_at_obj_in_light",
         "pick_clean_then_place_in_recep",
         "pick_heat_then_place_in_recep",
         "pick_cool_then_place_in_recep",
         "pick_and_place_with_movable_recep"]

GOALS_VALID = {"pick_and_place_simple": {"kitchen", "living-room", "bathroom", "bedroom"},
               "pick_two_obj_and_place": {"kitchen", "living-room", "bathroom", "bedroom"},
               "look_at_obj_in_light": {"living-room", "bedroom"},
               "pick_clean_then_place_in_recep": {"kitchen", "bathroom"},
               "pick_heat_then_place_in_recep": {"kitchen"},
               "pick_cool_then_place_in_recep": {"kitchen"},
               "pick_and_place_with_movable_recep": {"kitchen", "living-room", "bedroom"}}

pddl_goal_type = "pick_and_place_simple"  # default goal type

########################################################################################################################
# Video Settings

# filler frame IDs
BEFORE = 0
MIDDLE = 1
AFTER = 2

# number of image frames to save before and after executing the specified action
SAVE_FRAME_BEFORE_AND_AFTER_COUNTS = {
    'OpenObject': [2, 0, 2],
    'CloseObject': [2, 0, 2],
    'PickupObject': [5, 0, 10],
    'PutObject': [5, 0, 10],
    'CleanObject': [3, 0, 5],
    'HeatObject': [3, 0, 5],
    'CoolObject': [3, 30, 5],
    'ToggleObjectOn': [3, 0, 15],
    'ToggleObjectOff': [1, 0, 5],
    'SliceObject': [3, 0, 7]
}

# FPS
VIDEO_FRAME_RATE = 5

########################################################################################################################
# Data & Storage

save_path = DATA_SAVE_PATH
data_dict = OrderedDict()  # dictionary for storing trajectory data to be dumped

########################################################################################################################
# Unity Hyperparameters

BUILD_PATH = None

AGENT_STEP_SIZE = 0.25
AGENT_HORIZON_ADJ = 15
AGENT_ROTATE_ADJ = 90
CAMERA_HEIGHT_OFFSET = 0.75
VISIBILITY_DISTANCE = 1.5
HORIZON_GRANULARITY = 15

RENDER_IMAGE = True
RENDER_DEPTH_IMAGE = True
RENDER_CLASS_IMAGE = True
RENDER_OBJECT_IMAGE = True

MAX_DEPTH = 5000
STEPS_AHEAD = 5
SCENE_PADDING = STEPS_AHEAD * 3
SCREEN_WIDTH = DETECTION_SCREEN_WIDTH = 300
SCREEN_HEIGHT = DETECTION_SCREEN_HEIGHT = 300
MIN_VISIBLE_PIXELS = 10

# (400) / (600*600) ~ 0.13% area of image
# int(MIN_VISIBLE_RATIO * float(DETECTION_SCREEN_WIDTH) * float(DETECTION_SCREEN_HEIGHT))
# MIN_VISIBLE_PIXELS = int(MIN_VISIBLE_RATIO * float(DETECTION_SCREEN_WIDTH) * float(
#    DETECTION_SCREEN_HEIGHT))  # (400) / (600*600) ~ 0.13% area of image

########################################################################################################################
# Scenes and Objects

TRAIN_SCENE_NUMBERS = list(range(7, 31))           # Train Kitchens (24/30)
TRAIN_SCENE_NUMBERS.extend(list(range(207, 231)))  # Train Living Rooms (24/30)
TRAIN_SCENE_NUMBERS.extend(list(range(307, 331)))  # Train Bedrooms (24/30)
TRAIN_SCENE_NUMBERS.extend(list(range(407, 431)))  # Train Bathrooms (24/30)

TEST_SCENE_NUMBERS = list(range(1, 7))             # Test Kitchens (6/30)
TEST_SCENE_NUMBERS.extend(list(range(201, 207)))   # Test Living Rooms (6/30)
TEST_SCENE_NUMBERS.extend(list(range(301, 307)))   # Test Bedrooms (6/30)
TEST_SCENE_NUMBERS.extend(list(range(401, 407)))   # Test Bathrooms (6/30)

SCENE_NUMBERS = TRAIN_SCENE_NUMBERS + TEST_SCENE_NUMBERS

# Scene types.
'''
SCENE_TYPE = {"kitchen": range(1, 31),
              "LivingRoom": range(201, 231),
              "Bedroom": range(301, 331),
              "Bathroom": range(401, 431)}

SCENE_TYPE = ["kitchen", "living-room", "bedroom", "bathroom"]
'''

OBJECTS = [
    'AlarmClock',
    'Apple',
    'AppleSlice',
    'ArmChair',
    'BaseballBat',
    'BasketBall',
    'Bathtub',
    'BathtubBasin',
    'Bed',
    'Blinds',
    'Book',
    'Boots',
    'Bowl',
    'BowlDirty',
    'BowlFilled',
    'Box',
    'Bread',
    'ButterKnife',
    'Cabinet',
    'Candle',
    'Cart',
    'CD',
    'CellPhone',
    'Chair',
    'Cloth',
    'CoffeeMachine',
    'Container',
    'ContainerFull',
    'CounterTop',
    'CreditCard',
    'Cup',
    'Curtains',
    'Desk',
    'DeskLamp',
    'DishSponge',
    'Dirt',
    'Drawer',
    'Dresser',
    'Egg',
    'EggShell',
    'EggFried',
    'FloorLamp',
    'Footstool',
    'Fork',
    'Fridge',
    'GarbageCan',
    'Glassbottle',
    'HandTowel',
    'HandTowelHolder',
    'HousePlant',
    'Kettle',
    'KeyChain',
    'Knife',
    'Ladle',
    'Laptop',
    'LaundryHamper',
    'LaundryHamperLid',
    'Lettuce',
    'LightSwitch',
    'Microwave',
    'Mirror',
    'Mug',
    'MugFilled',
    'Newspaper',
    "Omelette",
    'Ottoman',
    'Painting',
    'Pan',
    'PaperTowel',
    'PaperTowelRoll',
    'Pen',
    'Pencil',
    'PepperShaker',
    'Pillow',
    'Plate',
    'Plunger',
    'Poster',
    'Pot',
    'Potato',
    'RemoteControl',
    'Safe',
    'SaltShaker',
    'Sandwich',
    'ScrubBrush',
    'Shelf',
    'ShowerDoor',
    'ShowerGlass',
    'Sink',
    'SinkBasin',
    'SoapBar',
    'SoapBottle',
    'Sofa',
    'Spatula',
    'Spoon',
    'SprayBottle',
    'Statue',
    'StoveBurner',
    'StoveKnob',
    'DiningTable',
    'CoffeeTable',
    'SideTable',
    'TeddyBear',
    'Television',
    'TennisRacket',
    'TissueBox',
    'Toaster',
    'Toilet',
    'ToiletPaper',
    'ToiletPaperHanger',
    'ToiletPaperRoll',
    'Tomato',
    'Towel',
    'TowelHolder',
    'TVStand',
    'Vase',
    'Watch',
    'WateringCan',
    'Window',
    'WineBottle',
]

OBJECTS_LOWER_TO_UPPER = {obj.lower(): obj for obj in OBJECTS}

OBJECTS_SINGULAR = [
    'alarmclock',
    'apple',
    'armchair',
    'baseballbat',
    'basketball',
    'bathtub',
    'bathtubbasin',
    'bed',
    'blinds',
    'book',
    'boots',
    'bowl',
    'box',
    'bread',
    'butterknife',
    'cabinet',
    'candle',
    'cart',
    'cd',
    'cellphone',
    'chair',
    'cloth',
    'coffeemachine',
    'countertop',
    'creditcard',
    'cup',
    'curtains',
    'desk',
    'desklamp',
    'dishsponge',
    'drawer',
    'dresser',
    'egg',
    'floorlamp',
    'footstool',
    'fork',
    'fridge',
    'garbagecan',
    'glassbottle',
    'handtowel',
    'handtowelholder',
    'houseplant',
    'kettle',
    'keychain',
    'knife',
    'ladle',
    'laptop',
    'laundryhamper',
    'laundryhamperlid',
    'lettuce',
    'lightswitch',
    'microwave',
    'mirror',
    'mug',
    'newspaper',
    'ottoman',
    'painting',
    'pan',
    'papertowel',
    'papertowelroll',
    'pen',
    'pencil',
    'peppershaker',
    'pillow',
    'plate',
    'plunger',
    'poster',
    'pot',
    'potato',
    'remotecontrol',
    'safe',
    'saltshaker',
    'scrubbrush',
    'shelf',
    'showerdoor',
    'showerglass',
    'sink',
    'sinkbasin',
    'soapbar',
    'soapbottle',
    'sofa',
    'spatula',
    'spoon',
    'spraybottle',
    'statue',
    'stoveburner',
    'stoveknob',
    'diningtable',
    'coffeetable',
    'sidetable'
    'teddybear',
    'television',
    'tennisracket',
    'tissuebox',
    'toaster',
    'toilet',
    'toiletpaper',
    'toiletpaperhanger',
    'toiletpaperroll',
    'tomato',
    'towel',
    'towelholder',
    'tvstand',
    'vase',
    'watch',
    'wateringcan',
    'window',
    'winebottle',
]

OBJECTS_PLURAL = [
    'alarmclocks',
    'apples',
    'armchairs',
    'baseballbats',
    'basketballs',
    'bathtubs',
    'bathtubbasins',
    'beds',
    'blinds',
    'books',
    'boots',
    'bottles',
    'bowls',
    'boxes',
    'bread',
    'butterknives',
    'cabinets',
    'candles',
    'carts',
    'cds',
    'cellphones',
    'chairs',
    'cloths',
    'coffeemachines',
    'countertops',
    'creditcards',
    'cups',
    'curtains',
    'desks',
    'desklamps',
    'dishsponges',
    'drawers',
    'dressers',
    'eggs',
    'floorlamps',
    'footstools',
    'forks',
    'fridges',
    'garbagecans',
    'glassbottles',
    'handtowels',
    'handtowelholders',
    'houseplants',
    'kettles',
    'keychains',
    'knives',
    'ladles',
    'laptops',
    'laundryhampers',
    'laundryhamperlids',
    'lettuces',
    'lightswitches',
    'microwaves',
    'mirrors',
    'mugs',
    'newspapers',
    'ottomans',
    'paintings',
    'pans',
    'papertowels',
    'papertowelrolls',
    'pens',
    'pencils',
    'peppershakers',
    'pillows',
    'plates',
    'plungers',
    'posters',
    'pots',
    'potatoes',
    'remotecontrollers',
    'safes',
    'saltshakers',
    'scrubbrushes',
    'shelves',
    'showerdoors',
    'showerglassess',
    'sinks',
    'sinkbasins',
    'soapbars',
    'soapbottles',
    'sofas',
    'spatulas',
    'spoons',
    'spraybottles',
    'statues',
    'stoveburners',
    'stoveknobs',
    'diningtables',
    'coffeetables',
    'sidetable',
    'teddybears',
    'televisions',
    'tennisrackets',
    'tissueboxes',
    'toasters',
    'toilets',
    'toiletpapers',
    'toiletpaperhangers',
    'toiletpaperrolls',
    'tomatoes',
    'towels',
    'towelholders',
    'tvstands',
    'vases',
    'watches',
    'wateringcans',
    'windows',
    'winebottles',
]

MOVABLE_RECEPTACLES = [
    'Bowl',
    'Box',
    'Cup',
    'Mug',
    'Plate',
    'Pan',
    'Pot',
]

MOVABLE_RECEPTACLES_SET = set(MOVABLE_RECEPTACLES)
OBJECTS_SET = set(OBJECTS) | MOVABLE_RECEPTACLES_SET

OBJECT_CLASS_TO_ID = {obj: ii for (ii, obj) in enumerate(OBJECTS)}

RECEPTACLES = {
        'BathtubBasin',
        'Bowl',
        'Cup',
        'Drawer',
        'Mug',
        'Plate',
        'Shelf',
        'SinkBasin',
        'Box',
        'Cabinet',
        'CoffeeMachine',
        'CounterTop',
        'Fridge',
        'GarbageCan',
        'HandTowelHolder',
        'Microwave',
        'PaintingHanger',
        'Pan',
        'Pot',
        'StoveBurner',
        'DiningTable',
        'CoffeeTable',
        'SideTable',
        'ToiletPaperHanger',
        'TowelHolder',
        'Safe',
        'BathtubBasin',
        'ArmChair',
        'Toilet',
        'Sofa',
        'Ottoman',
        'Dresser',
        'LaundryHamper',
        'Desk',
        'Bed',
        'Cart',
        'TVStand',
        'Toaster',
    }

NON_RECEPTACLES = OBJECTS_SET - RECEPTACLES

NUM_RECEPTACLES = len(RECEPTACLES)
NUM_CLASSES = len(OBJECTS)

# For generating questions
QUESTION_OBJECT_CLASS_LIST = [
    'Spoon',
    'Potato',
    'Fork',
    'Plate',
    'Egg',
    'Tomato',
    'Bowl',
    'Lettuce',
    'Apple',
    'Knife',
    'Container',
    'Bread',
    'Mug',
]

VAL_RECEPTACLE_OBJECTS = {
    'Pot': {'Apple',
            'AppleSliced',
            'ButterKnife',
            'DishSponge',
            'Egg',
            'Fork',
            'Knife',
            'Ladle',
            'Lettuce',
            'LettuceSliced',
            'Potato',
            'PotatoSliced',
            'Spatula',
            'Spoon',
            'Tomato',
            'TomatoSliced'},
    'Pan': {'Apple',
            'AppleSliced',
            'ButterKnife',
            'DishSponge',
            'Egg',
            'Fork',
            'Knife',
            'Ladle',
            'Lettuce',
            'LettuceSliced',
            'Potato',
            'PotatoSliced',
            'Spatula',
            'Spoon',
            'Tomato',
            'TomatoSliced'},
    'Bowl': {'Apple',
             'AppleSliced',
             'ButterKnife',
             'DishSponge',
             'Egg',
             'Fork',
             'Knife',
             'Ladle',
             'Lettuce',
             'LettuceSliced',
             'Potato',
             'PotatoSliced',
             'Spatula',
             'Spoon',
             'Tomato',
             'TomatoSliced',
             'Candle',
             'CD',
             'CellPhone',
             'Cloth',
             'CreditCard',
             'DishSponge',
             'KeyChain',
             'Mug',
             'PaperTowel',
             'Pen',
             'Pencil',
             'RemoteControl',
             'Watch'},
    'CoffeeMachine': {'Mug'},
    'Microwave': {'Apple',
                  'AppleSliced',
                  'Bowl',
                  'Bread',
                  'BreadSliced',
                  'Cup',
                  'Egg',
                  'Glassbottle',
                  'Mug',
                  'Plate',
                  'Potato',
                  'PotatoSliced',
                  'Tomato',
                  'TomatoSliced'},
    'StoveBurner': {'Kettle',
                    'Pan',
                    'Pot'},
    'Fridge': {'Apple',
               'AppleSliced',
               'Bowl',
               'Bread',
               'BreadSliced',
               'Cup',
               'Egg',
               'Glassbottle',
               'Lettuce',
               'LettuceSliced',
               'Mug',
               'Pan',
               'Plate',
               'Pot',
               'Potato',
               'PotatoSliced',
               'Tomato',
               'TomatoSliced',
               'WineBottle'},
    'Mug': {'ButterKnife',
            'Fork',
            'Knife',
            'Pen',
            'Pencil',
            'Spoon',
            'KeyChain',
            'Watch'},
    'Plate': {'Apple',
              'AppleSliced',
              'ButterKnife',
              'DishSponge',
              'Egg',
              'Fork',
              'Knife',
              'Ladle',
              'Lettuce',
              'LettuceSliced',
              'Mug',
              'Potato',
              'PotatoSliced',
              'Spatula',
              'Spoon',
              'Tomato',
              'TomatoSliced',
              'AlarmClock',
              'Book',
              'Candle',
              'CD',
              'CellPhone',
              'Cloth',
              'CreditCard',
              'DishSponge',
              'Glassbottle',
              'KeyChain',
              'Mug',
              'PaperTowel',
              'Pen',
              'Pencil',
              'TissueBox',
              'Watch'},
    'Cup': {'ButterKnife',
            'Fork',
            'Spoon'},
    'Sofa': {'BasketBall',
             'Book',
             'Box',
             'CellPhone',
             'Cloth',
             'CreditCard',
             'KeyChain',
             'Laptop',
             'Newspaper',
             'Pillow',
             'RemoteControl'},
    'ArmChair': {'BasketBall',
                 'Book',
                 'Box',
                 'CellPhone',
                 'Cloth',
                 'CreditCard',
                 'KeyChain',
                 'Laptop',
                 'Newspaper',
                 'Pillow',
                 'RemoteControl'},
    'Box': {'AlarmClock',
            'Book',
            'Candle',
            'CD',
            'CellPhone',
            'Cloth',
            'CreditCard',
            'DishSponge',
            'Glassbottle',
            'KeyChain',
            'Mug',
            'PaperTowel',
            'Pen',
            'Pencil',
            'RemoteControl',
            'Statue',
            'TissueBox',
            'Vase',
            'Watch'},
    'Ottoman': {'BasketBall',
                'Book',
                'Box',
                'CellPhone',
                'Cloth',
                'CreditCard',
                'KeyChain',
                'Laptop',
                'Newspaper',
                'Pillow',
                'RemoteControl'},
    'Dresser': {'AlarmClock',
                'BasketBall',
                'Book',
                'Bowl',
                'Box',
                'Candle',
                'CD',
                'CellPhone',
                'Cloth',
                'CreditCard',
                'Cup',
                'Glassbottle',
                'KeyChain',
                'Laptop',
                'Mug',
                'Newspaper',
                'Pen',
                'Pencil',
                'Plate',
                'RemoteControl',
                'SprayBottle',
                'Statue',
                'TennisRacket',
                'TissueBox',
                'ToiletPaper',
                'ToiletPaperRoll',
                'Vase',
                'Watch',
                'WateringCan',
                'WineBottle'},
    'LaundryHamper': {'Cloth'},
    'Desk': {'AlarmClock',
             'BasketBall',
             'Book',
             'Bowl',
             'Box',
             'Candle',
             'CD',
             'CellPhone',
             'Cloth',
             'CreditCard',
             'Cup',
             'Glassbottle',
             'KeyChain',
             'Laptop',
             'Mug',
             'Newspaper',
             'Pen',
             'Pencil',
             'Plate',
             'RemoteControl',
             'SoapBottle',
             'SprayBottle',
             'Statue',
             'TennisRacket',
             'TissueBox',
             'ToiletPaper',
             'ToiletPaperRoll',
             'Vase',
             'Watch',
             'WateringCan',
             'WineBottle'},
    'Bed': {'BaseballBat',
            'BasketBall',
            'Book',
            'CellPhone',
            'Laptop',
            'Newspaper',
            'Pillow',
            'TennisRacket'},
    'Toilet': {'Candle',
               'Cloth',
               'DishSponge',
               'Newspaper',
               'PaperTowel',
               'SoapBar',
               'SoapBottle',
               'SprayBottle',
               'TissueBox',
               'ToiletPaper',
               'ToiletPaperRoll',
               'HandTowel'},
    'ToiletPaperHanger': {'ToiletPaper',
                          'ToiletPaperRoll'},
    'TowelHolder': {'Towel'},
    'HandTowelHolder': {'HandTowel'},
    'Cart': {'Candle',
             'Cloth',
             'DishSponge',
             'Mug',
             'PaperTowel',
             'Plunger',
             'SoapBar',
             'SoapBottle',
             'SprayBottle',
             'Statue',
             'TissueBox',
             'ToiletPaper',
             'ToiletPaperRoll',
             'Vase',
             'HandTowel'},
    'BathtubBasin': {'Cloth',
                     'DishSponge',
                     'SoapBar',
                     'HandTowel'},
    'SinkBasin': {'Apple',
                  'AppleSliced',
                  'Bowl',
                  'ButterKnife',
                  'Cloth',
                  'Cup',
                  'DishSponge',
                  'Egg',
                  'Glassbottle',
                  'Fork',
                  'Kettle',
                  'Knife',
                  'Ladle',
                  'Lettuce',
                  'LettuceSliced',
                  'Mug',
                  'Pan',
                  'Plate',
                  'Pot',
                  'Potato',
                  'PotatoSliced',
                  'SoapBar',
                  'Spatula',
                  'Spoon',
                  'Tomato',
                  'TomatoSliced',
                  'HandTowel'},
    'Cabinet': {'Book',
                'Bowl',
                'Box',
                'Candle',
                'CD',
                'Cloth',
                'Cup',
                'DishSponge',
                'Glassbottle',
                'Kettle',
                'Ladle',
                'Mug',
                'Newspaper',
                'Pan',
                'PepperShaker',
                'Plate',
                'Plunger',
                'Pot',
                'SaltShaker',
                'SoapBar',
                'SoapBottle',
                'SprayBottle',
                'TissueBox',
                'ToiletPaper',
                'ToiletPaperRoll',
                'Vase',
                'WateringCan',
                'WineBottle',
                'HandTowel'},
    'TableTop': {'AlarmClock',
                 'Apple',
                 'AppleSliced',
                 'BaseballBat',
                 'BasketBall',
                 'Book',
                 'Bowl',
                 'Box',
                 'Bread',
                 'BreadSliced',
                 'ButterKnife',
                 'Candle',
                 'CD',
                 'CellPhone',
                 'Cloth',
                 'CreditCard',
                 'Cup',
                 'DishSponge',
                 'Glassbottle',
                 'Egg',
                 'Fork',
                 'Kettle',
                 'KeyChain',
                 'Knife',
                 'Ladle',
                 'Laptop',
                 'Lettuce',
                 'LettuceSliced',
                 'Mug',
                 'Newspaper',
                 'Pan',
                 'PaperTowel',
                 'Pen',
                 'Pencil',
                 'PepperShaker',
                 'Plate',
                 'Pot',
                 'Potato',
                 'PotatoSliced',
                 'RemoteControl',
                 'SaltShaker',
                 'SoapBar',
                 'SoapBottle',
                 'Spatula',
                 'Spoon',
                 'SprayBottle',
                 'Statue',
                 'TennisRacket',
                 'TissueBox',
                 'ToiletPaper',
                 'ToiletPaperRoll',
                 'Tomato',
                 'TomatoSliced',
                 'Vase',
                 'Watch',
                 'WateringCan',
                 'WineBottle',
                 'HandTowel'},
    'CounterTop': {'AlarmClock',
                   'Apple',
                   'AppleSliced',
                   'BaseballBat',
                   'BasketBall',
                   'Book',
                   'Bowl',
                   'Box',
                   'Bread',
                   'BreadSliced',
                   'ButterKnife',
                   'Candle',
                   'CD',
                   'CellPhone',
                   'Cloth',
                   'CreditCard',
                   'Cup',
                   'DishSponge',
                   'Egg',
                   'Glassbottle',
                   'Fork',
                   'Kettle',
                   'KeyChain',
                   'Knife',
                   'Ladle',
                   'Laptop',
                   'Lettuce',
                   'LettuceSliced',
                   'Mug',
                   'Newspaper',
                   'Pan',
                   'PaperTowel',
                   'Pen',
                   'Pencil',
                   'PepperShaker',
                   'Plate',
                   'Pot',
                   'Potato',
                   'PotatoSliced',
                   'RemoteControl',
                   'SaltShaker',
                   'SoapBar',
                   'SoapBottle',
                   'Spatula',
                   'Spoon',
                   'SprayBottle',
                   'Statue',
                   'TennisRacket',
                   'TissueBox',
                   'ToiletPaper',
                   'ToiletPaperRoll',
                   'Tomato',
                   'TomatoSliced',
                   'Vase',
                   'Watch',
                   'WateringCan',
                   'WineBottle',
                   'HandTowel'},
    'Shelf': {'AlarmClock',
              'Book',
              'Bowl',
              'Box',
              'Candle',
              'CD',
              'CellPhone',
              'Cloth',
              'CreditCard',
              'Cup',
              'DishSponge',
              'Glassbottle',
              'Kettle',
              'KeyChain',
              'Mug',
              'Newspaper',
              'PaperTowel',
              'Pen',
              'Pencil',
              'PepperShaker',
              'Plate',
              'Pot',
              'RemoteControl',
              'SaltShaker',
              'SoapBar',
              'SoapBottle',
              'SprayBottle',
              'Statue',
              'TissueBox',
              'ToiletPaper',
              'ToiletPaperRoll',
              'Vase',
              'Watch',
              'WateringCan',
              'WineBottle',
              'HandTowel'},
    'Drawer': {'Book',
               'ButterKnife',
               'Candle',
               'CD',
               'CellPhone',
               'Cloth',
               'CreditCard',
               'DishSponge',
               'Fork',
               'KeyChain',
               'Knife',
               'Ladle',
               'Newspaper',
               'Pen',
               'Pencil',
               'PepperShaker',
               'RemoteControl',
               'SaltShaker',
               'SoapBar',
               'SoapBottle',
               'Spatula',
               'Spoon',
               'SprayBottle',
               'TissueBox',
               'ToiletPaper',
               'ToiletPaperRoll',
               'Watch',
               'WateringCan',
               'HandTowel'},
    'GarbageCan': {'Apple',
                   'AppleSliced',
                   'Bread',
                   'BreadSliced',
                   'CD',
                   'Cloth',
                   'DishSponge',
                   'Egg',
                   'Lettuce',
                   'LettuceSliced',
                   'Newspaper',
                   'PaperTowel',
                   'Pen',
                   'Pencil',
                   'Potato',
                   'PotatoSliced',
                   'SoapBar',
                   'SoapBottle',
                   'SprayBottle',
                   'TissueBox',
                   'ToiletPaper',
                   'ToiletPaperRoll',
                   'Tomato',
                   'TomatoSliced',
                   'WineBottle',
                   'HandTowel'},
    'Safe': {'CD',
             'CellPhone',
             'CreditCard',
             'KeyChain',
             'Statue',
             'Vase',
             'Watch'},
    'TVStand': {'TissueBox'},
    'Toaster': {'BreadSliced'},
}

VAL_RECEPTACLE_OBJECTS['DiningTable'] = VAL_RECEPTACLE_OBJECTS['TableTop']
VAL_RECEPTACLE_OBJECTS['CoffeeTable'] = VAL_RECEPTACLE_OBJECTS['TableTop']
VAL_RECEPTACLE_OBJECTS['SideTable'] = VAL_RECEPTACLE_OBJECTS['TableTop']
del VAL_RECEPTACLE_OBJECTS['TableTop']

NON_RECEPTACLES_SET = (OBJECTS_SET - set(VAL_RECEPTACLE_OBJECTS.keys())) | set(MOVABLE_RECEPTACLES)

VAL_ACTION_OBJECTS = {
    'Heatable': {'Apple',
                 'AppleSliced',
                 'Bread',
                 'BreadSliced',
                 'Cup',
                 'Egg',
                 'Mug',
                 'Plate',
                 'Potato',
                 'PotatoSliced',
                 'Tomato',
                 'TomatoSliced'},
    'Coolable': {'Apple',
                 'AppleSliced',
                 'Bowl',
                 'Bread',
                 'BreadSliced',
                 'Cup',
                 'Egg',
                 'Lettuce',
                 'LettuceSliced',
                 'Mug',
                 'Pan',
                 'Plate',
                 'Pot',
                 'Potato',
                 'PotatoSliced',
                 'Tomato',
                 'TomatoSliced',
                 'WineBottle'},
    'Cleanable': {'Apple',
                  'AppleSliced',
                  'Bowl',
                  'ButterKnife',
                  'Cloth',
                  'Cup',
                  'DishSponge',
                  'Egg',
                  'Fork',
                  'Kettle',
                  'Knife',
                  'Ladle',
                  'Lettuce',
                  'LettuceSliced',
                  'Mug',
                  'Pan',
                  'Plate',
                  'Pot',
                  'Potato',
                  'PotatoSliced',
                  'SoapBar',
                  'Spatula',
                  'Spoon',
                  'Tomato',
                  'TomatoSliced'},
    'Toggleable': {'DeskLamp',
                   'FloorLamp'},
    'Sliceable': {'Apple',
                  'Bread',
                  'Egg',
                  'Lettuce',
                  'Potato',
                  'Tomato'}
}

# object parents
OBJ_PARENTS = {obj: obj for obj in OBJECTS}
OBJ_PARENTS['AppleSliced'] = 'Apple'
OBJ_PARENTS['BreadSliced'] = 'Bread'
OBJ_PARENTS['LettuceSliced'] = 'Lettuce'
OBJ_PARENTS['PotatoSliced'] = 'Potato'
OBJ_PARENTS['TomatoSliced'] = 'Tomato'

# force a different horizon view for objects of (type, location). If the location is None, force this horizon for all
# objects of that type.
FORCED_HORIZON_OBJS = {
    ('FloorLamp', None): 0,
    ('Fridge', 18): 30,
    ('Toilet', None): 15,
}

# openable objects with fixed states for transport.
FORCED_OPEN_STATE_ON_PICKUP = {
    'Laptop': False,
}

# list of openable classes.
OPENABLE_CLASS_LIST = ['Fridge', 'Cabinet', 'Microwave', 'Drawer', 'Safe', 'Box']
OPENABLE_CLASS_SET = set(OPENABLE_CLASS_LIST)

########################################################################################################################

# tokens used for evaluation
STOP_TOKEN = "<<stop>>"
SEQ_TOKEN = "<<seg>>"
TERMINAL_TOKENS = [STOP_TOKEN, SEQ_TOKEN]
ALL_SUBGOALS = [
    'GotoLocation',
    'PickupObject',
    'PutObject',
    'CoolObject',
    'HeatObject',
    'CleanObject',
    'SliceObject',
    'ToggleObject']

# TRAIN AND EVAL SETTINGS
# evaluation on multiple GPUs
NUM_EVAL_WORKERS_PER_GPU = 5
# reward config to use by default
REWARD_CONFIG = 'files/rewards.json'
# maximum number of subgoals in a task (used for normalization)
MAX_SUBGOALS = 25
# vocabulary file name
VOCAB_FILENAME = 'data.vocab'
# vocabulary with object classes
OBJ_CLS_VOCAB = 'files/obj_cls.vocab'

# TRAJECTORIES GENERATION
LOG_FILE = os.path.join(os.environ['ET_DATA'], 'logs_gen')
# paths to layouts
LAYOUTS_PATH = os.path.join(os.environ['ET_ROOT'], 'alfred/gen/layouts_procthor')
FF_PATH = os.path.join(os.environ['ET_ROOT'], 'alfred/gen/ff_planner/ff')
PLANNER_PATH = os.path.join(os.environ['ET_ROOT'], 'alfred/gen/planner')
# scene numbers from the paper
PAPER_TRAIN_SCENES = [
    1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 30, 201, 202, 203, 204, 205,
    206, 207, 208, 209, 210, 211, 212, 213, 214, 216, 217, 218, 220,
    221, 222, 223, 224, 225, 227, 228, 229, 230, 301, 302, 303, 304,
    305, 306, 307, 309, 310, 311, 312, 313, 314, 316, 317, 318, 319,
    320, 321, 322, 323, 324, 326, 327, 328, 329, 330, 401, 402, 403,
    405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417,
    418, 419, 420, 421, 422, 423, 426, 427, 428, 429, 430]
PAPER_VALID_UNSEEN_SCENES = [10, 219, 308, 424]
PAPER_TEST_UNSEEN_SCENES = [9, 29, 215, 226, 315, 325, 404, 425]
#SCENE_NUMBERS_PER_ROOM = {'kitchen': list(range(1, 31)),
#                          'living': list(range(201, 231)),
#                          'bedroom': list(range(301, 331)),
#                          'bathroom': list(range(401, 431))}


OBJECTS_ACTIONS = [
    'None', 'AlarmClock', 'Apple', 'AppleSliced', 'ArmChair', 'BaseballBat',
    'BasketBall', 'Bathtub', 'BathtubBasin', 'Bed', 'Book', 'Bowl',
    'Box', 'Bread', 'BreadSliced', 'ButterKnife', 'CD', 'Cabinet',
    'Candle', 'Cart', 'CellPhone', 'Cloth', 'CoffeeMachine', 'CoffeeTable',
    'CounterTop', 'CreditCard', 'Cup', 'Desk', 'DeskLamp', 'DiningTable',
    'DishSponge', 'Drawer', 'Dresser', 'Egg', 'Faucet', 'FloorLamp', 'Fork',
    'Fridge', 'GarbageCan', 'Glassbottle', 'HandTowel', 'Kettle', 'KeyChain',
    'Knife', 'Ladle', 'Laptop', 'Lettuce', 'LettuceSliced', 'Microwave', 'Mug',
    'Newspaper', 'Ottoman', 'Pan', 'Pen', 'Pencil', 'PepperShaker',
    'Pillow', 'Plate', 'Plunger', 'Pot', 'Potato', 'PotatoSliced', 'RemoteControl',
    'Safe', 'SaltShaker', 'Shelf', 'SideTable', 'Sink', 'SinkBasin', 'SoapBar',
    'SoapBottle', 'Sofa', 'Spatula', 'Spoon', 'SprayBottle', 'Statue',
    'StoveBurner', 'TVStand', 'TennisRacket', 'TissueBox', 'Toilet', 'ToiletPaper',
    'ToiletPaperHanger', 'Tomato', 'TomatoSliced', 'Vase', 'Watch', 'WateringCan',
    'WineBottle']

