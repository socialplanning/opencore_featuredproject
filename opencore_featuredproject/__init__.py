from BTrees.IOBTree import IOBTree
from Products.CMFCore.utils import getToolByName
from datetime import datetime
from zope.app.annotation.interfaces import IAnnotations
from zope.app.component.hooks import getSite
from persistent.dict import PersistentDict

def get_featured_project_structure():
    context = getSite()
    portal = getToolByName(context, 'portal_url').getPortalObject()
    annot = IAnnotations(portal)
    featured_structure = annot.get('opencore.feature-project', None)
    if featured_structure is None:
        featured_structure = IOBTree()
        annot['opencore.feature-project'] = featured_structure
    return featured_structure

def feature_project(project_id, description):
    """this stores the project_id in an annotation on the portal"""
    featured_structure = get_featured_project_structure()
    featured_structure[project_id] = PersistentDict(
        project_id=project_id,
        timestamp=datetime.now(),
        description=description,
        )

def get_featured_project_metadata():
    """get some metadata latest featured project, or None"""
    featured_structure = get_featured_project_structure()
    return featured_structure.values()

def get_index_of_latest_project(featured_structure):
    idxs = featured_structure.keys()
    n = len(idxs)
    if n == 0:
        return None
    else:
        return n - 1
