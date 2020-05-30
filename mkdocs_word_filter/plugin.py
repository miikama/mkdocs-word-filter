import os
import sys
import re


from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

import markdown

import logging
logger = logging.getLogger(__name__)

class ContentFilterPlugin(BasePlugin):

    line_option_name = "filter-lines-with"

    config_scheme = (
        (line_option_name, config_options.Type(list, default=[])),        
    )

    def __init__(self):
        """Set up default tokens to filter"""
        self.tokens_to_filter = (r'\toc', r'\newpage')

    def on_config(self, config, **kwargs):
        """
            Get the keywords to filter out from config
        """
        self.tokens_to_filter = []
        
        # Check if any patterns to filter are defined in the configuration
        if self.line_option_name not in self.config:           
            logger.warn("Did not find {} in config".format(self.line_option_name))
            return config

        # Only take strings
        for filter_token in self.config[self.line_option_name]:
            if not isinstance(filter_token, str):
                logger.warn('Received a configuration option {} under {} that was not a string, ignoring.'.format(filter_token, self.line_option_name))
                continue
            self.tokens_to_filter.append(filter_token)            

        return config
    
    def on_page_markdown(self, markdown, **kwargs):
        """
            Filter out the configured tokens
        """
        if not self.tokens_to_filter:
            return markdown

        filtered = ''.join(re.split('|'.join(map(re.escape, self.tokens_to_filter)), markdown))
        return filtered 
        