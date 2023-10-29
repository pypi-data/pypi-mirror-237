# -*- coding:utf-8 -*-
"""
@Author       : xupingmao
@email        : 578749341@qq.com
@Date         : 2023-02-12 00:00:00
@LastEditors  : xupingmao
@LastEditTime : 2023-01-22 00:07:43
@FilePath     : /xnote/handlers/note/note_helper.py
@Description  : 计划管理
"""
import xtemplate
import xauth
import xutils
from xutils import Storage
from handlers.plan.dao import MonthPlanDao
from handlers.note import dao as note_dao
from xutils import functions

class MonthPlanHandler:

    @xauth.login_required()
    def GET(self):
        kw = Storage()
        user_name = xauth.current_name_str()
        date = xutils.get_argument_str("date", "now")
        date = date.replace("-", "/")
        record = MonthPlanDao.get_or_create(user_name, date)

        if len(record.note_ids) > 0:
            note_ids = list(filter(lambda x:x!="", record.note_ids))
            record.notes = note_dao.batch_query_list(note_ids)
            record.notes.sort(key = lambda x:x.name)

        year, month = record.month.split("/")

        kw.record = record
        kw.year = int(year)
        kw.month = int(month)
        return xtemplate.render("plan/page/month_plan.html", **kw)


class MonthPlanAddAjaxHandler:
    @xauth.login_required()
    def POST(self):
        plan_id = xutils.get_argument_str("id", "")
        note_ids_str = xutils.get_argument_str("note_ids", "")
        note_ids = note_ids_str.split(",")
        if plan_id == "":
            return dict(code="400", message="参数id不能为空")

        user_name = xauth.current_name_str()
        record = MonthPlanDao.get_by_id(user_name, plan_id)
        if record != None:
            assert isinstance(note_ids, list)
            for id in note_ids:
                if id not in record.note_ids:
                    record.note_ids.append(id)
            record.save()
            return dict(code="success")
        else:
            return dict(code="500", message="计划不存在")

class MonthPlanRemoveAjaxHandler:
    @xauth.login_required()
    def POST(self):
        id = xutils.get_argument_str("id", "")
        note_id = xutils.get_argument_str("note_id", "")
        if id == "":
            return dict(code="400", message="参数id不能为空")
        if note_id == "":
            return dict(code="400", message="参数note_id不能为空")

        user_name = xauth.current_name_str()
        record = MonthPlanDao.get_by_id(user_name, id)
        if record != None:
            functions.listremove(record.note_ids, note_id)
            record.save()
            return dict(code="success")
        else:
            return dict(code="500", message="计划不存在")

xurls = (
    r"/plan/month", MonthPlanHandler,
    r"/plan/month/add", MonthPlanAddAjaxHandler,
    r"/plan/month/remove", MonthPlanRemoveAjaxHandler,
)