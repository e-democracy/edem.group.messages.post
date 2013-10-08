# coding=utf-8
from gs.shim.group.messages.post.postcontentprovider import \
    GSPostContentProvider
from canhide import can_hide_post


class EDEMPostContentProvider(GSPostContentProvider):
    def __init__(self, context, request, view):
        GSPostContentProvider.__init__(self, context, request, view)
        self.can_hide_post = can_hide_post
