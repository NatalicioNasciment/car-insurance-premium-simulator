from domain.entities.quotation import Quotation

class QuotationRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def save(self, quotation: Quotation):
        """
        Salva a cotação no banco de dados.
        """
        self.db_session.add(quotation)
        self.db_session.commit()
