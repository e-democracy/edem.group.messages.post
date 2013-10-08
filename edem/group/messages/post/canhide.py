# coding=utf-8
from gs.group.member.base.utils import user_admin_of_group

def can_hide_post(userInfo, groupInfo, postInfo):
    admin = user_admin_of_group(userInfo, groupInfo)
    retval = admin 
    assert type(retval) == bool
    return retval
