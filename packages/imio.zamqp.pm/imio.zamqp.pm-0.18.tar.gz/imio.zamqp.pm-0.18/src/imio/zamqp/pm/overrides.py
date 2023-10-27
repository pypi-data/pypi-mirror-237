# -*- coding: utf-8 -*-

from Products.PloneMeeting.adapters import PMAnnexPrettyLinkAdapter
from zope.i18n import translate


class IZPMAnnexPrettyLinkAdapter(PMAnnexPrettyLinkAdapter):
    """ """

    def _leadingIcons(self):
        """
          Manage icons to display before the annex title.
        """
        res = super(IZPMAnnexPrettyLinkAdapter, self)._leadingIcons()
        # display a 'barcode' icon if barcode is inserted in the file
        if self.context.scan_id:
            res.append(('++resource++imio.zamqp.pm/barcode.png',
                        translate('icon_help_barcode_inserted',
                                  domain="imio.zamqp.pm",
                                  context=self.request)))
        return res
