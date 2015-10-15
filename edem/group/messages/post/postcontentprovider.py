# coding=utf-8
from __future__ import absolute_import, unicode_literals
from gs.group.messages.post.hide.viewlet import HideViewlet
from .canhide import can_hide_post


class EDemHideViewlet(HideViewlet):
    @property
    def show(self):
        retval = can_hide_post(self.loggedInUser, self.groupInfo, 
                               self.manager.post)
        return retval
