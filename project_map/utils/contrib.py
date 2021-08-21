#-*- coding: utf-8 -*-
import os
import hashlib
from binascii import hexlify
from pytils.translit import slugify
from django.utils.module_loading import import_module



#==============================================================================
# create_hash
#==============================================================================
def create_hash(key):
    hash = hashlib.md5()
    hash.update(key)
    return hash.hexdigest()


#==============================================================================
# hash_unsorted_list
#==============================================================================
def hash_unsorted_list(value):
    lst = list(value)
    lst.sort()
    return create_hash('.'.join([str(x) for x in lst]))


#==============================================================================
# create_uid
#==============================================================================
def create_uid():
    return hexlify(os.urandom(16))


#==============================================================================
# get_unique_slug
#==============================================================================
def get_unique_slug(name, key=None):
    slugify_name = ''.join([slugify(u'%s' % name)[:18], create_uid() if key is None else create_hash(str(key))])
    return slugify_name


#==============================================================================
# uniq
#==============================================================================
def uniq(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x not in seen and not seen_add(x)]




def get_object(path, fail_silently=False):
    # Return early if path isn't a string (might already be an callable or
    # a class or whatever)
    if not isinstance(path, (str, unicode)):
        return path
    try:
        return import_module(path)
    except ImportError:
        try:
            dot = path.rindex('.')
            mod, fn = path[:dot], path[dot + 1:]
            return getattr(import_module(mod), fn)
        except (AttributeError, ImportError):
            if not fail_silently:
                raise




