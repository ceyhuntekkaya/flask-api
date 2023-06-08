







class Detection(Base, BaseModelClass):
    __tablename__ = "detectiontable"

    id = Column(Integer, primary_key=True)
    detectionstarttime = Column(TIMESTAMP)
    detectionlat = Column(REAL)
    detectionlon = Column(REAL)


