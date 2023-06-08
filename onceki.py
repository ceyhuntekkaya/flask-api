


class Config():
    __tablename__ = "aselsan_config"

    id = Column(Integer, primary_key=True)

    # Information
    status = Column(Integer, default=1)
    config_json = Column(JSON)

    # System timing
    created_at = Column(TIMESTAMP, default=datetime.now())
    deleted_at = Column(TIMESTAMP)


class System(Base, BaseModelClass):
    __tablename__ = "aselsan_system"

    id = Column(Integer, primary_key=True)

    # Information for deletion
    status = Column(Integer, default=1)

    # Information
    system_status = Column(Enum("training", "live", "standby", name="SystemStatusEnum"), default="standby")

    # System timing
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)


class Logs(Base, BaseModelClass):
    __tablename__ = "aselsan_logs"

    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=datetime.now())

    # Information
    key = Column(String)
    log = Column(JSON)

    # Relation
    user_id = Column(Integer, ForeignKey("aselsan_users.id"))
    user = relationship("User", back_populates="logs")


class Detection(Base, BaseModelClass):
    __tablename__ = "detectiontable"

    id = Column(Integer, primary_key=True)
    detectionstarttime = Column(TIMESTAMP)
    detectionlat = Column(REAL)
    detectionlon = Column(REAL)


class IdentificationTypes(Base, BaseModelClass):
    __tablename__ = "identificationtypetable"

    id = Column(Integer, primary_key=True)
    identificationid = Column(Integer)
    identification = Column(String)
