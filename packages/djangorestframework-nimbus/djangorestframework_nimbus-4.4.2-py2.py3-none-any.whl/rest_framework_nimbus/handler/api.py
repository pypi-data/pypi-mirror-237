# -*- coding: utf-8 -*-
import logging
from django.conf import settings
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.views import exception_handler, set_rollback
from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework_nimbus.err_code import ErrCode

logger = logging.getLogger(__name__)


def api_render_data(data, accepted_media_type=None, renderer_context=None, **kwargs):
    status_code = str(renderer_context['response'].status_code)
    response = {
        "code": ErrCode.SUCCESS,
        "msg": "SUCCESS",
        "data": data,
    }
    if not status_code.startswith('2'):
        response["code"] = ErrCode.ERROR
        response["msg"] = "ERROR"
        try:
            err_code, err_detail = _get_exception_info(ex=data, default_code=status_code)
            response["code"] = err_code
            response["data"] = err_detail
        except KeyError:
            logger.error(data)
            response["code"] = ErrCode.ERROR
            response["data"] = data
    return response


def api_exception_data(exc, context=None, **kwargs):
    logger.exception(exc)
    status_code = getattr(exc, "status_code", status.HTTP_400_BAD_REQUEST)
    code = str(ErrCode.ERROR)
    response = {
        "code": code,
        "msg": "ERROR",
        "data": "",
    }
    err_code, err_detail = _get_exception_info(ex=exc, default_code=code)
    response["code"] = err_code
    response["data"] = err_detail
    return Response(response, status=status_code)


def _get_exception_info(ex, default_code=status.HTTP_400_BAD_REQUEST):
    logger.error(ex)
    if isinstance(ex, dict):
        err = ex.get("detail", "")
    elif isinstance(ex, str):
        err = ex
    if isinstance(err, dict):
        err_code = err.get("code", default_code)
    else:
        err_code = getattr(err, "code", default_code)
    if isinstance(err, dict):
        err_detail = err.get("detail", err)
    else:
        err_detail = getattr(err, "detail", err)
    if not err_detail and settings.DEBUG:
        err_detail = str(ex)
    return err_code, err_detail

