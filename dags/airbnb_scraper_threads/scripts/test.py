import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from selenium_airbnb_active_venice_links_scraper import generate_links_to_scrape, get_available_rooms_at_link
import threading
from datetime import datetime
import logging
import sqlalchemy
from models import Base, db_url, save_or_update_airbnb_room_instance
from sqlalchemy.orm import Session
import queue

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main_logger')



def main():
    engine = sqlalchemy.create_engine(db_url,echo=False) # We have also specified a parameter create_engine.echo, which will instruct the Engine to log all of the SQL it emits to a Python logger that will write to standard out. 
    Base.metadata.create_all(engine)


    links_to_scrape = generate_links_to_scrape()
    logger.info(f"number of links to scrape: {len(links_to_scrape)}")
    
    a = get_available_rooms_at_link(link_to_get = links_to_scrape[7])
    print(a)
