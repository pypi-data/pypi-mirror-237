import time

import pytest
from dcentralab_qa_infra_automation.pages.coinbasePages.ConfirmPage import ConfirmPage
from dcentralab_qa_infra_automation.pages.coinbasePages.ConnectToWebsitePage import ConnectToWebsitePage
from dcentralab_qa_infra_automation.pages.coinbasePages.CreatePasswordPage import CreatePasswordPage
from dcentralab_qa_infra_automation.pages.coinbasePages.CreateWalletPage import CreateWalletPage
from dcentralab_qa_infra_automation.pages.coinbasePages.ImportWalletPage import ImportWalletPage
from dcentralab_qa_infra_automation.pages.coinbasePages.ReceiveCryptoToUsername import ReceiveCryptoToUsernamePage
from dcentralab_qa_infra_automation.pages.coinbasePages.UseAnExistingWalletPage import UseAnExistingWalletPage
from dcentralab_qa_infra_automation.utils.WalletsActionsInterface import WalletsActionsInterface

"""
Coinbase wallet actions
@Author: Efrat Cohen
@Date: 03.2023
"""


# TODO - Add messages for logger
class CoinbaseActions(WalletsActionsInterface):
    """
    coinbase actions class
    this class implements wallet actions interface.
    """

    def __init__(self, driver):
        self.driver = driver
        self.logger = pytest.logger
        self.create_wallet_page = CreateWalletPage(self.driver)
        self.use_existing_wallet_page = UseAnExistingWalletPage(self.driver)
        self.import_wallet_page = ImportWalletPage(self.driver)
        self.create_password_page = CreatePasswordPage(self.driver)
        self.receive_crypto_username_page = ReceiveCryptoToUsernamePage(self.driver)
        self.connect_wallet_to_website_page = ConnectToWebsitePage(self.driver)
        self.confirm_page = ConfirmPage(self.driver)

    def import_wallet(self):
        """
        import coinbase wallet process implementation
        """
        # Open new tab
        self.driver.switch_to.new_window("tab")

        # Focus on the new tab window
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.driver.get(pytest.properties.get("coinbase.connect.url"))

        # Check if create or import wallet page loaded
        assert self.create_wallet_page.is_page_loaded()

        # Click on already have a wallet
        self.create_wallet_page.click_on_already_have_a_wallet()

        # Check is use an existing wallet page loaded
        assert self.use_existing_wallet_page.is_page_loaded()

        # Click on enter recovery phrase
        self.use_existing_wallet_page.click_on_enter_recovery_phrase()

        # Check if import wallet page loaded
        assert self.import_wallet_page.is_page_loaded()

        # Insert recovery phrase
        self.import_wallet_page.insert_recovery_phrase()

        # Click on import wallet button
        self.import_wallet_page.click_on_import_wallet()

        # Check is create password page loaded
        assert self.create_password_page.is_page_loaded()

        # Insert password
        self.create_password_page.insert_password()

        # Verify password
        self.create_password_page.verify_password()

        # Click on agree terms checkbox
        self.create_password_page.click_on_agree_terms_checkbox()

        # Click on submit
        self.create_password_page.click_on_submit()

        # Check if page after wallet connection loaded
        assert self.receive_crypto_username_page.is_page_loaded()

        time.sleep(3)

        # Close coinbase current active tab
        self.driver.close()

        # Switch focus to first tab
        self.driver.switch_to.window(self.driver.window_handles[0])

    def connect_wallet(self):
        """
            connect to wallet implementation
        """
        time.sleep(8)

        # Coinbase popup instance
        w_handle = self.driver.window_handles[1]

        # Switch to pop up window
        self.driver.switch_to.window(w_handle)

        # Check is connect to website popup loaded
        assert self.connect_wallet_to_website_page.is_page_loaded()

        # Click on connect button
        self.connect_wallet_to_website_page.click_on_connect_button()

        time.sleep(2)

        # Switch focus to site tab
        self.driver.switch_to.window(self.driver.window_handles[0])

    def confirm(self):
        time.sleep(5)

        # Coinbase popup instance
        w_handle = self.driver.window_handles[1]

        # Switch to pop up window
        self.driver.switch_to.window(w_handle)

        # Check is got it button exist - if exists
        if self.confirm_page.is_got_it_button_exist():
            # Click on got_it button
            self.confirm_page.click_on_got_it_button()

        time.sleep(1)

        # Check is confirm button exist.
        assert self.confirm_page.is_confirm_button_exist()

        # Click on confirm button
        self.confirm_page.click_on_confirm_button()

        time.sleep(5)

        # Switch focus to site tab
        self.driver.switch_to.window(self.driver.window_handles[0])

    def switch_network(self):
        pass
