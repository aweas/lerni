from .meta import *


class Pages(Base):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    url_name = Column(Text, unique=True)
    name = Column(Text)
    widgets = relationship("Widgets")
    pre = Column(Text)

    def __init__(self, url_name, name, pre=""):
        self.url_name = url_name
        self.name = name
        self.pre = pre


class Widgets(Base):
    __tablename__ = 'pages_widgets'
    id = Column(Integer, primary_key=True)
    page_id = Column(Integer, ForeignKey('pages.id'))
    page = relationship("Pages")
    column = Column(Integer)
    row = Column(Integer)
    size_x = Column(Integer)
    size_y = Column(Integer)
    data = Column(Text)
    add_class = Column(Text)

    def __init__(self, page_id, column, row, size_x, size_y, data, add_class=""):
        self.page_id = page_id
        self.column = column
        self.row = row
        self.size_x = size_x
        self.size_y = size_y
        self.data = data
        self.add_class = add_class


class Bells(Base):
    __tablename__ = 'bells'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    order = Column(Integer)
    start = Column(Time)
    start_len = Column(Integer)
    end = Column(Time)
    end_len = Column(Integer)
    type_id = Column(Integer, ForeignKey('bells_types.id'))
    type = relationship("BellsTypes")

    def __init__(self, name, order, start, start_len, end, end_len, type_id):
        self.name = name
        self.order = order
        self.start = start
        self.start_len = start_len
        self.end = end
        self.end_len = end_len
        self.type_id = type_id


class BellsTypes(Base):
    __tablename__ = 'bells_types'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    def __init__(self, name):
        self.name = name


class Graduates(Base):
    __tablename__ = 'graduates'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    graduation = Column(Text)
    about = Column(Text)

    def __init__(self, name, graduation, about):
        self.name = name
        self.graduation = graduation
        self.about = about


class Competitors(Base):
    __tablename__ = 'competitors'
    id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    competition_group_id = Column(Integer, ForeignKey('competitors_groups.id'))
    competition_group = relationship("CompetitorsGroups")
    competition_id = Column(Integer, ForeignKey('competitors_competitions.id'))
    competition = relationship("CompetitorsCompetitions")
    competitor_type_id = Column(Integer, ForeignKey('competitors_types.id'))
    competitor_type = relationship("CompetitorsTypes")
    competitor_tutor_id = Column(Integer, ForeignKey('competitors_tutors.id'))
    competitor_tutor = relationship("CompetitorsTutors")
    start_year = Column(Integer)
    end_year = Column(Integer)

    def __init__(self, first_name, last_name, competition_id, competitor_type_id,
                 competitor_tutor_id, start_year, end_year, competition_group_id):
        self.first_name = first_name
        self.last_name = last_name
        self.competition_id = competition_id
        self.competitor_type_id = competitor_type_id
        self.competitor_tutor_id = competitor_tutor_id
        self.start_year = start_year
        self.end_year = end_year
        self.competition_group_id = competition_group_id


class CompetitorsGroups(Base):
    __tablename__ = 'competitors_groups'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    competitors = relationship("Competitors")

    def __init__(self, name):
        self.name = name


class CompetitorsCompetitions(Base):
    __tablename__ = 'competitors_competitions'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    subject_id = Column(Integer, ForeignKey('log_subjects.id'))
    subject = relationship("Subjects")
    competitors = relationship("Competitors")

    def __init__(self, name, subject_id):
        self.name = name
        self.subject_id = subject_id


class CompetitorsTypes(Base):
    __tablename__ = 'competitors_types'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    competitors = relationship("Competitors")

    def __init__(self, name):
        self.name = name


class CompetitorsTutors(Base):
    __tablename__ = 'competitors_tutors'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    competitors = relationship("Competitors")

    def __init__(self, name):
        self.name = name


class PingResults(Base):
    __tablename__ = 'ping_results'
    id = Column(Integer, primary_key=True)
    ip_id = Column(Integer, ForeignKey('ping_ips.id'))
    ip = relationship("PingIPs")
    result = Column(Boolean)
    date = Column(DateTime)

    def __init__(self, ip_id, result):
        self.ip_id = ip_id
        self.result = result
        self.date = datetime.datetime.now()


class PingIPs(Base):
    __tablename__ = 'ping_ips'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    ip = Column(Text)
    scan = Column(Boolean)
    results = relationship("PingResults")

    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.scan = True