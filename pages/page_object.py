#!/usr/bin/env python

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Tests.
#
# The Initial Developer of the Original Code is Mozilla.
#
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   David Burns
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

from page import Page
from selenium.webdriver.common.by import By

import urllib

class MySiteHomePage(Page):

    _some_locator = (By.ID, 'some_locator')
    _page_title = 'MySiteHomePage Page Title' 
    
    def go_to_home_page(self):
        self.selenium.get(self.base_url)

    def get_response_code(self, url):
        # check if response status 200
        response = urllib.urlopen(url)
        if response.getcode() == 200:
            result = 'The request returned an HTTP 200 response.'
        elif response.getcode() == 404:
            result = 'The request returned an HTTP 404 response.'
        elif response.getcode() == 503:
            result = 'The request returned an HTTP 503 response.'
        else:
            result = 'The response code was %s' % response.getcode()
        return result
 
    @property
    def header(self):
        return MySiteHomePage.HeaderRegion(self.testsetup)

    @property
    def footer(self):
        return MySiteHomePage.FooterRegion(self.testsetup)
    
    def sharelinks(self):
        return MySiteHomePage.ShareLinksRegion(self.testsetup)
    
    class HeaderRegion(Page):
        
        _header_locator = (By.ID, 'branding')
        
        #Header Locators List
        _home_link_locator = (By.ID, 'bla bla')
        _signin_link_locator = (By.NAME, 'bla bla')
        _signout_link_locator = (By.CSS_SELECTOR, '#bla bla bla')
        _myaccount_link_locator = (By.XPATH, 'bla bla bla')
        _language_locator = (By.ID, 'flang')
        
        _mozilla_logo_link_locator = (By.CSS_SELECTOR, '.mozilla')

        def click_home_logo(self):
            self.selenium.find_element(*self._home_link_locator).click()

        @property
        def is_mozilla_logo_visible(self):
            return self.is_element_visible(self._mozilla_logo_link_locator)

        def click_mozilla_logo(self):
            self.selenium.find_element(*self._mozilla_logo_link_locator).click()


        @property
        def logged_in(self):
            return self.is_element_visible(*self._signout_link_locator)

        @property
        def logged_out(self):
            return self.is_element_visible(*self._signin_link_locator)

        def click_signin(self):
            self.selenium.find_element(*self._signin_link_locator).click()

        def click_signout(self):
            self.selenium.find_element(*self._signout_link_locator).click()

    class FooterRegion(Page):
        
        _footer_locator = (By.ID, 'footer')
        #Footer Locators List
        _footer_link_locator = (By.CSS_SELECTOR, 'bla bla')
        
        def change_locale(self):
            self.selenium.find_element(*self._language_locator).click()
        
    class ShareLinksRegion(Page):
        
        _twitter_twit_locator = (By.ID, 'twitter')
        _facebook_like_locator = (By.ID, 'facebook')