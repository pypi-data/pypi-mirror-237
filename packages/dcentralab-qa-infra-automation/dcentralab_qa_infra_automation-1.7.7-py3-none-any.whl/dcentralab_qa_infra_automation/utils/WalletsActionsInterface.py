from abc import abstractmethod


class WalletsActionsInterface:
    @abstractmethod
    def import_wallet(self):
        pass

    @abstractmethod
    def is_wallet_imported(self):
        pass

    @abstractmethod
    def switch_network(self):
        pass

    @abstractmethod
    def connect_wallet(self):
        pass

    @abstractmethod
    def confirm(self):
        pass
