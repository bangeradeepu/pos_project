
FOOD_TAG = {
    'VEG': 0,
    'NON_VEG': 1,
    'EGG': 2,
}

ORDER_STATUS = {
    'WAITING': 0,
    'CONFIRMED': 1,
    'IN_PROGRESS': 2,
    'READY': 3,
    'PACKED': 4,
    'DISPATCHED': 5,
    'DELIVERED': 6,
}

ITEM_TYPE = {
    'SINGLE': 0,
    'COMBO': 1,
    'VARIANT': 2,
}

ITEM_TAG = {
    'BESTSELLER': 0,
    'NEW': 1,
    'RECOMMENDED': 2,
    'MUST_TRY': 3,
}

SETTINGS = {
    'TIMINGS': 0,
    'PAYMENT_OPTIONS': 1,
    'DELIVERY_RANGE': 2,
    'ORDERS_STATUS': 3,
}

CATEGORY_VARIANTS = {
    'APP': 0,
    'WEB': 1,
    'INTERNAL': 2,
}

OUTLET_TYPE = {
    'CLOUD_KITCHEN': 0,
    'RESTAURANT': 1,
}

DISPLAY_IN = {
    'ALL': 0,
    'APP': 1,
    'WEB': 2,
    'NONE': 3,
}

ADDRESS_TYPES = {
    'HOME': 'HOME',
    'WORK': 'WORK',
    'OTHER': 'OTHER',
}

MAIN_SOCKET_EVENTS = {
    'ORDER_UPDATE': 0,
    'ITEM_UPDATE': 1,
}

ORDER_UPDATES = {
    'DE_UPDATE': 'DE_UPDATE',
    'STATUS_UPDATE': 'STATUS_UPDATE',
    'ITEMS_UPDATE': 'ITEMS_UPDATE',
    'DETAILS_UPDATE': 'DETAILS_UPDATE',
}

ITEM_SOCKET_EVENT = {
    'SOLD_OUT': 0,
    'DISPLAY_IN': 1,
    'RANK': 2,
}

ORDER_TIME = {
    'IMMEDIATE': 0,
    'PRE_ORDER': 1,
}

ORDER_TYPE = {
    'HOME_DELIVERY': 0,
    'TAKE_AWAY': 1,
    'DINE_IN': 2,
    'NCKOT': 3,
}

PAYMENT_MODE = {
    'COD': 'COD',
    'ONLINE': 'ONLINE',
}

COUPON_TYPE = {
    'PERCENTAGE': 0,
    'FREEBIE': 1,
    'OTHER': 2,
    'INFLUENCER': 3,
}

GENERAL_SETTINGS = {
    'DETECTION_TYPES': {
        'DISTANCE': 'DISTANCE',
        'LAYERS': 'LAYERS',
    },
    'TIMINGS': 'TIMINGS',  # {from, to}
    'DELIVERY_DETECTION': 'DELIVERY_DETECTION',  # {type: dist/boundary, max_boundary: 'filename.json'}
    'STATUS': 'STATUS',  # {active: { web: bool, app: bool }, message: '' },
    'ADDITIONAL_CHARGES': 'ADDITIONAL_CHARGES',  # Array of objects
    # {
    #   name: "",
    #   value: "",
    #   value_type: "percentage/fixed",
    #   type: "tax/additional charge",
    #   target: "Items/Delivery Charge/Total"
    # }
}

ADDITIONAL_CHARGES_KEYS = {
    'VALUE_TYPE': {
        'FIXED': 'FIXED',
        'PERCENTAGE': 'PERCENTAGE',
    },
    'TYPE': {
        'TAX': 'TAX',
        'ADDITIONAL_CHARGE': 'ADDITIONAL_CHARGE',
    },
    'TARGET': {
        'ITEMS': 'ITEMS',
        'DELIVERY_CHARGE': 'DELIVERY_CHARGE',
        'TOTAL': 'TOTAL',
    },
}

LOCATION_FILES = {
    'LOCATION_SETTINGS': 'location_settings.json',
    'LOCATION_LAYERS': 'location_layers.json',
    'LOCATION_DISTANCES': 'location_distances.json',
}

REVIEW_TYPES = {
    'DELIVERY': 'DELIVERY',
    'ORDER_ITEM': 'ORDER_ITEM',
}
