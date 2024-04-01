TARGET_SCORE: int = 0.7
END_INDEX_POSITION: int = 4
START_INDEX_POSITION: int = 3
TARGET_TOPONYMS = [
    "пр",
    "проспект",
    "проспекте",
    "ул",
    "улица",
    "улице",
    "площадь",
    "площади",
    "пер",
    "переулок",
    "проезд",
    "проезде",
    "дорога",
    "дороге",
]
REPLACEMENT_DICT = {
    "пр": "проспект",
    "ул": "улица",
    "пер": "переулок",
    "улице": "улица",
    "проспекте": "проспект",
    "площади": "площадь",
    "проезде": "проезд",
    "дороге": "дорога",
}

GLOBAL_CRS = 4326
GLOBAL_METRIC_CRS = 3857
GLOBAL_EPSG = "EPSG:4326"

OSM_TAGS = {
    "subway": ["yes"],
    "amenity": ["university", "school"],
    "landuse": [
        "brownfield",
        "cemetery",
        "commercial",
        "construction",
        "flowerbed",
        "grass",
        "industrial",
        "meadow",
        "military",
        "plant_nursery",
        "recreation_ground",
        "religious",
        "residential",
        "retail",
    ],
    "natural": ["water", "beach"],
    "leisure": [
        "garden",
        "marina",
        "nature_reserve",
        "park",
        "pitch",
        "sports_centre",
    ],
    "highway": [
        "construction",
        "footway",
        "motorway",
        "pedestrian",
        "primary",
        "primary_link",
        "residential",
        "secondary",
        "service",
        "steps",
        "tertiary",
        "tertiary_link",
        "unclassified",
    ],
    "railway": ["rail", "subway"],
    "amenity": [
        "arts_centre",
        "atm",
        "bank",
        "bar",
        "boat_rental",
        "bus_station",
        "bicycle_rental",
        "biergarten",
        "cafe",
        "car_wash",
        "childcare",
        "cinema",
        "clinic",
        "clinic;doctors;audiologist",
        "college",
        "community_centre",
        "courthouse",
        "coworking_space",
        "dancing_school",
        "dentist",
        "doctors",
        "driving_school",
        "events_venue",
        "fast_food",
        "fire_station",
        "food_court",
        "fountain",
        "fuel",
        "hookah_lounge",
        "hospital",
        "internet_cafe",
        "kindergarten",
        "language_school",
        "library",
        "music_school",
        "music_venue",
        "nightclub",
        "offices",
        "parcel_locker",
        "parking",
        "payment_centre",
        "pharmacy",
        "place_of_worship",
        "police",
        "post_office",
        "pub",
        "recycling",
        "rescue_station",
        "restaurant",
        "school",
        "social_centre",
        "social_facility",
        "studio",
        "theatre",
        "training",
        "university",
        "vending_machine",
        "veterinary",
        "townhall",
        "shelter",
        "marketplace",
        "monastery",
        "planetarium",
        "research_institute",
    ],
    "building": [
        "apartments",
        "boat",
        "bunker",
        "castle",
        "cathedral",
        "chapel",
        "church",
        "civic",
        "college",
        "commercial",
        "detached",
        "dormitory",
        "garages",
        "government",
        "greenhouse",
        "hospital",
        "hotel",
        "house",
        "industrial",
        "kindergarten",
        "kiosk",
        "mosque",
        "office",
        "pavilion",
        "policlinic",
        "public",
        "residential",
        "retail",
        "roof",
        "ruins",
        "school",
        "service",
        "ship",
        "sport_centre",
        "sports_hall",
        "theatre",
        "university",
    ],
    "man_made": [
        "bridge",
        "courtyard",
        "lighthouse",
        "mineshaft",
        "pier",
        "satellite",
        "tower",
        "works",
    ],
    "leisure": [
        "amusement_arcade",
        "fitness_centre",
        "playground",
        "sauna",
        "stadium",
        "track",
    ],
    "office": [
        "company",
        "diplomatic",
        "energy_supplier",
        "government",
        "research",
        "telecommunication",
    ],
    "shop": [
        "alcohol",
        "antiques",
        "appliance",
        "art",
        "baby_goods",
        "bag",
        "bakery",
        "bathroom_furnishing",
        "beauty",
        "beauty;hairdresser;massage;cosmetics;perfumery",
        "bed",
        "beverages",
        "bicycle",
        "binding",
        "bookmaker",
        "books",
        "boutique",
        "butcher",
        "car",
        "car_parts",
        "car_repair",
        "carpet",
        "cheese",
        "chemist",
        "clothes",
        "coffee",
        "computer",
        "confectionery",
        "convenience",
        "copyshop",
        "cosmetics",
        "cosmetics;chemist",
        "craft",
        "craft;paint",
        "curtain",
        "dairy",
        "deli",
        "doityourself",
        "doors",
        "dry_cleaning",
        "e-cigarette",
        "electrical",
        "electronics",
        "electronics;fishing",
        "erotic",
        "estate_agent",
        "fabric",
        "farm",
        "fireplace",
        "fishing",
        "flooring",
        "florist",
        "frame",
        "frozen_food",
        "furniture",
        "games",
        "garden_centre",
        "gas",
        "general",
        "gift",
        "glaziery",
        "gold_buyer",
        "greengrocer",
        "hairdresser",
        "hairdresser_supply",
        "hardware",
        "health_food",
        "hearing_aids",
        "herbalist",
        "honey",
        "houseware",
        "interior_decoration",
        "jeweller_tools",
        "jewelry",
        "kiosk",
        "kitchen",
        "laundry",
        "leather",
        "lighting",
        "lottery",
        "massage",
        "medical_supply",
        "mobile_phone",
        "money_lender",
        "motorcycle",
        "music",
        "newsagent",
        "nuts",
        "optician",
        "orthopaedic",
        "orthopaedics",
        "outdoor",
        "outpost",
        "paint",
        "pastry",
        "pawnbroker",
        "perfumery",
        "pet",
        "pet_grooming",
        "photo",
        "pottery",
        "printer_ink",
        "printing",
        "radiotechnics",
        "repair",
        "seafood",
        "second_hand",
        "security",
        "sewing",
        "shoes",
        "sports",
        "stationery",
        "stationery;copyshop",
        "storage_rental",
        "supermarket",
        "tableware",
        "tailor",
        "tattoo",
        "tea",
        "ticket",
        "tobacco",
        "toys",
        "travel_agency",
        "variety_store",
        "watches",
        "water_filter",
        "weapons",
        "wine",
    ],
    "bus": ["yes"],
    "public_transport": ["platform", "station", "stop_position"],
    "railway": ["tram_stop", "station"],
}

STOPWORDS = ['часу',
             'улицами',
             'анониму',
             'зданьем',
             'пр',
             'проспект',
             'часами',
             'проспектами',
             'доме',
             'дорогами',
             'анонима',
             'дорогою',
             'домом',
             'дорогу',
             'часам',
             'улице',
             'домов',
             'годы',
             'анонимам',
             'году',
             'зданье',
             'проспекте',
             'лет',
             'зданьях',
             'проспекта',
             'дорогах',
             'дом',
             'анонимах',
             'часах',
             'утрам',
             'городу',
             'здании',
             'улицей',
             'зданиям',
             'годами',
             'зданиями',
             'вечерах',
             'ул',
             'домам',
             'часа',
             'вечера',
             'летах',
             'зданьям',
             'улиц',
             'улицам',
             'улицею',
             'дому',
             'дням',
             'утро',
             'анониме',
             'анонимы',
             'утр',
             'днями',
             'дня',
             'зданию',
             'домах',
             'лета',
             'дорог',
             'зданием',
             'проспектом',
             'зданий',
             'дороге',
             'улица',
             'часов',
             'город',
             'городе',
             'городов',
             'вечерам',
             'дней',
             'утрах',
             'городам',
             'днях',
             'проспектам',
             'дне',
             'вечер',
             'анонимов',
             'дома',
             'зданьи',
             'днём',
             'утре',
             'зданью',
             'часы',
             'годам',
             'проспектов',
             'домами',
             'года',
             'здание',
             'городами',
             'дороги',
             'вечеру',
             'годе',
             'города',
             'годов',
             'вечеров',
             'год',
             'летам',
             'фото',
             'годом',
             'здравствуйте',
             'утром',
             'дню',
             'вечером',
             'городом',
             'улицы',
             'гг',
             'дорога',
             'улицу',
             'здания',
             'зданья',
             'утру',
             'час',
             'зданьями',
             'вечерами',
             'дорогой',
             'часе',
             'анонимом',
             'зданиях',
             'день',
             'часом',
             'дорогам',
             'годах',
             'проспекту',
             'проспекты',
             'утра',
             'городах',
             'улицах',
             'аноним',
             'утрами',
             'проспектах',
             'вечере',
             'дни',
             'летами',
             'анонимами',
             'фото',
             'фото',
             'фото',
             'фото',
             'фото',
             'фото',
             'фото',
             'фото',
             'фото',
             'фото',
             'фото',
             'фото',
             'улица',
             'улицы',
             'улице',
             'улицу',
             'улицей',
             'улицею',
             'улице',
             'улицы',
             'улиц',
             'улицам',
             'улицы',
             'улицами',
             'улицах',
             'дом',
             'дома',
             'дому',
             'дому',
             'дом',
             'домом',
             'доме',
             'дому',
             'дома',
             'домов',
             'домам',
             'дома',
             'домами',
             'домах',
             'проспект',
             'проспекта',
             'проспекту',
             'проспект',
             'проспектом',
             'проспекте',
             'проспекты',
             'проспектов',
             'проспектам',
             'проспекты',
             'проспектами',
             'проспектах',
             'дорога',
             'дороги',
             'дороге',
             'дорогу',
             'дорогой',
             'дорогою',
             'дороге',
             'дороги',
             'дорог',
             'дорогам',
             'дороги',
             'дорогами',
             'дорогах',
             'час',
             'часа',
             'часу',
             'часу',
             'час',
             'часом',
             'часе',
             'часу',
             'часы',
             'часов',
             'часам',
             'часы',
             'часами',
             'часах',
             'год',
             'года',
             'году',
             'год',
             'годом',
             'годе',
             'году',
             'года',
             'годы',
             'лета',
             'годов',
             'лет',
             'годам',
             'года',
             'годы',
             'годами',
             'годах',
             'году',
             'гг',
             'гг',
             'гг',
             'гг',
             'гг',
             'гг',
             'летам',
             'лета',
             'летами',
             'летах',
             'утро',
             'утра',
             'утру',
             'утро',
             'утром',
             'утре',
             'утра',
             'утр',
             'утрам',
             'утра',
             'утрами',
             'утрах',
             'здравствуйте',
             'ул',
             'ул',
             'ул',
             'ул',
             'ул',
             'ул',
             'ул',
             'ул',
             'ул',
             'ул',
             'ул',
             'ул',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'пр',
             'здание',
             'зданье',
             'здания',
             'зданья',
             'зданию',
             'зданью',
             'здание',
             'зданье',
             'зданием',
             'зданьем',
             'здании',
             'зданье',
             'зданьи',
             'здания',
             'зданья',
             'зданий',
             'зданиям',
             'зданьям',
             'здания',
             'зданья',
             'зданиями',
             'зданьями',
             'зданиях',
             'зданьях',
             'город',
             'города',
             'городу',
             'город',
             'городом',
             'городе',
             'города',
             'городов',
             'городам',
             'города',
             'городами',
             'городах',
             'аноним',
             'анонима',
             'анониму',
             'анонима',
             'анонимом',
             'анониме',
             'анонимы',
             'анонимов',
             'анонимам',
             'анонимов',
             'анонимами',
             'анонимах',
             'утро',
             'утра',
             'утру',
             'утро',
             'утром',
             'утре',
             'утра',
             'утр',
             'утрам',
             'утра',
             'утрами',
             'утрах',
             'день',
             'дня',
             'дню',
             'день',
             'днём',
             'дне',
             'дни',
             'дней',
             'дням',
             'дни',
             'днями',
             'днях',
             'дню',
             'вечер',
             'вечера',
             'вечеру',
             'вечер',
             'вечером',
             'вечере',
             'вечера',
             'вечеров',
             'вечерам',
             'вечера',
             'вечерами',
             'вечерах']
