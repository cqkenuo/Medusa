#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Mongo import MongoExpressRemoteCodeExecutionVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(MongoExpressRemoteCodeExecutionVulnerability.medusa,Url, Values, proxies = proxies, ** kwargs)
    Prompt("Mongo")
