# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_kaiju(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def run_kaiju(self, params, context=None):
        """
        Kaiju Method
        :param params: instance of type "KaijuInputParams" (Kaiju App Input
           Params) -> structure: parameter "workspace_name" of type
           "workspace_name" (** The workspace object refs are of form: ** ** 
           objects = ws.get_objects([{'ref':
           params['workspace_id']+'/'+params['obj_name']}]) ** ** "ref" means
           the entire name combining the workspace id and the object name **
           "id" is a numerical identifier of the workspace or object, and
           should just be used for workspace ** "name" is a string identifier
           of a workspace or object.  This is received from Narrative.),
           parameter "reads_ref" of type "data_obj_ref", parameter
           "tax_levels" of list of String, parameter "db_type" of String,
           parameter "seg_filter" of type "bool" (A boolean - 0 for false, 1
           for true. @range (0, 1)), parameter "greedy_run_mode" of type
           "bool" (A boolean - 0 for false, 1 for true. @range (0, 1)),
           parameter "min_match_length" of Long, parameter
           "greedy_min_match_score" of Double, parameter
           "greedy_allowed_mismatches" of Long
        :returns: instance of type "KaijuOutput" (Kaiju App Output) ->
           structure: parameter "report_name" of type "data_obj_name",
           parameter "report_ref" of type "data_obj_ref"
        """
        return self._client.call_method(
            'kb_kaiju.run_kaiju',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_kaiju.status',
                                        [], self._service_ver, context)
