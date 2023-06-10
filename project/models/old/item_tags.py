from setting.db import db


class ItemsTags(db.Model):
    __tablename__ = "items_tags"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, db.ForeignKey("items.id"))
    tag_id = Column(Integer, db.ForeignKey("tags.id"))
