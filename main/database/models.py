from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Route(Base):
    __tablename__ = "routes"

    route_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    route_short_name: Mapped[str | None] = mapped_column(String(50))
    route_long_name: Mapped[str | None] = mapped_column(String(255))
    route_type: Mapped[int] = mapped_column()
    route_url: Mapped[str | None] = mapped_column(String(500))
    route_color: Mapped[str | None] = mapped_column(String(6))
    route_text_color: Mapped[str | None] = mapped_column(String(6))
    route_sort_order: Mapped[int | None] = mapped_column()

    trips: Mapped[list["Trip"]] = relationship(back_populates="route")

    def __repr__(self) -> str:
        return f"Route(route_id={self.route_id!r}, route_short_name={self.route_short_name!r}, route_long_name={self.route_long_name!r})"


class Shape(Base):
    __tablename__ = "shapes"

    shape_id: Mapped[str] = mapped_column(String(50), primary_key=True)

    trips: Mapped[list["Trip"]] = relationship(back_populates="shape")
    points: Mapped[list["ShapePoint"]] = relationship(back_populates="shape")

    def __repr__(self) -> str:
        return f"Shape(shape_id={self.shape_id!r})"


class ShapePoint(Base):
    __tablename__ = "shape_points"

    shape_id: Mapped[str] = mapped_column(String(50), ForeignKey("shapes.shape_id"), primary_key=True)
    shape_pt_sequence: Mapped[int] = mapped_column(primary_key=True)
    shape_pt_lat: Mapped[float] = mapped_column()
    shape_pt_lon: Mapped[float] = mapped_column()

    shape: Mapped["Shape"] = relationship(back_populates="points")

    def __repr__(self) -> str:
        return f"ShapePoint(shape_id={self.shape_id!r}, sequence={self.shape_pt_sequence!r}, lat={self.shape_pt_lat!r}, lon={self.shape_pt_lon!r})"


class Stop(Base):
    __tablename__ = "stops"

    stop_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    stop_code: Mapped[str | None] = mapped_column(String(50))
    stop_name: Mapped[str] = mapped_column(String(255))
    stop_lat: Mapped[float] = mapped_column()
    stop_lon: Mapped[float] = mapped_column()
    stop_url: Mapped[str | None] = mapped_column(String(500))

    stop_times: Mapped[list["StopTime"]] = relationship(back_populates="stop")

    def __repr__(self) -> str:
        return f"Stop(stop_id={self.stop_id!r}, stop_name={self.stop_name!r}, lat={self.stop_lat!r}, lon={self.stop_lon!r})"


class Trip(Base):
    __tablename__ = "trips"

    trip_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    route_id: Mapped[str] = mapped_column(String(50), ForeignKey("routes.route_id"))
    service_id: Mapped[str] = mapped_column(String(50))
    trip_headsign: Mapped[str | None] = mapped_column(String(255))
    direction_id: Mapped[int | None] = mapped_column()
    block_id: Mapped[str | None] = mapped_column(String(50))
    shape_id: Mapped[str] = mapped_column(String(50), ForeignKey("shapes.shape_id"))
    wheelchair_accessible: Mapped[int | None] = mapped_column()

    route: Mapped["Route"] = relationship(back_populates="trips")
    shape: Mapped["Shape"] = relationship(back_populates="trips")
    stop_times: Mapped[list["StopTime"]] = relationship(back_populates="trip")

    def __repr__(self) -> str:
        return f"Trip(trip_id={self.trip_id!r}, route_id={self.route_id!r}, direction_id={self.direction_id!r}, shape_id={self.shape_id!r})"


class StopTime(Base):
    __tablename__ = "stop_times"

    trip_id: Mapped[str] = mapped_column(String(50), ForeignKey("trips.trip_id"), primary_key=True)
    stop_sequence: Mapped[int] = mapped_column(primary_key=True)
    arrival_time: Mapped[str | None] = mapped_column(String(20))
    departure_time: Mapped[str | None] = mapped_column(String(20))
    stop_id: Mapped[str] = mapped_column(String(50), ForeignKey("stops.stop_id"))

    trip: Mapped["Trip"] = relationship(back_populates="stop_times")
    stop: Mapped["Stop"] = relationship(back_populates="stop_times")

    def __repr__(self) -> str:
        return f"StopTime(trip_id={self.trip_id!r}, stop_id={self.stop_id!r}, sequence={self.stop_sequence!r})"