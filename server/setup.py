import logging
import random

from faker import Faker
from server.main import app

import packages.social
import packages.users

logging.getLogger('faker').setLevel(logging.ERROR)

# Create database
app.metadata.create_all()

# Create fake data
fake = Faker()
